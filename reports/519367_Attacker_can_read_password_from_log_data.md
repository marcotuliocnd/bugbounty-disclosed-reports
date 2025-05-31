# Attacker can read password from log data

## Report Details
- **Report ID**: 519367
- **URL**: https://hackerone.com/reports/519367
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-31T20:55:20.158Z
- **Disclosed**: 2019-06-15T12:47:55.648Z

## Reporter
- **Username**: kingamir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: midpoint_h1c

## Vulnerability Information
## Summary:
Attacker can read plain text password from log data.

## Steps To Reproduce:

  1. From application dashboard choose Users section, I simultaneously ran process hacker to see the process disk write and read behavior.
  2. change the password of one of the users, and you see in process hacker window the place for log data creation.
  3. Open the file in favorite editor in that place:
%UserProfile%\AppData\Local\Temp\tomcat.1470616378544174392.8080\work\Tomcat\localhost\midpoint 

## Supporting Material/References:
I have uploaded a video for POC.

## Impact

Attacker can read plain text password from log data.

## Attachments
- PlainText.mp4
