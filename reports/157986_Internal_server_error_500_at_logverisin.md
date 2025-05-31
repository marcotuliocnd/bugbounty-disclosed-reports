# Internal server error 500 at log.veris.in 

## Report Details
- **Report ID**: 157986
- **URL**: https://hackerone.com/reports/157986
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T21:38:39.474Z
- **Disclosed**: 2016-08-13T06:39:00.222Z

## Reporter
- **Username**: ak1t4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: veris

## Vulnerability Information
INTRO:

i have discovered an internal server error (500) at log.veris.in in sentry app & possible DoS  injection with data garbage

EXPLOITABILITY:

Steps:

1)After Sending this request Sentry is crash with an internal server error showing version of sentry and the capability of sending the issue with a form:

https://log.veris.in/_static/31633a13250d151db904018a5b4bfc4d9954a727/sentry/dist

2) The issue form permit send multiple reports without any validation and 200 code reply like this request:

--

POST /api/embed/error-page/?eventId=40df85725d9745f4b01148e7deab5858&dsn=https%3A%2F%2Feb32d006141e48a8a439a2fe7fe50b43%40log.veris.in%2F1 HTTP/1.1
Host: log.veris.in
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Referer: https://log.veris.in/_static/31633a13250d151db904018a5b4bfc4d9954a727/sentry/dist
Content-Length: 48
Cookie: _ga=GA1.2.102943685.1470375862; __utma=82828177.102943685.1470375862.1470375862.1470447007.2; __utmz=82828177.1470375862.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); sentrysid="gAJ9cQEoWAoAAAB0ZXN0Y29va2llWAYAAAB3b3JrZWRxAlUFX25leHRYGQAAAC9hcGkvZW1iZWQvZXJyb3ItcGFnZS9pbi91Lg:1bWbwu:4ElVwbfFwj-m5qT7IQA5bqTFDNk"; csrf=QtgwRAMxUpMON9GE4JWHuSRyONQBsIqs
Connection: close

name=test&email=test%40email.com&comments=test&=

----

and response:

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 09 Aug 2016 21:34:33 GMT
Content-Type: application/json
Content-Length: 0
Connection: close
Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With
Content-Language: es
Access-Control-Max-Age: 1000
Vary: Accept-Language, Cookie
Access-Control-Allow-Origin: 
Access-Control-Allow-Methods: GET, POST, OPTIONS
Strict-Transport-Security: max-age=31536000

--


3) The POST method  can change it for DELETE method, and the server responses with source code of sentry page form (see screenshots)



IMPACT:

*An attacker can use this information for information gathering  and possible exploit of sentry app
*An attacker can use the post form (without user validation or captcha or limit report) and send  multiple reports with garbage data for possible DoS in server resources  (cpu, me, disk, etc)


FIX:

Change permissions over sentry app log report and  close for unauthorized access

Let me know if more info needed

Best Regards


@ak1t4










## Attachments
- Captura_de_pantalla_2016-08-09_a_las_18.15.29.png
- Captura_de_pantalla_2016-08-08_a_las_1.44.40.png
- Captura_de_pantalla_2016-08-08_a_las_1.44.26.png
- Captura_de_pantalla_2016-08-08_a_las_0.37.41.png
- Captura_de_pantalla_2016-08-09_a_las_18.19.51.png
- Captura_de_pantalla_2016-08-09_a_las_18.19.45.png
