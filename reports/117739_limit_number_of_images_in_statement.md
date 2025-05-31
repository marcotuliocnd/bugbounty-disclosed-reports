# limit number of images in statement

## Report Details
- **Report ID**: 117739
- **URL**: https://hackerone.com/reports/117739
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-02-20T23:00:19.790Z
- **Disclosed**: 2017-06-16T13:55:05.733Z

## Reporter
- **Username**: hogarth45
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello

The use of the images in the statements 

`![](http://blackdoorsec.net:80/1    "HTTP") `

There appears to be no limit on how many can be inserted.
On my own account "https://gratipay.com/~34534534fsfs/" I placed 100

Gratipay users could unknowingly become part of a DDoS attack against another site.

I would recommend limiting the number of images that can be placed.

Attached is a video of just a traffic counter being triggered by the page load.

## Attachments
- Gratipay.avi
