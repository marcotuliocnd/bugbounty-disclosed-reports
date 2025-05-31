# Subdomain take over signup.websummit

## Report Details
- **Report ID**: 172698
- **URL**: https://hackerone.com/reports/172698
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-28T18:11:57.806Z
- **Disclosed**: 2017-01-29T10:01:48.916Z

## Reporter
- **Username**: glc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: websummit

## Vulnerability Information
Subdomain take over



Hi,

You have a subdomain aka `signup.websummit.net` that point to a third party service hosted on Heroku: `wsv1.herokuapp.com`. The nslookup command shows the DNS configuration.

```
$ nslookup signup.websummit.net 8.8.8.8
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
signup.websummit.net	canonical name = wsv1.herokuapp.com.
wsv1.herokuapp.com	canonical name = us-east-1-a.route.herokuapp.com.
Name:	us-east-1-a.route.herokuapp.com
Address: 23.23.94.135
```

However it seems that your didn't own/claim the name `wsv1` on Heroku. That means an attacker could take it and trick your users/staff by copying your primary website and design.


**PoC:**

See the attached screenshots.


**Risk:**

- fake website
- malicious code injection
- users tricking
- company impersonation

Since the vulnerable subdomain is called `signup`, it's a perfect place to create a fake login/subscribe page to steal users credentials. An attacker would post links on forums or send emails and then wait for people to signup on the site he owns.


**Remediation:**

Remove the cname entry or claim the subdomain `wsv1` on Heroku.
See also:
https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/
https://medium.com/@atom/subdomain-takeover-through-external-services-f0f7ee2b93bd#.hglqnm2gg
http://yassineaboukir.com/blog/neglected-dns-records-exploited-to-takeover-subdomains/


Note that I claimed the domain on Heroku, let me know if you want to get it back, I'll delete it soon.

## Attachments
- subto_20160928_notfound.png
- subto_20160928_nslookup.png
- subto_20160928_owned1.png
- subto_20160928_owned2.png
