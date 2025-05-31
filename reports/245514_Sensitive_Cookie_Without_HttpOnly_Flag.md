# Sensitive Cookie Without 'HttpOnly' Flag

## Report Details
- **Report ID**: 245514
- **URL**: https://hackerone.com/reports/245514
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-07-03T11:43:28.427Z
- **Disclosed**: 2017-07-03T17:56:12.349Z

## Reporter
- **Username**: jatanvora
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
hello wakatime security team

i found security vulnerability:Sensitive Cookie Without 'HttpOnly' Flag

when i was testing your website then i notice that there is some csrftoken cookie appare in responce
but the cookie have not httponly flag.you must should set httponly flag for some following security resons 
The HttpOnly flag directs compatible browsers to prevent client-side script from accessing cookies. Including the HttpOnly flag in the Set-Cookie HTTP response header helps mitigate the risk associated with Cross-Site Scripting (XSS) where an attacker's script code might attempt to read the contents of a cookie and exfiltrate information obtained. When set, browsers that support the flag will not reveal the contents of the cookie to a third party via client-side script executed via XSS.

request:
GET / HTTP/1.1
Host: wakatime.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: csrftoken=bbdf6a9801dcbf0f9d9c550889e329b92c34e346; session=.eJwFwTEOgCAMAMC_dHZAUEP5DJHSGqNCUmQy_N27D6ipvPXiAgFSyrLt6M2cKYkRzEjrarxHdhYTWnILu2WDCaqeR1QWVmWFUPp9T9DfJ7balbhB-Mb4AYjwHus.DDu6uw.kVmY8vHB5SEBffquBd7M0NEFdD0; _ga=GA1.2.858545108.1499081025; _gid=GA1.2.1080471503.1499081025; _gat=1; _hp2_ses_props.1557708959=%7B%22ts%22%3A1499081025761%2C%22d%22%3A%22wakatime.com%22%2C%22h%22%3A%22%2F%22%7D; _hp2_id.1557708959=%7B%22userId%22%3A%221418123477830247%22%2C%22pageviewId%22%3A%224144766225614678%22%2C%22sessionId%22%3A%221248345008666788%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

responce:
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 03 Jul 2017 11:31:41 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Cache-Control: no-cache
Set-Cookie: csrftoken=bbdf6a9801dcbf0f9d9c550889e329b92c34e346; Expires=Mon, 10-Jul-2017 11:31:41 GMT; Max-Age=604800; Secure; Path=/
Vary: Cookie
Set-Cookie: session=.eJwFwUEOhCAMAMC_9MyBFTWUzxAp7WqWlaSVk_HvztyQRdl2SLI1YwdkKlf_8QkJSqmybhj9p1IRL1iRlsXHiBwmLDhRmDnMKzjoenyzsrAqK6RztOZgXP9sfSixQbqf5wWabyQX.DDu8nQ.HJJjZvVsyEWAwpeUJdH3VPK5ZQQ; Secure; HttpOnly; Path=/
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' data: https://*.stripe.com https://*.braintreegateway.com https://api.github.com https://*.olark.com https://wakatime.disqus.com https://*.disquscdn.com https://analytics.twitter.com https://platform.twitter.com https://static.ads-twitter.com/ https://www.google-analytics.com https://heapanalytics.com https://*.heapanalytics.com https://connect.facebook.net https://load.sumome.com https://sumome-140a.kxcdn.com; img-src 'self' data: https://ssl.google-analytics.com https://s-static.ak.facebook.com https://syndication.twitter.com https://sumome.com https://sumome-140a.kxcdn.com https://checkout.paypal.com https://bitbucket.org https://avatar-cdn.atlassian.com assets-cdn.github.com www.google-analytics.com https://*.braintreegateway.com heapanalytics.com https://analytics.twitter.com t.co *.twimg.com *.facebook.com *.olark.com *.disqus.com *.disquscdn.com *.githubusercontent.com *.gravatar.com *.wp.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://*.olark.com https://sumome-140a.kxcdn.com *.disquscdn.com; media-src https://*.olark.com https://*.amazonaws.com; font-src 'self' https://fonts.gstatic.com; frame-src 'self' https://*.stripe.com https://www.facebook.com https://s-static.ak.facebook.com https://staticxx.facebook.com https://*.twitter.com https://*.olark.com https://disqus.com www.youtube.com player.vimeo.com checkout.paypal.com; object-src 'self'; connect-src 'self' api.github.com www.google-analytics.com heapanalytics.com https://sumome.com *.olark.com https://avatar-cdn.atlassian.com https://secure.gravatar.com *.disqus.com;
Content-Length: 37899

<!DOCTYPE html>
<html>
......(i remove this informetion because of report length)
</html>

as you seen in responce there is a folloing cookie
csrftoken=bbdf6a9801dcbf0f9d9c550889e329b92c34e346; Expires=Mon, 10-Jul-2017 11:31:41 GMT; Max-Age=604800; Secure; Path=/

but this cookie have not httponly flag and it contain a csrftoken informetion

for more informetion let me know.

regard 
black panther (jatan)

## Attachments
No attachments
