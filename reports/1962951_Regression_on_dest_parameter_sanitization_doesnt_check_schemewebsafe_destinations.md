# Regression on dest parameter sanitization doesn't check scheme/websafe destinations

## Report Details
- **Report ID**: 1962951
- **URL**: https://hackerone.com/reports/1962951
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-27T01:00:35.756Z
- **Disclosed**: 2023-06-03T14:15:34.096Z

## Reporter
- **Username**: mrzheev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hi team, I get Xss via javascript:alert() url on login page parameter dest=

###Payload Url Xss : 
```javascript:alert(document.domain);```

##XSS Javascript URL
###Steps and reproduction :

- Using a browser, navigate to: https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F
- Copy and modify the "dest" parameters so that the URL redirects to dest=javascript:alert(document.domain);
- Send this in a new browser window and after login you will get a pop up (Xss Triggered).

##Proof of Concept (PoC) :
https://www.reddit.com/login/?dest=javascript:alert(document.domain);


{F2316733}


Reference :
https://brightsec.com/blog/open-redirect-vulnerabilities/
https://hackerone.com/reports/1930763

## Impact

When an attacker manages to perform a redirect in JavaScript, many dangerous vulnerabilities may occur. As Open Redirects are mostly used in phishing scams, people are not aware of the fact that Open Redirects can also be part of more complex attack chains where multiple vulnerabilities are exploited. And JavaScript-based Open Redirect is a key part of that chain. For example, redirecting the user to javascript: something() ends up being a dangerous Cross-Site Scripting injection.
and the attacker can steal the victim's cookies

## Attachments
- bandicam_2023-04-27_03-15-21-520.mp4
