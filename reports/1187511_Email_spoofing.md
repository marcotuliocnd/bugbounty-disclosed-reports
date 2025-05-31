# Email spoofing

## Report Details
- **Report ID**: 1187511
- **URL**: https://hackerone.com/reports/1187511
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-07T06:14:37.621Z
- **Disclosed**: 2021-05-13T10:20:43.792Z

## Reporter
- **Username**: tmsm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Email spoofing is possible
To verify:
visit :https://www.kitterman.com/spf/validate.html? and type your domain name to check SPF record 
you can see the results as: NO valid SPF record found
POC:
1.visit http://emkei.cz//
2.fill the from email as admin@sifchain.finance
3.to email as victim email address, enter subject, data and click send
4.you will receive the mail in your inbox

## Impact

email spoofing

## Attachments
- POC_sifchain.finance.PNG
- POC_1sifchain.finance.PNG
