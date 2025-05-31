# Net::SMTP with tls allows forged certificates as long as the hostname matches

## Report Details
- **Report ID**: 980249
- **URL**: https://hackerone.com/reports/980249
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-11T18:05:31.353Z
- **Disclosed**: 2021-01-25T01:48:01.803Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
I'd like to report a very odd behavior I observed in the
Net::SMTP
module, part of Ruby's standard library.

It seems when performing a TLS connection the code checks the certificate hostname, but not the certificate signature or issuer. This of course makes little sense, as an attacker can create a self-signed (or signed by whatever fake CA) certificate with a matching hostname.

To test:

* Create a test certificate for a random test hostname (e.g. smtp.example):
```
openssl req -new -newkey rsa:2048 -days 9999 -nodes -x509 -keyout server.key -out server.crt -batch -subj '/CN=smtp.example/'
```
* Run a TLS server with that certificate. the error we're looking after happens before any SMTP activity, so it doesn't really matter if it's a "real" SMTP server, we can use an openssl test server for this:
```
openssl s_server -accept 465 -cert smtp.pem -key smtp.pem
```
* Now redirect smtp.example and another hostname (let's use smtp2.example) to localhost via /etc/hosts:
```
127.0.0.1	smtp.example
127.0.0.1	smtp2.example
```
* Now try to connect to it with Net::SMTP and tls enabled:
```
require 'net/smtp'
smtp = Net::SMTP.new("smtp.example", 465)
smtp.enable_tls
smtp.start
```

This will succeed (and then hang as the server does not answer to the SMTP commands).

Try the same with smtp2.example, it will complain like this:
```
/usr/lib64/ruby/2.7.0/openssl/ssl.rb:395:in `post_connection_check':
hostname "smtp2.example" does not match the server certificate (OpenSSL::SSL::SSLError)
```
I also tested this with starttls, the behavior is the same.

The documentation of Net::SMTP does not say anything about certificate validation. Though I think it's a reasonable assumption that if I use tls that it is secure by default.

There may be some arguing about this, as Net::SMTP can both be used for authenticated SMTP / submission SMTP and for unauthenticated SMTP, which is usually used for relaying. In the latter case certificates are usually not tested. Thus there should probably a parameter to disable certificate validation.

In any case: I think the current behavior is clearly a bug and a security risk.

## Impact

Man in the middle attacker can intercept TLS SMTP connections with a forged certificate.

## Attachments
No attachments
