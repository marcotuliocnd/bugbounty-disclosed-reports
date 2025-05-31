# ActionView sanitize helper bypass with 'style' and 'svg' tags

## Report Details
- **Report ID**: 2931688
- **URL**: https://hackerone.com/reports/2931688
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-01-11T06:01:41.040Z
- **Disclosed**: 2025-02-06T01:36:33.075Z

## Reporter
- **Username**: taise
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Rails-html-sanitizer, which Rails AtionView also uses fails to sanitize input when `svg` and `style` OR `math` and `style` are allowed
An example would be as follows;

```ruby
<%= sanitize @comment.body, tags: ["math", "style"] %>
<%# or %>
<%= sanitize @comment.body, tags: ["svg", "style"] %>
```

You could see other patterns/places where this is used in the security advisory.
View [#2503220](https://hackerone.com/reports/2503220) for details.

## Impact

Sanitizer bypass that leads to XSS on applications built with it.
It also affects applications using Rails Action View's sanitize helper: https://api.rubyonrails.org/v7.2/classes/ActionView/Helpers/SanitizeHelper.html

## Attachments
No attachments
