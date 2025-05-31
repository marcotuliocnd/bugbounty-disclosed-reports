# Cross-site scripting on algorithm collaborator 

## Report Details
- **Report ID**: 615672
- **URL**: https://hackerone.com/reports/615672
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-06-15T13:02:06.375Z
- **Disclosed**: 2022-12-21T20:12:27.620Z

## Reporter
- **Username**: irisrumtub
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quantopian

## Vulnerability Information
Hi again my favorite VDP team. I bring you 8th bug and 4th cross-site scripting. Currently trying to upload python code via self-serve data, not looking for XSS'es only, but they're a thing still, right?

**Summary:**
By sending specially crafted websockets request attacker can run javascript in algorithm collaborator's web browser

**Description:**
This is actually quite a funny bug. Some time ago when I was testing algo debugger, i noticed that there is a request to */algorithms/algoid/x* which usually happens when i try to insert html's <img src=x>. But since some time your cloudflare became more strict and adding inline scripts in request might result in 403 Forbidden, so i remove them and try without them. But at that time i couldn't find the image that caused that request. I sent that to Chris.
Today i was trying to test against debugger again. The purpose wasn't to find XSS, but i spammed XSS payloads alongside with some different stuff. And again that request to page *X*. And i noticed that debugger removed part of my payload which contained image. That's it! That should be the vulnerable place. 
However typing html entity in it didn't produce anything. And html was injected only on my side, not the other collaborator's. So i decided to take a look at the websocket request that sends it
It turned out that HTML's <> and other entities were encoded. So i tried intercepting the websockets request and enter <img src=x onerror=alert(1)> and it worked not only on me, but on collaborator as well.
So is it TogetherJS library that is in charge of websockets? I think you might need to encode payloads server-side to avoid this kind of things. I would be glad to help you test the fix for this.


## Steps To Reproduce:


  1. Intercept websockets message like this (debugger input update)
{F509648}
  2. Replace value with raw html/javascript
  3. Send the message. Payload will work in collaborator's browser


## Test account information

irisrumtub+hackerone@mail.ru
tvburis+hackerone@gmail.com

## Impact

Run javascript in victim's browser

## Attachments
- WS_message.png
