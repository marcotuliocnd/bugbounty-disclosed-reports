# Bad content-type in response header when getting document can lead to html injection

## Report Details
- **Report ID**: 173721
- **URL**: https://hackerone.com/reports/173721
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-03T21:13:23.868Z
- **Disclosed**: 2017-01-12T20:45:39.433Z

## Reporter
- **Username**: trichimtrich_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Bug
When request document by genesis_id or filename, the content-type field in response header is 'text/html'.
And the document content can be anything. So if we upload an odt file with html format and share with other users, it can lead to html injection when others request that file.

## PoC
- img1 via es_id
- img2 via filename (share with others)


## Attachments
- img1.png
- img2.PNG
