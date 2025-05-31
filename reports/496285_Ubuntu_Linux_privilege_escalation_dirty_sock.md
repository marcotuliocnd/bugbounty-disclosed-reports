# Ubuntu Linux privilege escalation (dirty_sock)

## Report Details
- **Report ID**: 496285
- **URL**: https://hackerone.com/reports/496285
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-14T22:15:46.992Z
- **Disclosed**: 2019-08-28T01:49:16.747Z

## Reporter
- **Username**: initstring
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hi team,
This week, I have publicly disclosed the dirty_sock local root exploit affecting multiple Linux Operating Systems.

Very detailed information on the vulnerability can be found in my blog posting [here](https://initblog.com/2019/dirty-sock/).

And the exploit code can be found in my GitHub repository [here](https://github.com/initstring/dirty_sock).

The vulnerability exists in stock versions of Ubuntu Linux due to the default inclusion of the snapd service, but all Linux distributions are vulnerable if they install the package. The disclosure was handled directly with Canonical via the bug tracked [here](https://bugs.launchpad.net/snapd/+bug/1813365).

A large percentage of the Internet is safer today than it was a week ago, due to the amazing response by the team at Canonical.

## Impact

Linux relies on a functioning security model, particularly in environments shared by multiple users. The ability of any user to obtain immediate root access completely breaks this model, putting sensitive data all around the world at risk of exposure.

The exploits provided allow any user to immediately elevate to a root account.

## Attachments
No attachments
