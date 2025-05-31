# Buffer Overflow in smblib.c

## Report Details
- **Report ID**: 721333
- **URL**: https://hackerone.com/reports/721333
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-23T19:42:43.059Z
- **Disclosed**: 2021-07-28T23:54:29.293Z

## Reporter
- **Username**: aaron_costello
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary:

In Squid 4.8, a local buffer overflow vulnerability exists in the 
Smb_Connect() and Smb_Connect_Server() functions of Squid's smblib.c, in which an attacker can achieve code execution that can result in the disclosure of credential hashes. The cause of this overflow is due to the SMB domain controller names being passed down from user input and eventually into an array without performing appropriate bounds checking on said array.

I submitted a patch, which was accepted and merged, which can be found here: 
https://github.com/squid-cache/squid/pull/494

## Disclosure Timeline
15/10/19 - Initial discovery and disclosure to the Squid team via squid-bugs private email list
16/10/19 - Acknowledgement of the vulnerability by the Squid team
17/10/19 - I volunteered to fix the issue, and create a pull request on Github (See above link)
17-19/10/19 - The fix was reviewed, accepted, then merged (Fix is also backported to older Squid Versions)
23/10/19 - CVE-2019-18353 assigned

## To Note
Due to the fact that this is a local (as opposed to remote) overflow, and used primarily by squid auth helpers for downgrading (As pointed out by a member of the squid team when he said an advisory would not be released because of the 'nature' of what the squid helpers are doing); I am setting the severity as medium and not expectant for a bounty.

## Impact

Code execution resulting in the retrieval of credential hashes

## Attachments
No attachments
