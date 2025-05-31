# Cleartext Password returned in JSON response

## Report Details
- **Report ID**: 215083
- **URL**: https://hackerone.com/reports/215083
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-21T12:12:03.109Z
- **Disclosed**: 2018-03-04T06:36:23.833Z

## Reporter
- **Username**: ryudox
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pushwoosh

## Vulnerability Information
Password was returned in the JSON response (For changing of password), which could be recovered by accessing the firefox.exe memory dump. The password string is persistent in the RAM (even after restarting Firefox application) until you restart the computer.

Refer to the .docx for more information

## Attachments
- Pushwoosh_password_disclosure_in_JSON_response.docx
