# Stored XSS through name / last name on https://██████████/

## Report Details
- **Report ID**: 1072616
- **URL**: https://hackerone.com/reports/1072616
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-06T09:28:37.657Z
- **Disclosed**: 2021-03-11T20:53:52.354Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
There is stored XSS Vulnerability on https://█████/██████ by rendering unsafe input being registered on the account name and last name.

███


## Step-by-step Reproduction Instructions

1. Navigate to 
```javascript
https://█████/login/?next=/███%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252F████████%252Fcgi%252Flogin.cgi%253Freturn_to%253Dhttps%25253A%25252F%25252F███████%25252Fcgi%25252Fmyaccount.cgi%26client_id%3D6G3AXPQNPXK5SVESYCB8AMCPHQQ3ENCRK8G2QNWY%26state%3DBEAEb6NGMQ7kWZwZS2pNNFv4p7JwBk86%26scope%3Dopenid%2520profile
```
2. Create your account, with your name as <IMG SRC=X ONERROR=ALERT(1)>
3. Log in and navigate to https://███/██████

## Suggested Mitigation/Remediation Actions

Sanitizing the input on the account name fields will prevent the issue.

##Best Regards
nagli

## Impact

Executing javascript on behalf of the victim

## Attachments
No attachments
