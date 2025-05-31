# Two-factor authentication bypass on Grab Android App

## Report Details
- **Report ID**: 202425
- **URL**: https://hackerone.com/reports/202425
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-31T18:45:16.840Z
- **Disclosed**: 2017-09-12T19:19:02.464Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
## Description
I found the endpoint using android app `https://p.grabtaxi.com/api/passenger/v2/profiles/edit` which allow me to bypass 2FA (sms code) due to lack of rate limiting\code expiration after unsuccessful attempts.
The root cause of the problem it that facts: no rate limiting+ no code expiration. Since code has 4 digits, attacker just need to count all possible combinations from 1000 to 9999.
What happens if we do the wrong request to `https://p.grabtaxi.com/api/passenger/v2/profiles/edit` endpoint? Let's take a look:

```
PUT /api/passenger/v2/profiles/edit HTTP/1.1
Content-Type: application/x-www-form-urlencoded
x-mts-ssid: [current session id, its too long so i removed it for report space economy]
x-request-id: 3b609418-0e40-4f86-8ff6-4f23dfac420f
Host: p.grabtaxi.com
Content-Length: 26
Accept-Encoding: gzip
Connection: Keep-Alive

profileActivationCode=3122
```

Response (bad request):

```
HTTP/1.1 400 Bad Request
Content-Encoding: gzip
Content-Type: application/json; charset=utf-8
Date: Tue, 31 Jan 2017 17:45:43 GMT
X-Api-Source: grabapi
X-Request-Id: 01800ddb-fb58-4b53-aecc-97473225f732
Content-Length: 47
Connection: keep-alive

{"status":400,"code":4000}
```
And what when code will be correct?
Response (correct request):

```
HTTP/1.1 204 No Content
Content-Type: application/json; charset=utf-8
Date: Tue, 31 Jan 2017 17:45:43 GMT
X-Api-Source: grabapi
X-Request-Id: 9d0eae1a-9c16-4aa5-8b40-01105a7cb994
Connection: keep-alive
```
I looked to it, and wrote a simple C# tool which sends all possible codes combinations, until it finds a correct code. Source code and POC tool included to the report (it requires at least Windows 7 and NET 4.0 to run).

## Impact
The attacker can bypass 2FA authentication on Grab android app. Attacker can succeed in the account takeover, changing email, phone number of the victim who use Google Auth on the app etc.

## Steps To Reproduce:
1. Login to your Grab Android app using Google with valid phone number (2FA on the phone login option is correctly implemented, and not vulnerable).
2. Edit your profile name and press Save.
3. The 4-digit sms code will be send to your phone. Dont look to it now:)
4.  Use my POC tool (written on C#, requires .NET 4.0). You need a one header from the any app web request (`x-mts-ssid`) for proper testing. You can extract it from the any request from Android app, using some Web Proxy.
If you have troubles with extracting x-mts-ssid session header from the web request - let me know. It can be tricky thing (i used android emulator, connected to Charles Web Proxy, for request monitoring).
Open the program, paste the x-mts-ssid in the text field and press "Start". Wait till process will ends (correct code will be found).
5. Compare code from the tool, and code that you received on the phone earlier - they must be equal. Also i wrote a POC video (https://drive.google.com/file/d/0B8dmpoHKDZsZSFI5WXY2RzRYT00/view?usp=sharing).

## Mitigation/Remediation Steps:
I suggest you implement a rate-limiting on this endpoint, or force 2FA code expiring after, for example, 5 wrong attempts (or both of this for better security).




## Attachments
- tool.zip
