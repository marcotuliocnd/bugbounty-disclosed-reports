# XSS in new.loading.page.html

## Report Details
- **Report ID**: 2419227
- **URL**: https://hackerone.com/reports/2419227
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-03-16T22:27:20.485Z
- **Disclosed**: 2024-03-17T14:06:19.848Z

## Reporter
- **Username**: aviv_keller
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gocd

## Vulnerability Information
# Overview
The vulnerability arises from inadequate handling of query parameters, enabling attackers to insert `javascript:` URIs as redirectors within the `new.loading.page.html` file.

```js
var redirectToLanding = function() {
  var locationData = window.location.search.match(/(\?|&)redirect_to=([^&]+)(&|$)/);
  if (locationData === null) {
    window.location.reload(true);
  } else {
    window.location = decodeURIComponent(locationData[2]);
  }
}
```

[View Permalink](https://github.com/gocd/gocd/blob/0199f22311c83c88ee249a3a71907ce6f58ebd9f/jetty/src/main/resources/loading_pages/new.loading.page.html#L397-L404)

When the URL's query is `?redirect_to=javascript:alert("XSS")`, `locationData[2]` equals `'javascript:alert("XSS")'`. Subsequently, triggering `redirectToLanding` leads to XSS exploitation.

## Impact

Attackers can inject javascript: URIs to execute unauthorized scripts, potentially stealing sensitive information such as session cookies or performing actions on behalf of the user.

## Attachments
No attachments
