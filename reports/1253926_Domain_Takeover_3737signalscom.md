# Domain Takeover [3737signals.com]

## Report Details
- **Report ID**: 1253926
- **URL**: https://hackerone.com/reports/1253926
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-08T00:28:59.309Z
- **Disclosed**: 2021-08-13T18:23:31.997Z

## Reporter
- **Username**: mrmax4o4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Hi,
While i was analyzing the `Basecamp3` Android app i found `3737signals.com` on the source code as i understand you are passing it to the `intent`to view it on some case.

{F1368921}

When I opened it on the browser I got DNS error says `the domain name does not exist`

{F1368922}

As you can see at the bottom of the page `webmaster` is the domain name provider so I navigated to [webmaster.com](https://www.webmasters.com) and searched for `3737sihttps://www.webmasters.com/domains/new.php?domain=3737signals.com&Action=Submit&Domain=3737signals&Suffix=.com&x=0&y=0gnals.com` and found that it's available to [register](https://www.webmasters.com/domains/new.php?domain=3737signals.com&Action=Submit&Domain=3737signals&Suffix=.com&x=0&y=0) 

{F1368920}

I am not sure if it's yours but if it's not just notify me to self close the report

## Impact

- Fake website
- Malicious code injection
- Users tricking
- Company impersonation

This issue can have really huge impact on the companies reputation someone could post malicious content on the compromised site and then your users will think it's official but it's not.

Best Wishes,
MrMax

## Attachments
- Basecamp_STO.png
- Basecamp_STO2.png
- Basecamp_STO3.png
