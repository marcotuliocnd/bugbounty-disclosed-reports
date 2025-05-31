# Impersonation of Wakatime user using Invitation functionality.

## Report Details
- **Report ID**: 257119
- **URL**: https://hackerone.com/reports/257119
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-05T17:48:46.378Z
- **Disclosed**: 2017-08-06T16:20:38.921Z

## Reporter
- **Username**: asaxena2190
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi wakatime team,

I have found a vulnerability in your leaderboard invitation functionality which can be used to trick the victims on the name of wakatime. 

Anyone can sign up with any email id and use the leadersboard invitation to invite anyone. This loophole can be leveraged for impersonation of any user to the victims. 

Eg. If bob steave is the name of Alice's boss. Then Attacker can create a wakatime account with his Bob's real id like bob.steave@gmail.com and without confirming his this email address he can send the invitation to Alice. Now there is no doubt Alice will accept the invitation as well as he will perform the all steps provided by that invitation mail. Which can be done by the above vulnerability.

**Description:** Wakatime have a feature in which a user can invite anyone to his leaderboard. There are 3 fields Name , Email Id and role. But the Name field should be restricted to maximum 20 words. But wakatime is allowing 200 characters to this field. Which can be enough to construct a completely different mail.

**Steps to reproduce:**
1. Login into the account.
2. Create a leaderboard.
3. Invite a victim without verifying email address.
4. Invitation email will be successfully sent.(Vulnerability 1)
4. In name field write some social engineering message.
5. Input victim's Email Id 
6. Invite him.
7. He will receive the mail which is constructed by attacker with some social engineering method on the name of wakatime.
8. If victim is already a member of wakatime, he can be tricked to steal his information. (Vulnerability 2)

**Browser:** Tried on three browser.

**Fix:** 
Limit the name field to max 20 or 25.

Screen shot is attached.
Please check it.

Thanks,
Akash Saxena

## Attachments
- Screenshot_20170804-232946.png
- Screenshot_20170804-231952.png
