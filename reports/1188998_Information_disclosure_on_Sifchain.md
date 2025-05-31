#  Information disclosure on Sifchain

## Report Details
- **Report ID**: 1188998
- **URL**: https://hackerone.com/reports/1188998
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-08T12:50:53.537Z
- **Disclosed**: 2021-05-08T17:07:55.222Z

## Reporter
- **Username**: rohitburke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
Hello Team,
I have found user/admin usernames disclosed.
Using REST API, we can see all the WordPress users/authors with some of their information. (such as id, name, login name, etc.) and employees of Sifchain without authentication on https://sifchain.finance/

## Steps To Reproduce:
You can find the information disclosure by going to the following URL  (https://sifchain.finance/wp-json/wp/v2/users/)

 
## Supporting Material/References:
    1) https://hackerone.com/reports/753725
    2) https://hackerone.com/reports/138244

## Impact

1) Malicious users  could collect the usernames disclosed and be focused throughout BF (bruteforce) attack (as the usernames are now known), making it less harder to penetrate the systems.
2) Therefore this information can be used to do bruteforce login.

## Attachments
- Screenshot_(18).png
- Screenshot_(12)_LI.jpg
- recording-1620478143075.webm
