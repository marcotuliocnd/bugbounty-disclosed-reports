# Reflected XSS vector

## Report Details
- **Report ID**: 190247
- **URL**: https://hackerone.com/reports/190247
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-11T00:39:09.185Z
- **Disclosed**: 2017-02-22T17:41:20.978Z

## Reporter
- **Username**: creased
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gocd

## Vulnerability Information
Hello GoCD team,

I noticed a reflected / stored XSS vulnerability vector that could potentially be used to impact security of GoCD users.

- https://www.go.cd/user/upoad/..%2F..%2F
- https://docs.go.cd/current/user/upoad/..%2F..%2F

As you should see, this link is considered as valid by the HTTP service and thus does not cause redirect to root of *.go.cd nor return of an HTTP error code (e.g., 404 not found) as it should be...

Such a link can be used to load an unexpected script located on the HTTP server of *.go.cd, eventually uploaded by user (see screenshot)

Please let me know if you need more information!

Looking forward!

## Attachments
- docs_gocd_xss_vector.png
- gocd_xss_vector.png
