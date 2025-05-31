# CSV Injection at https://assets-paris-demo.codefi.network/

## Report Details
- **Report ID**: 1748961
- **URL**: https://hackerone.com/reports/1748961
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-25T08:59:53.872Z
- **Disclosed**: 2023-01-04T08:49:17.703Z

## Reporter
- **Username**: 0xjackal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: consensys

## Vulnerability Information
## Summary:
Hi consensys Security Team.

I have found CSV Injection when generate report at https://assets-paris-demo.codefi.network/

CSV Injection, also known as Formula Injection, occurs when websites embed untrusted input inside CSV files.
When a spreadsheet program such as Microsoft Excel or LibreOffice Calc is used to open a CSV, any cells starting with = will be interpreted by the software as a formula. Maliciously crafted formulas can be used for three key attacks:

    - Hijacking the user’s computer by exploiting vulnerabilities in the spreadsheet software, such as CVE-2014-3524.
    - Hijacking the user’s computer by exploiting the user’s tendency to ignore security warnings in spreadsheets that they downloaded from their own website.
    - Exfiltrating contents from the spreadsheet, or other open spreadsheets.


## Steps To Reproduce:
1. Create an account at https://assets-paris-demo.codefi.network/ 
2. Go to Client management
3. Create new client 
4. At Client name* Put this paylaod:- `=cmd|' /C notepad'!'A1'`
5. After create new client Download the data.

## Supporting Material/References:

{F2002581}

##Similar valid reports at hackerone:-
   - https://hackerone.com/reports/118582
   - https://hackerone.com/reports/223344
   - https://hackerone.com/reports/386116

Please let me know if need more info.
Best Regards.
@doosec101

## Impact

This vulnerability can be harm for normal user because if malicious user injected any malicious script in token note and when customer user download CSV file then inserted command directly runs when CSV file open.

##FIX:-
    Prefix =, +, - and @ symbols with a ' in issues when exporting them to a .csv file.

## Attachments
- bandicam_2022-10-25_10-50-26-062.mp4
