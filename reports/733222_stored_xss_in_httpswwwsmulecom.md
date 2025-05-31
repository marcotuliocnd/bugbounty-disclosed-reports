# stored xss in https://www.smule.com

## Report Details
- **Report ID**: 733222
- **URL**: https://hackerone.com/reports/733222
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-09T19:42:41.298Z
- **Disclosed**: 2019-11-12T18:40:38.926Z

## Reporter
- **Username**: hami
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: smule

## Vulnerability Information
hi team ,
I found a stored xss in www.smule.com

**Summary:** [add summary of the vulnerability]

The most damaging type of XSS is Stored XSS (Persistent XSS). An attacker uses Stored XSS to inject malicious content (referred to as the payload), most often JavaScript code, into the target application. If there is no input validation, this malicious code is permanently stored (persisted) by the target application, for example within a database. For example, an attacker may enter a malicious script into a user input field such as a blog comment field or in a forum post.

When a victim opens the affected web page in a browser, the XSS attack payload is served to the victim’s browser as part of the HTML code (just like a legitimate comment would). This means that victims will end up executing the malicious script once the page is viewed in their browser
##details :

parameter vulnerable :Blurb, Location and Name ,this all vulnerable to xss

payload:"></script><script>alert(document.cookie)</script>
payload 2:</script><script>akert(1)</script>

## Steps To Reproduce:
       
    1- login and go to settings
    2- add payload to field Blurb
    3- refresh page
    4- xss will pop up

## poc : in video below

## Impact

Stealing cookies.
can lead to user's Session Hijacking.
can also lead to disclosure of sensitive data.
and more

## Attachments
No attachments
