# Harvesting all private invites using leave program fast-tracked invitation and security@ email forwarding feature

## Report Details
- **Report ID**: 334205
- **URL**: https://hackerone.com/reports/334205
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-06T11:26:21.381Z
- **Disclosed**: 2018-04-18T05:04:38.513Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi HackerOne,

**Summary:**

I have found a way that it is possible to harvest all private invitation using the new __Leave Program__ feature together with the `security@` email forwarding feature __without any user interaction__.

---

**Description:**

First, when the program activated the `security@` email forwarding on hackerone and the hacker sent an email to `security@company.com` which is activated, hackerone system will send an invite to hackers and this invite will allow hackerone to become a participants of private program.

Now, hackers can choose to leave to the program in __exchange__ of another automated invite when the hackers filled-up the leave program survey form using the new __Leave Program__ functionality. (see image below)

{F282541}


---
### Now how to exploit it ? , very easy.. hackerone will do it for you fully automated without any user interaction
---

### Steps To Reproduce

Assumes that you don't have any invites (as in 0 invites)

  1. First step you have to find program with `security@` email forwarding enabled on hackerone, this is easy just go to https://hackerone.com/bug-bounty-programs, click all the program and send a test email to their declared `security at` email on their public page, if you received a response to submit your bug, then that means `security@` is activated in hackerone.  
███████

  2. Lets take `███████`, send a test mail to that address
  3. You will received an invitation email via `security@` email forwarding feature.
  4. Click the __Submit Vulnerability__ , you are now a participants.
  5. Now leave the program and fill-up the leave survey then confirm leave.
  7. You'll be fast-tracked for invites, invitation will come most likely arriving in the next 24 hours as stated.
  8. __REPEAT STEP 2 to 7__ after getting a new invite came from fast-tracked invites.

__NOTE:__ Ask more information if you are having trouble understanding my submission.__

But this is easy to exploit, just send an email to: `██████ > get invites > leave to ██████████ > get new invites came from fast-tracked > repeat`

## Impact

An attacker can harvest all private invitation without any user interaction, in a matter of few months you can have 100+ private invitation by just daily repeating the steps i provided above.

__INVITES ALL YOU CAN__

Let me know if you need more information.

Cheers
Japz

## Attachments
- invitation_queu.JPG
