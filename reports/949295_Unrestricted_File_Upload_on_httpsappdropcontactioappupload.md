# Unrestricted File Upload on https://app.dropcontact.io/app/upload/

## Report Details
- **Report ID**: 949295
- **URL**: https://hackerone.com/reports/949295
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-01T15:56:54.626Z
- **Disclosed**: 2020-08-11T10:45:15.009Z

## Reporter
- **Username**: omarelfarsaoui
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dropcontact

## Vulnerability Information
hi team,
 I found  Unrestricted File Upload Vulnerabilities on  https://app.dropcontact.io/app/upload/.

## Steps To Reproduce:

  1. Create an account in https://app.dropcontact.io/app/
  1. go to https://app.dropcontact.io/app/upload/
  1. try to upload html file , you will see message only (: .csv, .txt, .xls, .xlsx) allowed.
  1. change the HTML file extension to txt and try to upload it again 
  1. it work and the file successfully uploaded

## Supporting Material/References:
https://www.exploit-db.com/docs/english/45074-file-upload-restrictions-bypass.pdf
https://www.opswat.com/blog/file-upload-protection-best-practices

{F932903} 


## how to fix 
To avoid these types of file upload attacks: 
1. File type verification
1. Restrict specific file extensions 
1. add verification in both back-End and front-End

## Impact

this is not really impact because the app not report the full path for the files uploaded.
but if an attacker found a way to get the path . it wil be used to get attackes like xss or even rce .

Best Regards,
@omarelfarsaoui

## Attachments
- poc-2020-08-01_17.39.00.mp4
