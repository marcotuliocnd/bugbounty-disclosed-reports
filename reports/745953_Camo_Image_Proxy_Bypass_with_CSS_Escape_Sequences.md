# Camo Image Proxy Bypass with CSS Escape Sequences

## Report Details
- **Report ID**: 745953
- **URL**: https://hackerone.com/reports/745953
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-11-25T14:29:47.901Z
- **Disclosed**: 2019-12-18T03:15:27.464Z

## Reporter
- **Username**: zhutyra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
## Summary

With CSS escape sequences it is possible to bypass CSS url detection and filtering.

## Details

Users can use HTML tags in their Profile Bio in *About Me* and *Wish List* fields. Among other filtering and sanitization, image URLs are replaced by URLs on internal image proxy. For example, this content in *About Me*:
```html
<span style="background:url(http://foo.com/bar)">XX</span>
```
Will be replaced by this:
```html
<span style="background:url(https://camo.stream.highwebmedia.com/f923a95762fc0b6025015c00b58922b72f25096d/687474703a2f2f666f6f2e636f6d2f626172)" target="_blank" rel="nofollow">XX</span>
```
The problem is that the parser doesn't support CSS escape sequences, and for example this form, with letter `r` written as hexadecimal escape sequence, will not be detected as image link:
```html
<span style="background:u\72l(http://foo.com/bar)">XX</span>
```
## Steps To Reproduce:

Put the code mentioned above in your Bio.
{F643234}
After saving the edit, you can use the Developer Tools to inspect the element and see that the URL has not been replaced.
{F643235}
And in Network monitor in Developer Tools you can see that it was processed. In this case blocked by Content Security Policies.
{F643236}

## Note

I'm not aware of any immediate security threat from this. Like, I have no accompanying CSRF or information leak and I assume use of browsers that adhere to CSP. But definitely it is something that should be fixed.

## Impact

The room owner can force room visitors to make unintended URL requests.

## Attachments
- 01-edit.png
- 02-inspect.png
- 03-network.png
