# https://wakatime.com/ website CSP "script-src" includes "unsafe-inline"

## Report Details
- **Report ID**: 244766
- **URL**: https://hackerone.com/reports/244766
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-30T14:28:48.665Z
- **Disclosed**: 2017-07-24T14:31:50.312Z

## Reporter
- **Username**: silv3rpoision
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Description: 
The wakatime.com website (https://wakatime.com/) has a Content-Security-Policy configured.
However, the "script-src" parameter is set to "unsafe-inline", which allows injection of user passed values, which in result can be misused for Cross-Site Scripting attacks. As a best practice, this value should not be included as a "script-src" parameter, if possible.

Steps To Reproduce

The header can be read using a simple curl query:
cache-control:no-cache
content-encoding:gzip
content-security-policy:default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' data: https://*.stripe.com https://*.braintreegateway.com https://api.github.com https://*.olark.com https://wakatime.disqus.com https://*.disquscdn.com https://analytics.twitter.com https://platform.twitter.com https://static.ads-twitter.com/ https://www.google-analytics.com https://heapanalytics.com https://*.heapanalytics.com https://connect.facebook.net https://load.sumome.com https://sumome-140a.kxcdn.com; img-src 'self' data: https://ssl.google-analytics.com https://s-static.ak.facebook.com https://syndication.twitter.com https://sumome.com https://sumome-140a.kxcdn.com https://checkout.paypal.com https://bitbucket.org https://avatar-cdn.atlassian.com assets-cdn.github.com www.google-analytics.com https://*.braintreegateway.com heapanalytics.com https://analytics.twitter.com t.co *.twimg.com *.facebook.com *.olark.com *.disqus.com *.disquscdn.com *.githubusercontent.com *.gravatar.com *.wp.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://*.olark.com https://sumome-140a.kxcdn.com *.disquscdn.com; media-src https://*.olark.com https://*.amazonaws.com; font-src 'self' https://fonts.gstatic.com; frame-src 'self' https://*.stripe.com https://www.facebook.com https://s-static.ak.facebook.com https://staticxx.facebook.com https://*.twitter.com https://*.olark.com https://disqus.com www.youtube.com player.vimeo.com checkout.paypal.com; object-src 'self'; connect-src 'self' api.github.com www.google-analytics.com heapanalytics.com https://sumome.com *.olark.com https://avatar-cdn.atlassian.com https://secure.gravatar.com *.disqus.com;
content-type:text/html; charset=utf-8
date:Fri, 30 Jun 2017 14:27:18 GMT
server:nginx
set-cookie:session=.███; Secure; HttpOnly; Path=/
set-cookie:csrftoken=███████; Expires=Fri, 07-Jul-2017 14:27:18 GMT; Max-Age=604800; Secure; Path=/
status:200
strict-transport-security:max-age=31536000; includeSubDomains; preload
vary:Cookie
x-content-type-options:nosniff
x-frame-options:SAMEORIGIN
x-xss-protection:1; mode=block

As can be seen, "unsafe-inline" is included in in the list of "script-src" parameters. 
This does not result in an immediate threat, but should be excluded, if possible, as a best practice. For further information, see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src

## Attachments
No attachments
