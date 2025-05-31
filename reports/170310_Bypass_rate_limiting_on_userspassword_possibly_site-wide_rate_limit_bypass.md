# Bypass rate limiting on /users/password (possibly site-wide rate limit bypass?)

## Report Details
- **Report ID**: 170310
- **URL**: https://hackerone.com/reports/170310
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-09-19T02:04:54.448Z
- **Disclosed**: 2016-12-08T12:22:29.212Z

## Reporter
- **Username**: zseano
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi there,

I noticed when we hit the /users_sign_in endpoint too many times it will give us 

`````
HTTP/1.1 429 Too Many Requests
Date: Mon, 19 Sep 2016 01:52:19 GMT
Content-Type: text/plain
`````

However, this can be "reset" although I struggle to get it to work EVERYTIME on /users/sign_in. This however, does work all the time on /users/password endpoint hence why i'm reporting so maybe you can investigate further on the /users_sign_in endpoint.

If we send the following POST:

`````
POST /users/password HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 206
Cache-Control: max-age=0
Origin: https://hackerone.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
DNT: 1
Referer: https://hackerone.com/users/password/new
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6
Cookie: cookies_here

authenticity_token=your_token_here&utf8=%E2%9C%93&user%5Bemail%5D=email@here.com&commit=Send
`````

Now send the request around ~10 times and it'll hit "Too Many Requests". Now simply add %00 on the end of the email and resend even more password reset emails. 

&user%5Bemail%5D=email@here.com%00 - and keep adding %00 everytime you are rate limited. After a while you can go back to just %00 as it resets after so long.

I tried this on the /users/sign_in endpoint like I said and was successful for about ~50 login attempts before it just died and kept giving me a Precondition error each time (I wonder if I need to change auth_token every few requests?). I'm going to keep investigating in the morning.

No real impact with just mass emailing someone a reset password link, but I thought it was worth reporting because the rate limiting bypass might exist in other areas (with the use of the null byte %00)

{F121260}

## Attachments
- ss_(2016-09-19_at_03.02.28).png
