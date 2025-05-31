# Authentication Bypass with usage of PreSignedURL

## Report Details
- **Report ID**: 2337427
- **URL**: https://hackerone.com/reports/2337427
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-27T19:50:47.574Z
- **Disclosed**: 2024-03-22T17:06:13.638Z

## Reporter
- **Username**: kolokokop
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
Hello,

## Summary

It was identified that ownCloud Infinite Scale (oCIS) is prone to vulnerability that allows access any file without authentication. Prior knowledge of username and filename is needed to access file.

In this instance, vulnerability was result of the default enabled PreSignedURL, which incorrectly checks the expiry date in `OC-Date` and `OC-Expires` variables. If the date has expired, the signing key has not been checked and access to file is granted.

## Steps to reproduce

1. Login to the ownCloud Infinite Scale instance - e.g. `admin` username was used.

2. Create new file - Press "New" and "Plain text file" - `secret.txt` filename was used.

{F3011022}

3. Add some content to the file - e.g. "secret file content" and save the file.

{F3011023}

In addition, it is possible to check that the file is not public or shared with anyone.

{F3011024}

4. Access the file without authentication with the following link builded with known username and known filename:

`https://{ownload-instance}/remote.php/dav/files/{username}/{filename}?OC-Credential={username}&OC-Verb=GET&OC-Expires=60&OC-Date=2024-01-27T00:00:00.000Z&OC-Signature=notchecked`

In particular the following link was used:

`https://localhost:9200/remote.php/dav/files/admin/secret.txt?OC-Credential=admin&OC-Verb=GET&OC-Expires=60&OC-Date=2024-01-27T00:00:00.000Z&OC-Signature=notchecked`

{F3011032}

## Details

Default settings for PreSignedURL allows usage of GET requests and therefore download files.


[`services/proxy/pkg/config/defaults/defaultconfig.go`](https://github.com/owncloud/ocis/blob/v4.0.5/services/proxy/pkg/config/defaults/defaultconfig.go#L74):

```go
		PreSignedURL: config.PreSignedURL{
			AllowedHTTPMethods: []string{"GET"},
			Enabled:            true,
		},
```

Inside function [`validate`](https://github.com/owncloud/ocis/blob/v4.0.5/services/proxy/pkg/middleware/signed_url_auth.go#L73) another function [`urlIsExpired`](https://github.com/owncloud/ocis/blob/v4.0.5/services/proxy/pkg/middleware/signed_url_auth.go#L126) is called to check for expiration of `OC-Date` and `OC-Expires`.However, in the case of expired dates, the function returns a null error, resulting in successful authentication of requests without checking the user's signing signature/key.

{F3011035}

{F3011036}

{F3011037}

## Vulnerable versions

The following tags on GitHub was found to be vulnerable - it was not tested on different branches/tags:

- v5.0.0-rc.3
- v5.0.0-rc.2
- v4.0.5

## Temporary remediation

Disabling PreSignedURLs, e.g. with environment variable `PROXY_ENABLE_PRESIGNEDURLS=false` blocked unrestricted access to files.

## Impact

Broken Access Control vulnerabilities have severe consequences, both for organizations and end-users. Attackers exploiting Broken Access Control can gain access to sensitive data, including personal information, financial records, or confidential documents, compromising user privacy and security. In this instance, it was possible to access the organization's and users' private files without authentication.

## Attachments
- steps-1-create-file.png
- steps-2-add-content.png
- steps-3-file-not-shared-or-public.png
- steps-4-access-file-request.png
- debug-0-validate-expired-but-no-error.png
- debug-1-urlIsExpired.png
- debug-2-Authenticate-validate-returns-no-error.png
