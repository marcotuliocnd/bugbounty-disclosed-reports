# SVG file upload leads to XML injection

## Report Details
- **Report ID**: 845832
- **URL**: https://hackerone.com/reports/845832
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-10T02:57:12.746Z
- **Disclosed**: 2020-08-14T21:43:55.163Z

## Reporter
- **Username**: tushr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Upload Avatar option allows the user to upload image/* . Thus enabling the upload of many file formats including SVG files (MIME type: image/svg+xml) 
SVG files are XML based graphics files in 2D images. Thus, this opens up an attack vector to upload specially crafted malicious SVG files. 
The attacks that are possible using SVG files are:

1. XSS attack: Stored XSS can be performed by including a "<script>alert(1)</script>" payload inside the XML code of the SVG file can make the browser execute the javascript when the file is rendered. However, only possible when using an <svg> tag to call the file. In this case, <img> tag is used thus not exploitable.
2. XXE attack: Injecting malicious XML code inside the SVG file thus executing once the server parses the SVG. [Follow steps to reproduce for this]
3. DOS attack: Billion laugh attack is an application-level DOS and can lead to resource exhaustion making the server slow down or crash. I have not tried this but found the below resource about it:
                            https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#billion-laugh-attack

## Steps to reproduce
  1. I observed that when uploading a user avatar picture, the first request was sent to 
       https://api.topcoder.com/v3/members/oldsoul/photoUploadUrl
       with a POST parameter "contentType" telling the type of file being uploaded. I changed the value to "image/svg+xml".  
       Now, the response had a preSignedURL variable pointing to the valid S3 object creation URL, and a token variable which gives a random number which is added to the file name which is being uploaded.
                                     F781757
  
  2. Second request is a PUT request to https://api.topcoder.com/v3/members/oldsoul/photo
       with a token variable which is same as the token variable which we received in the first request. Also a variable "contentType" which is used in determining the extension of the file being uploaded. I changed the value to "image/svg+xml"
                                     F781767
  
  3. Now, I sent a PUT request to the "preSignedURL" that we got from the first request with HTTP header "Content-Type: image/svg+xml". The body of this request contains the SVG file data to be uploaded.    F781788


----------------------------------------------------XXE SSRF------------------------------------------------
   1. For Fetching External resources from a remote server, 
   upload SVG with <image xlink:href="http://159.65.151.4:81/svg" /> to the SVG file [observed connection to my server when listening via netcat on port 81]  =>   F781770

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   style="overflow: hidden; position: relative;"
   width="300"
   height="200">
  <image x="10" y="10" width="276" height="110" xlink:href="http://159.65.151.4:81/svg" stroke-width="1" id="image3204" />
  <rect x="0" y="150" height="10" width="300" style="fill: black"/>
</svg>

(This is the IP of my personal server. You can include a public resource like http://images.google.com/intl/es_ALL/images/logos/images_logo_lg.gif)  =>  F781773

   2. For fetching local files from the server itself (LFI),

I created another user named testing68 and uploaded an avatar picture for it. Added the picture link for testing68 user to the XML payload  =>  F781779

  <image x="10" y="10" width="276" height="110" xlink:href="/member/profile/testing68-1586481096585.png" stroke-width="1" id="image3204" />


## Supporting Material/References:
SImilar Reports: 
https://hackerone.com/reports/97501
https://hackerone.com/reports/142709

Reference material:
https://qy.sg/x-ctf-finals-2016-john-slick-web-25/
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#xxe-inside-svg


Thanks

## Impact

Exploiting an XXE attack, allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any backend or external systems that the application itself can access.

Exploiting the billion laugh DOS attack can mess with the availability of the server and since it is an application level DOS network level filters will not be effective to stop such attack.

## Attachments
- topcoder11.png
- topcoder12.png
- topcoder_ssrf.png
- topcoder_ssrf2.png
- topcoder13.png
- topcoder14.png
