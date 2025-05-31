# Private program email forwarding response invitation not expire after first use.

## Report Details
- **Report ID**: 209140
- **URL**: https://hackerone.com/reports/209140
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-26T17:03:34.500Z
- **Disclosed**: 2018-05-30T00:28:23.357Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi Hackerone Team,

Before i reported that email forwarding of private can be enumerated and any user join to private program here #201369 , __but this seems by design__, but now it i found a related issue which can cause a security impact on private program because the email forwarding response of `HackerOne` did not expire after first use.

**Description (Include Impact):**

If a user __Quits__ to a private program, this user can rejoined without the knowledge of private program owners, also you can check further if the user become Banned it seems that the linked on email still not expire and this can cause security implication if the banned user can rejoined to the program without the knowledge of the program owner, for reproduction steps please see below.

### Steps To Reproduce

1. Send a test mail to `█████████` which is private and have email forwarding setup.
2. Click and follow the link on the email response and you become auto invited to the program (intentional).
3. __NO NOT__ submit the test report (__means the email link already used, but you did not continue to submit the report, you are now participants to the program__).
4. Now Quit to the program.
5. Go to email and click the same link and you can get back without requesting another link (using submit report via email forwarding)

__Link on the email response of forwarding feature should expire after first use__
{F164319}

### Impact:

When the user quits, or if the program owner dicided to remove/banned the user on participating private program, the user should not get back unless the program owners decide to un-banned and the user/researcher gets invited again. 

### Mitigation:

The email forwarding feature should expire after it's first use, do not allow the attacker to reused the link to join to the program.

Please ask if you need more information.

Regards
Japz


## Attachments
No attachments
