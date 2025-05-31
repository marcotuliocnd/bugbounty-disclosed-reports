# myshopify.com domain takeover

## Report Details
- **Report ID**: 320355
- **URL**: https://hackerone.com/reports/320355
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-27T15:51:11.492Z
- **Disclosed**: 2018-02-27T17:59:38.712Z

## Reporter
- **Username**: 0xacb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify Security Team,

I just received your email and I'm sorry for any inconvenience. Yes, it was me.
Basically, I just tried to audit your website using some black box testing. Unfortunately, I didn't read about those guidelines, such as creating a store on https://partners.shopify.com/ and I created a normal trial account.

I'm glad you found a bug as a result of inspecting my activity logs. And you're right, I didn't notice the bug.

I tried many different things, such as:

- I tried to bypass the open redirect filter, without success: https://www.shopify.com/login?redirect=//acme
- I explored the domain DNS check tool to get RCE without success. I tried to use some command injection techniques, but I didn't receive any requests on my server (█████). I tried to use curl and netcat to perform external requests.
- I think I managed to add domains that were not verified by the DNS tool by submitting them using the last endpoint, but those domains remain "Not connected".

I have all my requests on Burp, but I didn't save the session. As far as I can remember, this was what I tested. I would like to know what was the bug. If possible, I would like to test it further.

Thank you,
André

## Impact

None

## Attachments
No attachments
