# CSS injection via BB code tag "█████"

## Report Details
- **Report ID**: 587727
- **URL**: https://hackerone.com/reports/587727
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-22T10:48:40.010Z
- **Disclosed**: 2019-09-26T14:57:09.048Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phpbb

## Vulnerability Information
The input to the "█████" BBcode tag is not properly filtered. It gets converted into a CSS style attribute for a span HTML element.

Quotes (") are removed, so there's no way to break out of the CSS style attributed. However it is possible to arbitrarily dress the resulting span element.

To illustrate this here's an example:

███████

This will place a skull on the top of the page (by using position:fixed). I'll attach a screenshot as well.

The power of CSS pretty much allows arbitrary placement of elements across the page. This may also be used in UI redressing attacks.

## Impact

Attacker can arbitrarily redress page via forum posts.

## Attachments
- phpbb-css-redress.png
