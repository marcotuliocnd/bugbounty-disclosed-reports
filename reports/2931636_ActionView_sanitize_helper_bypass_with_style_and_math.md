#  ActionView sanitize helper bypass with style and math

## Report Details
- **Report ID**: 2931636
- **URL**: https://hackerone.com/reports/2931636
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-01-11T06:18:45.459Z
- **Disclosed**: 2025-02-06T01:33:59.140Z

## Reporter
- **Username**: mokusou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Rails-html-sanitizer, which Rails AtionView also uses fails to sanitize input when `math` and `style` are allowed
An example would be as follows;
```ruby
<%= sanitize @comment.body, tags: ["math", "style"] %>
```

You could see other patterns/places where this is used in the security advisory.

View #2519941 for details.

## Impact

Sanitizer bypass that leads to XSS on applications built with it.
It also affects applications using Rails Action View's sanitize helper: https://api.rubyonrails.org/v7.2/classes/ActionView/Helpers/SanitizeHelper.html

## Attachments
No attachments
