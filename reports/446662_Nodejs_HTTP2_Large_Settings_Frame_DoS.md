# Node.js HTTP/2 Large Settings Frame DoS

## Report Details
- **Report ID**: 446662
- **URL**: https://hackerone.com/reports/446662
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-18T12:19:36.854Z
- **Disclosed**: 2020-07-02T19:55:27.225Z

## Reporter
- **Username**: galgo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
Hi,
 
I would like to report a vulnerability in the http2 module of Node.js. 
 
In section 10.5 of the HTTP/2 RFC an attack is described where an attacker is sending large SETTINGS frames that includes many settings inside it. 
We tested this scenario by opening many connections to the server and sending a SETTINGS frame with payload size of 14400 bytes and we were able to overload one CPU core with 100% usage with a single machine. 
Another important thing to mention is that node doesn’t close the connection to the server after some time so the attacker is able to continue sending those large SETTINGS frames.

This was tested against Node version 8.11.3
You can the code that was used to start the http2 server and also the script that we used for attacking it attached.

## Impact

Denial of Service

## Attachments
- Settings_Frame_DoS.zip
