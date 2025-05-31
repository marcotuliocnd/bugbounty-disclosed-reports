# Bypass of #1047119: Missing Rate Limit while creating Plug-Ins at https://my.stripo.email/cabinet/plugins/

## Report Details
- **Report ID**: 1076047
- **URL**: https://hackerone.com/reports/1076047
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-11T11:21:24.147Z
- **Disclosed**: 2021-01-13T15:47:33.414Z

## Reporter
- **Username**: savxiety
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
 I have found a bypass for the report https://hackerone.com/reports/1047119
It seems that a proper fix was not issued therefore the issue still remains.

## Steps To Reproduce:

  1. Create a Plug-In and capture the request.
  1. Send this to Intruder
  1. Follow the rest in the Video POC.


## POC
**Video POC**
In this section, I have shown clear and concise steps to reproduce the vulnerability.
{F1152962}
From the above video POC, as you could see, I was able to send 100 requests to create plug-ins at a very fast speed occupying disk space and costing the company.
**Request To Send**

```python
POST /cabinet/stripeapi/v1/plugin/357981/plugins HTTP/1.1
Host: my.stripo.email
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=UTF-8
Cache-Control: no-cache
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
X-XSRF-TOKEN: 867d2a4a-9d3f-407e-9527-83cf47c3d8cc
Content-Length: 108
Origin: https://my.stripo.email
Connection: close
Referer: https://my.stripo.email/cabinet/
Cookie: _ga=GA1.2.820184997.1610358469; _gid=GA1.2.285492738.1610361098; _pin_unauth=dWlkPVptSmlOR1EyTWpjdFlURmpNUzAwWmpCakxXRXlOR0V0TWpWbVltSm1NVGcwWW1ZeQ; amplitude_id_246810a6e954a53a140e3232aac8f1a9stripo.email=eyJkZXZpY2VJZCI6ImJmOGY2ZTlmLWZlOWMtNDY2Mi1hOTg3LTI2NWFmNGYyZGQ1YVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYxMDM2MTExMDM2NCwibGFzdEV2ZW50VGltZSI6MTYxMDM2MTEyMTAxOSwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; _fbp=fb.1.1610361110716.1635574013; _pin_unauth=dWlkPVptSmlOR1EyTWpjdFlURmpNUzAwWmpCakxXRXlOR0V0TWpWbVltSm1NVGcwWW1ZeQ; G_ENABLED_IDPS=google; __stripe_mid=d3200dd8-4e6b-45be-9da3-54783b95e87c96fb16; __stripe_sid=2d31cbbe-d4e2-4904-bc96-28f4fa8313c8ff08c1; token=eyJhbGciOiJSUzUxMiJ9.eyJhdXRoX3Rva2VuIjoie1widXNlckluZm9cIjp7XCJpZFwiOjM1ODI3OSxcImVtYWlsXCI6XCJzYXZpcnN1ZGFAZ21haWwuY29tXCIsXCJsb2NhbGVLZXlcIjpcImVuXCIsXCJmaXJzdE5hbWVcIjpcInNhdmlyXCIsXCJsYXN0TmFtZVwiOm51bGwsXCJmYWNlYm9va0lkXCI6bnVsbCxcIm5hbWVcIjpudWxsLFwicGhvbmVzXCI6W10sXCJhY3RpdmVcIjp0cnVlLFwiZ3VpZFwiOm51bGwsXCJhY3RpdmVQcm9qZWN0SWRcIjozNjMzMTgsXCJzdXBlclVzZXJWMlwiOmZhbHNlLFwiZ2FJZFwiOlwiZTk3NDJlNDAtNDhkYy00ZTE3LWFlNzItMWExY2M4ZmQ1Y2QyXCIsXCJvcmdhbml6YXRpb25JZFwiOjM1Nzk4MSxcIm93bmVkUHJvamVjdHNcIjpbMzYzMzE4XSxcImZ1bGxOYW1lXCI6XCJzYXZpciBudWxsXCJ9LFwiaXNzdWVkQXRcIjoxNjEwMzYxMTQwNzU1LFwiYXBpS2V5XCI6bnVsbCxcInByb2plY3RJZFwiOm51bGwsXCJ4c3JmVG9rZW5cIjpcIjg2N2QyYTRhLTlkM2YtNDA3ZS05NTI3LTgzY2Y0N2MzZDhjY1wiLFwicm9sZVwiOlwiQ0FCSU5FVF9VU0VSXCIsXCJhdXRob3JpdGllc1wiOltdfSIsImV4cCI6MTYxMDQ0NzU0MH0.Uf9QUHgo9TYJte2-hFDDFDcW80OVpmHXZMUf2thntSYYthCA07Fu94XVs7RFRiZMOTnjqyLhJK3p7CwAf61xNAD8WbTtoAlIcia82nNYQ4ueIItzExfQJWQHXD8GSIBRBp-VCbXBOJaXt5KQntnPCCwzvpmrE_LTKwX9MkxkmKkLmU3oCxxfpd8MKo3s-bTvNJsnT91_K3eJwdMGl78KjI3Jnk5JQe3fj4NFHk7P-snsGInO8jlY9ikY6ndInrEZ23WLfNu1Qh86DC2aLVdaTnSJg6F_w5jtFxIKpdtoRTDEpSJbEdyu3UMoOJZl8MPtx8WaMMJA-iuyqD2BUGGL89ULjkCCVb2BSCHx5HzAO8pWPvFUZNRami5sLvuBbfjr_sNKYTVXb9XY_Z4cuPNQ1AGjAMeotmsn0qlv41u-BWQnLjRV7YGVhP3SeboK79MnG0YCRCwmytt8UBqbcA8VEGOKmWxGMbIAYYC7OKApOHwtr419UtGvva261ObGfXlKsENyap0PrszXRPYpB_Oi9U_AR9ZrB100QrNNVJywsTTaD7Mi6q0B22958NnmHvn5QzjYiZmULxngLyM7s2pAMxGDQ8OOFE6JV7bpsFrOCRpLdNsK3EENNc5jsRAxUsYWUjZAHzgueW789g9QGmjq-wFL77dlR_aUNrCVbhh87pc; _ga=GA1.3.820184997.1610358469; _gid=GA1.3.285492738.1610361098; JSESSIONID=5269D92EB21DAB4CF3F411313361E107; intercom-session-b1m243ec=OXJKNnkvYnA4aUhMUE9TakVEVlBzT3BKS3JVYW0vNEZJQlR0ZCtIdVU2K3NHa29QcGswb2RtQmFyUDBYdWlQZS0tRmJFalMwdkI2VUJnZHpHZUFRdUkzZz09--295709016df61f9c47f9ff869f4f1b26a8169ae2

{"email":"<YOUR-EMAIL>","name":"test","webUrl":"pxqx0kafueopargwjcp9bmtiv91zpo.burpcollaborator.net"}
```

##Description
I also noticed that If I choose 100 threads instead of 50, after a few requests with `200 OK` responses, I got a `503 Service Temporarily Unavailable`. You may want to investigate this as well. I also wanted to add that after about 20-30 seconds, I was able to send the same amount of requests again which would charge the application by creating Plug-Ins massively.


## Supporting Material/References:
{F1152961}

## Impact

- Bypass of #1047119
- An attacker can create a lot of Plug-Ins which would occupy memory and charge the application.

## Mitigation
As a hacker who is on the good side, I wanted to suggest some mitigations which would help protect against this issue and would prevent any further bypasses :)

- Add a Google Recaptcha Verification here when a user requests to create more than 1 plugin in a small period of time.
- Allow only 10 Plug-Ins per day, per user. 
- Add Rate limiting

~Thanks :)
@savxiety

## Attachments
No attachments
