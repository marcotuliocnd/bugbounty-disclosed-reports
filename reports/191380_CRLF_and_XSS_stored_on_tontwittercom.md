# CRLF and XSS stored on ton.twitter.com

## Report Details
- **Report ID**: 191380
- **URL**: https://hackerone.com/reports/191380
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-15T11:41:34.369Z
- **Disclosed**: 2017-07-05T23:54:50.638Z

## Reporter
- **Username**: seifelsallamy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hey,

###[1] CRLF:
It's similar to #52042 but weaker
to reproduce go to:
https://ton.twitter.com/1.1/ton/data/dm/x/%E5%98%8A%E5%98%8Dset-cookie%3A%20test%3Dtest%3B%20Domain%3D.twitter.com%3B%20Path%3D%2F%3B%20Expires%3DSat%2C%2015-Dec-2018%2009%3A45%3A55%20UTC

you will find that `test` cookie with the value `test` has been added to your cookies

###[2] XSS:
XSS can occur by injecting a `.jpg` image 
and uploading it to twitter
then changing the extension from `.jpg` to `.html`
to reproduce open messages and start a conversation 
upload this image F143743 and send it in the conversation 
open the image source url it will look alike 

https://ton.twitter.com/i/ton/data/dm/123456789/987654321/AbCdEf.jpg:large

remove the last part `:large`
and put `%23.html`
XSS popup box will popup

however this image can only appear to you and to the one who you send it to because it is a private message
and to send the message you have to follow the victim and the victim has to follow you in most cases
and ton.twitter.com has no valuable cookies at all 
so the impact will be a phishing page or let the victim downloading a malicious software after sending the injected image on a message 

###CRLF + XSS:
both bugs separately are too weak 
but by joining them together the impact will be much more powerful
ton.twitter.com showing the image to the one who has a valid `auth_token` cookie with a value that has the right to see the injected image 
as example the attackers' `auth_token` is valid and has the right to see the injected image
so if the attacker injected his own `auth_token` to the victim by CRLF
the injected image will appear to the victim even if the victim not following you
causing a XSS to occur 
the following URL will:
[1] change auth_token value to my own `auth_token` value to make the injected image appear in your pc
[2] will redirect you to the injected imaged
[3] Javascript will be executed causing attacker's phishing page to appear
https://ton.twitter.com/1.1/ton/data/dm/809353163740483587/809353151434330112/O5hEYiOt.jpg%2523.html%E5%98%8A%E5%98%8Dset-cookie%3A%20auth_token%3Db2868e3d5fd901a1cf4819afd147ee893f331294%3B%20Domain%3D.twitter.com%3B%20Path%3D%2F%3B%20Expires%3DSat%2C%2015-Dec-2018%2009%3A45%3A55%20UTC%3BSecure%3BHTTPOnly

###Impacts
[1] phishing
[2] crlf injection (cookie injection &  DOS may occur & cache poisoning )
[3] under certain circumstances it may lead to bypassing CSP in https://twitter.com 

###POCS
F143759
F143760
F143761

Thank you!

## Attachments
- xss.jpg
- poc1.jpg
- poc2.jpg
- poc3.jpg
