# XSS when clicking "Share to Twitter" at quora.com/widgets/embed_iframe?path=...

## Report Details
- **Report ID**: 258876
- **URL**: https://hackerone.com/reports/258876
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-11T09:00:04.923Z
- **Disclosed**: 2018-01-11T19:59:23.801Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quora

## Vulnerability Information
**Summary:**
The endpoint at `https://{language}.quora.com/widgets/embed_iframe?path={path_to_answer_in_same_language}` shows the answer you specify in _path_ (like `/Question/answer/User`) in a format useful to embed.
There is one button _Share_ that when clicked shows another button _Share to Twitter_. The `href` attribute of this last button is of the format `javascript: window.open(&quot;https://twitter.com/intent/tweet?text=Answer on @Quora by @User to Question? http://qr.ae/nnnn&quot;, &quot;Share Answer to Twitter&quot;, &quot;width=600, height=250&quot;)`.
The problem is that you can create a question with `"` (quotes) and inject Javascript code that is going to be executed when the user clicks _Share to Twitter_.

**Description (Include Impact):**
It requires user interaction, but it works.

### Steps To Reproduce

1. Go to https://www.quora.com/
2. Click on _Ask Question_ 
3. Enter a valid question which includes `"-alert(document.domain)-"` somewhere. I entered `Question ignore "-alert(document.domain)-"?` and it was accepted as valid
4. Now you may be in the page of the question you just asked
5. Click on _Answer_
6. Enter anything
7. Click on _Submit_
8. Copy the path from the address bar. Mine was `/Question-ignore-alert-document-domain/answer/Cuenta-Para-Probar`
9. Go to `https://www.quora.com/widgets/embed_iframe?path={path_from_last_step}`. Mine is https://www.quora.com/widgets/embed_iframe?path=/Question-ignore-alert-document-domain/answer/Cuenta-Para-Probar
10. Click on _Share_
11. Click on _Share to Twitter_
12. `alert(document.domain)` is executed

### Optional: Your Environment (Browser version, Device, app version, os version etc)

 * It is not browser dependent. Anyway, I tested it on Firefox, Chrome and Safari for Mac.

### Optional: Supporting Material/References (Screenshots)

 * I don't think is necessary, but let me know if you need something else.

## Attachments
No attachments
