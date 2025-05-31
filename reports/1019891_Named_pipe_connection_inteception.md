# Named pipe connection inteception

## Report Details
- **Report ID**: 1019891
- **URL**: https://hackerone.com/reports/1019891
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-27T12:35:10.399Z
- **Disclosed**: 2020-12-17T23:24:05.745Z

## Reporter
- **Username**: gabriel_sztejnworcel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mariadb

## Vulnerability Information
With MariaDB running on Windows, when local clients connect to the server over named pipes, it's possible for an unprivileged user with an ability to run code on the server machine to intercept the named pipe connection and act as a man-in-the-middle, gaining access to all the data passed between the client and the server, and getting the ability to run arbitrary SQL commands on behalf of the connected user.

On Windows, MariaDB allows local clients to connect to the server over named pipes. Unfortunately, when creating the named pipe server, the security descriptor is not set correctly, and as a result every user on the system can create pipe server instances. This allows for the following attack scenario:
1.	The attacker creates a pipe server instance and waits for a client to connect to it.
2.	Once a client is connected, the attacker connects to the real pipe server instance as a client.
3.	At this point, the attacker is connected to the legitimate client and server, and can pass the messages back and forth, reading the messages (as they are passed in clear text) and possibly changing the messages.

Please see the attached report and POC tool for more information.

## Impact

- All the SQL requests/responses from the intercepted connection
- Ability to run SQL commands

## Attachments
- Vulnerability_Report.docx
- tool.zip
