# [https://█████████/]&&[https://█████████/] Open Redirection

## Report Details
- **Report ID**: 537047
- **URL**: https://hackerone.com/reports/537047
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-12T22:30:05.170Z
- **Disclosed**: 2022-03-22T11:53:42.330Z

## Reporter
- **Username**: mandark
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lyst

## Vulnerability Information
***Summary***

Hi Team,

An attacker can redirect vicitm on an external website using ``https://████/account/login``  endpoint because ``next`` parameter is not being validated properly.

***Affected URL***

`https://███/account/login/?next=///////////////////////////evil.com`

***Steps to Reproduce***

1) Go https://████/account/login/?next=%2Fapp%2F .
2) Add this payload `////////////////////////////evil.com` to the `?next=` parameter .
3) Registeran account in the normal way .
4) You will be redirected to evil.com website .

***POC***
{F467696}

***References***

* https://hackerone.com/reports/347645
* https://hackerone.com/reports/125003
* https://hackerone.com/reports/411723

## Impact

* Open redirects allow a malicious attacker to redirect people unknowingly to a malicious
website .
* Simplifies phishing attacks .

## Attachments
- 2019-04-13_00-26-10.mp4
