# Attacker can trick other into logging in as themselves

## Report Details
- **Report ID**: 233379
- **URL**: https://hackerone.com/reports/233379
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-30T20:23:22.648Z
- **Disclosed**: 2017-06-13T07:54:18.180Z

## Reporter
- **Username**: fixit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
Hi Team,

This bug is similar to bug report https://hackerone.com/reports/2228 as this bug also allows a user to be logged in as the attacker. An attacker can escalate this to attach his account with the victims profile and monitor his activities.

Login CSRF is a type of attack where the attacker can force the user to log in to the attacker’s account on a website and thus reveal information about what the user is doing while logged in.

An attacker could exploit this bug as follows:
1: Attacker initiates google OAuth process with mixmax.com
2: Attacker allows access to mixmax app
3: Attacker records and drops redirection to mixmax.com (in order not to consume token)
4: Attacker directs victim to https://app.mixmax.com/_oauth/google/callback?state={state}&code={ode}
5: A white page see to victim and in backend, Victim is now logged in as attacker.

To mitigate this vulnerability,state parameter is solution for this but in this case state parameter is not getting validated on server side.

Let me know if any additional info is needed.

## Attachments
No attachments
