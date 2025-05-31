# Reflected XSS on ███████

## Report Details
- **Report ID**: 971360
- **URL**: https://hackerone.com/reports/971360
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-31T15:56:07.082Z
- **Disclosed**: 2020-09-03T17:20:00.027Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary**:
Reflected Cross site Scripting (XSS) on████leaving.html?url=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

**Steps To Reproduce**:
1. Navigate to███leaving.html?url=
2. Enter a crafted XSS payload like "><script>alert("xss by nagli")</script>
3. Alert will pop :-)

█████████

**How can the system be exploited with this bug?**
The attacker can execute JS code, which could lead to stealing cookies and full account takeover.

**Recommendations for fix**
Content based escaping on the users input, in this case on the redirect parameter.

**Best Regards,**
nagli

## Impact

Attacker can execute JS code on the Victim Behalf.

## Attachments
No attachments
