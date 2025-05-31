# Reflected XSS in OAuth complete endpoints

## Report Details
- **Report ID**: 1502099
- **URL**: https://hackerone.com/reports/1502099
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-03-06T21:01:59.518Z
- **Disclosed**: 2023-09-28T09:31:32.736Z

## Reporter
- **Username**: zerodivisi0n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
The following endpoints are vulnerable to reflected XSS:
```
GET /oauth/{service:[A-Za-z0-9]+}/complete
GET /api/v3/oauth/{service:[A-Za-z0-9]+}/complete
GET /signup/{service:[A-Za-z0-9]+}/complete
GET /login/{service:[A-Za-z0-9]+}/complete
```

The vulnerability exists due to the lack of sanitizing `redirect_to` field in `state` query param [here](https://github.com/mattermost/mattermost-server/blob/c114aba628e06e726aa1b5d9f3736d1fd154594c/web/oauth.go#L287-L288).

## Steps To Reproduce:

  1. Setup local mattermost instance e.g. on address [http://localhost:8065](http://localhost:8065) ([server guide](https://developers.mattermost.com/contribute/server/developer-setup/), [webapp guide](https://developers.mattermost.com/contribute/webapp/developer-setup/))
  1. Enable gitlab auth at Enable gitlab auth at [http://localhost:8065/admin_console/authentication/gitlab](http://localhost:8065/admin_console/authentication/gitlab). (There may be other ways to enable OAuth, this one seemed the easiest to me)
  1. Open the following link: [http://mattermost:8065/login/gitlab/complete?code=x&state=eyJhY3Rpb24iOiJtb2JpbGUiLCJyZWRpcmVjdF90byI6InRlc3RcIj48c2NyaXB0PmFsZXJ0KGRvY3VtZW50LmRvbWFpbik8L3NjcmlwdD4ifQ==](http://mattermost:8065/login/gitlab/complete?code=x&state=eyJhY3Rpb24iOiJtb2JpbGUiLCJyZWRpcmVjdF90byI6InRlc3RcIj48c2NyaXB0PmFsZXJ0KGRvY3VtZW50LmRvbWFpbik8L3NjcmlwdD4ifQ==). This link contains base64-encoded payload in `state` param: `{"action":"mobile","redirect_to":"test\"><script>alert(document.domain)</script>"}`
  1. Get javascript alert with current domain.

## Impact

An attacker can distribute a link in a chat with malicious javascript code. This code can send ajax requests on behalf of the user.

## Attachments
No attachments
