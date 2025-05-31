# Cross site scripting (content-sniffing)

## Report Details
- **Report ID**: 363845
- **URL**: https://hackerone.com/reports/363845
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-10T01:18:04.447Z
- **Disclosed**: 2018-06-10T09:25:13.334Z

## Reporter
- **Username**: said778
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
This type of XSS can only be triggered on (and affects) content sniffing browsers.

This script is possibly vulnerable to Cross Site Scripting (XSS) attacks.

This vulnerability affects /sign-up
URL encoded POST input sign-in.currency was set to USD<WDILR9>G8OAI[!+!]</WDILR9>
The input is reflected inside a text element

put this URL https://liberapay.com/about/me/edit&sign-in.currency=USD%3CWDILR9%3EG8OAI%5b%21%2b%21%5d%3C/WDILR9%3E

now put 

csrf_token=oiCrDqa91GRS4YBFb4jzZQzpgxSZN38I & form.repost=false&sign-in.back-to=/about/me/edit & sign-in.currency=USD<WDILR9>G8OAI%5b%21%2b%21%5d</WDILR9> & sign-in.email=sample%40email.tst

you will see the email sent 
and that is allowing the attacker to access any cookies or session tokens retained by the browser. 

Response

HTTP/1.1 400 Bad Request
Content-Type: application/json; charset=UTF-8
Content-Length: 196
Connection: keep-alive
X-Xss-Protection: 1; mode=block
Content-Security-Policy: default-src 'self' liberapay.com;connect-src 'self' *.liberapay.org *.mangopay.com *.payline.com;form-action 'self';img-src * blob: data:;object-src 'none';report-uri https://liberapay.report-uri.com/r/d/csp/enforce;upgrade-insecure-requests;
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Set-Cookie: csrf_token=oiCrDqa91GRS4YBFb4jzZQzpgxSZN38I; Domain=.liberapay.com; expires=Sun, 17 Jun 2018 00:42:27 GMT; Path=/; SameSite=lax; secure
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 4287cc50ea852744-FRA

## Impact

Cross site scripting (also referred to as XSS) is a vulnerability that allows an attacker to send malicious code (usually in the form of Javascript) to another user. Because a browser cannot know if the script should be trusted or not, it will execute the script in the user context allowing the attacker to access any cookies or session tokens retained by the browser.

## Attachments
No attachments
