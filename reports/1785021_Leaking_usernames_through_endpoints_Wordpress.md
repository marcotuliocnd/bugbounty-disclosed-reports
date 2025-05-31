# Leaking usernames through endpoints Wordpress

## Report Details
- **Report ID**: 1785021
- **URL**: https://hackerone.com/reports/1785021
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-11-27T09:24:19.959Z
- **Disclosed**: 2024-08-10T01:20:23.256Z

## Reporter
- **Username**: alitoni224
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hi first, some of my usernames have been leaked by endpoints https://alt.mtn.com/wp-json/wp/v2/users

## Steps To Reproduce:
[The steps are as follows]

  1. Open the subdomain https://alt.mtn.com 
  1. Add the path https://alt.mtn.com/wp-json/wp/v2/users/192
  1. [You will notice the user information and you can also reveal many user names by changing it id user As in the pictures ]
{F2050805}
{F2050804}

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  #1735586
#356047

## Impact

by API The attacker can find many information and names of active users

## Attachments
- PoC.png
- PoC_2.png
