# Stored XSS in wordpress.com

## Report Details
- **Report ID**: 733248
- **URL**: https://hackerone.com/reports/733248
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-09T22:04:23.291Z
- **Disclosed**: 2020-02-17T11:34:36.958Z

## Reporter
- **Username**: adhamsadaqah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Stored XSS as a comment or as a post (body or title)  at 
`https://wordpress.com/read/feeds/{blog_id}/posts/{post_id}`
`https://yoursubdomain.wordpress.com`
using the payload:
 ```
<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;
```
## Steps To Reproduce:
- As a comment 
  1. Log in to wordpress.com
  2. Choose a post from the feeds
  3. Add a comment with the payload:
         `<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;`
 4. By clicking on `Click Here`, an alert will fire with cookies of the domain `wordpress.com`
- As a post
  1. Log in to wordpress.com
  2. Create a new post or site.
  3. Add the payload `<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;`  to the body or the title of the blog post
  4. preview or publish your new blog post
  5. By clicking on `Click Here`, an alert will fire with cookies of the domain `yoursubdomain.wordpress.com` or `wordpress.com` if the post is previewed from the WordPress feed.  
 6. If you add comments to your blog post and using the payload mentioned above as a comment an Stored XSS alert will fire when you click on the link.

## Impact

- Perform arbitrary requests on the behalf of other users with security context of  wordpress.com or blogsubdomain.wordpress.com
- Read any data the attacked user has access to.

## Attachments
- POC2.png
- POC1.png
