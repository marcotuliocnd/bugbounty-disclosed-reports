# Subdomain takeover on https://cloudfront.ubnt.com/ due to non-used CloudFront DNS entry

## Report Details
- **Report ID**: 210188
- **URL**: https://hackerone.com/reports/210188
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-02T20:15:54.196Z
- **Disclosed**: 2017-05-07T18:18:34.562Z

## Reporter
- **Username**: linkks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
So lately I have discovered that CloudFront is not validating which user that connects a CNAME:d domain to a CloudFront Origin. This means that if I could find a domain that is still pointing to CloudFront, without being connected to any Origin as a Custom CNAME, I can actually claim the domain myself and point it to whatever I want.

dig cloudfront.ubnt.com

; <<>> DiG 9.10.3-P4-Debian <<>> cloudfront.ubnt.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52550
;; flags: qr rd ra; QUERY: 1, ANSWER: 9, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;cloudfront.ubnt.com. IN A

;; ANSWER SECTION:
cloudfront.ubnt.com. 268 IN CNAME du6drkqe7qw4g.cloudfront.net.
du6drkqe7qw4g.cloudfront.net. 29 IN A 52.222.171.58
du6drkqe7qw4g.cloudfront.net. 29 IN A 52.222.171.143
du6drkqe7qw4g.cloudfront.net. 29 IN A 52.222.171.238
du6drkqe7qw4g.cloudfront.net. 29 IN A 52.222.171.216
du6drkqe7qw4g.cloudfront.net. 29 IN A 52.222.171.144
du6drkqe7qw4g.cloudfront.net. 29 IN A 52.222.171.190
du6drkqe7qw4g.cloudfront.net. 29 IN A 52.222.171.55
du6drkqe7qw4g.cloudfront.net. 29 IN A 52.222.171.71

;; Query time: 7 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Wed Feb 22 03:26:49 MSK 2017
;; MSG SIZE rcvd: 218

;; ANSWER SECTION:
cloudfront.ubnt.com. 268 IN CNAME du6drkqe7qw4g.cloudfront.net.

You should most likely just remove the DNS-entry for this domain, and also make sure you constantly remove DNS records pointing to CloudFront (and other services as well of course) when you stop using them.

As you might understand, the consequences of this are pretty bad. I now can serve whatever I like on this domain, even fetching httpOnly cookies. I would also be able to issue an SSL for this domain through AlphaSSL or Let's Encrypt (that only needs meta/file verification to issue the certificate) That would end up with the ability to read secure cookies as well.

Also, there's no way at all for a visitor of this page to validate that the content on this domain is not served by UBNT, making it extremely easy to utilize this for targeting the organization by fake login forms / spear phishing using your own domain to plant the attack.

You can read about this sort of attacks here : http://labs.detectify.com/post/109964122636/hostile-subdomain-takeover-using

## Attachments
- 1ulCdCJc_1_.png
