# [engineering.udemy.com] - Subdomain Takeover (ghost.io)

## Report Details
- **Report ID**: 368119
- **URL**: https://hackerone.com/reports/368119
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-18T12:08:08.453Z
- **Disclosed**: 2018-06-27T22:03:46.205Z

## Reporter
- **Username**: kazan71p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
Hi Security Team,

Found that DNS record of `engineering.udemy.com` domain was pointing to inactive ghost.io instance. So when we visit https://engineering.udemy.com we will be notified that site doesn't exist.

{F310092}

```
$ host engineering.udemy.com
engineering.udemy.com is an alias for udemy-engineering-blog.ghost.io.
udemy-engineering-blog.ghost.io has address 141.101.114.35
udemy-engineering-blog.ghost.io has address 141.101.115.35
udemy-engineering-blog.ghost.io has address 190.93.244.35
udemy-engineering-blog.ghost.io has address 190.93.245.35
udemy-engineering-blog.ghost.io has address 190.93.246.35
```

So I've registered PRO account for 20$/month on ghost.org and created publication with the name `udemy-engineering-blog`, as a next step I configured custom DNS record for my publication.

{F310093}

CNAME record was already configured, so I could successfully pass validation and even have valid SSL certificate and now can serve content on behalf of `engineering.udemy.com`

https://engineering.udemy.com/

{F310094}

## Impact

Attacker is able to serve any content on behalf of `engineering.udemy.com` domain

## Attachments
- Screenshot_at_Jun_18_18-39-58.png
- Screenshot_at_Jun_18_18-48-17.png
- Screenshot_at_Jun_18_19-03-23.png
