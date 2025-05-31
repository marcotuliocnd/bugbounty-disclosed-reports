# Clickjacking on donation page

## Report Details
- **Report ID**: 921709
- **URL**: https://hackerone.com/reports/921709
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-07-12T21:52:04.959Z
- **Disclosed**: 2020-07-16T11:25:16.069Z

## Reporter
- **Username**: b0d8e6c576cada9bb87be7b
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:

Vulnerable URL: https://wordpressfoundation.org/donate/

Clickjacking on the vulnerable URL allows an attacker to redirect a victim to do a donation at an attacker's page.

## Steps To Reproduce:

1)  To test whether the page is vulnerable to clickjacking or not use this code

<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="5">
<title>i Frame</title>
</head>
<body>
<center><h1>THIS PAGE IS VULNERABLE TO CLICKJACKING</h1>
<iframe src="https://wordpressfoundation.org/donate/" frameborder="0 px" height="1200px" width="1920px"></iframe>
</center>
</body>
</html>

2) To test whether an attacker is able to trick the victim to donate money to the attacker's payment gateway
             i) Open the attached page "donation.html "
             ii) Click on the button give once
             iii) The page will be redirected to the attacker's PayPal money request page.

*Sorry for the bad UI and please remove my payment-request id after the vulnerability check from donation.html page.

## Recommendations

To control where your site can be embedded, use the frame-ancestors directive:
Content-Security-Policy: frame-ancestors 'none'  (The page cannot be displayed in a frame, regardless of the site attempting to do so.)
Content-Security-Policy: frame-ancestors 'self' (The page can only be displayed in a frame on the same origin as the page itself.)
Content-Security-Policy: frame-ancestors *uri* (The page can only be displayed in a frame on the specified origins.)

## Impact

If an attacker is successful in tricking the victim to a click jacked page. He can trick the victim to donate money to the attacker's account. An attacker may also craft a page to gather victim's information, He may use also use BEEF hook id to take control of victim's browser.

## Attachments
- donation.html
