# pam-ussh may be tricked into using another logged in user's ssh-agent

## Report Details
- **Report ID**: 204802
- **URL**: https://hackerone.com/reports/204802
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-09T00:04:01.367Z
- **Disclosed**: 2017-03-20T19:57:39.640Z

## Reporter
- **Username**: solardiz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
https://github.com/uber/pam-ussh was open-sourced today (kudos!) and is presumably used within Uber's infrastructure. This is a PAM module written a Go that "will authenticate a user based on them having an ssh certificate in their ssh-agent signed by a specified ssh CA." A cursory look at the code and the documentation reveals that the module trusts the SSH_AUTH_SOCK environment variable to determine the Unix domain socket it will use to talk to ssh-agent:

https://github.com/uber/pam-ussh/blob/a50585bb7a0f16cd4e813509ad1393731cbb9a14/pam_ussh.go#L70

The documentation suggests configuring the module for sudo's PAM stack. Since sudo is normally installed SUID root and invokes its PAM stacks with root privileges, it may happily talk to another user's ssh-agent via that other user's and agent's Unix domain socket, despite of this socket not being accessible to the invoking user directly (since it's protected with Unix file permissions). Being an environment variable, SSH_AUTH_SOCK is under control of the user/attacker invoking sudo. In other words, the code and suggested setup effectively bypass Unix file permissions on ssh-agent sockets.

This appears to be a design error of pam-ussh.

## Security Impact
A local user may trick pam-ussh and thus sudo to authenticate itself using another local user's certificate. This other user has to be currently logged in, with ssh-agent active. (The attack script may wait for this condition to be met.) The attacking user doesn't have to possess any certificate at all, nor use ssh-agent themselves. In fact, the attack may likely be mounted even by a compromised system service pseudo-user, provided that sudo is within its reach.

## Reproduction Steps
Not having access to a setup that Uber actually uses within its infrastructure, I can only be moderately confident that this security issue applies and these steps will work. That said, the reproduction steps may be roughly as follows:

1. Login (over SSH or otherwise) as a non-privileged user to a shell account on a system with pam-ussh deployed for sudo.

2. Check the process list and directories matching /tmp/ssh-* for instances of ssh-agent and their sockets corresponding to other logged in users. If none, then wait until this changes.

3. Infer the target user's ssh-agent socket pathname by listing /tmp/ssh-* and obtaining the PID from the process list. The pathname may be of the form /tmp/ssh-RND/agent.PID, where the "RND" and "PID" portions are determined from the directory listing and the process list, respectively.

4. Invoke a command like "SSH_AUTH_SOCK=/tmp/ssh-RND/agent.PID sudo bash" with the "RND" and "PID" substituted with substrings identified above.

## Specifics
* If applicable, what account were you using to test?
 * N/A
* If applicable, what domain(s) does this vulnerability affect?
 * Unclear - it's internal infrastructure that might be in use behind a variety of Uber services
* Does this only affect specific versions or vendors?
 * pam-ussh at least as published on GitHub as of today (Feb 8, 2017)

This might or might not be within scope of Uber's bug bounty program, and I have not actually reproduced the issue - only having identified its likelihood through the source code and documentation. Yet I figured I'd give this communication channel a try, and report this. I'd appreciate a review of these findings and any feedback you might provide.

A related concern is that Go's runtime might not be suitable for use in SUID/SGID programs yet - e.g., it might also have environment variables it trusts too much, as well as many other issues that libc's have been hardened against over the years (and decades). I have not looked into that yet, but you might want to.

## Attachments
No attachments
