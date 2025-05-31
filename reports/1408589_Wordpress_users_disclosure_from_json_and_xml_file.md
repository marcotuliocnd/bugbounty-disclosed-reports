# Wordpress users disclosure from json and xml file

## Report Details
- **Report ID**: 1408589
- **URL**: https://hackerone.com/reports/1408589
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-23T22:31:35.245Z
- **Disclosed**: 2022-09-02T09:25:29.735Z

## Reporter
- **Username**: drak3hft7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
It's possible to get information about the users registered (such as: username) without authentication in Wordpress via API on:
https://www.mtn.co.sz/wp-json/oembed/1.0/embed?url=https://www.mtn.co.sz/&format=json
https://www.mtn.co.sz/author-sitemap.xml

## Steps To Reproduce:
The path https://www.mtn.co.sz/wp-json/wp/v2/users/me  is configured correctly. Active usernames cannot be displayed and the application responds with code 401, saying that I am not authorized.

{F1523939}

But there is this active path, which allows anyone to view active usernames:
https://www.mtn.co.sz/wp-json/oembed/1.0/embed?url=https://www.mtn.co.sz/&format=json
https://www.mtn.co.sz/author-sitemap.xml

{F1523940}

{F1523941}

Username found:
- waseem
- nkosivile

These users can be used to bruteforce, thanks also to the enabled xmlrpc.php file. Perform this request with Burp:
```
POST /xmlrpc.php HTTP/1.1
Host: www.mtn.co.sz
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Te: trailers
Content-Length: 180

<methodCall> <methodName>wp.getUsersBlogs</methodName> <params> <param><value>\{\{admin\}\}</value></param> <param><value>\{\{password\}\}</value></param></params></methodCall>
```
You can replace the "admin" parameter with the username.

{F1523945}

## Impact

It's possible to get all the users registered on the system and create a bruteforce directed to these users.

**Suggested Mitigation/Remediation Actions**
As already done for the "/wp-json/wp/v2/users/" path, I recommend blocking the active path as well.
If the XMLRPC.php file is not used, it should be disabled and removed completely to avoid potential risks by bruteforce. Otherwise, it should at least be blocked from outside access.

## Attachments
- 01.PNG
- 02.PNG
- 03.PNG
- 04.PNG
