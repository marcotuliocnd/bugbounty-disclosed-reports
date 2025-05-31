# Tor Project - Full Path Disclosure

## Report Details
- **Report ID**: 269426
- **URL**: https://hackerone.com/reports/269426
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-19T07:37:53.055Z
- **Disclosed**: 2023-11-28T09:00:24.082Z

## Reporter
- **Username**: yox
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Hi there,

While you are primarily interested in the network/browser issues, I would like to report a web bug I discovered and thought the best place to do that would be here.

# Vulnerability

Type: Full Path Disclosure [CWE-209]
Affected endpoint: https://explorer.ooni.torproject.org
Example: https://explorer.ooni.torproject.org//x

# Details
Vulnerability details as follows.

## Impact
This security vulnerability could potentially allow a malicious hacker to map an attack against internal systems. For example, if this were to be chained with another vulnerability such as path traversal; it may lead to compromise of internal systems.

## Mitigation
Typically these sort of errors occur from incorrect data types, in this case it seems like it is just a simple 404 page which is however leaking too much information to the user. 

A best practice method is to log these type of errors to a local text file, while showing the user a friendly 404 message. This is often achieved by disabling error reporting on the application side.

## Attachments
- chrome_2017-09-19_08-25-58.png
