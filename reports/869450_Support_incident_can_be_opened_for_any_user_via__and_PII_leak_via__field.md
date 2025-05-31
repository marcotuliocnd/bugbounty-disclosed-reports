# Support incident can be opened for any user via /███████ and PII leak via █████████ field

## Report Details
- **Report ID**: 869450
- **URL**: https://hackerone.com/reports/869450
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-09T07:35:40.751Z
- **Disclosed**: 2021-02-18T19:05:02.147Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A malicious user can open an incident for any user via the ████/████████ page. This would allow the attacker to trick the victim into taking actions such as clicking a link or opening a file that has been attached to the incident.

## Impact
A victim could be tricked into visiting a link, opening a file, or sending PII to the attacker via the incident. Because the attacker opened the incident, they can see all comments left by the victim.

## Step-by-step Reproduction Instructions

1. Browse to ████ and create an account or login.
2. Browse to ██████████/█████████. You will be able to create an incident on this page.
3. In the `█████████` field, you can select any user you want to assign the incident to. The `i` button beside the caller field also allows you to view various PII about the user.
███████
██████
4. You can attach files in the top right corner using the attachment button.
5. Once you have chosen a victim (`██████`) and filled in the `additional comments` section with your phishing message, you can click `Submit` in the top right corner.
██████
6. Browse to ███████/home.do and you can see a list of your open incidents. You may need to filter by `All`. 
7. Click the incident that you assigned to the victim. 
███████
8. You can now use this page to monitor the victims response. This could be used to communicate with the victim, posing as an administrator and soliciting PII or causing other malicious effects.
█████████
9. The victim will receive an e-mail that the incident has been submitted on their behalf. Once they log-in, they will see the following:
██████████
███████
10. Obviously an adversary would create an account posing as an Air University administrator or something believable, but here is what a phishing attempt could look like using this vulnerability:
███
11. Meanwhile, the attacker is monitoring the incident waiting on the victim to respond and can even see when the victim has viewed the incident.
███

## Suggested Mitigation/Remediation Actions
This feature should be locked down to administrative access only. Regular users should not be allowed to submit tickets directly to other users or view other users PII.

## Impact

A victim could be tricked into visiting a link, opening a file, or sending PII to the attacker via the incident. Because the attacker opened the incident, they can see all comments left by the victim.

## Attachments
No attachments
