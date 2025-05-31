# The csrf token remains same after user logs in

## Report Details
- **Report ID**: 361400
- **URL**: https://hackerone.com/reports/361400
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-06-03T18:55:18.745Z
- **Disclosed**: 2018-06-04T09:05:45.391Z

## Reporter
- **Username**: d4w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
###Description
As the CSRF token doesn't change after login. Any other user that uses the same workstation is vulnerable. A safer way would be to use dynamic CSRF token or just change the token after login, so attacker doesn't get hold of this.

### Details of the attacks scenario in a shared workstation environment

1. The attacker simply copies the authenticity token. This token is the only protection against the CSRF attack.
2. Any other user that uses the workstation after that is vulnerable to CSRF. The attacker simply needs to craft a link with the required GET or POST method as he already have the CSRF token and send it to the victim via email, chat etc.
3. he attacker can trick the victim in doing anything he wants without the user being aware of it.

## Impact

Any other user that uses the same workstation is vulnerable to CSRF attack

## Attachments
No attachments
