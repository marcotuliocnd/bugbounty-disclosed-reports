# CSRF in twitterflightschool.com ( CAN POST ON TIMELINE WITHOUT USER PERMISSION)

## Report Details
- **Report ID**: 115158
- **URL**: https://hackerone.com/reports/115158
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-07T04:18:28.053Z
- **Disclosed**: 2017-11-06T19:09:21.383Z

## Reporter
- **Username**: cymtrick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
1) Go to twitterflightschool.com and start intercepting every request .
2) No csrf tokens are present in the requests
3) Even in account settings there are no csrf tokens
Attacker could post on twitter timeline of user (https://twitterflightschool.com/module/twitter-for-executives/chapter/final)
Tcp dump:
```
POST /api/twitter/upload HTTP/1.1
Host: twitterflightschool.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://twitterflightschool.com/module/twitter-for-executives/chapter/final
Content-Length: 328
Cookie: _ga=████; connect.sid=████████; _gat=1
Connection: keep-alive

updatedAt=2016-01-29T19%3A43%3A41.223Z&createdAt=2016-01-29T19%3A43%3A41.223Z&url=%2Fassets%2Fgifs%2Fl.gif&_id=56abc0ed22d87b9d6a64a4c2&body=%5Bobject%20Object%5D&__v=0&text=This%20bird%E2%80%99s%20gotta%20fly!%20%23TwitterFlightSchool%20completed.%20Learn%20about%20Twitter%20ads%20at%3A%20https%3A%2F%2Ftwitterflightschool.com
```
Every user on twitterflightschool can be subjected to csrf token.
Tcp dump while account settings:
```
POST /api/users/me HTTP/1.1
Host: twitterflightschool.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://twitterflightschool.com/register
Content-Length: 244
Cookie: _ga=█████████; _gat=1; connect.sid=████
Connection: keep-alive

country=IN&email=███████%40gmail.com&firstname=prashanth&lastname=varma&language=en-US&twitterId=1192789765&username=prashanth_scss&verificationUrl=https%3A%2F%2Ftwitterflightschool.com%2Fverify%2F&companyType=other&othercompany=lol
```
Tcp dump while enrolling :
```
POST /api/users/track/{COURSE_ID}/enroll HTTP/1.1
Host: twitterflightschool.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://twitterflightschool.com/track-selection
Content-Length: 20
Cookie: _ga=█████; _gat=1; connect.sid=██████
Connection: keep-alive

twitterId=1192789765
```

Regards
prashanth

## Attachments
No attachments
