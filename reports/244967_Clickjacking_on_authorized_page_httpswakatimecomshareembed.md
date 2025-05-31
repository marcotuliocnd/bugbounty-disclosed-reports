# Clickjacking on authorized page https://wakatime.com/share/embed

## Report Details
- **Report ID**: 244967
- **URL**: https://hackerone.com/reports/244967
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-01T02:53:51.505Z
- **Disclosed**: 2017-07-05T06:21:31.084Z

## Reporter
- **Username**: silv3rpoision
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hii,
https://wakatime.com/share/embed is vulnerabel to clickjaking.
Description:
I found the resource on https://wakatime.com/share/embed, which can be vulnerable to the Clickjacking.

Impact
The resource without X-Frame-Options potentially vulnerable to the Clickjacking. The vulnerability exist only for authenticated users (possible UI redressing in the Dashboard).As it is on a authenticated page so a attacker make many benefits of it and can click jack any user

Step-by-step Reproduction Instructions

Go to the https://wakatime.com/share/embed
Look to the response headers. or Create .html file with next content: <iframe src="https://wakatime.com/share/embed"></iframe>

Suggested Mitigation/Remediation Actions
Adding X-Frame-Options: DENY header will solve this problem.

Thnx plzz review it and fix as soon as possible.

Regards Piyush kumar

## Attachments
No attachments
