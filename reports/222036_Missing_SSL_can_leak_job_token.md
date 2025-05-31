# Missing SSL can leak job token 

## Report Details
- **Report ID**: 222036
- **URL**: https://hackerone.com/reports/222036
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-18T23:36:48.264Z
- **Disclosed**: 2017-11-01T18:33:56.324Z

## Reporter
- **Username**: c0rte
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hello,

Description:

The Web app jobs.wordpress.net transmits sensitive data in cleartext in a communication channel that can be sniffed by unauthorized actors.

Attack Scenario:

Attacker simply monitors network traffic (like an open wireless network), and steals the user’s session cookie. Attacker then replays this cookie and hijacks the user’s session, accessing the user’s private data.

This could leak Job token, leak user information and jobs created by users. 

Thanks,
Diogo Real

## Attachments
No attachments
