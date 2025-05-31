# No Rate Limit On  Contact Us 

## Report Details
- **Report ID**: 1166069
- **URL**: https://hackerone.com/reports/1166069
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-04-15T22:37:37.193Z
- **Disclosed**: 2021-08-27T17:23:35.014Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
hello dear suuport 

i have found issue on https://app.upchieve.org

step

1 goto here https://app.upchieve.org
2 login into your account
3 goto here https://app.upchieve.org/contact (contact)
4 type Message and open burp
HTTP request 
===========
POST /api-public/contact/send HTTP/2
Host: app.upchieve.org
Cookie: __cfduid=d5286a2604ae20eb69c722f6666fe12c91618525779; connect.sid=s%3AJKSnG-mkXobDr_u1f2tfXEx0L6B9n7P5.Ovg6QT8%2BSt2xdbZDsJ94dryZYpCQcH9tSiythb36a7U; ph_JRMZGA_RF-346IQfReUvbuoVD3Q94BM7Jij8Nk4dQbA_posthog=%7B%22distinct_id%22%3A%226078bbee3e0d0e00246b7eec%22%2C%22%24device_id%22%3A%22178d7912801885-019acf5c037b948-4c3f237d-1fa400-178d791280280f%22%2C%22%24sesid%22%3A%5B1618525988362%2C%22178d7a7d32f75-065efd10c2d0dc8-4c3f237d-1fa400-178d7a7d331fa0%22%5D%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22%24referrer%22%3A%22%24direct%22%2C%22%24referring_domain%22%3A%22%24direct%22%2C%22%24user_id%22%3A%226078bbee3e0d0e00246b7eec%22%2C%22%24active_feature_flags%22%3A%5B%5D%7D
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=§0.5§
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
X-Requested-With: XMLHttpRequest
Content-Length: 86
Origin: https://app.upchieve.org
Referer: https://app.upchieve.org/contact
Te: trailers
Connection: close

{"responseData":{"email":"dolfomo5284@zevars.com","topic":"Feedback","message":"ffff"}}

add Accept-Language: en-US,en;q=§0.5§ to NULL payload 
(F1267176)
Done

## Impact

No Rate Limit On  Contact Us

## Attachments
- 455.PNG
