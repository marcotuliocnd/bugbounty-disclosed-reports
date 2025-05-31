# XSS reflected on [https://www.pixiv.net]

## Report Details
- **Report ID**: 766633
- **URL**: https://hackerone.com/reports/766633
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-31T23:31:06.441Z
- **Disclosed**: 2020-12-17T03:33:46.885Z

## Reporter
- **Username**: bcobain23
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pixiv

## Vulnerability Information
## Summary:
I found a xss reflected on https://www.pixiv.com URL and in the search bottom from Chrome IOS 13.1

## Steps To Reproduce:

  1. In the URL https://www.pixiv.net/en/%5B'-alert(document.cookie)-'%5D Add Payload ['-confirm(3)-']
  1. In the URL https://www.pixiv.net/en/%5B'-alert(document.cookie)-'%5D Add ['-alert(document.cookie)-']
  1. In the Search Bar Add ['-confirm(3)-'] and the URL is https://www.pixiv.net/en/tags/%5B'-confirm(3)-'%5D#discover

## Impact

Steal Cookie

## Attachments
- image3.jpeg
- image1.jpeg
- image0.png
- image2.png
