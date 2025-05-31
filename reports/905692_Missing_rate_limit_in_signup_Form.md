# Missing rate limit in signup Form 

## Report Details
- **Report ID**: 905692
- **URL**: https://hackerone.com/reports/905692
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-22T21:34:47.895Z
- **Disclosed**: 2020-07-28T22:51:46.926Z

## Reporter
- **Username**: ahmedelmalky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trycourier

## Vulnerability Information
Hello Team ,
##Description 
When signing up for an account, you enter your email. When this email is already in use, the server
 responds with 
``
{"UserConfirmed":true,"UserSub":"ae294fff-6d55-407d-9676-1f3518029037"}
``
This in not a problem, but the fact that you could send this request unlimited times is the issue.

This way we can easily get a list of all users emails signed up at" trycourier App" .
 
Vulnerable Endpoint :https://www.trycourier.app/register/email

POC : Watch The Video Please .

Link OF POC in Video : https://drive.google.com/file/d/1aA6MHjLx5u29RhzqOZzlNqKYuOPbwBrE/view?usp=sharing

Now i have 200 responses with status 200 .

that 's mean that i have created 200 new account

when the request repeat with same email it response with 500 
``
{"__type":"UsernameExistsException","message":"An account with the given email already exists."}
``
that mean it just in the Bucket  [recorded in DB ].

##Fix

to fix this issue, you could implement an timeout after a number of requests in a period of time.

to return "429 Too Many Requests" when making multiple requests in a short period of time

or use capatcha .

## Impact

the attacker can make for example 1 M request that lead to fill your DB with fake accounts .

report From H1 : https://hackerone.com/reports/275186

## Attachments
- Screenshot_from_2020-06-22_23-30-44.png
