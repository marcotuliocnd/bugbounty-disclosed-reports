# [█████] Reflected GET XSS  (/personnel.php?...&rcnum=*) with mouse action

## Report Details
- **Report ID**: 648348
- **URL**: https://hackerone.com/reports/648348
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-17T21:26:41.188Z
- **Disclosed**: 2019-12-02T19:28:17.055Z

## Reporter
- **Username**: jarvis0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
I will combine this vulnerability with this vulnerability (described in this report #648222). If you have not read this report, I recommend reading that report first, and then studying this report.

##### I want to note that this report cannot be closed as a duplicate to the above described report. why? because this vulnerability exists for authorized users. Using the bypass authorization bug I just had the opportunity to explore the internal structure of the site.

If you study the last report, as well as the reports that you described there, you can understand that the developers have already tried to fix some vulnerabilities by simply restricting access to the site. It was not effective. It is strongly recommended to fix each vulnerability separately.

### Steps to reproduce

1) Turn on Live Interception in burp (Proxy-Intercept) Go to this link
> https://█████████/personnel.php?content=training&folder=FA_CERT&item=FA05.01.01&rcnum='%20onmouseover=alert('jarvis7')%20'

2) Intercept request. Press right mouse button-> Do intercept -> Response this request
{F531647}

3) Delete this redirection
{F531649}

Answer:
███

4) Then you need move the mouse cursor to 2 icons near text:
████

Result:
████

#### This is not duplicate to this report #648305 ! Because I already submit one of XSS, this - #512269 moth ago, but as you can see, I can inject payloads in other places now.

## Impact

JavaScript can still be dangerous if misused as part of malicious content:

-  Malicious JavaScript has access to all the objects that the rest of the web page has access to. This includes access to the user’s cookies. Cookies are often used to store session tokens. If an attacker can obtain a user’s session cookie, they can impersonate that user, perform actions on behalf of the user, and gain access to the user’s sensitive data.
- JavaScript can read the browser DOM and make arbitrary modifications to it. Luckily, this is only possible within the page where JavaScript is running.
- JavaScript can use the XMLHttpRequest object to send HTTP requests with arbitrary content to arbitrary destinations.
- JavaScript in modern browsers can use HTML5 APIs. For example, it can gain access to the user’s geolocation, webcam, microphone, and even specific files from the user’s file system. Most of these APIs require user opt-in, but the attacker can use social engineering to go around that limitation.

## Attachments
No attachments
