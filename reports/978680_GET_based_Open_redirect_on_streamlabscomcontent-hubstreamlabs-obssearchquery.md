# GET based Open redirect on [streamlabs.com/content-hub/streamlabs-obs/search?query=]

## Report Details
- **Report ID**: 978680
- **URL**: https://hackerone.com/reports/978680
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-10T21:28:18.577Z
- **Disclosed**: 2020-10-09T22:13:52.657Z

## Reporter
- **Username**: raywando
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
## Summary:
Description: in the following link, the parameter `query` is reflecting in multiple places, one of them is in the `<meta>` tag in the head section of the HTML source, the reflection is in the `content` attribute to be precise (check the below image)

{F983200}

And i was able to break out of the `content` attribute and was able to bypass the Cloudflare protection that wouldnt let me to add `http-equiv` attribute by using `%00` char to finally achieve the following redirect using a crafted payload

{F983205}

PoC: `https://streamlabs.com/content-hub/streamlabs-obs/search?query=0;url=https://google.com"%20http-%00equiv="refresh"`
Payload: `0;url=https://google.com/document.cookie"%20http-%00equiv="refresh"` 
Readable payload: `0;url=https://google.com/" http-equiv="refresh"`

## Impact

Open redirect

## Attachments
- BurpSuitePro_fbYxtoK5TV.png
- BurpSuitePro_K0xRt92DW2.png
