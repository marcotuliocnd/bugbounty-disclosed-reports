# Blind SSRF in "Integrations" by abusing a bug in Ruby's native resolver.

## Report Details
- **Report ID**: 287245
- **URL**: https://hackerone.com/reports/287245
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-03T23:32:34.644Z
- **Disclosed**: 2017-11-09T18:36:34.928Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
# Summary

HackerOne allows bug bounty programs to integrate their reports queue with issue tracking tools such as Jira and Phabricator. By abusing a bug that I discovered in Ruby's native resolver, I am able to bypass the SSRF filter and could potentially scan your internal network.

# Vulnerability Details

HackerOne uses the [private_address_check](https://github.com/jtdowney/private_address_check) gem to prevent SSRF on the "Integrations" panel: https://hackerone.com/{BBP}/integrations. The actual filtering takes place in [lib/private_address_check.rb](https://github.com/jtdowney/private_address_check/blob/c95a538542d8d5bd8b969d9d8d95753e74fb7e52/lib/private_address_check.rb). The process starts by attempting to resolve the user-supplied URL with `Resolv::getaddresses` and then compares the returned value with a the values in the blacklist. I discovered a bug in `Resolv::getaddresses` that allows me to return an empty value, which is not included in the blacklist and therefore completely bypasses any checks.

```ruby
def resolves_to_private_address?(hostname)
    ips = Resolv.getaddresses(hostname)
    ips.any? do |ip| 
      private_address?(ip)
    end
end
```

The bypass consists of providing encoded IP addresses that when forwarded on to the operating system in `lib/resolv.rb` return an empty value.

```
http://0177.1:22/
http://0x7f.1:22/
http://127.000.001:22/
```

I discovered the bug in `Resolv::getaddresses` by running it on different Linux machines and noticing that the outputs vary. Until the Ruby Core come up with a better solution I suggest not relying on this library for any security-related features.

**Machine 1** returned the following:

```
irb(main):001:0> require 'resolv'
irb(main):002:0> Resolv.getaddresses("127.000.000.1")
=> []
```

And **Machine 2** returned this:

```
irb(main):001:0> require 'resolv'
irb(main):002:0> Resolv.getaddresses("127.000.000.1")
=> ["127.0.0.1"]
```

# Exploit

Admittedly, I was unable to actually exploit this issue and I am still playing around to see if I can exfiltrate valuable data. The current issue only consists of a filter bypass.

# Mitigation

I would suggest using `Socket.getaddrinfo()` as it is more reliable and is not affected by this bug. Something along the lines of this should work:

```ruby
require "socket"
...
def resolves_to_private_address?(hostname)
  ips = Socket.getaddrinfo(hostname, nil).sample[3]
  ips.any? do |ip| 
    private_address?(ip)
  end
end
```

My suggested patch can be found here: {F236338}.

## Attachments
- private_address_check.rb.patch
