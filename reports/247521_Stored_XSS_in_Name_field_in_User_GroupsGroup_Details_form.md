# Stored XSS in Name field in User Groups/Group Details form

## Report Details
- **Report ID**: 247521
- **URL**: https://hackerone.com/reports/247521
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-09T22:57:51.983Z
- **Disclosed**: 2017-08-17T22:13:13.947Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
## Intro

"The Crayons of Madagascar"

__Type of issue__: Core CMS issue
__Level of severity__: Internal Attack Vector
__Concrete5 version__: 8.2.0 RC2 rev. 32c9daf352645d4fafedb7b956e7f2de4e153ab3

## Summary

There is Stored XSS vulnerability in User Groups->Group Details ```Name``` field. This vulnerability might be used to perform internal attack against other concrete5 users with permissions to view User Groups list.

To execute this vulnerability, user has to be tricked to perform some additional actions or attacker has to wait until user will perform those action.

## Steps to reproduce

- log in to concrete5 instance
- go to Members->User Groups and use existing group or add new one for the next step
- in groups list click selected group and select ```Edit Group``` option from dropdown menu

{F201525}

- in ```Name``` field, put the following payload:

```
locals" onclick=alert('XSS!') "'>
```

- save changes by clicking ```Update Group``` button.

```Name``` field is properly sanitized in (almost) all context is used. 
Except one.


On the User Groups screen, use seacrh feature to find ```locals``` group (put ```locals``` into seacrh field and press Enter):

{F201526}


Click on the link. Malicious payload will be executed:


{F201527}



## Impact

This internal attack allows to execute malicious JavaScript agains other panel users. Impact of this attack is very limited, however still should be considered as potential (very low) security issue.


## Testing environment

System:

- Concrete5 version 8.2.0 RC2, commit 32c9daf352645d4fafedb7b956e7f2de4e153ab3, installed localy
- PHP ver. 5.6.30
- Apache HTTP Server 2.4.25 for macOS
- MySQL ver. 5.7.13 for macOS

This vulnerability was tested on macOS Sierra 10.12.5 with following browsers:

- Chrome 59.0.3071.115
- Chromium build 61.0.3131.0
- Opera 46.0.2597.32


## Wrap up

I hope my report will help keep Concrete5 safe in the future.

Best Regards,

Rafal 'bl4de' Janicki

## Attachments
- 1.png
- 2.png
- 3.png
