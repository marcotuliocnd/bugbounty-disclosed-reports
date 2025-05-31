# Open redirect on the https://tt.hboeck.de

## Report Details
- **Report ID**: 503922
- **URL**: https://hackerone.com/reports/503922
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-01T17:47:36.835Z
- **Disclosed**: 2019-03-03T16:24:37.830Z

## Reporter
- **Username**: zophi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hannob

## Vulnerability Information
Hi Team!

Testing request:
`POST /public.php?return=%2F HTTP/1.1
Host: tt.hboeck.de
...........
op=login&login={….}&password={...}&profile=0`

Vulnerable parameter: `return`

Method: `POST` -> `GET` -> OK

POC:
`https://tt.hboeck.de/public.php?return=http%3a%2f%2fevil.com%2f&op=login&login=password=&profile=0`

## Impact

User can be redirect to malicious site.

## Attachments
- redir.jpg
