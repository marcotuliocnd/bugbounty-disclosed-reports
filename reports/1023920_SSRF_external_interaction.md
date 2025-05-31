# SSRF external interaction

## Report Details
- **Report ID**: 1023920
- **URL**: https://hackerone.com/reports/1023920
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-01T15:18:17.179Z
- **Disclosed**: 2020-12-11T12:56:40.002Z

## Reporter
- **Username**: 0xcharan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
hi team,

i found ssrf external interaction on your website which is https://my.stripo.email/cabinet/#/login?guid=&tn=&locale=en on chatbox 

description:- the attacker might cause the server to make connection back to it self
or to other web services within the organization infrastructure or to external third party systems

steps to reproduce:-

1)navigate to this website  https://my.stripo.email/cabinet/#/login?guid=&tn=&locale=en 
2))there you can find chat box
3)paste burp collaborator URL or http://pingb.in
4)you will get HTTP request to your server

note:-i previously submitted this issues in bug crowd it marked as p4 so i set severity to low and i tested many chat application not all are vulnerable example bug crowd chat system.

## Impact

by this vulnerability attacker can map out attack surface

## Attachments
- ssrfpoc.png
