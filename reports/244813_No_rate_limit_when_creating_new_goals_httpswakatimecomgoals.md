# No rate limit when creating new goals [https://wakatime.com/goals]

## Report Details
- **Report ID**: 244813
- **URL**: https://hackerone.com/reports/244813
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-30T17:56:07.760Z
- **Disclosed**: 2017-07-03T09:39:52.167Z

## Reporter
- **Username**: tty_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi there,

I was testing and found out that there's no rate limit on goals section [https://wakatime.com/goals]  that means you can create multiple goals in a sec, which would lead to server crash since there's no limit per request that a user can make. I made at least 100 request, and still got 200 OK responses per each request.  

###Steps to reproduce 

1)Intercept the request when you're creating a new goal
2) Then simply repeat that post request many times you want 




###Post request that im repeating 

```
POST /api/v1/users/current/goals HTTP/1.1
Host: wakatime.com
Connection: close
Content-Length: 46
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://wakatime.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3142.0 Safari/537.36 autochrome/red
X-CSRFToken: adffe57a9635628d6ef50435a08cc2b543293980
Content-Type: application/json
Referer: https://wakatime.com/goals
Accept-Language: en-US,en;q=0.8
Cookie: remember_token=e350a773-4dd5-4fbe-93fa-763d2dd225a2|784f02e3404fc81f6e101f3564f31c9a4a84c9f136fa7c426d4ecdbec3a1e48cdc4cf860294667b07c9b7f124729e42f6114f31a6dc48c403f3a0491c2dcc9f7; _okdetect=%7B%22token%22%3A%2214988410719200%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22wakatime.com%22%7D; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1498841086724%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=4159-757-10-7625; _ga=GA1.2.1165272144.1498753609; _gid=GA1.2.763748265.1498753609; _hp2_ses_props.1557708959=%7B%22ts%22%3A1498841068638%2C%22d%22%3A%22wakatime.com%22%2C%22h%22%3A%22%2Fdashboard%22%7D; _hp2_id.1557708959=%7B%22userId%22%3A1424637112097517%2C%22pageviewId%22%3A%224150811392355228%22%2C%22sessionId%22%3A%223005467842143517%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D; csrftoken=adffe57a9635628d6ef50435a08cc2b543293980; session=.eJwNy0kKwzAMAMC_6ByDkSwv-UxQLImWhhTs5hT693buc8Pmw-YDVpdj2gJ9Dv-8X3bCCqLuxkVaJs5YNZtzTMQSa--4cyJs1GqEBa5pY3vqPxlxlFIoJFUOyXcLjVxCyaSoisiC8P0Bqlkizw.DDgZ9g.DdlPQP-f2ljtInsoD4XHkl8gLfs; olfsk=olfsk5546653557287846; wcsid=FP2zSkV88lcS2uJE5079D0Ngb52OVa4B; hblid=YVkNBgVNELp1F6IU5079D0N2B4OrVBbg; _oklv=1498843744296%2CFP2zSkV88lcS2uJE5079D0Ngb52OVa4B

{"type":"coding","seconds":3600,"delta":"day"}
```

###Response

