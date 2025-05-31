# The Microsoft Store Uber App Does Not Implement Certificate Pinning

## Report Details
- **Report ID**: 293358
- **URL**: https://hackerone.com/reports/293358
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-11-28T03:18:23.439Z
- **Disclosed**: 2017-12-24T20:16:01.570Z

## Reporter
- **Username**: gregoryvperry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
The Microsoft Store Uber App (Windows Phone Architecture) does not properly implement certificate pinning.

## Security Impact
Layer-2+ network traffic transmitted from and received by the app can be surreptitiously intercepted and transparently modified by an attacker, with no warnings or errors presented to the app user.

## Reproduction Steps
A transparent Layer-2 MITM proxy was configured between a device running the most recent release of the Uber app for Windows Phone Architecture and an Internet gateway. Self-signed certificates were asserted on behalf of the remote systems that the app communicated with. All traffic transmitted and received by the Uber app was able to be captured and then modified transparently, without any notifications or certificate warnings sent to the app user.

## Specifics
* Account GregPerry804@gmail.com was used for testing
* It appears that the apps for iOS and Android properly implement certificate pinning, with only the Windows Phone Architecture Uber App affected by this vulnerability.

## Impact

In this scenario an attacker has the ability to modify a rider's profile, to access previous trip histories, to schedule and/or cancel Uber driver dispatches, and the ability to access and/or modify stored payment information.

Driver functionality was not tested. If the Uber Driver role is also implemented within the Microsoft Phone Architecture Uber App, then all functionality encapsulated within the app as relates to driver functionality could be surreptitiously observed and/or transparently modified as well.

This particular vulnerability can be implemented as an ARP cache poisoning attack, making it especially relevant to Uber riders who utilize wireless access points at public hotspots to dispatch Uber rides.

## Attachments
No attachments
