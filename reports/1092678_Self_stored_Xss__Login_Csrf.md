# Self stored Xss + Login Csrf

## Report Details
- **Report ID**: 1092678
- **URL**: https://hackerone.com/reports/1092678
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-02T06:49:38.518Z
- **Disclosed**: 2021-06-30T20:45:12.512Z

## Reporter
- **Username**: biest
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
User can set username between 8-20 alphanumeric characters, but with the help of inspect element attacker can manipulate ```██████=``` & can insert a  xss payload resulting in self stored xss & with the help of  login csrf  attacker can force the victim into attacker's account causing successful execution of javascript.

█████████

Payload used = ```"><img src onerror=confirm(document.cookie)>```

## Impact

Able to execute javascript in victim's browser

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit [Sign in](███████) and sign in
2. Click on Change username -->  Open inspect element --> change max length of new username and confirm username to ```100```
3. Now enter the payload in``` new username```  and  ```confirm username``` field & click on submit --> Sign out
4.  Enter the credentials to sign in --> Intercept request using burp --> Action --> Engagement Tools --> Generate Csrf poc --> Copy html.
5. Open notepad & paste --> save as .html file
6. Open the html file in any browser to confirm the vulnerability.

Poc attached :-

███████

## Suggested Mitigation/Remediation Actions
Sanitization of input must be done



## Attachments
No attachments
