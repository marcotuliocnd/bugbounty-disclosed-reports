# App PIN code can be bypassed in Files iOS

## Report Details
- **Report ID**: 2245437
- **URL**: https://hackerone.com/reports/2245437
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-11-09T08:35:49.228Z
- **Disclosed**: 2023-12-18T08:26:41.519Z

## Reporter
- **Username**: spell1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Team,

Hope you are doing great.

Note: IoS APP Vs.: 4.9.1

I got a vulnerability in your applications via which an attacker is able to bypass the PIN.
The attacker just need to bruteforce the 4 digit PIN as unlimited tries is accepted by the application, the attacker can simply do a bruteforce and access the application.

PoC:
{F2844276}

## Impact

Authentication Bypass leading to application access

## Attachments
- RPReplay_Final1699518334.mp4
