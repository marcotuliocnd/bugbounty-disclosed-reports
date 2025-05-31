# XXE through injection of a payload in the XMP metadata of a JPEG file

## Report Details
- **Report ID**: 836877
- **URL**: https://hackerone.com/reports/836877
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-04-02T05:09:42.965Z
- **Disclosed**: 2020-04-21T09:29:34.893Z

## Reporter
- **Username**: moebius
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Users are able to change their avatar picture. The avatar picture upload functionality is prone to a XXE attack when parsing the image file. Specifically, the XXE attack is executed through the injection of a payload in the "XMP metadata" of the uploaded JPEG file.

Proof of concept (note the "Burp Collaborator Payload pointing to an External DTD"):
```
POST /edit-profile-avatar!uploadImage.jspa HTTP/1.1
Host: ███████informatica.com

  [...REDACTED...PLEASE.SEE.SCREENSHOTS.FOR.FULL.PAYLOAD]
```

And I received the following calls (note the User-Agent "Java██████" confirming the vulnerability):

```
Interaction 0 
Type: HTTP 
Client IP: ███████ 
Timestamp: 2020-Apr-02 01:44:27 UTC  
Protocol: HTTP  

RAW HTTP request: 

GET /x.dtd HTTP/1.1 
Cache-Control: no-cache 
Pragma: no-cache 
User-Agent: Java██████ 
Host: N.syuj65rfsb27o1u78jcinsinnet6ky8n.burpcollaborator.net 
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2 Connection: keep-alive
```

Similar calls were received from another IP address: 146.112.138.73

Furthermore, the affected host should not be allowed to start a new connection to the Internet.

## Impact

This issue can be abused to read arbitrary files and list directory contents from the filesystem of the XML processor application. I didn't try any reading, but JAVA (JSPA is a JAVA Servlet File) is calling my external service, so the vulnerability is confirmed.

## Attachments
- Screen_Shot_2020-04-02_at_2.04.53_AM.png
- Screen_Shot_2020-04-02_at_2.05.10_AM.png
- Screen_Shot_2020-04-02_at_2.05.44_AM.png
