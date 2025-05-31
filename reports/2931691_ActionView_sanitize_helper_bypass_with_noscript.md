# ActionView sanitize helper bypass with noscript

## Report Details
- **Report ID**: 2931691
- **URL**: https://hackerone.com/reports/2931691
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-01-11T05:59:32.358Z
- **Disclosed**: 2025-02-06T01:35:47.138Z

## Reporter
- **Username**: taise
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Rails-html-sanitizer, which Rails AtionView also uses fails to sanitize input when `noscript` are allowed.
An example would be as follows;
```ruby
<%= sanitize '<noscript><p id="</noscript><script>alert(1)</script>"></noscript>' %>
```

You could see other patterns/places where this is used in the security advisory.
View [#250964](https://hackerone.com/reports/2509647) for details.

## Impact

Sanitizer bypass that leads to XSS on applications built with it.
It also affects applications using Rails Action View's sanitize helper: https://api.rubyonrails.org/v7.2/classes/ActionView/Helpers/SanitizeHelper.html

## Attachments
No attachments
