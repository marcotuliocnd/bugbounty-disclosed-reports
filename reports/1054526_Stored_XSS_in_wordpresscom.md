# Stored XSS in wordpress.com

## Report Details
- **Report ID**: 1054526
- **URL**: https://hackerone.com/reports/1054526
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-09T02:09:07.615Z
- **Disclosed**: 2021-02-17T09:44:34.456Z

## Reporter
- **Username**: ucuping
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hello Team,
I found the Stored XSS vulnerability in the Custom Style section, this vulnerability can result in an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, performing requests in the name of the victim or for phishing attacks, by inviting the victim to become part of the manager or administrator.

## Platform(s) Affected:
wordpress.com

## Steps To Reproduce:
1. As an attacker, go to the feedback section, then go to the Polling section.
2. Add a new post or edit an existing post.
3. Scroll down, click All Styles.
4. Add a new Style.
5. Named the temporary style, click Save Style.
6. Change the Style Name with <noscript><p title= "</noscript><img src=x onerror=alert(document.cookie)>">, check the checkbox next to Save Style, click Save Style.
7. Script will be run.
8. Invite the victim in a way, go to manage then users.
9. Click invite, enter username or email, and send.
10. As a Victim, accept the attacker's invitation.
11. Go to the Feedback section.
12. Then go to the Polling section.
13. Add a new post or edit an existing post.
14. Scroll down, click All Styles.
15. Enter the Style that has been created by the previous Attacker.
16. Script will be run.

## Supporting Material/References:
F1109567
F1109568
F1109569

## Impact

this vulnerability can result in an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, performing requests in the name of the victim or for phishing attacks, by inviting the victim to become part of the manager or administrator.

## Attachments
- Screenshot_(538).png
- Screenshot_(539).png
- 2020-12-09_08-24-14.mp4
