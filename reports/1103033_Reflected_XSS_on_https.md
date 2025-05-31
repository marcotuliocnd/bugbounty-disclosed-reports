# Reflected XSS on https://█████

## Report Details
- **Report ID**: 1103033
- **URL**: https://hackerone.com/reports/1103033
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-14T02:53:07.238Z
- **Disclosed**: 2021-03-11T20:52:12.645Z

## Reporter
- **Username**: ibring
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#Summary:

Reflected xss can use to steal user information because it is coming from trusted website.
an user can easily trust it and attacker can easily steal user information

#Steps To Reproduce:

  1.  go to https://████?profile_id=%22%3E%3C/script%3E%3Cscript%3Ealert(%27xss%27)%3C/script%3E

2.    you will able to see xss


#Supporting Material/References:

screenshot

Thank you
@ibring
Impact

## Impact

attacker can steal user information via xss

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
#Steps To Reproduce:

  1.  go to https://█████████?profile_id=%22%3E%3C/script%3E%3Cscript%3Ealert(%27xss%27)%3C/script%3E

2.    you will able to see xss

## Suggested Mitigation/Remediation Actions
validate user input don't allow execute special character in source code



## Attachments
No attachments
