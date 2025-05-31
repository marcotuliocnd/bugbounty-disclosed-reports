# Insufficient validation on Digits bridge

## Report Details
- **Report ID**: 168116
- **URL**: https://hackerone.com/reports/168116
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-13T19:44:33.505Z
- **Disclosed**: 2020-08-20T11:20:39.071Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an issue in one of the login methods, [getLoginStatus()](https://docs.fabric.io/web/digits/sign-in-with-phone-number.html) in Digits, which allows attacker to retrieve the OAuth credential data of an application victims authorized.

#Details
The *getLoginStatus()* method provides a seamless login option. If a user has logged in Digits, a website can use this method to get the user's OAuth credentials instead of asking him to authorize it. The way it works is to embed an iframe (https://www.digits.com/bridge) onto a web page, and communicate with the web page through *postMessage()*. Currently, there is a security check in place which prevents a website to call this method with other app's key by making sure the HTTP Referer is the registered domain. The protection works because embedding an iframe involves sending the *Referer* header in the request. If app A wants to call the method and pretend itself as app B, it won't work because the *Referer* header is from app A instead of the registered domain of app B.

However, It was found that if the *Referer* header is left empty, the validation will also think this is valid. The problem is that there is a way for a website to disable sending *Referer* for out bound requests by using the tag `<meta name="referrer" content="never">`. This allows an attacker to bypass the validation.

#PoC
1. Prepare a Periscope account which is associated with a phone number, and make sure you have logged in Digits (https://www.digits.com/signin) with that number
2. Go to http://innerht.ml/pocs/digits-bridge-referer-bypass
3. Wait for a while
4. You Periscope account will be renamed as "Pwn3d"

#Fix
Instead of validating HTTP Referer, using the app's registered domain as the *targetOrigin* in [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) is more reliable. That way, only the correct recipient can read the transferred data.

## Attachments
No attachments
