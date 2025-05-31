# Server-Side request forgery in New-Subscription feature of the calendar app

## Report Details
- **Report ID**: 427835
- **URL**: https://hackerone.com/reports/427835
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-24T12:13:55.702Z
- **Disclosed**: 2019-12-12T09:42:20.199Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
CVSS
----

8.5 High [CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:N)

Description
-----------

The "New Subscription" functionality of the official [Calendar](https://github.com/nextcloud/calendar) app allows authenticated users to direct the server to perform arbitrary external requests, and then displays the full response to the user. The requests can be directed to external websites as well as the internal network. 

An attacker can use this vulnerability to exfiltrate data from the internal network that is not protected by other mechanisms, or to perform actions in the name of the server in the internal network which do not contain other protection mechanisms (reduced security is common in internal networks).

An attacker can also use this issue to scan the internal network as well as external websites for further vulnerabilities.

A user account is required, but it does not require extended permissions.
 
POC
---

    GET /nextcloud/nextcloud/index.php/apps/calendar/v1/proxy?url=http%3A%2F%2Flocalhost%2Fsecret HTTP/1.1

    HTTP/1.1 200 OK
    [...]
    secret

The "secret" file is an example of a file located in the internal network that is not protected by further authentication. Its content is displayed in full and as-is (the same is true for more complex files). 

Solution
--------

The given URL should be verified before making a request. If it is pointing to a private address, the request should not be performed. To reduce the impact of potential misuse of the host as a scanner, requests could be throttled.

Additionally, the impact of the issue could be reduced by processing the response server-side instead of client-side. Instead of displaying the entire HTTP response to the client, the response could be parsed and validated to ensure that it is in a calendar format. This way, non-calendar/ics information from internal networks would not leak to an attacker.

## Impact

exfiltrate data from the internal network and perform actions in the name of the server in the internal network

## Attachments
No attachments
