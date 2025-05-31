# Missing CSRF Protection in  /stats EndPoint.

## Report Details
- **Report ID**: 415350
- **URL**: https://hackerone.com/reports/415350
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-09-27T16:46:30.865Z
- **Disclosed**: 2018-10-09T00:14:14.151Z

## Reporter
- **Username**: kaustubh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##EndPoint /affiliates/stats. doesnot verify the CSRF Tokens##


## Steps To Reproduce:

 1. Login with the your account 
 2. Navigate to the URL https://chaturbate.com/affiliates/stats.. 
 3. Check the stats in default its todays date or this week in select period.
4. Intercept the request and change the parameter to whatever you want to set.
5. generate the POC And open it in browser
6. You can see the changes in the form.

## Supporting Material/References:
Please find attached for the CSRF POC and CSRF_1 for PreCSRF And CSRF_2 For Post CSRF.

## Impact

Attacker may change the parameters in stat or may force user to download the malicious .

## Attachments
- Csrf.html
- csrf_1.png
- csrf_2.png
