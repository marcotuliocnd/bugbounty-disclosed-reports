# Rate limit missing sign-in page

## Report Details
- **Report ID**: 1285441
- **URL**: https://hackerone.com/reports/1285441
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-31T11:16:29.103Z
- **Disclosed**: 2023-07-11T19:58:37.558Z

## Reporter
- **Username**: dreamer_eh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
Hello there,

A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works.

The sign-in page where brute force is enabled and there is no rate limit: **https://metdata.tva.gov/**

I made 1.5k+ requests but still, the server is not blocking my requests.

* F1395048 

##Steps To Reproduce:
* Burp suite to brute forcing on the sign-in page.

## Impact

Attackers are able to access NTID and password.

## Attachments
- image.png
