# Bypassing quota limit 

## Report Details
- **Report ID**: 173622
- **URL**: https://hackerone.com/reports/173622
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-10-03T10:19:05.513Z
- **Disclosed**: 2017-03-10T19:10:11.187Z

## Reporter
- **Username**: nordin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi
an user can upload files despite having a limited quota by changing value of  "OC-Total-Length" in header  to "A" or adding "X-Expected-Entity-Length" in header with "A" value

in normal insuffisant storage we have:

PUT /remote.php/webdav/a.jpg HTTP/1.1
Content-Type: application/octet-stream
OC-Async: 1
OC-Chunk-Size: 10000000
OC-Total-Length: 200

Response
HTTP/1.1 507 Insufficient Storage

after changing OC-Total-Length: A , the file is created and the response is:

HTTP/1.1 201 Created

the user can largely exceed its quota and bypass admin restriction
affected version:  Latest stable version: 10.0.1 

## Attachments
No attachments
