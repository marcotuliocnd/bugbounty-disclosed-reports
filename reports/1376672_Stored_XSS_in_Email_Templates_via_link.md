# Stored XSS in Email Templates via link

## Report Details
- **Report ID**: 1376672
- **URL**: https://hackerone.com/reports/1376672
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-20T22:12:22.509Z
- **Disclosed**: 2021-11-18T06:05:44.136Z

## Reporter
- **Username**: rioncool22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
## Summary:
Stored cross-site scripting (also known as second-order or persistent XSS) arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way.

## FYI:
I Install judge.me in Shopify E-Commerce

## Steps To Reproduce:

  1.  Go to `Requests > Email Templates`

{F1488407}

  2. Click `New Templates`

{F1488408}

3. Edit this block 

{F1488410}

4. Insert Link with XSS payload (See image below)

{F1488413}

5. Then save email
6. To trigger the XSS, you can click `Click Here` text

{F1488415}

## Impact

Session Hijacking, Cookie Stealing

## Attachments
- Screenshot_194.png
- Screenshot_195.png
- Screenshot_196.png
- Screenshot_197.png
- Screenshot_198.png
