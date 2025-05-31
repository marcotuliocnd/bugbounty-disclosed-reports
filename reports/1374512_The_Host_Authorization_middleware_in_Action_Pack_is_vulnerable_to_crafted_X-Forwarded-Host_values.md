# The Host Authorization middleware in Action Pack is vulnerable to crafted X-Forwarded-Host values

## Report Details
- **Report ID**: 1374512
- **URL**: https://hackerone.com/reports/1374512
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-19T18:33:36.091Z
- **Disclosed**: 2021-11-18T21:03:04.941Z

## Reporter
- **Username**: mshtawythug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Title:         The Host Authorization middleware in Action Pack is vulnerable to crafted X-Forwarded-Host values
Scope:         https://github.com/rails/rails
Weakness:      Open Redirect
Severity:      Medium
Link:          https://hackerone.com/reports/1189310
Date:          2021-05-09 06:29:19 +0000
By:            @mshtawy
CVE IDs:       CVE-2021-22942, CVE-2021-22881

Details:
### Steps to reproduce
This is a follow up to  [CVE-2021-22881](https://github.com/advisories/GHSA-8877-prq4-9xfw) and  https://github.com/rails/rails/commit/83a6ac3fee8fd538ce7e0088913ff54f0f9bcb6f

with a controller like the following
```ruby
class TestsController < ApplicationController
  extend ActiveSupport::Concern

  def index
    redirect_to('/')
  end
end
```
when sending a request like the following where the URL has a mixed case characters 
``` bash
curl 'http://localhost:3000/tests' -H 'X-Forwarded-Host: Evil.com'
```
Or all capital case 
``` bash
curl 'http://localhost:3000/tests' -H 'X-Forwarded-Host: EVIL.COM'
```

### Expected behavior
```html
<div id="container">
  <h2>To allow requests to evil.com, add the following to your environment configuration:</h2>
  <pre>config.hosts &lt;&lt; "Evil.com"</pre>
</div>
```

### Actual behavior
```html
<html><body>You are being <a href="http://Evil.com/">redirected</a>.</body></html>% 
```

### System configuration
**Rails version**: 
Tested on Rails 6.1.3.1 and Rails 6.1.3.2
**Ruby version**:
N/A

### Notes

This was fixed in `main` in this PR https://github.com/rails/rails/pull/41435 but still affects <= 6.1.3.1 

The problem is in this code https://github.com/rails/rails/blob/6-1-stable/actionpack/lib/action_dispatch/middleware/host_authorization.rb#L115

``` ruby
origin_host = valid_host.match(
  request.get_header("HTTP_HOST").to_s.downcase)
forwarded_host = valid_host.match(
  request.x_forwarded_host.to_s.split(/,\s?/).last)
```

`forwarded_host` is missing a `downcase` after the `.to_s`, which results in `nil` assigned to `forwarded_host`, which then results in `true` in the following  code
```ruby
origin_host && @permissions.allows?(origin_host[:host]) && (forwarded_host.nil? || @permissions.allows?(forwarded_host[:host]))
```
because of the `nil?` check on the `forwarded_host`
```ruby
forwarded_host.nil? || @permissions.allows?(forwarded_host[:host])
```

The examples I gave are using `localhost`, but I also confirmed this using a production environment with a configuration like the following

```ruby
    Rails.application.config.hosts = %w(.EXAMPLE.com)
```

## Impact

Hackers can redirect victims to a malicious website.

Timeline:
2021-08-03 20:27:55 +0000: @tenderlove (bug triaged)


---

2021-09-07 20:30:35 +0000: @tenderlove (cve id added)


---

2021-10-05 20:37:19 +0000: @tenderlove (bug resolved)

## Impact

Hackers can redirect victims to a malicious website.

## Attachments
No attachments