```
HTTP/1.1 201 CREATED
Server: nginx
Date: Fri, 30 Jun 2017 17:29:44 GMT
Content-Type: application/json
Content-Length: 2487
Connection: close
Set-Cookie: csrftoken=adffe57a9635628d6ef50435a08cc2b543293980; Expires=Fri, 07-Jul-2017 17:29:44 GMT; Max-Age=604800; Secure; Path=/
Vary: Cookie
Set-Cookie: session=.eJwNy0kKwzAMAMC_6ByDkSwv-UxQLImWhhTs5hT693buc8Pmw-YDVpdj2gJ9Dv-8X3bCCqLuxkVaJs5YNZtzTMQSa--4cyJs1GqEBa5pY3vqPxlxlFIoJFUOyXcLjVxCyaSoisiC8P0Bqlkizw.DDgcCA.zWEZl5ILKRLsGHmRYHlk9ixXWUg; Secure; HttpOnly; Path=/
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' data: https://*.stripe.com https://*.braintreegateway.com https://api.github.com https://*.olark.com https://wakatime.disqus.com https://*.disquscdn.com https://analytics.twitter.com https://platform.twitter.com https://static.ads-twitter.com/ https://www.google-analytics.com https://heapanalytics.com https://*.heapanalytics.com https://connect.facebook.net https://load.sumome.com https://sumome-140a.kxcdn.com; img-src 'self' data: https://ssl.google-analytics.com https://s-static.ak.facebook.com https://syndication.twitter.com https://sumome.com https://sumome-140a.kxcdn.com https://checkout.paypal.com https://bitbucket.org https://avatar-cdn.atlassian.com assets-cdn.github.com www.google-analytics.com https://*.braintreegateway.com heapanalytics.com https://analytics.twitter.com t.co *.twimg.com *.facebook.com *.olark.com *.disqus.com *.disquscdn.com *.githubusercontent.com *.gravatar.com *.wp.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://*.olark.com https://sumome-140a.kxcdn.com *.disquscdn.com; media-src https://*.olark.com https://*.amazonaws.com; font-src 'self' https://fonts.gstatic.com; frame-src 'self' https://*.stripe.com https://www.facebook.com https://s-static.ak.facebook.com https://staticxx.facebook.com https://*.twitter.com https://*.olark.com https://disqus.com www.youtube.com player.vimeo.com checkout.paypal.com; object-src 'self'; connect-src 'self' api.github.com www.google-analytics.com heapanalytics.com https://sumome.com *.olark.com https://avatar-cdn.atlassian.com https://secure.gravatar.com *.disqus.com;

{"data":{"chart_data":[{"actual_seconds":0,"actual_seconds_text":"0 secs","goal_seconds":3600,"goal_seconds_text":"1 hr","range":{"date":"2017-06-23","end":"2017-06-23T21:59:59Z","start":"2017-06-22T22:00:00Z","text":"Fri Jun 23rd 2017","timezone":"Europe/Tirane"},"range_status":"fail"},{"actual_seconds":0,"actual_seconds_text":"0 secs","goal_seconds":3600,"goal_seconds_text":"1 hr","range":{"date":"2017-06-24","end":"2017-06-24T21:59:59Z","start":"2017-06-23T22:00:00Z","text":"Sat Jun 24th 2017","timezone":"Europe/Tirane"},"range_status":"fail"},{"actual_seconds":0,"actual_seconds_text":"0 secs","goal_seconds":3600,"goal_seconds_text":"1 hr","range":{"date":"2017-06-25","end":"2017-06-25T21:59:59Z","start":"2017-06-24T22:00:00Z","text":"Sun Jun 25th 2017","timezone":"Europe/Tirane"},"range_status":"fail"},{"actual_seconds":0,"actual_seconds_text":"0 secs","goal_seconds":3600,"goal_seconds_text":"1 hr","range":{"date":"2017-06-26","end":"2017-06-26T21:59:59Z","start":"2017-06-25T22:00:00Z","text":"Mon Jun 26th 2017","timezone":"Europe/Tirane"},"range_status":"fail"},{"actual_seconds":0,"actual_seconds_text":"0 secs","goal_seconds":3600,"goal_seconds_text":"1 hr","range":{"date":"2017-06-27","end":"2017-06-27T21:59:59Z","start":"2017-06-26T22:00:00Z","text":"Tue Jun 27th 2017","timezone":"Europe/Tirane"},"range_status":"fail"},{"actual_seconds":0,"actual_seconds_text":"0 secs","goal_seconds":3600,"goal_seconds_text":"1 hr","range":{"date":"2017-06-28","end":"2017-06-28T21:59:59Z","start":"2017-06-27T22:00:00Z","text":"Wed Jun 28th 2017","timezone":"Europe/Tirane"},"range_status":"fail"},{"actual_seconds":0,"actual_seconds_text":"0 secs","goal_seconds":3600,"goal_seconds_text":"1 hr","range":{"date":"2017-06-29","end":"2017-06-29T21:59:59Z","start":"2017-06-28T22:00:00Z","text":"Yesterday","timezone":"Europe/Tirane"},"range_status":"fail"},{"actual_seconds":0,"actual_seconds_text":"0 secs","goal_seconds":3600,"goal_seconds_text":"1 hr","range":{"date":"2017-06-30","end":"2017-06-30T21:59:59Z","start":"2017-06-29T22:00:00Z","text":"Today","timezone":"Europe/Tirane"},"range_status":"pending"}],"delta":"day","id":"9330955b-4409-4776-887d-55f7708acceb","improve_by_percent":null,"is_enabled":true,"languages":[],"projects":[],"seconds":3600,"status":"fail","subscribers":[{"email":null,"email_frequency":"Once per week","full_name":"","user_id":"dc308571-b992-46f8-a9de-f19834f0bb0d","username":"codeguyh1"}],"title":"Code 1 hr per day","type":"coding"}}

```


###PoC (Video Unlisted)
https://youtu.be/p3cXgsTRqTM

Regards,
diti



## Attachments
- wakatime-poc-no-rate-limiting.png
