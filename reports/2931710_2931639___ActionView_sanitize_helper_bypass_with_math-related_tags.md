# #2931639   ActionView sanitize helper bypass with math-related tags

## Report Details
- **Report ID**: 2931710
- **URL**: https://hackerone.com/reports/2931710
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-01-11T06:22:55.473Z
- **Disclosed**: 2025-02-06T01:33:39.962Z

## Reporter
- **Username**: mokusou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Rails-html-sanitizer, which Rails AtionView also uses, fails to sanitize input when the style tag is allowed, leading to XSS.
A vulnerable example would have been as follows;

```ruby
<%= sanitize @comment.body, tags: ["math", "mtext", "table", "style", "mglyph"] %>
<%# or %>
<%= sanitize @comment.body, tags: ["math", "mtext", "table", "style", "malignmark"] %>
```

You could see other patterns/places where this is used in the security advisory.
View #2519936 for details.

## Impact

Sanitizer bypass that leads to XSS on applications built with it.
It also affects applications using Rails Action View's sanitize helper: https://api.rubyonrails.org/v7.2/classes/ActionView/Helpers/SanitizeHelper.html

## Attachments
No attachments
