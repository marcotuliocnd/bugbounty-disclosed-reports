# Insecure ███████ credentials on staging app at ████ leads to application takeover

## Report Details
- **Report ID**: 1051885
- **URL**: https://hackerone.com/reports/1051885
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-07T03:22:46.281Z
- **Disclosed**: 2021-02-10T21:03:16.766Z

## Reporter
- **Username**: skarsom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A ██████████ application called "████" has an old endpoint that accepts insecure/test ████████ credentials despite being a publicly-accessible IP. This endpoint also provides the ability to view information that may be FOUO, to exfiltrate information on registered personnel or contractors, to upload files, and to change configuration settings with ███████████████ privileges.

**Description:**
The IP address ███ points to a deployment of an application called ████/█████, which is a DoD-owned system on █████████). The login for this deployment accepts insecure ███ credentials (███).

There is also an authentication/█████ panel accessible at https://██████████externally accessible with these credentials.

The ████████ system available through this login includes file upload features, data exfiltration and management, workspace management, and infrastructure management.

The ██████████ / authentication █████████istration system available through this login includes file import/export privileges, user management, RBAC management, HTTP header management, OAuth credential management, session management, and frankly anything else you can think of that would be in an ████████ panel.

████████ frontend:
#███████
#██████
#█████

███████ backend:
#███
#█████████
#█████
#██████
#██████

## Step-by-step Reproduction Instructions
1. Navigate to https://████
2. Enter the username "██████" and the password "██████████"
3. After logging in, click "Launch" under ██████
4. Navigate to https://███████████
5. Enter the username "███" and the password "█████████"

## Product, Version, and Configuration (If applicable)
████████████
███
Build Date: 25 November 2020

## Suggested Mitigation/Remediation Actions
1. Immediately disable insecure ███████████████ credentials.
2. I would recommend preventing external access to the ████████ █████████ portal/requiring CAC as a best practice.

## Impact

An unauthorized attacker can exfiltrate intelligence and personnel information stored in a staging █████/█████.
An unauthorized attacker can modify, insert, and delete intelligence and personnel information stored in a staging ████████/███████.

An unauthorized attacker can exfiltrate, modify, upload to, download from, and/or deny access to a staging ██████ environment through the ██████ ████ panel. 

I did not feel comfortable seeing whether I could escalate file uploads to an RCE before getting DOD consent.

## Attachments
No attachments
