# DNS Max Responses for DOS

## Report Details
- **Report ID**: 1033107
- **URL**: https://hackerone.com/reports/1033107
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-12T18:32:25.903Z
- **Disclosed**: 2020-12-16T22:08:53.517Z

## Reporter
- **Username**: zeus1999
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
See Github (my issue): https://github.com/nodejs/node/issues/36063


When i try to fetch the A Dns records of following domain: ticbrasil.com.br I dont get any response.
I think thats the case because there are over 1300 responses.

Version: v12.18.4, v14.15.0
Platform: 64-bit Windows 10 Pro & Enterprise

What steps will reproduce the bug?
var dns = require('dns'); dns.resolve4('ticbrasil.com.br', function (err, addresses, family) { console.log(err); console.log(addresses); console.log(family); });

How often does it reproduce? Is there a required condition?
It happends everytime

What is the expected behavior?
https://pastebin.com/Tv53Na89

What do you see instead?
Nothing/No output

## Impact

mmomtchev commented 3 hours ago
@mhdawson someone should contact Mitre or whoever you usually contact, this is a confirmed remote security vulnerability. If an attacker can trigger a DNS resolution for an address chosen by him, then it is exploitable for DoS. It is a very high-risk vulnerability. I don't think a remote access is possible, but this should probably be evaluated by an expert.

@jasnell
 
Member
jasnell commented 2 hours ago
We can look into this further but I have to point out: we have a defined process for properly reporting and investigating potential security vulnerabilities. As soon as this issue was suspected as being a security issue, that process should have been followed with investigation and fixes investigated in the private Node.js repo we use for that purpose, otherwise this ends up risking a zero-day for all Node.js users.

## Attachments
No attachments
