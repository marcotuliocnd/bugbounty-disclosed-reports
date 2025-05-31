# Requesting Mediation possible on reports that are too old for mediation

## Report Details
- **Report ID**: 159512
- **URL**: https://hackerone.com/reports/159512
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-15T17:27:10.806Z
- **Disclosed**: 2016-08-17T22:07:09.794Z

## Reporter
- **Username**: troubleshooter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Hackerone Team,

it is possible to request mediation for reports, that have the closedTooLongToMediate-parameter set to true,
by requesting a mediation for a new report and changing the report id to the old report.

PoC report: https://hackerone.com/reports/77834

My Request looks like:
````
POST /reports/OLD_REPORT_ID/hacker_help HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: */*
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate, br
DNT: 1
X-CSRF-Token: VALID_TOKEN
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com/bugs?subject=user&report_id=*******&view=open&substates%5B%5D=new&substates%5B%5D=needs-more-info&substates%5B%5D=triaged&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1
Content-Length: 163
Cookie: __cfduid=d2bffe76709824599079c764e028a8bad1471178340; __Host-session=bzVwRnZmR1QzSXBOanNya2FXeUxxQW1CQ3R6SHgwMHZXY24rVVJGbWVzcW1OR1pTcFJPRVNMcFBTcDlBa3lOaHRyYmNXbUR6VkN3czE0d1NxNHh4R0RIWUl4NFNOdnBYU1czdm1WR2liZFlLTVZGU0dJN2l0YzU2b3NOVk8zNkVzQmZDVzIyM3lxa3Y3Si9PQ2xjLzJWTG14NlV5UjB3Q0RNdkVOUVRiVG5pa1ZaRktNQi91US82cDhlZGF1Zno5bjZReVpNL0k5bkRyRVliTFowVWtac1Jwa21pdXgzYnl3RkZ0QkRCV2p5Z3hVbHVCUHEvN3VSMUd0QXUrQ2gxS1JzTWpXdEZVYWc3a2s3cC94YkFkeHR4NUpENW9wY0ZNME42N1VBMVBNMHdKQTRRSUt2VitrZ2gveEhOWE9sMU0xWHBGeEl1eGdXM2JmZDNXK0w3M3RwK2dTWFF3VC9TcGZtM1h3cGpGVXhIb2dNWlY3bFlCNGF2Zm9UZ01RcXhpTjJpNXlKMXdJbVM3MkxmVnJTSm93M0Q0Y2F3eXBQVjdaTE1oRHdxeUdoOXA0dk5uT21UMHBNT0NVMWp2VHFXdS0tMFg0aU9SekM2QWZ6MGs4U3dieDhGUT09--334ef06ec1ac7a1d1eee09dac2ac25e9a7553856
Connection: close

message=Example+Message&mediation_type=resolution



## Attachments
No attachments
