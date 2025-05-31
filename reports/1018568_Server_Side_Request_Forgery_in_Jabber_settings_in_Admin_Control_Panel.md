# Server Side Request Forgery in 'Jabber settings' in Admin Control Panel

## Report Details
- **Report ID**: 1018568
- **URL**: https://hackerone.com/reports/1018568
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-10-26T02:08:22.204Z
- **Disclosed**: 2020-12-20T17:04:13.089Z

## Reporter
- **Username**: they
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phpbb

## Vulnerability Information
## Overview
The 'Jabber settings' panel inside the Administrator Control Panel can be used to access resources that would otherwise only be accessible by the host machine, including resources/services hosted on the `localhost` interface. This can be performed by setting the 'jabber server' parameter to the desired IP address, such as `127.0.0.1` and the port to the desired port. In some cases, service type/version numbers can be gathered as well as this information is printed to screen.

## How to trigger
Set 'jabber server' to 127.0.0.1
Set 'Jabber port' to whatever port you want to check.
Check the 'Enabled' radio button
Click submit

If the port is closed, you will see a socket error message 'Connection refused' error like this:
{F1051582}

Some such as mysqld simply return:
> Could not authorize on Jabber server.

## Example Recording
I have hosted an internal sshd service on `127.0.0.1:2222` to demonstrate that software type and version information is returned to the Administrator Control Panel. I am `ssh`'d into `phpbb-ubuntu`, which is running the aforementioned sshd service in debug mode so you can see the request hit. 
{F1051590}

## Setup info
Base OS: Ubuntu 20.04.1
phpbb Version: 3.3.1
{F1051573}

## Impact

An attacker could use this to interact with and enumerate services and resources on behalf of the host machine (including resources hosted on the `localhost` interface). This can be used to port scan and, in some cases, perform service versioning/enumeration on the `localhost` interface as well as on machines hosted on the same network as the phpbb host machine.

## Attachments
- version.png
- howtotrigger.png
- conn_refused.png
- recording-1603676588353.webm
