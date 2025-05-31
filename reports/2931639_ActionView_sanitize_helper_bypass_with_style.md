# ActionView sanitize helper bypass with style

## Report Details
- **Report ID**: 2931639
- **URL**: https://hackerone.com/reports/2931639
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-01-11T06:18:52.402Z
- **Disclosed**: 2025-02-06T01:34:06.252Z

## Reporter
- **Username**: mokusou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Rails-html-sanitizer, which Rails AtionView also uses, fails to sanitize input when the `style` tag is allowed, leading to XSS.
A vulnerable example would have been as follows;
```ruby
<%= sanitize @comment.body, tags: ["style"] %>
```

You could see other patterns/places where this is used in the security advisory.
View #2519936 for details.

## Impact

Sanitizer bypass that leads to XSS on applications built with it.
It also affects applications using Rails Action View's sanitize helper: https://api.rubyonrails.org/v7.2/classes/ActionView/Helpers/SanitizeHelper.html

## Attachments
No attachments
