# Web cache deception attack - expose token information

## Report Details
- **Report ID**: 397508
- **URL**: https://hackerone.com/reports/397508
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-21T02:07:00.233Z
- **Disclosed**: 2018-09-20T02:14:53.128Z

## Reporter
- **Username**: memon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hello,

I have found new Vulnerability in your website which called Web cache deception attack.
It's found first time in Paypal.

###Web Cache Deception Attack
Websites often tend to use web cache functionality to store files that are often retrieved, to reduce latency from the web server.

####Let's see an example of web cache.
Website http://www.example.com is configured to go through a reverse proxy. A dynamic page that is stored on the server and returns personal content of users, such as http://www.example.com/home.php, will have to create it dynamically per user, since the data is different for each user. This kind of data, or at least its personalized parts, isn't cached. What's more reasonable and common to cache are static, public files: style sheets (css), scripts (js), text files (txt), images (png, bmp, gif), etc. This makes sense because these files usually don't contain any sensitive information. In addition, as can be found in various best practices articles about web cache configuration, it's recommended to cache all static files that are meant to be public, and disregard their HTTP caching headers.
What happens when accessing a URL like http://www.example.com/home.php/non-existent.css
A GET request to that URL will be produced by the browser. The interesting thing is the server's reaction – how does it interpret the request URL? Depending on its technology and configuration (the URL structure might need to be built slightly different for different servers), the server returns the content of http://www.example.com/home.php. And yes, the URL remains http://www.example.com/home.php/non-existent.css. The HTTP headers will be the same as for accessing http://www.example.com/home.php directly: same caching headers and same content type (text/html, in this case).

### Steps To Reproduce:
1. Login to your account.
2. Go to `https://chaturbate.com/my_collection/`.
3. Then after go to `https://chaturbate.com/my_collection/min.js`.
4. Open private mode (Incognito window) or Any other browser  and paste `https://chaturbate.com/my_collection/min.js` url in address bar. Now you can see then without authanticated i can all the detaills of user account.

#####Attached video PoC for more information.

I hope you understand.

Regards,
Memon

## Impact

An attacker who lures a logged-on user to access `https://chaturbate.com/my_collection/min.js` will caue this page – containing the user's personal content and Token information – to be cached and thus publicly-accessible. It could get even worse, if the body of the response contains (for some reason) the session identifier, security answers or CSRF tokens. All the attacker has to do now is to access this page on his own and expose this data.

## Attachments
- web_cache.mov
