# Potential Open-Redirection

## Report Details
- **Report ID**: 765227
- **URL**: https://hackerone.com/reports/765227
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-12-27T19:07:32.542Z
- **Disclosed**: 2019-12-27T20:54:00.331Z

## Reporter
- **Username**: damn007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Steps To Reproduce:
=====================
>1_ visit : [Normal Link](https://iandunn.name/wordpress/wp-login.php?redirect_to=https%3A%2F%2Fiandunn.name%2Fwordpress%2Fwp-admin%2F&reauth=1).
>2_ Sign-in with your wordpress account and you will directed to [This](https://iandunn.name/wordpress/wp-admin/)
>3_Change the value of the **Parameter** : redirect_to .. To the attacker website let's say : (https://vul-example.com)
>4_**NOTE THAT** : you must URL-encode the vulnerable link first

## Impact

**Phishing** attacks to get Users to visit malicious sites without realizing it.

## Attachments
No attachments
