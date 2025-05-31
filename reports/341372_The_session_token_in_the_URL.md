# The session token in the URL

## Report Details
- **Report ID**: 341372
- **URL**: https://hackerone.com/reports/341372
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-20T18:56:18.265Z
- **Disclosed**: 2018-06-19T18:29:37.399Z

## Reporter
- **Username**: mandark
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello team 
I found that tat the URL transport the Session token and it's a sentive information so Placing session tokens into the URL increases the risk that they will be captured by an attacker.
###fix
Applications should use an alternative mechanism for transmitting session tokens, such as HTTP cookies or hidden fields in forms that are submitted using the POST method.

## Impact

an attacker can capture these tokens

## Attachments
- 1.PNG
