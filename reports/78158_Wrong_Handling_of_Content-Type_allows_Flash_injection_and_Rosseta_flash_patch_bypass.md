# Wrong Handling of Content-Type allows Flash injection and Rosseta flash patch bypass

## Report Details
- **Report ID**: 78158
- **URL**: https://hackerone.com/reports/78158
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-07-23T13:03:39.060Z
- **Disclosed**: 2019-11-12T09:43:40.625Z

## Reporter
- **Username**: benhayak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hey, 
I spent some time reversing the mitigation of Rosetta Flash. This research helped me to discover a very interesting bug:

Adobe Flash player uses "string searching" (similar to indexOf) over the entire response's "Content-Type" header value to match the "application/x-shockwave-flash" string. Once matched, the flash player will skip all checks/restrictions and render the file as a valid Flash file. Therefore responses which will include this string *anywhere* within the content header will allow the execution of various file types as flash applications (such files types may be images,videos,css,text files, and so on) - MIME Sniffing. This bug will also fully bypass an existing nosniff header: X-Content-Type-Options: nosniff. 

Example vulnerable response header:
Content-Type: text/plain; lang=application/x-shockwave-flash

Some web applications allow user data inside the content-type header. Such header injection can include "language" , "encoding type"(UTF-8,ISO.) etc or response splitting (vulnerable in Chrome).


There are two main case scenarios: 

Classic MIME Sniffing - Rendering Images/text/media as Flash:
1. The web application allows uploading an image file.
2. Viewing the uploaded image is served through an Servlet that accepts encoding/language parameter.
3. The attacker uploads a malicious flash file as an Image: "flashsniff.png"
4. The attacker forge a malicious web page with the following payload
<object type="application/x-shockwave-flash"
data="http://vulnerable-site.com/RenderImageServlet.php?imgId=1234&lang=application/x-shockwave-flash">
<param name="AllowScriptAccess" value="always">
</object>

4. The hosting server will respond with the following headers:
HTTP/1.1 200 OK
....
X-Content-Type-Options: nosniff
....
Content-Length: 733
Content-Type: image/png; charset=utf-8; lang=application/x-shockwave-flash

In this case Flash will execute malicious file types as flash applications even when X-Content-Type-Options: nosniff is on.
PoC (Rendering Images as FLASH Files) 

http://poc.benhayak.com/Flash/SniffingFlash.html
Here I just present an alert as a PoC but this could've been a flash that will leak information via SOP bypass.


Rosetta Flash patch bypass using only alpha numeric flash:
Brilliant Michele Spagnuolo made an amazing research and discovered the possibility to make execute flash files using only alphanumeric charset via jsonp endpoints: https://miki.it/blog/2014/7/8/abusing-jsonp-with-rosetta-flash/

A mitigation was implemented to avoid this risk by:
1. If content-type is application/x-shockwave-flash, execute the flash. (string search!)
2. Verify there's at least 1 non alphanumeric character which is not a valid UTF-8 in the incoming string.

Since flash will ignore anything but the "application/x-shockwave-flash" value in the content-type string. using this bug will bypass the rosseta flash patch and allow executing Flash applications via jsonp endpoints once again!

PoC: (LOOK at the network panel for "attacker.com/crossdomain.xml" to see a SOP bypass via Michele's techinique)

 http://poc.benhayak.com/Flash/rossetabypass.html


Regards,
Ben Hayak


## Attachments
No attachments
