# Credientals Over GET method in plain Text

## Report Details
- **Report ID**: 490899
- **URL**: https://hackerone.com/reports/490899
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-04T08:15:00.270Z
- **Disclosed**: 2019-02-17T17:48:57.512Z

## Reporter
- **Username**: d33van
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
Hi Team,

Description 
While I was testing the application i found this bug where the application is sending the credentials over Plain text in URL : https://auth.ratelimited.me/login?username=testqaz%40grr.la&password=D33vanh%40h%40h%40

Vulnerable URl https://auth.ratelimited.me

## Impact

Impact: if the application is sending the credentials over GET request it will be saved in the history of the Browser

## Attachments
- Credientals_Over_GET_method_in_plain_Text.PNG
- Credientals_over_GET_request_in_Plain_text.wmv
