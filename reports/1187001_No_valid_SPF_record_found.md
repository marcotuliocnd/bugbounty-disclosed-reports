# No valid SPF record found

## Report Details
- **Report ID**: 1187001
- **URL**: https://hackerone.com/reports/1187001
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-05-06T19:21:41.532Z
- **Disclosed**: 2021-12-09T19:17:54.444Z

## Reporter
- **Username**: tamilarasi11
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Email spoofing is possible

To verify:
visit : https://www.kitterman.com/spf/validate.html and type your domain name to check SPF records
you can see the results as: No valid SPF record found.

POC:
1. visit: https://emkei.cz/
2. fill the from email as help@sifchain.finance
3.To email as victim email address, enter subject, data and click send.
4. you will receive the email in your inbox

## Impact

Email spoofing

## Attachments
- Screenshot_(9).png
- Screenshot_(11).png
