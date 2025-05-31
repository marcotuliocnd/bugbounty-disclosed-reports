# Ratelimits do not apply to OCS DataResponse

## Report Details
- **Report ID**: 1214158
- **URL**: https://hackerone.com/reports/1214158
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-06-01T12:10:56.814Z
- **Disclosed**: 2021-08-11T09:14:01.884Z

## Reporter
- **Username**: lukasreschkenc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Using `$response->throttle()` on a DataResponse doesn't work as it is being transformed by BaseResponse into a OCS response. This response does not propagate any throttled setting.

## Impact

Ratelimits on OCS DataResponse not functional.

## Attachments
No attachments
