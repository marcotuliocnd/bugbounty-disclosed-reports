# Reflected XSS on https://www.zomato.com

## Report Details
- **Report ID**: 311639
- **URL**: https://hackerone.com/reports/311639
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-02T12:39:58.735Z
- **Disclosed**: 2018-04-07T07:07:31.208Z

## Reporter
- **Username**: strukt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hello,

I found an XSS issue due to the incorrect handling of the \ character in a <script> context, the following link works as a PoC that alerts the location of the document:

https://www.zomato.com/googleOAuth2Callback?)}(alert)(location);{%3C!--&state=\

The issue exists because, given that the \ character supplied as the `state` parameter value is not well escaped and reflected into the page, we are able to use it to escape the " and then inject our own JS code to execute it on the page.

Note: This only works when the page is opened by an authenticated user

## Impact

This allows an attacker to inject custom Javascript codes that can be used to steal information from Zomato's user base and lure them to malicious websites on the internet on behalf of Zomato's website.

## Attachments
No attachments
