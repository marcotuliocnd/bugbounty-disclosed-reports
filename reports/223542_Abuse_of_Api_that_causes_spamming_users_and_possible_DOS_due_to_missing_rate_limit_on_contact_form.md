# Abuse of Api that causes spamming users and possible DOS due to missing rate limit on contact form

## Report Details
- **Report ID**: 223542
- **URL**: https://hackerone.com/reports/223542
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-04-24T18:50:02.719Z
- **Disclosed**: 2017-05-17T14:23:21.046Z

## Reporter
- **Username**: khalidamin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
##Summary:
In your sub-domain: https://demo.weblate.org/ , there's an endpoint that doesn't have any rate limit on it to prevent spamming you by filling the contact you form multiple times to bomb you with tons of emails.

##Description:
Spamming and Possible DOS is being possible due to missing rate limit on this endpoint.

**Request**
POST /contact/ HTTP/1.1
Host: demo.weblate.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://demo.weblate.org/
Cookie:XXX
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 334

csrfmiddlewaretoken=XXX&subject=&name=&email=asd%40yahoo.com&message=&content=

**Suggested Fix**
Implement additional checking per API request such as a unique token or identifier that changes per request to prevent mass spamming, additional Rate limiting measures can be implemented such as IP blacklisting, or account banning if a certain amount of requests are made.

##Steps To Reproduce:
1- Visit https://demo.weblate.org/contact/?t=reg
2- Fill the form, send it and intercept the request
3- Using burp intruder mass replay the request.

Thank you.

## Attachments
No attachments
