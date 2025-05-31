# Stored XSS in the guide's GameplayVersion (www.dota2.com)

## Report Details
- **Report ID**: 380045
- **URL**: https://hackerone.com/reports/380045
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-10T02:00:39.493Z
- **Disclosed**: 2019-01-07T20:03:56.643Z

## Reporter
- **Username**: mvc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
Hi, team!

The beginning of this issue looks like my previous report #369043, but this one will be much more interesting :) So let's go!

Steps to reproduce:

1) Open dota2 client and create new simple guide with XSS in the name.

{F318796}

2) Publish this guide on steam.

{F318797}

3) Now go to the Fiddler app and look at the request from dota2 client:

{F318798}

The XSS script placed in the title, the title displays a safe HTML on the site, so, for now nothing terrible happens.

4) Next I write some piece of code in the Fiddler app:

```
if (oSession.uriContains("/cloud/CB/")) {
    var strBody=oSession.GetRequestBodyAsString();       
    strBody=strBody.replace("mvc123<svg/onload=alert(document.domain)>","mvc123");
    strBody=strBody.replace("7.18","7.18<svg/onload=alert(document.domain)>");
    oSession.utilSetRequestBody(strBody);       
}
```

So I transfer the XSS script from "Title" to "GameplayVersion". I decided to go this way, since in this case the content length of build's file does not change and it successfully passes the hash sum comparison.

5) Now we return to the dota2 client, click "Edit" and change anything in the our build and publish it again. And we see that the PUT request was successful and the XSS data in it is arranged the way we wanted:

{F318801}

6) Next i follow to the Dota2 Workshop Manager.

{F318802}

And here we see our public file ID. This connection with the public guide files I was found in the preparation of the previous report, but I did not know how to apply it (before today).

7) Put this FileID into a link below and we get the public infected page:

http://www.dota2.com/workshop/builds/view?fileid=949580646106367888

And the result in the latest versions of Firefox and Chrome:

{F318805}

{F318803}

{F318804}

Sincerely, @mvc

## Impact

As on any cross-site-scripting vulnerability. The top line would be that the attacker might steals cookies to abuse users session.

## Attachments
- Screenshot_1.png
- Screenshot_2.png
- Screenshot_2.png
- Screenshot_3.png
- Screenshot_4.png
- Screenshot_5.png
- Screenshot_6.png
- Screenshot_7.png
