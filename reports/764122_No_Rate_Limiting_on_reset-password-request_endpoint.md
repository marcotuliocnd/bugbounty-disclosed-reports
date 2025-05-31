# No Rate Limiting on /reset-password-request/ endpoint

## Report Details
- **Report ID**: 764122
- **URL**: https://hackerone.com/reports/764122
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-24T16:42:55.748Z
- **Disclosed**: 2020-02-04T07:40:01.173Z

## Reporter
- **Username**: tess
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
Hi there !

I noticed when we hit the /reset-password-request/ endpoint too many times via some proxy for e.g:- (Burp) there is no rate limit on that endpoint and you can spam the email with 100's of requests and resend even more password reset emails to the users as there is no rate limiting on that.

I tried this on this /reset-password-request/ endpoint and like I said I was successful for sending ~100 and was even able to send like 100+ request to the user for password reset requests. 

If we send the following POST request:

POST /██████████
Host: my.stripo.email
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: ████████
Authorization: Bearer null
Content-Type: application/json;charset=UTF-8
Cache-Control: no-cache
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
X-XSRF-TOKEN: eyJpdiI6ImlLbHNFTXVhRFJYd1BjVHdcL1JDR1pBPT0iLCJ2YWx1ZSI6IjNkcXlcL3FBZ2FpdVdsR3hZUG0ya2NDczlWZW5ha0NNc1dzZE40UFFHeWJGckpKWVlvcjltTnp3SjYzVzFYZExaIiwibWFjIjoiNDIzOGQ0M2E2MTBlMGJhMTg2ODJkZDY1NDg2MjZmNjgxMzk5NzIyZDI3OGQwMWZkNjgwN2Y1MWMxYjQxODM3ZiJ9
Content-Length: 2
Cookie: G_AUTHUSER_H=2; _ga=GA1.2.1301643941.1577144541; _gid=GA1.2.2107470528.1577144541; amplitude_id_246810a6e954a53a140e3232aac8f1a9stripo.email=eyJkZXZpY2VJZCI6ImQwODk5ZThiLTAzNzgtNDFhOC1hZTI0LWI5NmFlMDFjOThhMFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU3NzIwMzkwNjg2MiwibGFzdEV2ZW50VGltZSI6MTU3NzIwMzkxMjEzOCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; _fbp=fb.1.1577144543206.1698377278; XSRF-TOKEN=eyJpdiI6ImlLbHNFTXVhRFJYd1BjVHdcL1JDR1pBPT0iLCJ2YWx1ZSI6IjNkcXlcL3FBZ2FpdVdsR3hZUG0ya2NDczlWZW5ha0NNc1dzZE40UFFHeWJGckpKWVlvcjltTnp3SjYzVzFYZExaIiwibWFjIjoiNDIzOGQ0M2E2MTBlMGJhMTg2ODJkZDY1NDg2MjZmNjgxMzk5NzIyZDI3OGQwMWZkNjgwN2Y1MWMxYjQxODM3ZiJ9; laravel_session=eyJpdiI6IndTU29CNTZwWFBYS1hcL3hEdVlRYVJRPT0iLCJ2YWx1ZSI6Ikc2K082dStNbEFZK0dGczUwMmlKUlhvd2h6MTlBTlpEcmI3dGdLeGdua3Q4S245ZG1ZQlhLNU9WWnNWOTkwd08iLCJtYWMiOiI5NGNiNDE2NTIwZDY1OTY3NTgwYzQ1ZTY4MjQ5MDcxNmE0YzNjNzdjZDk1Njc2MTBkYmE0YTgxNzk3YmZkZmI1In0%3D; __stripe_mid=31b5c136-ae4e-41ae-97d1-ab1481edd986; __stripe_sid=7f4481cf-48e0-4106-b1e2-191b5b19edac; G_ENABLED_IDPS=google; _gat_UA-96386569-1=1; intercom-id-b1m243ec=db681607-ad70-4dd9-99b1-adb9219366b6
Connection: close

{}

Thanks,
T E S S.

## Impact

No real Impact with just mass emailing someone a reset password link, but I thought it was worth reporting because there should be a rate limiting over here as it might exist in other areas.

## Attachments
No attachments
