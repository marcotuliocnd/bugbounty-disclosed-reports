# Weak rate limit could lead to ATO due to weak password protection mechanisms

## Report Details
- **Report ID**: 1065186
- **URL**: https://hackerone.com/reports/1065186
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-12-23T15:17:00.612Z
- **Disclosed**: 2021-12-15T18:40:41.587Z

## Reporter
- **Username**: bombon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Although the server sends a message when attempting to brute force the login endpoint, if you enter the right credentials the server will ignore that error and will give access to the account.
 **When the server sends this error, it should not give access until the 3400+ seconds ends**
Additionally, when you create an account the minimum password length is just 5 characters with no especial characters
```http
HTTP/1.1 200 OK
Date: Wed, 23 Dec 2020 14:40:53 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Set-Cookie: __cfduid=d191afcbe4c1251f6b30748328b1fb38e1608734453; expires=Fri, 22-Jan-21 14:40:53 GMT; path=/; domain=.dubsmash.com; HttpOnly; SameSite=Lax; Secure
X-Powered-By: Express
Access-Control-Allow-Origin: *
Cf-Ipcountry: US
Etag: W/"1c6-rSeAGxcTYF4pPpzI2dToH9KSAN0"
Via: 1.1 vegur
CF-Cache-Status: DYNAMIC
cf-request-id: 0731a4c556000003dc4b098000000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Strict-Transport-Security: max-age=0; includeSubDomains
X-Content-Type-Options: nosniff
Server: cloudflare
CF-RAY: 6062d71bbfa503dc-ORD
Content-Length: 454

{"errors":[{"serviceError":{"status_code":429,"message":"Request was throttled. Expected available in 3414 seconds.","error_code":1},"message":"Request was throttled. Expected available in 3414 seconds.","locations":[{"line":2,"column":3}],"path":["loginUser"],"extensions":{"code":"INTERNAL_SERVER_ERROR","exception":{"status_code":429,"message":"Request was throttled. Expected available in 3414 seconds.","error_code":1}}}],"data":{"loginUser":null}}
```
## Impact:
This can lead to account takeover since the password limit to create an account is `5 `and  it doesn't need any especial characters, which can be chained to fully compromised an user, and easier for an attacker to perform a bruteforcing attack

## Steps To Reproduce:

1 -> Go to the login page at `https://dubsmash.com/login?redirect=/` supply any wrong credentials and send that request to burp using burp repeater.

It should look like this.
```http
POST /graphql HTTP/1.1
Host: gateway-production.dubsmash.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://dubsmash.com/login?redirect=/
content-type: application/json
X-Dubsmash-Device-Id: 00a0ee27-a0e3-4701-9e25-5985f1d95c60
X-Accept-Content-Language: en_US
Origin: https://dubsmash.com
Content-Length: 622
DNT: 1
Connection: close

{"operationName":"LogInUserMutation","variables":{"username":"wrongcredentials@gmail.com","password":"password","client_id":"o80K4ofRjCcqdvIxaUVefAPCcnZAyJv4","client_secret":"mYrjmUEG47w2Wk6Kwe8wax1vAdiwUxEi"},"query":"mutation LogInUserMutation($username: String!, $password: String!, $client_id: String!, $client_secret: String!) {\n  loginUser(input: {username: $username, password: $password, grant_type: PASSWORD, client_id: $client_id, client_secret: $client_secret}) {\n    user {\n      uuid\n      username\n      __typename\n    }\n    access_token\n    refresh_token\n    token_type\n    __typename\n  }\n}\n"}
```

2   -> Send that same request multiple times until you get an error saying `Request was throttled. Expected available in 3000+ seconds`

3   ->Supply my credentials `username: ███████ password:████████`

You should be able to access my account even though the server said request were 'throttled'

## Impact

This could lead to account takeover since the password limit to create an account is `5 `and  it doesn't need any especial characters, which can be chained to fully compromised an user, and easier for an attacker to perform a bruteforcing attack.

## Attachments
No attachments
