# All user password hash can be seen from admin panel

## Report Details
- **Report ID**: 1489892
- **URL**: https://hackerone.com/reports/1489892
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-02-23T14:14:34.414Z
- **Disclosed**: 2022-06-11T23:31:01.289Z

## Reporter
- **Username**: dark_haxor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
# Summary:
During my primary research I found that `api/users?page=1&userId=&firstName=test&lastName=&email=&partnerOrg=&highSchool=` this endpoint gives hashed password of all users.

# Steps To Reproduce:
+ Login to Admin and go to Admin--> Search Users.
+ We see a request like this was send and in response we get the hashed password of all the users.

{F1630381}

##HTTP Request:

```
GET /api/users?page=1&userId=&firstName=test&lastName=&email=&partnerOrg=&highSchool= HTTP/2
Host: hackers.upchieve.org
Cookie: connect.sid=s%3AaF9AzSGty6cZOHNTyahImdIzUoSDCWuB.ofJzU1Tr25W2Kd2unMFlpS66K4VsPtK3YE0xmHvUZGU; _gcl_au=1.1.2044852401.1644683211; _ga=GA1.2.1811282066.1644683221; _csrf=whFQZop0bR6xQh6KtmNQLBfS; __cf_bm=2KDOr5.OqRrhRkG3HhcUs0vp57z5O6ajxpDfiZBVfGA-1645624338-0-AU9Yc7GzGOeS+GILwGKIEWzbToj/4SEhBw5wog9uHW0rWkomQxhuC756xXzHVx5vQZWpm8qGUUNBPxFB6cvtTQ9BfzCJWA5Zq9jDYP3Z9p+Olw+qCSjBa/rjulVDF51Kjg==; io=zIQg9SCEJ_ZblHVdAAAy; _gid=GA1.2.1980510602.1645624337; ph_bogus_posthog=%7B%22distinct_id%22%3A%22619ea2c8488636001138121f%22%2C%22%24device_id%22%3A%2217eeec24dba290-06a553129ffb21-4c3e227d-1fa400-17eeec24dbb903%22%2C%22%24user_id%22%3A%22619ea2c8488636001138121f%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22%24referrer%22%3A%22%24direct%22%2C%22%24referring_domain%22%3A%22%24direct%22%2C%22%24session_recording_enabled%22%3Afalse%7D
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Newrelic: eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI2NzQ5NzQiLCJhcCI6IjQyOTE2Mzc1MCIsImlkIjoiNzFhMzgxOGNjZDQ2OGNkYyIsInRyIjoiYjBiM2Q0YTI3N2NjZDZmODBmOWU2NWIwODBlY2U1NDAiLCJ0aSI6MTY0NTYyNTExMDY0N319
Traceparent: 00-b0b3d4a277ccd6f80f9e65b080ece540-71a3818ccd468cdc-01
Tracestate: 2674974@nr=0-1-2674974-429163750-71a3818ccd468cdc----1645625110647
X-Csrf-Token: KeypPQND-ch0LQMIPkTckMoZdYHTBgA4Mha0
X-Requested-With: XMLHttpRequest
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
```

## Impact

Chances that weak passwords can be cracked and people might have same passwords for email and other places.

## Attachments
- one_1_upchieve.png
