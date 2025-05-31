# Disclosed Version of PORTS SSH|HTTP|SSL

## Report Details
- **Report ID**: 358102
- **URL**: https://hackerone.com/reports/358102
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-27T13:57:25.961Z
- **Disclosed**: 2018-06-14T14:41:15.737Z

## Reporter
- **Username**: bb00x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
I found Version of ports are disclosed ,But the intersting that SSH port is open and showing his version 
==> OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
F:302383
Searching I have found that this version has common vulunrablitie
https://vuldb.com/?id.89622
So it's not good to disclose the version of this port(SSH) 
##Fix
make sure you have patched version or just by hiding his version

## Impact

Give an attacker the ability to make specific attack

## Attachments
- II.PNG
