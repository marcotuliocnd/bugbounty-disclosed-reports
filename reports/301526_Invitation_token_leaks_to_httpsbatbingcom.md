# Invitation token leaks to https://bat.bing.com

## Report Details
- **Report ID**: 301526
- **URL**: https://hackerone.com/reports/301526
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-31T12:10:46.226Z
- **Disclosed**: 2018-01-11T18:57:53.679Z

## Reporter
- **Username**: zuriel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary**

Invitation page contains iframes that points to https://b5s.hackerone-ext-content.com/#!/invitations/<invitation token> and https://a4l.hackerone-ext-content.com/#!/invitations/<invitation token>. A *GET* request to these endpoints executes a script that points to `https://bat.bing.com/bat.js`. The corresponding request to bing contains the invitation tokens.

**Description**

While checking the source code of an team invitation page (https://hackerone.com/invitations/8e44119f60be8670d1e3f99a01359cbc), I found two iframe links - `https://b5s.hackerone-ext-content.com/#!/invitations/8e44119f60be8670d1e3f99a01359cbc` and `https://a4l.hackerone-ext-content.com/#!/invitations/8e44119f60be8670d1e3f99a01359cbc` where `8e44119f60be8670d1e3f99a01359cbc`is the invitation token. {F250542}


To find out more about these endpoints,i issued a simple GET requests to these urls. GET requests to these endpoints returned a page that contains a script that points to - `https://bat.bing.com/bat.js`.

The response of the GET request to https://b5s.hackerone-ext-content.com/#!/invitations/8e44119f60be8670d1e3f99a01359cbc looks as follows: 

```
<!DOCTYPE html>
<html>
  <head></head>
  <body style="background-color: transparent">
    <script>
      (function(w,d,t,r,u){var f,n,i;w[u]=w[u]||[],f=function(){var o={ti:"5295042"};o.q=w[u],w[u]=new UET(o),w[u].push("pageLoad")},n=d.createElement(t),n.src=r,n.async=1,n.onload=n.onreadystatechange=function(){var s=this.readyState;s&&s!=="loaded"&&s!=="complete"||(f(),n.onload=n.onreadystatechange=null)},i=d.getElementsByTagName(t)[0],i.parentNode.insertBefore(n,i)})(window,document,"script","https://bat.bing.com/bat.js","uetq");
    </script>
    <noscript>
      <img src="//bat.bing.com/action/0?ti=5295042&Ver=2" height="0" width="0" style="display:none; visibility: hidden;" />
    </noscript>
  </body>
</html>
```

As we can see the page calls a script at `https://bat.bing.com/bat.js` and the script is executed. 

The script fires a corresponding request to bat.bing.com that contains the invitation token. It looks as follows:

```
https://bat.bing.com/action/0?ti=5295042&Ver=2&mid=ab8e7bd3-541b-59ea-0551-7041b2ede6e3&evt=pageLoad&sid=bbebc657-0&lt=127&pi=1001431019&lg=en-US&sw=1366&sh=768&sc=24&p=https://b5s.hackerone-ext-content.com/#!/invitations/8e44119f60be8670d1e3f99a01359cbc&r=&msclkid=███
```

The `p` parameter contains the entire url along with the invitation token - `p=https://b5s.hackerone-ext-content.com/#!/invitations/8e44119f60be8670d1e3f99a01359cbc` where `8e44119f60be8670d1e3f99a01359cbc`is the invitation token.

Thus the invitation token is sent to bat.bing.com as a part of the request.

## Impact

1. Leaking member invitation tokens can reveal pretty much everything about a program. 
1. Private programs could be adversely affected by leaking private invitation tokens.

## Attachments
- bl1.PNG
