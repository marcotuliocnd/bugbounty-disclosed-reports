# Html Injection and Possible XSS in main nordvpn.com domain

## Report Details
- **Report ID**: 780632
- **URL**: https://hackerone.com/reports/780632
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-22T16:20:26.412Z
- **Disclosed**: 2020-02-21T11:28:56.877Z

## Reporter
- **Username**: kiriknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary:
HTML injection in main domain can allow hackers forward users to any another domain. Also, if anybody can find method to bypass cloudflare filter hackers can steak cookie with with vuln 

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Go to https://nordvpn.com/blog/?1%25%32%32%25%33%65%25%33%63%25%32%66%25%36%31%25%33%65%25%33%63%25%36%31%25%30%63href%25%33%64%25%32%32http://3232235777
  2. Check, that links on the bottom of page goes to 192.168.1.1
   {F692879}

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

The vulnerability allow a malicious user to inject html tags and (possible) execute Javascript which could lead to steal user's session

## Attachments
- Screenshot_2020-01-22_19-14-54.png
