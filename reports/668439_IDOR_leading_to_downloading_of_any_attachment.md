# IDOR leading to downloading of any attachment

## Report Details
- **Report ID**: 668439
- **URL**: https://hackerone.com/reports/668439
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-06T17:54:04.922Z
- **Disclosed**: 2020-04-11T09:00:27.154Z

## Reporter
- **Username**: naaash
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bcm

## Vulnerability Information
## Description:
Hey team, 
I came across an endpoint on your android app which could be used to download any attachment which is being uploaded onto your server. All the attacker needs to do is bruteforce the simple **ID** which surprisingly is a randomly generated number( I personally think it's based on the time and it later gets converted using a epoch converter). What makes it worse it that, that particular endpoint doesn't even check for proper implementation of **Authorization Header**.

## Steps to reproduce:
* On the attacker's device, intercept all the requests using **Burpsuite**.
* Send an attachment from the victim's account to the attacker's account.
* In the **Burpsuite's**  log you'll come across a request something similar to this:

```

GET /attachments/938540538 HTTP/1.1
X-Signal-Agent: OWA
Accept-Encoding: gzip, deflate
X-Client-Version: BCM Android/5.1 Model/generic_Google_Nexus_6 Version/1.26.0 Build/1393 Area/200 Lang/en
Host: ameim.bs2dl.yy.com
Connection: close
User-Agent: okhttp/3.12.0

```

* Over here the ID number `938540538` will be different for each attachment.
* Put this particular request the repeater tab and change the ID value to `359912920` (which was sent to some other person).
* This is what it should look like: {F548523}
* You can even try it out by removing the `Authorization` Header completely and still the attacker will end up getting the attachment.

## PoC:

* Have a look at the video over here: {F548509}

## Impact

Getting access to all the attachments uploaded by any user.

## Attachments
- PoC_attachment.mp4
- 1.PNG
