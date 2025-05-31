# No authentication on email address for password reset functionality/ https://platform.thecoalition.com/forgot-password

## Report Details
- **Report ID**: 315512
- **URL**: https://hackerone.com/reports/315512
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-13T10:02:59.618Z
- **Disclosed**: 2018-05-03T08:06:18.244Z

## Reporter
- **Username**: startedfromthebottom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coalition

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** It was observed that the forgot password functionality on https://platform.thecoalition.com/forgot-password did not verify the email addresses of user accounts before sending an email to them. An attacker can use this functionality and send faulty password reset links to legitimate users.

**Description:** It was also observed that the website did not verify the authenticity of the email and accepted any arbitrary test mail. It also allowed multiple requests for the same email id without any limit. This vulnerability can be leveraged to spam genuine users of platform.thecoalition.com.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1.Visit the site https://platform.thecoalition.com/login
  2.Go to the forgot password functionality on https://platform.thecoalition.com/forgot-password
  3.Write an arbitrary email of attackers choice and click email me reset functions.

## Impact

An attacker could leverage this vulnerability by sending faulty password reset links 'n' number of times to legitimate users of platform.thecoalition.com  . This can also be done to add unnecessary load to the server by sending illegitimate mails repeatedly via using this functionality

## Attachments
- COALITION.png
