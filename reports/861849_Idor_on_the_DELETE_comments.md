# Idor on the DELETE /comments/

## Report Details
- **Report ID**: 861849
- **URL**: https://hackerone.com/reports/861849
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-28T22:30:42.188Z
- **Disclosed**: 2020-05-13T17:17:24.324Z

## Reporter
- **Username**: tandav
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rghost

## Vulnerability Information
## Summary:
[Idor on /comments]

## Steps To Reproduce:
[Make sure you have 2 different ID's to maintain 2 different session for ensurity]

  1. The request can be tamper with the ID of different (comment) both the functions of edit/delete can be used
  2. Delete gets hampered with the Captcha which is thrown but the Comment of different user can be observed in the request
  3. Assume user 1"victim" made a comment "comment X" user 2 can edit the request for editing his comment "Y" to "X" further as the attacker failed editing the comment of victim, further disabling the edit option for user 1 :| that will make user 1"victim" left with only option to delete the comment. sed very sed
  4. Even this works widely with Burp_Intruder that means it doesn't even have rate limit.

## Impact

An attacker with a privilege to the user can harness the activities of any user around intentionally or target them widely.

## Attachments
No attachments
