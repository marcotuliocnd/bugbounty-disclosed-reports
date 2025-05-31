# Error Page Content Spoofing or Text Injection

## Report Details
- **Report ID**: 1196253
- **URL**: https://hackerone.com/reports/1196253
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-13T19:03:40.542Z
- **Disclosed**: 2021-06-15T23:51:36.681Z

## Reporter
- **Username**: g4urav_19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
i want to report a context spoofing or text injection at   api-cryptoeconomics.sifchain.finance and   market-data.sifchain.finance

steps to reproduce:
1: Just browse this target on any browser
2: Target:  https://api-cryptoeconomics.sifchain.finance/ 
3: Then add any text or content after the "/" , i added this content
4: For example: !!!ATENTION!This_server_is_on_Maintenance_please_go_to_WWW.EVIL.COM
5: Now browser reflect the content or text which you add in url.

Repeat the same process for https://market-data.sifchain.finance/

You can see also image which i had attached
F1300496
F1300495

## Impact

Fix & Mitigation:
Fix 404 error page to a new who not allow text content injection

## Attachments
- 2021-05-14_00_31_47-Error.png
- 2021-05-14_00_32_03-Error.png
