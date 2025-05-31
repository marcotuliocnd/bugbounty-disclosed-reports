# Account takeover due to CSRF in "Account details" option on █████████

## Report Details
- **Report ID**: 410099
- **URL**: https://hackerone.com/reports/410099
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-15T14:41:48.657Z
- **Disclosed**: 2019-01-11T13:02:29.557Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Hi DoD team,
similarly to the previous CSRF that I've reported, I've found another CSRF in the same domain, but on the `Account details` option.

**Description:**
The CSRF issue allows me to modify the datas of every victim that is targeted using the CSRF file, and leading to account takeover simply setting my email as email of the victim: logging out I can recover the password of the infected account using the attacker-email that has replaced the victim-email.

**Step-by-step Reproduction Instructions**
1. Login as victim and check your infos in the account details
2. Open the CSRF malicious file {F346689}
3. Recheck the infos: now the email is different (also the username) {F346690}

(In the video the `@` char is replaced with `%40` (url encoded version of the `@` char), but is due to a problem in the CSRF value, simply replacing `%40` to `@` in the `email` parameter, the `@` char appears).

For account takeover now:
1. Go in anonymous mode (now you're the attacker that hasn't access to the accounts)
2. The victim has opened the CSRF file, so your email is setted in the victim's account
3. Go on the login, and request the `Forgot password` option, inserting the email used for replace the one of the victim
4. You obtain a link for reset the password (I've not done a video, but if you can't reproduce the steps I can do one for these steps also :))

**Suggested Mitigation/Remediation Actions**
Use captchas and CSRF-tokens for be sure that the victim is changing the datas knowing that.

## Impact

The ██████████████████ShopCart has a POST CSRF issue also in the account details, that can lead to account takeover replacing the email of the victim with the email of the attacker, and requesting a new password using the `Forgot password` option.

## Attachments
No attachments
