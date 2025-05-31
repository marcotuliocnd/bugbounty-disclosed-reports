# Disclose any user's private email through API

## Report Details
- **Report ID**: 196655
- **URL**: https://hackerone.com/reports/196655
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-08T02:06:07.300Z
- **Disclosed**: 2017-02-24T18:52:55.777Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
#Description:
I have found a security vulnerability that allows an attacker to disclose any user's private email.
An attacker can disclose any user's private email by creating a sandbox program then adding that user to a report as a participant.
Now if the attacker issued a request to fetch the report through the API , the response will contain the invited user private email at the activities object.


#Steps to reproduce:
1. Go to any report submitted to your program. 
2. Add the victim username as a participant to your report.
3. Generate an API token.
4. Fetch the report through the API

```
curl "https://api.hackerone.com/v1/reports/[report_id]" \
  -u "api_idetifier:token"
```
The response will contain the invited user email at the `activities` object:
```json
"activities":{"data":[{"type":"activity-external-user-invited","id":"1406712","attributes":{"message":null,"created_at":"2017-01-08T01:57:27.614Z","updated_at":"2017-01-08T01:57:27.614Z","internal":true,"email":"<victim's_email@example.com>"}
```



## Attachments
No attachments
