# https://mathfacts.khanacademy.org/ includes code from unprivileged localhost port

## Report Details
- **Report ID**: 331752
- **URL**: https://hackerone.com/reports/331752
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-01T08:37:08.083Z
- **Disclosed**: 2019-05-25T13:57:49.939Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
The webpage
* https://mathfacts.khanacademy.org/
contains an invalid javascript include at the bottom of the page:
    <script src="http://localhost:8021/webpack-dev-server.js"></script>

This is probably some unintended leftover from the development.

In normal situations this will only cause the browser to be unable to connect. But it can actually become a security risk. The port in question (8021) is an unprivileged port, which means on standard operating systems it's possible for every user on the system to run a service on this port.

If you imagine a Desktop computer that is usable by multiple users. One user can run a local service in his account opening this port, thus serving whatever javascript he wants and thus arbitrarily change the appearance of the served webpage for any other user on the same computer.

## Impact

An attacker with user privileges can manipulate the webpage https://mathfacts.khanacademy.org/ for all users using the same computer.

## Attachments
No attachments
