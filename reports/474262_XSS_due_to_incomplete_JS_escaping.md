# XSS due to incomplete JS escaping

## Report Details
- **Report ID**: 474262
- **URL**: https://hackerone.com/reports/474262
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-03T10:28:41.554Z
- **Disclosed**: 2020-05-14T23:02:44.214Z

## Reporter
- **Username**: jessecampos
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
`ActionView::Helpers::JavaScriptHelper` inside ` rails/actionview/lib/action_view/helpers/javascript_helper.rb` provides JS escaping in Rails, but fails to protect template literal strings. As such, there are two ways XSS can occur:

###XSS via template literal break out:
1) Create a view with the following code: 
```
<script>let a = `<%= j '`+alert`' %>`</script>
```
2) The alert will execute because backticks aren't escaped.

###XSS via template literal placeholder evaluation:
1) Create a view with the following code:
```
<script>let a = `<%= j '${alert()}' %>`</script>
```
2) The alert will execute because `${expression}` isn't escaped
(escaping `$` with `\$` seems sufficient)

## Impact

Attackers can leverage this weakness to [steal private information, hijack accounts and distribute malware](https://chefsecure.com/blog/the-12-exploits-of-xss-mas-infographic) by injecting malicious code instead of an alert.

## Attachments
No attachments
