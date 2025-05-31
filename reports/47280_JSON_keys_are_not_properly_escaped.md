# JSON keys are not properly escaped

## Report Details
- **Report ID**: 47280
- **URL**: https://hackerone.com/reports/47280
- **State**: Closed
- **Severity**: high
- **Submitted**: 2015-02-10T01:00:04.032Z
- **Disclosed**: 2015-06-16T19:38:34.244Z

## Reporter
- **Username**: einstein_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Rails does not escape hash keys properly in `to_json` when generating json.

Values are escaped as expected
```ruby
irb(main):001:0> {"a"=>"<>"}.to_json
=> "{\"a\":\"\\u003c\\u003e\"}"
```

However keys are not:
```ruby
irb(main):002:0> {"<>"=>"a"}.to_json
=> "{\"<>\":\"a\"}"
```

This is because the `json` gem calls `.to_s` on the keys [here](https://github.com/flori/json/blob/259dee6c9bdda08ed0c1fc2e69bfbb2d377faba0/ext/json/ext/generator/generator.c#L738) which transforms the `EscapedString` back into a simple `String` so it doesn't go through the escaping process that values go through [here](https://github.com/EiNSTeiN-/rails/blob/3820788e4c2825dd77c779ba5b3bc29689e04e1d/activesupport/lib/active_support/json/encoding.rb#L54-L60).

**Security consideration**: this issue is a vector for XSS when an arbitrary value is used as a key and reflected in a javascript tag. Consider this piece of code:
```ruby
javascript_tag "var json=#{params.to_json}"
```
When params is something like `{"</script><script>alert(1)//"=>"xss"}` then `<>` are not escaped as they should and the javascript tag looks like this:
```html
<script>
//<![CDATA[
var json={"</script><script>alert(1)//":"xss"}
//]]>
</script>
```
The `</script>` inside the json object will terminate the opening script tag because it has precedence over everything else, and `alert(1)` is executed.

I believe this issue also applies to 4.2-stable and master.

Note that I opened a PR for a related issue in the json gem (https://github.com/flori/json/pull/235) which occurs when `ActiveSupport.escape_html_entities_in_json = false` because the forward slash is never escaped (neither in rails nor in the json gem). It might be worth fixing this in rails as well.

## Attachments
No attachments
