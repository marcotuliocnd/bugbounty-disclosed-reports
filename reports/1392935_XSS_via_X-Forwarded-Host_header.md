# XSS via X-Forwarded-Host header

## Report Details
- **Report ID**: 1392935
- **URL**: https://hackerone.com/reports/1392935
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-06T15:34:40.467Z
- **Disclosed**: 2022-01-29T13:18:29.225Z

## Reporter
- **Username**: oblivionlight
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
Summary:
The https://www.omise.co/ website is vulnerable to a cross-site scripting flaw if the server receives a crafted X-Forwarded-Host header.

Description:
The server reads data directly from the HTTP request and reflects it back in the HTTP response. Reflected XSS exploits occur when an attacker causes a victim to supply dangerous content to a vulnerable web application, which is then reflected back to the victim and executed by the web browser. The most common mechanism for delivering malicious content is to include it as a parameter in a URL that is posted publicly or e-mailed directly to the victim. URLs constructed in this manner constitute the core of many phishing schemes, whereby an attacker convinces a victim to visit a URL that refers to a vulnerable site. After the site reflects the attacker's content back to the victim, the content is executed by the victim's browser.


Steps To Reproduce:
Original Link - https://www.omise.co/

 1. Visit https://www.omise.co/ capture the request in Intercept 
 2. Send the request to Repeater add X-Forwarded-Host: bing.com"><img src/onerror=prompt(document.cookie)>  below Host: www.omise.co
 3. The JavaScript alert box displays some cookie information. 

Mitigation:
Ignore invalid browser headers. Filter metacharacters from user input.

POC:
Attached Video.

## Impact

This flaw allows attackers to pass rogue JavaScript to unsuspecting users. The user’s browser has no way to know the script should not be trusted, so it will execute the script and because the browser thinks the script came from a trusted source, aka your website, a malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with your site. These scripts can even rewrite the content of the HTML page.

## Attachments
- recording-1636212632887.webm
