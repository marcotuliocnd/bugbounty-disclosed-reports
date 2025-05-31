# A single user can subscribe a community multiple times

## Report Details
- **Report ID**: 362601
- **URL**: https://hackerone.com/reports/362601
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-06T02:16:48.591Z
- **Disclosed**: 2018-06-07T20:15:19.109Z

## Reporter
- **Username**: mkind
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
There is no proper validation while subscribing for a community. A user can subscribe a single community multiple times.

Steps to recreate:
Step 1: Open any community
Step 2: Click on subscribe button
Step 3: Capture the POST request and submit it multiple times
Step 4: Check the subscription count

POST Request:
--------------------------------
POST /for/nocommunity/subscribe HTTP/1.1
Host: liberapay.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://liberapay.com/for/nocommunity
Cookie: __cfduid=d5a7372c0620f73d866bac0869443206a1528250205; csrf_token=hmxFrGGb7FULfeeMuDIIamnotahacker; session="163767:1:VTi89XOnmnZWYLXMBlE8G_a_8gZCZAz5"
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 43

csrf_token=hmxFrGGb7FULfeeMuDIIamnotahacker

Response:
--------------------
HTTP/1.1 302 Found
Date: Wed, 06 Jun 2018 02:11:26 GMT
Connection: close
[TRUNCATED]

## Impact

Any user can increase his/her community subscriber's count to any number.

## Attachments
No attachments
