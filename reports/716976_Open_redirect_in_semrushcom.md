# Open redirect in semrush.com

## Report Details
- **Report ID**: 716976
- **URL**: https://hackerone.com/reports/716976
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-18T00:33:49.162Z
- **Disclosed**: 2019-10-25T14:54:22.105Z

## Reporter
- **Username**: batuhanu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
**Summary:** 
There is an open redirect on https://www.semrush.com/login/?redirect_to=.
By using /\ at the start of the link, you can bypass the open redirect filter.

**Description:** 
An attacker can control the value of the "redirect_to" parameter and make it redirect to a malicious endpoint.

## Steps To Reproduce:
Visit: `www.semrush.com/login/?redirect_to=/\google.com`
Once you login, you will be redirected to google.com

## Impact

This vulnerability can be used for phishing attacks

## Attachments
No attachments
