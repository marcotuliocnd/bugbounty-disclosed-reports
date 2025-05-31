# Scope information is leaked when visiting policy scopes tab of any External Program

## Report Details
- **Report ID**: 1868473
- **URL**: https://hackerone.com/reports/1868473
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-09T11:24:18.884Z
- **Disclosed**: 2023-03-10T05:38:29.908Z

## Reporter
- **Username**: buraaqsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello Team,

## Summary:
The new scope policy feature displays all Program names and scopes that are using the new functionality.

### Details:
A ``External program + invite-only`` consider ``hackerone.com/████`` as a unauthenticated user I see only ``Policy`` tab, and no option to view scopes.
██████████


This is also a private program, and this is how it looks and has all tabs and supports/implemented new scope policy feature.

██████████

We know that new scope policy is implemented at ``/policy_scopes``. If you appending it to ``hackerone.com/███``, application breaks and gives out all the programs' scope under it. See below image,

███████

████████

████

I was able to confirm some of my private programs listed in this leak and are they not publicly available programs. As far as I understand, this leaks only program which have new scope policy implemented.

Private Programs for example:
> https://hackerone.com/██████████
>https://hackerone.com/█████
> https://hackerone.com/██████████
> https://hackerone.com/████

It is also observed that, once you visit and application break and show all domain, hackerone.com breaks and struggle to load - DoS

████

## Steps to reproduce:
Use Burp Suite, and a browser (keep it unauth) to reproduce and follow steps listed below.

1. Visit ``https://hackerone.com/█████████/policy_scopes``
2. Go to burp, search for the request which says ``PolicyScopeAssetGroupsQuery`` as ``operationName`` send it to repeater
3. Increase the size to 2215 (more than that the api doesn't give any results)

████

4. You can search for the private program's domains in response, e.g ``███.com, ██████████.com, ████.io etc``
            
████████ ---------> ███████

█████████ ---------> ████

█████████ ---------> ████████

**Left side are images of  data leaks from above vulnerability**
**Right side are images from my private programs**

Let me know if you need any other details :)

Kind regards,
@buraaqsec

## Impact

Unauthorized user is able to view private programs' details.

## Attachments
No attachments
