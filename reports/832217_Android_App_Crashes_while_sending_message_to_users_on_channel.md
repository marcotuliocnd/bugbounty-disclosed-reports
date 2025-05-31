# Android App Crashes while sending message to users/ on channel 

## Report Details
- **Report ID**: 832217
- **URL**: https://hackerone.com/reports/832217
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-26T16:15:23.098Z
- **Disclosed**: 2021-03-18T13:03:48.953Z

## Reporter
- **Username**: legalizenepal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
## Description
 I found a security vulnerability in Rocket's latest android app by which I was able to remotely crash any  user’s app  instantly just by just sending a simple message in private or in channel. The vulnerability  require the victim open the message. 


## Devices and Versions

Rocket.Chat.Android version: (e.g. 4.5.1)
Mobile device model and OS version: (tested on :+1: -- " **Android 6.0, 8.0, 10.0**"), probably any other android version

## Steps to reproduce

> Create new #test channel
> Send POC Code onto the channel
> Open Mobile App
> App gets crashed

## POC
### Crafted code to crash mobile app
https://i.postimg.cc/zvBWdMzT/Screenshot-20200320-112405.png

### Message Preview
https://i.postimg.cc/fbCJ6KgC/Screenshot-20200320-112541.png

### App Gets Crashed
https://i.postimg.cc/26J8DXdQ/Screenshot-20200320-112711.png

### Code Link
https://pastebin.com/raw/JEDcC5Yr

**There is no such problem in iOS client and rocket web**

## Impact

An attacker could crash the internal chat user's phone, everytime he/she opens the rocket chat , i.e posting crafted code on #general channel

Hi, i even posted the issue on github, before i got to know about rocket chat on H1, but issue still not fixed, so just tryna keep you updated guys.

https://github.com/RocketChat/Rocket.Chat.ReactNative/issues/1907

## Attachments
No attachments
