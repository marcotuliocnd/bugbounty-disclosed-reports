# Race Condition allows to get more free trials and get more than 100 languages and strings for free

## Report Details
- **Report ID**: 1087188
- **URL**: https://hackerone.com/reports/1087188
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-26T04:27:47.386Z
- **Disclosed**: 2021-02-25T18:04:46.457Z

## Reporter
- **Username**: b9cc1792602cc31402c20c9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi there,

As there is rate limit in the website, but it doesn't prevent users to take more than 1 trial which later leads to loss of the company, because by getting more trials I can get more strings and languages limit.

Steps to reproduce:

1) Create an account on https://hosted.weblate.org and setup burp suite with your browser.
2) Now, click on add project from the top + icon > select add a new translation project.
3) Turn on the intercept and click on Gratis trial for commercial hosting >  Start Trial
4) Capture the request and send it to Turbo intruder.
5) Add "Test: %s" header in the request and select race.py config.
6) Start attack, you will get 6 trials. As projects are free and unlimited but you can get more strings limit. In one trial you get 50,000 strings limit, but with 6 trials you get 50,000 x 6 strings limit and more than 100 languages.


Affected HTTP request:

POST /trial/ HTTP/1.1
Host: hosted.weblate.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hosted.weblate.org/
Content-Type: application/x-www-form-urlencoded
Content-Length: 84
Origin: https://hosted.weblate.org
Connection: close
Cookie: __cfduid=d584084fe0b125b922a38b58143580cde1610884176; django_language=en; sessionid=csxoox0ruxn11cayzveitj55vnrh9v20
Upgrade-Insecure-Requests: 1

csrfmiddlewaretoken=D74cp8jYYfF2xMBJ3TtawMKpI7T6OU27yuUYwra8QWOmMaryGdqTjWTzU1a15Q2z

## Impact

Get free trials and get more strings, languages limit.

Remediation: Set IP based rate limit and allow only 1 req for trial.

## Attachments
No attachments
