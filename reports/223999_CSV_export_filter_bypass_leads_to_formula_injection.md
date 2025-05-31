# CSV export filter bypass leads to formula injection.

## Report Details
- **Report ID**: 223999
- **URL**: https://hackerone.com/reports/223999
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-26T09:00:34.649Z
- **Disclosed**: 2017-05-17T15:19:18.397Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Dear Weblate bug bounty team,

# Summary
---

The [new filter](https://github.com/WeblateOrg/weblate/commit/1216f65655ca4b3f32b9d59605eb4446d503bdbf) can be bypassed using: `%0A-3+3+cmd|' /C calc'!D2`.

~~~python
text = "%0A-3+3+cmd|' /C calc'!D2"
def csv_filter_bypass():
    if text and text[0] in ('=', '+', '-', '@'):
        return "'" + text
return text
~~~

# How can this be fixed?
---

You need to escape and detect more characters as follows:

~~~python
text = "%0A-3+3+cmd|' /C calc'!D2"
def csv_filter_fix():
    if text and text[0] in ('=', '+', '-', '@', '|', '%'):
        text = text.replace("|", "\|")
        return "'" + text + "'"
return text
~~~

You can compare your results with the following demonstration:

~~~python
text = "%0A-3+3+cmd|' /C calc'!D2"

def csv_filter_bypass():
    if text and text[0] in ('=', '+', '-', '@'):
        return "'" + text
    return text

def csv_filter_fix():
    if text and text[0] in ('=', '+', '-', '@', '|', '%'):
        text = text.replace("|", "\|")
        return "'" + text + "'"
    return text

csv_filter_bypass()
csv_filter_fix()
~~~

Best regards,
Ed

## Attachments
No attachments
