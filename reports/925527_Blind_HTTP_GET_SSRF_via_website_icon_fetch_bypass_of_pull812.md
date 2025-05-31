# Blind HTTP GET SSRF via website icon fetch (bypass of pull#812)

## Report Details
- **Report ID**: 925527
- **URL**: https://hackerone.com/reports/925527
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-07-16T16:40:56.817Z
- **Disclosed**: 2020-09-11T13:24:08.854Z

## Reporter
- **Username**: shielder
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bitwarden

## Vulnerability Information
After a credential has been added to vault.bitwarden.com (or any self-hosted installation), if the settings allow website icons to be fetched (https://bitwarden.com/help/article/website-icons/), the Bitwarden server will try to fetch the icon image.

The relevant source code is https://github.com/bitwarden/server/blob/master/src/Icons/Controllers/IconsController.cs#L42-L65 and https://github.com/bitwarden/server/blob/master/src/Icons/Services/IconFetchingService.cs#L59
As we can see in the second link, just the domain is used as entrypoint to retrieve the icon image. After trying both HTTPS and HTTP connections, if an HTTP redirect happens the backend will try to follow it, for a maximum of 2 times.

The merged pull request https://github.com/bitwarden/server/pull/812 (which seems based on the vulnerable code snippet available on https://stackoverflow.com/a/8113687) tries to prevent SSRF attacks by checking if the domain resolves to a private IP, but that protection can be bypassed because not all IPs are checked: for example "0.0.0.0" (which will request "127.0.0.1") or the private subnet "169.254.0.0/16" used in many cloud environments as metadata API (e.g. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html) will pass that test and send the HTTP request to the private host.

### Proof-of-concept
0. Buy a domain and set it up on a server with a public IP address
1. Setup a webserver on the domain, e.g. nginx
2. Setup a malicious nameserver for the domain, I've used https://github.com/Crypt0s/FakeDns with the following configuration (change the domain name and IP with yours):

```
A www.yourdomain.com YOUR.PUBLIC.IP
A .*.local.yourdomain.com 0.0.0.0
```

4. Create a redirect index page on the newly created webserver, e.g. (change the domain name with yours):

```php
<?php
header("location: http://test.local.yourdomain.com/PATH_IS_KEPT");
exit();
```

3. Create a self-hosted Bitwarden instance following the instructions at https://bitwarden.com/help/article/install-on-premise/ and create an account
4. Log-in via cli on the `icons` docker instance and setup a dummy TCP listener on port 80, this will confirm we can request arbitrary HTTP endpoints on 127.0.0.1 
(**NOTE: i'm opening this socket just for PoC purposes -- of course the attacker wouldn't have such access however they could attack other locally-exposed services, such as the metadata API on 169.254.169.254**), e.g.:

```
# perl -MIO::Socket::INET -ne 'BEGIN{$l=IO::Socket::INET->new( LocalPort=>80,Proto=>"tcp",Listen=>5,ReuseAddr=>1); my $l=$l->accept(); while(<$l>){ print $_; }; close($l);}'
```

5. Log-in Bitwarden and add a credential with URL "www.yourdomain.com" (change the domain name with yours)
6. Notice the request at https://github.com/bitwarden/server/blob/master/src/Icons/Services/IconFetchingService.cs#L301-L314 arrives on the local TCP listener, e.g.:

```
root@2efebadd421d:/app# perl -MIO::Socket::INET -ne 'BEGIN{$l=IO::Socket::INET->new( LocalPort=>80,Proto=>"tcp",Listen=>5,ReuseAddr=>1); my $l=$l->accept(); while(<$l>){ print $_; }; close($l);}'
GET /PATH_IS_KEPT HTTP/1.1
Host: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299
Accept-Language: en-US, en; q=0.8
Cache-Control: no-cache
Pragma: no-cache
Accept: text/html, application/xhtml+xml, application/xml; q=0.9, image/webp, image/apng, */*; q=0.8
Request-Id: |3d01319c-4dccd9dac66f3032.3.
Accept-Encoding: gzip, deflate

^C
root@2efebadd421d:/app#
```

### Bonus potential bypass (unverified) 
It could also be possible to bypass such check via a DNS resolution Time-of-check/Time-of-use (TOCTOU, https://cwe.mitre.org/data/definitions/367.html) attack, similarly to what was done in https://hackerone.com/reports/541169.

By controlling a domain name and its nameserver an attacker can reply to the first DNS A resolution (the private IP check in https://github.com/bitwarden/server/blob/master/src/Icons/Services/IconFetchingService.cs#L295) with a non-private IP address (with a very low TTL, such as 0, this way it is resolved again next time) to pass the check and then reply to the second DNS A resolution (the HTTP client DNS resolution triggered in https://github.com/bitwarden/server/blob/master/src/Icons/Services/IconFetchingService.cs#L318) with any IP they want. Doing so allows them to bypass again the new protection and use any IP they want for the HTTP request. 

Here's a step-by-step explanation of the attack:

0. The malicious user inputs a credential with URL "http://shielder.it" (whose nameserver they control)
1. Bitwarden's backend requests a name resolution for the domain to check if it is a private IP (1st resolution, in https://github.com/bitwarden/server/blob/master/src/Icons/Services/IconFetchingService.cs#L295)
2. the attacker nameserver replies with any non-private IP, e.g. 8.8.8.8, with a low TTL, e.g. 0
3. the Bitwarden backend checks it is not a private IP and tries to setup an HTTP request to it
4. since the 1st resolution's TTL has now expired, the Bitwarden's server HTTP client resolves it again (2nd resolution, triggered by https://github.com/bitwarden/server/blob/master/src/Icons/Services/IconFetchingService.cs#L318)
5. the malicious nameserver now replies with a private IP address, e.g. 10.10.10.3
6. the Bitwarden backend sends a HTTP request using the last IP address, e.g. 10.10.10.3

Moreover, the attacker has the ability to send HTTP GET requests to arbitrary endpoint through the redirect technique I have talked about above.

As said previously, I haven't verified this second attack can actually work, however I wanted to point out it **should** theoretically be possible.

### Remediation

Here are my suggestions for the attack scenarios i have presented:
* Consider in the check all the potential private IPs which now pass it, for example I suggest to have a look at what GitLab does (it is Ruby code but readable) at https://gitlab.com/gitlab-org/gitlab-foss/-/blob/master/lib/gitlab/url_blocker.rb
* Verify the DNS resolution is not perfomed again after the IP is checked, if possible "lock" the HTTP request to the verified IP address so it is not sent using an unverified IP address

### Credits
Please credit "polict of Shielder" in your changelog/hall-of-fame for the discovery of this vulnerability.

## Impact

A malicious Bitwarden user can use the Bitwarden server to scan the local network and send arbitrary HTTP GET requests to a locally-exposed host, such as localhost or an endpoint in 169.254.0.0/16. The privilege to send such requests could potentially allow them to get hold of reserved information or escalate their privileges.

## Attachments
No attachments
