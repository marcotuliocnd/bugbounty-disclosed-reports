# SSH backdated version open port

## Report Details
- **Report ID**: 255627
- **URL**: https://hackerone.com/reports/255627
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-01T20:53:11.352Z
- **Disclosed**: 2017-11-23T17:47:22.774Z

## Reporter
- **Username**: walidhossain010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
	
You are running a version of OpenSSH which is older than 6.7

Versions prior than 6.7 are vulnerable to an off by one error
that allows local users to gain root access, and it may be
possible for remote users to similarly compromise the daemon
for remote access.

In addition, a vulnerable SSH client may be compromised by
connecting to a malicious SSH daemon that exploits this
vulnerability in the client code, thus compromising the
client system.An attacker may use this flaw to set up a brute force attack against
the remote host.

Solution : Upgrade to OpenSSH 6.7 or apply the patch for
prior versions. (See: https://www.openssh.org)

## Attachments
No attachments
