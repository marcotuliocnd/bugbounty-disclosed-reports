#  Username enumeration via Openssh 7.6

## Report Details
- **Report ID**: 776461
- **URL**: https://hackerone.com/reports/776461
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-16T15:04:02.098Z
- **Disclosed**: 2020-02-04T01:59:32.669Z

## Reporter
- **Username**: dre4dpir4terob3rts
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Username enumeration
I have found a vulnerability in your site that  allows me to verify if an user exits in the ssh due to the use of OpenSSH 7.6p1.

PoC
1  Download and compile the given exploit file
2  open a terminal and run the exploit
I have attached a Screenshot if  detailed PoC is needed please inform me.

## Impact

The attacker can get a list of users available in the ssh.

## Attachments
- Screenshot_2020-01-16_20-31-54.png
- Screenshot_2020-01-16_20-32-23.png
- sshuserenumeration.py
