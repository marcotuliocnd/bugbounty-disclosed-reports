# HTML injection in review content

## Report Details
- **Report ID**: 1036995
- **URL**: https://hackerone.com/reports/1036995
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-11-17T19:30:39.938Z
- **Disclosed**: 2021-12-17T17:44:06.122Z

## Reporter
- **Username**: 0xteles
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
Hi Judge Security Team, 

I found a HTML Injection in review parameter at the https://judgeme-pentest.myshopify.com/products/pentest and at the judge.me

###Steps

1. Go to https://judgeme-pentest.myshopify.com/products/pentest
2. Click on "Write Review"
3. fill in the fields normally. 

{F1083621}

4.  Now, go to your profile review in the judge.me
5. Edit your Review
6. In Review body, enter this payload: ``` <a href=https://google.com/>CLICK HERE</a>```
7. Save and go to  https://judgeme-pentest.myshopify.com/products/pentest 

{F1083622}

8. Boyaah. 

{F1083623}

## Impact

the attacker can insert HTML codes on the page

## Attachments
- poc1.png
- poc2.png
- poc3.png
