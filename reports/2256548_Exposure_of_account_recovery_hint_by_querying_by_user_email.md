# Exposure of account recovery hint by querying by user email

## Report Details
- **Report ID**: 2256548
- **URL**: https://hackerone.com/reports/2256548
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-11-18T08:59:40.844Z
- **Disclosed**: 2024-01-11T08:20:53.720Z

## Reporter
- **Username**: francisconeves97
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
Hey all!

Hope everything is good! While testing I noticed that I can issue queries to https://api.accounts.firefox.com/v1/recoveryKey/hint?email=email-to@attack.com to get a specific user Account Recovery Keys hint.

This does not seem like an issue on itself but could be used to escalate phishing attacks for example.

The page where you input the hint displays the following:
{F2866742}

But I am considering this should not be public information, and only be available to a user by a email link.

## Steps To Reproduce:
Go to https://api.accounts.firefox.com/v1/recoveryKey/hint?email=███████ and check my hint.

```
GET /v1/recoveryKey/hint?email=███ HTTP/2
Host: api.accounts.firefox.com
Sec-Ch-Ua: "Chromium";v="119", "Not?A_Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9
Priority: u=0, i
```

## Impact

Leaking any user's Account Recovery Keys hint can be used to steal user's keys or craft more complex phishing attacks.

## Attachments
- image.png
