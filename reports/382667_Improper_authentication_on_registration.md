# Improper authentication on registration

## Report Details
- **Report ID**: 382667
- **URL**: https://hackerone.com/reports/382667
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-17T17:11:52.614Z
- **Disclosed**: 2018-08-24T13:34:05.332Z

## Reporter
- **Username**: lezibintlgent
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
> Hope you are doing well, one can register himself to semrush with any email ID. It means that there is no authentication mechanism if that email id is valid/invalid. Therefore a person with email ID that does not exist can also register and login to your platform.

**Summary:** 
[one can register himself to semrush with any email ID. It means that there is no authentication mechanism if that email id is valid/invalid. Therefore a person with email ID that does not exist can also register and login to your platform.
]

**Description:** 
[Hope you are doing well, one can register himself to semrush with any email ID. It means that there is no authentication mechanism if that email id is valid/invalid. Therefore a person with email ID that does not exist can also register and login to your platform.
]

## Browsers Verified In:

  * [Google chrome]
  * [Mozilla]

## Steps To Reproduce:

[reproduce steps]
  1. [Register the email ID that does not exist]
  2. [Click register button and then login to the account]
  3. [Signout and again sign in using previous email ID]

## Supporting Material/References:
[**Obligated field**]
  * Screenshots
)

## Impact

Attacker can take benefit by using this weak access control and further login with the fake account that doesnot exit.

## Attachments
- semrush2.png
- semrush1.png
