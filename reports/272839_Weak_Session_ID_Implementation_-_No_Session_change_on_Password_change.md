# Weak Session ID Implementation - No Session change on Password change

## Report Details
- **Report ID**: 272839
- **URL**: https://hackerone.com/reports/272839
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-28T21:50:41.561Z
- **Disclosed**: 2017-10-05T16:03:13.684Z

## Reporter
- **Username**: cosmopolitan_fi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
**Summary:** [Weak session id implementation]

**Description:** [Unikrn does not change session id after password is changed. Reusing same session ids, after password is changed is highly risky. 
Example scenario: Hacker has successfully brute forced the password of a victim and has access to the account. The victim notices that something's off and chooses to change the password of the account. Hacker has still full access to the account, even after the password is changed, because of the working session id that he got from the server when he logged in to the victim's account.]


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. [Intercept requests when logged in to unikrn and retrieve current session id]
  2. [Change the password of the user]
  3. [Do the step 1 again and compare the session id]

## Supporting Material/References:

If necessary, check my Proof of Concept video.

https://drive.google.com/file/d/0B28KqsVY5jK6aVdTYzg5RTNMcGM/view



## Attachments
No attachments
