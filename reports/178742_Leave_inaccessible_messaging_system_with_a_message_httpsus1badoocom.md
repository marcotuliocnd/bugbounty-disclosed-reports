# Leave inaccessible messaging system with a message (https://us1.badoo.com)

## Report Details
- **Report ID**: 178742
- **URL**: https://hackerone.com/reports/178742
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-29T05:08:24.542Z
- **Disclosed**: 2017-01-19T19:16:51.906Z

## Reporter
- **Username**: ahiezer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
Hello, to test the messaging system I found a vulnerability that allows Inaccessible leave mensajaria system to another user (only required to send a message).

The vulnerability is in the system as the mobile version smiles and app do not have that system is only vulnerable version desktop

VULNERABLE https://us1.badoo.com
NOT VULNERABLE Version mobile (https://m.badoo.com/) App

Reproduction steps

1 .- Visit https://badoo.com/ and access your account
2 .- Selecione a user and send the message http: //www.ab99
3 .- The user who received the message could not read or write messages.

Exploitability

This is an easy mui vulnerability to exploit only requires sending a simple message, an attacker could selecionar massively users and leave them unable to read messages on your platform.

Technical details

This problem is in the system that generates smiles, which transforms :) to its corresponding image, to be more specific is in BuildLink of SmileViewController https://badoocdn.com//v2/en-us/-/js/ hon_v3 / page.messenger.1101.j


## Attachments
- PoC.mp4
