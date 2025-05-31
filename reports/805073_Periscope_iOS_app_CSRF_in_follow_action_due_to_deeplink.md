# Periscope iOS app CSRF in follow action due to deeplink

## Report Details
- **Report ID**: 805073
- **URL**: https://hackerone.com/reports/805073
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-26T09:10:46.564Z
- **Disclosed**: 2020-03-31T22:53:53.375Z

## Reporter
- **Username**: mgf15
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Summary

This issue is mainly in the Periscope iOS app against CSRF follow action using deeplink.

as the report  #583987 the CSRF work on iOS app 

POC 1

QR code to follow periscope profile 

`pscp://user/periscopeco/follow
`

███████

POC2 by kunal94

```
<!DOCTYPE html>
<html>
<a href="pscp://user/<any user-id>/follow">CSRF DEMO</a>
</html>
```
video
█████████

## Impact

CSRF Follow against any user in periscope iOS app

## Attachments
No attachments
