# More content spoofing through dir param in the files app

## Report Details
- **Report ID**: 154827
- **URL**: https://hackerone.com/reports/154827
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-07-29T05:41:44.494Z
- **Disclosed**: 2016-11-04T17:16:25.899Z

## Reporter
- **Username**: lmx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi! It's still possible to use an invalid `dir` param to spoof messages in the directory breadcrumbs area.

For example, you can use URL-encoded periods to bypass the directory traversal prevention. By referencing a path that returns a 301, you can add a message in the dir param F108266:

https://demo.nextcloud.com/index.php/apps/files/?dir=%2E%2E/%2E%2E/%2E%2E/.well-known/caldav/Error%20-%20please%20restart%20your%20computer%20to%20continue

Also, in Chrome, the presence of a null byte (%00) in the url causes a CSP error for an ajax request upon pageload, which prevents the redirect to `dir=/` and allows you to put a message in the dir param F108267:

https://demo.nextcloud.com/index.php/apps/files/?dir=%00Error!%20Please%20restart%20your%20computer%20and%20try%20again

Please let me know if you need more info. Thanks!

## Attachments
- 301-response.png
- chrome-null-byte.png
