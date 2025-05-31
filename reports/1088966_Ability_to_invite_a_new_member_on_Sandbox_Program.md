# Ability to invite a new member on Sandbox Program

## Report Details
- **Report ID**: 1088966
- **URL**: https://hackerone.com/reports/1088966
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-27T20:32:07.211Z
- **Disclosed**: 2021-04-05T21:13:40.858Z

## Reporter
- **Username**: ex1st3nc3_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
In the description 
> HackerOne offers a sandbox for hackers to help them test program functionality for security vulnerabilities. To create a program, go here. You can select any product edition, giving you access to almost all features HackerOne offers. Hackers can create up to 30 programs in the sandbox. It is currently **not** possible to invite program members to new programs in the sandbox.

However in the Sandbox program the owner allows to invite a new Security member after estabilishing the program

## Steps to produce

1. Create a new sandbox program

2.  Go to [https://hackerone.com/{YOUR-PROGRAM}/team_members](https://hackerone.com/{YOUR-PROGRAM}}/team_members)

3. Invite any user

██████

4. As you can see you can invite a user even though in the description it says 

> It is currently **not** possible to invite program members to new programs in the sandbox.

███

██████████

## Impact

Allows the attacker to invite a ``team_member`` to the sandbox program even though its not permitted.

## Attachments
No attachments
