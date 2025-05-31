# Clickjacking or URL Masking 

## Report Details
- **Report ID**: 204198
- **URL**: https://hackerone.com/reports/204198
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-07T13:33:57.940Z
- **Disclosed**: 2017-08-10T05:10:43.866Z

## Reporter
- **Username**: dhiraj-mishra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
I am able to reproduce the bug in :
Brave: 0.13.2 
rev: 25b1199fb6154b089cbad37926483239495b9800 
Muon: 2.0.19 
libchromiumcontent: 54.0.2840.100 
V8: 5.4.500.41 
Node.js: 7.0.0 
Update Channel: dev 
os.platform: win32 
os.release: 6.1.7601 
os.arch: x64

Steps to reproduce : 
1. Open click.html 
2. Then try to visit google.com 
OR 
http://hackies.in/click.html

Visually the browser says you(user) will be visiting google.com but it actually goes to 
datarift.blogspot.in 
An attacker may craft the link and may perform phishing attack or spoofing and etc.

Just do a mouseover on the link and see left bottom the URL says the browser will be visiting google.com but actually goes to datarift.blogspot.in 

In case if the repro doesn't works please perform the testcase 1 more time. 
Attaching the test case and the click.html file and Video POC for reference

## Attachments
- POC.ZIP
