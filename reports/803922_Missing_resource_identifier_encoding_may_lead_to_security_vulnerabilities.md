# Missing resource identifier encoding may lead to security vulnerabilities

## Report Details
- **Report ID**: 803922
- **URL**: https://hackerone.com/reports/803922
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-24T20:41:03.367Z
- **Disclosed**: 2020-05-13T18:18:36.253Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
(I initially submitted this to the GitHub repository because the ActiveResource repository is not listed in scope. I was redirected here by @rafaelfranca)

A number of methods in the ActiveResource library, such as `ActiveResource::Base#find` and `ActiveResource::Base#exists?` don't URL encode the resource identifier that is passed to them. Consider the following code:

```ruby
require 'activeresource'
 
 class Test < ActiveResource::Base
   self.site = 'http://127.0.0.1:8080'
end

Test.exists? '?a=1'
```

The code above is expected to make a request to `http://127.0.0.1:8080/tests/%3fa%3d1.json` by properly URL encoding the resource identifier. Instead, it makes a request to `http://127.0.0.1:8080/tests/?a=1.json`.

This was tested against ActiveResource 5.1.0 and 5.0.0, both have the same unexpected behavior.

## Impact

Because the index `/tests/` returns an array of objects, the code will throw an exception. However, due to the time difference that could be observed, an attacker could potentially exploit this by injecting a filter parameter to index endpoint of the resource. E.g.

| Resource identifier | Objects returned | RTT |
| ---- | ---- | ---- |
| `?type=a&` | 1 | 500ms |
| `?type=b&` | 0 | 100ms |

## Attachments
No attachments
