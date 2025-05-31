# Unauthorised Account Detail Modification 

## Report Details
- **Report ID**: 868146
- **URL**: https://hackerone.com/reports/868146
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-07T15:16:07.269Z
- **Disclosed**: 2020-06-19T15:37:21.424Z

## Reporter
- **Username**: 5kyw41k3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Introduction
=========
Hi `5kyw41k3r` here,

==I found an Unauthorised Account Detail Modification  in KA website==...

Defination
=========
```
It is a flaw which allows a malicious actor to modify the details of an account. I have included a video made by me for demonstration purposes using a test account...
```
Reproduction Steps:-
============== 
==I have included a video in the attachments==
+ You need burp proxy correctly configured and working properly.
+ Go to settings and make minor changes to your account.
+ Hit save and then intercept that request.
+ Disconnect your browser and your proxy
+ Send the Step 3 request to the repeater and forward all unnecessary requests.
+ Modify the request as shown in the video
There you have it! ==Notice how you can change you nickname and DOB which is actually not authorized in the browser itself.==   

Here's the vid=====> ████████

## Impact

Impact
======

Well, khan academy being used in schools like mine as it says on the page;
>This is because Khan Academy is used in many schools...

Anyone can change these details by getting hold of those requests, which you can do through the inspect element...No rocket science!

This can lead to a lot of issues such as leakage of sensitive data(==Such as parent emails and accounts==)

They could also perform identity theft through this method.

 I strongly recommend to fix this as soon as possible. 
Hoping for swag!

Thanks and Stay Safe at Home,
`5kyw41k3r`

## Attachments
No attachments
