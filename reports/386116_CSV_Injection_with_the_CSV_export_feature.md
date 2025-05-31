# CSV Injection with the CSV export feature

## Report Details
- **Report ID**: 386116
- **URL**: https://hackerone.com/reports/386116
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-24T06:11:19.552Z
- **Disclosed**: 2018-09-20T00:05:50.076Z

## Reporter
- **Username**: hackaccinocraft
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hi there,

hope you are well,

The "Download as a CSV" feature of ``` does not properly "escape" fields. So that particular field is vulnerable to CSV injection.

**Steps of POC**

Step 1 : Go to any chat room and donate any token to some and in note insert ```=4+4```.
Step 2 : Now go to on this link and download transaction history. 
Step 3 : Download file as CSV and open it you can =4+4 become 8 so it's prove CSV injection.

**POC video**
███

Malicious user can take big advantage of this vulnerability because from that vulnerability we can run base OS command on any anonymous user account.

**Prevention**
Strip "=" only, it's not foolproof fix, see this report [#72785](https://hackerone.com/reports/72785) you have to strip +/-/@ and | as well.

Reference,

https://hackerone.com/reports/72785
https://hackerone.com/reports/223344
https://hackerone.com/reports/244292

Please let me know if you want more information regarding this report.

Cheers, 
Ninjan

## Impact

This vulnerability can be harm for normal user because if malicious user injected any malicious script in token note and when customer user download CSV file then inserted command directly runs when CSV file open.

## Attachments
No attachments
