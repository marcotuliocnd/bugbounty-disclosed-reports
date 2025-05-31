# Unexpected deserialization in Kredis

## Report Details
- **Report ID**: 1702859
- **URL**: https://hackerone.com/reports/1702859
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-17T07:55:51.251Z
- **Disclosed**: 2023-08-16T04:50:31.204Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Unexpected classes may be deserialized because `JSON.load` is used to cast json in [Kredis](https://github.com/rails/kredis).

https://github.com/rails/kredis/blob/v1.3.0/lib/kredis/type/json.rb

```ruby
module Kredis
  module Type
    class Json < ActiveModel::Type::Value
      def type
        :json
      end

      def cast_value(value)
        JSON.load(value)
      end
```      

### PoC

prepare kredis with rails

```
❯ rails new rails_server -G -M -O -C -A -J -T
# Rails 7.0.4 install

❯ cd rails_server

# Edit Gemfile to uncomment `gem "kredis"` 
❯ bundle install
# kredis 1.3.0 install

❯ rails kredis:install
```

```ruby
❯ bundle exec rails c
Loading development environment (Rails 7.0.4)
irb(main):001:0> abc = 'abc'.to_json_raw_object
=> {"json_class"=>"String", "raw"=>[97, 98, 99]}

irb(main):002:0> json = Kredis.json "json_load"
=>
#<Kredis::Types::Scalar:0x00000001099ea250
...

irb(main):003:0> json.value = abc
=> {"json_class"=>"String", "raw"=>[97, 98, 99]}

irb(main):004:0> json.value
=> "abc"
```

The return value of `json.value` should be a hash object, but it is deserialized as a string object.

```ruby
irb(main):005:0> json.value = /test/
=> /test/

irb(main):006:0> json.value
=> "(?-mix:test)"

irb(main):007:0> json.value = /test/.as_json
=> "(?-mix:test)"

irb(main):008:0> json.value
=> "(?-mix:test)"

irb(main):009:0> require 'json/add/core'
=> true

irb(main):010:0> json.value = /test/.as_json
=> {"json_class"=>"Regexp", "o"=>0, "s"=>"test"}

irb(main):011:0> json.value
=> /test/
```

If [json/add/core](https://github.com/flori/json/tree/master/lib/json/add)  is loaded, classes such as regular expressions can also be deserialized.

## Impact

If a hash is passed to `Kredis.json` by user input, reading the value may cause unexpected problems.

The only deserializable classes are those with `self.json_create` declared, usually String class are possible.(https://github.com/flori/json/blob/v2.6.2/lib/json/pure/generator.rb#L434)


If `json/add/core` is loaded, it is possible to deserialize RegExp, etc., thus risking ReDoS, etc.

## Attachments
No attachments
