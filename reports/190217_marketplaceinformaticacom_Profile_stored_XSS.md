# [marketplace.informatica.com] Profile stored XSS

## Report Details
- **Report ID**: 190217
- **URL**: https://hackerone.com/reports/190217
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-10T22:21:44.175Z
- **Disclosed**: 2017-04-19T17:39:07.985Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
The user name and lastname are inserted into JS with quotes non-escaped:

```javascript
var pageNameDTM = "%name% %lastname%".replace(/[^a-zA-Z0-9 ]/g, "").replace(/  +/g, " ");
```

**PoC:**

1. Log into your account
2. Set your name and lastname to **"-alert(document.domain)-"**
3. Open your profile page https://marketplace.informatica.com/people/%email% from another account

The script will be executed:

{F142515}

## Attachments
- inf_mp_xss.png
