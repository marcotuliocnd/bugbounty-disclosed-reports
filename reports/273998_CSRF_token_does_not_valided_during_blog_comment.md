# CSRF token does not valided during blog comment

## Report Details
- **Report ID**: 273998
- **URL**: https://hackerone.com/reports/273998
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-03T07:32:14.444Z
- **Disclosed**: 2017-10-16T05:49:29.614Z

## Reporter
- **Username**: ranjit_p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
SUMMURY
=================
i tested that all post request has CSRF token.
During Author profile creation also a CSRF token is posted. Now when i removed this CSRF token , show   s error like bellow 
```
CSRF validation failed

0 /var/www/csprng/src/Cabin/Bridge/Controller/Author.php(52): Airship\Engine\Controller->post(Object(Airship\Cabin\Bridge\Filter\Author\AuthorFilter))
/var/www/csprng/src/Engine/AutoPilot.php(485): Airship\Cabin\Bridge\Controller\Author->create()
 /var/www/csprng/src/Engine/AutoPilot.php(315): Airship\Engine\AutoPilot->serve(Array, Array)
 /var/www/csprng/src/public/index.php(86): Airship\Engine\AutoPilot->route(Object(Airship\Engine\Networking\HTTP\ServerRequest))
{main}
```
So its a CSRF validation failed error.
Now if request submitted with proper CSRF token, then response will be 302 redirect.
So, i come to this point that if proper CSRF token provided then we get 302 redirect as success response and If CSRF validation failed then we get above error response or something else.

Now  during Blog Reply comment Following request POST data is made
```

_CSRF_TOKEN=KrkFX0bGkcwgoIKX8Y7KKr1F%3A0ElYiUhZ5wJDSS8kE2FmPxY58Dr3533SH63ZRJBPBfO-&author=47&name=&email=&url=&message=ssdfsfsfsf+sfsd&g-recaptcha-response=03AJzQf7Ojuy_9znHGgl-bZOSweJZo...............

```
Now remove the CSRF_TOKEN and see  302 redirect as response header, this  indicate that request is successfull and server does not checked CSRF here And no CSRF validation error.
```
HTTP/1.1 302 Found
Date: Tue, 03 Oct 2017 01:15:15 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Cache-Control: no-store, no-cache, must-revalidate
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Location: https://cspr.ng/blog/2017/05/csprng-airship-dev-branch#comments
Pragma: no-cache
Status: 302 Found
```
i checked four file are reponsible for blog comment and non of them are checking CSRF.
https://github.com/paragonie/airship/blob/master/src/Cabin/Bridge/Controller/Blog.php
https://github.com/paragonie/airship/blob/master/src/Cabin/Bridge/Model/Blog.php
https://github.com/paragonie/airship/blob/master/src/Cabin/Hull/Model/Blog.php
https://github.com/paragonie/airship/blob/master/src/Cabin/Hull/Controller/BlogPosts.php#107
here i see only the last file verify google captcha but not CSRF

STEP TO REPRODUCE
======================
1. goto any  post and comment
2. capture request and remove CSRF token
3. submit that request and see successfull, no CSRF validation error


## Attachments
No attachments
