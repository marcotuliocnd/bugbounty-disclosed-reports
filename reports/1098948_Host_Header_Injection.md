# Host Header Injection

## Report Details
- **Report ID**: 1098948
- **URL**: https://hackerone.com/reports/1098948
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-09T06:35:33.391Z
- **Disclosed**: 2021-05-10T06:14:06.190Z

## Reporter
- **Username**: streetdragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kartpay

## Vulnerability Information
## Summary:
Hello Team,
While performing security testing on your Main Domain, I found a Host Header Injection Vulnerability.

Vulnerability Description:
An attacker can manipulate the Host header as seen by the web application and cause the application to behave in unexpected ways.
Very often multiple websites are hosted on the same IP address. This is where the Host Header comes in. This header specifies which website should process the HTTP request. The web server uses the value of this header to dispatch the request to the specified website. Each website hosted on the same IP address is called a virtual host. And It's possible to send requests with arbitrary Host Headers to the first virtual host.

## Browsers Verified In:

  * Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 

## Steps To Reproduce:
If possible, the application should avoid incorporating user-controllable data into redirection targets. In many cases, this behavior can be avoided in two ways:

  1. Remove the redirection function from the application, and replace links to it with direct links to the relevant target URLs.
  2.Maintain a server-side list of all URLs that are permitted for redirection. Instead of passing the target URL as a parameter to the redirector, pass an index into this list.

## Supporting Material/References:
Vulnerable URL: http://kartpay.com

  * [attachment / reference]
Video POC Attached below.

## Impact

Tampering of Host header can lead to the following attacks:
1) Web Cache Poisoning-Manipulating caching systems into storing a page generated with a malicious Host and serving it to others.

2) Password Reset Poisoning-Exploiting password reset emails and tricking them to deliver poisoned content directly to the target.

3) Cross Site Scripting - XSS can be performed, if the value of Host header is used for writing links without HTML-encoding. For example Joomla used to write Host header to every page without HTML Encoding like this: <link href=”http://_SERVER['HOST']”> which led to cross site scripting.

4) Access to internal hosts-To access internal hosts.

5.) It can also lead to Phishing Attacks.

## Attachments
- Burp_Suite_Professional_v2020.2.1_-_Test_1_-_Licensed_to___Dr.FarFar_-___WwW.Dr-FarFar.CoM_______FaceBook.Com_Dr.FarFar_______Twitter.Com_3XS0___2021-02-09_11-41-25.mp4
