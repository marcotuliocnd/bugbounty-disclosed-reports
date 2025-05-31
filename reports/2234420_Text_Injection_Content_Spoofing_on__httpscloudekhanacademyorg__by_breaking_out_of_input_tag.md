# Text Injection/ Content Spoofing on  https://cloud.e.khanacademy.org  by breaking out of input tag.

## Report Details
- **Report ID**: 2234420
- **URL**: https://hackerone.com/reports/2234420
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-10-31T20:09:20.589Z
- **Disclosed**: 2023-12-22T23:41:39.984Z

## Reporter
- **Username**: grassye
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hello security team,

Target: https://cloud.e.khanacademy.org/
Position: https://cloud.e.khanacademy.org/districts-demo-form?utm_source=INJECTION_HERE&utm_medium=INJECTION_HERE

Introduction: Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

In order for the text to get injected, an attacker first need to break out of input tag because, the parameters with those values are reflected in the DOM inside input tags.So, an attacker can identify and simply break out of input tag by entering :( "> ) at the beginning of the text .Here, then only the injected text is visible to the screen  and  here it comes with the risk of phishing.

** Steps to Reproduce:
1.Go to https://cloud.e.khanacademy.org/districts-demo-form?utm_source=INJECTION_HERE&utm_medium=INJECTION_HERE,
2.Enter "> to close out of input tag in place of INJECTION_HERE, either as value of parameter:utm_source or utm_medium,
3. After the "> characters, enter anything you want to show to the victim in order to phish,
4.Observe below  the submit button , the text after "> , is reflected in the page.

## Impact

The attacker will play with the trust of victim and may fool him/her to enter credentials to attacker's site.This can't only be the case, there arises so many phishing  scenarios and it also affects the reputation of the organization.

## Attachments
- vokoscreenNG-2023-11-01_12-54-57.mkv
