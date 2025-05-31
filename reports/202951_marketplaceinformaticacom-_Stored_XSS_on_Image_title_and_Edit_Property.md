# [marketplace.informatica.com]- Stored XSS on Image title and Edit Property

## Report Details
- **Report ID**: 202951
- **URL**: https://hackerone.com/reports/202951
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-02T17:08:00.847Z
- **Disclosed**: 2017-04-21T12:06:39.594Z

## Reporter
- **Username**: fillawful
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
By uploading and image with the title of ``` "><svg onload=alert(1)>.jpg``` and allowing anyone to edit the Document under collaboration settings, XSS can be triggered by any user attempting to edit the document.

 POC
====
1.  Log into marketplace and go to profile page.  Select New > Document
2.  Choose to upload document and browse to your image with the javascript payload as the name.
3.  Enter anything as Description and and tags field
4.  Select visibility open to anyone
5. Expand collaboration options and allow anyone to edit document. (This drastically increases security issue.)
6. Choose to publish
7. After publishing choose to Edit Document from the right hand menu and observe XSS.

Please see accompanying screenshots as POC

### Please let me know if you need any more information. Cheers!


## Attachments
- Upload.PNG
- EditDocument.PNG
- AnyOneCanEdit.PNG
- XSS.PNG
