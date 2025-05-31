# Persistent CSV injection

## Report Details
- **Report ID**: 459532
- **URL**: https://hackerone.com/reports/459532
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-10T09:56:23.899Z
- **Disclosed**: 2019-01-11T13:39:33.860Z

## Reporter
- **Username**: 8r33
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Hi Team,

https://www.semrush.com/notes is vulnerable to persistent csv injection (stored csv injection) 

POC:
1) Login into application and open https://www.semrush.com/notes

2) click on "Add note" button

3) And enter csv injection payloads like =4+4, =HYPERLINK("http://evil.com", "EVIL") and click on save

4) and click on "Export to CSV"

5) Open the downloaded csv file

6) Observe the payload you entered in the above step


Reference:
https://payatu.com/csv-injection-basic-to-exploit/

## Impact

Attacker can execute kernel/OS level commands from victims machine.

As it is stored at database, so users across SEMrush who ever downloads that csv file will be victims for the attacker.

Also attacker can use victims to perform DDOS attack from victims machines.

## Attachments
- 2.png
- 3.png
- 4.png
