# Stored XSS in blog comments through Shopify API

## Report Details
- **Report ID**: 192210
- **URL**: https://hackerone.com/reports/192210
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-18T13:43:21.084Z
- **Disclosed**: 2017-03-16T04:22:33.627Z

## Reporter
- **Username**: prakharprasad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi there!

As far I understand the Shopify Shop have blogs which allow users to comment on blog posts, however the comments with HTML content automatically gets sanitised and then posted to avoid XSS issue. However using the API for comment modification, any application with comment permission can modify a comment and include arbitrary HTML leading to XSS. 

**Steps to Reproduce** 

1.  Open the Shopify Shop's blog and post a comment on a blogpost through a browser. 
2. Note the *comment id*, this can be easily grabbed by checking the HTML after the comment is posted: 
Eg. `<div id="comment-2929551246" class="comment border-bottom clearfix">`
3. Now setup an application with comment permission on the Shop 
4. Send the following JSON to the API endpoint /admin/comments/<comment-id>.json
`  {
  "comment": {
    "id": <comment-id>,
    "body": "blahblah",
    "body_html": "blah<img src=x onerror=alert(0);>"
  }
  }`
5. Send request twice.
6. Visit the blog post, JS in the comment should execute.

I believe this is a valid bug as the comment should get stripped of HTML, which is not the case in case of the above request, however it does gets stripped when posted via web or modified through the comment API documentation at https://help.shopify.com/api/reference/comment#update. To insert arbitrary HTML I've purposely added `body_html` in the request, which is not mentioned in the API reference, the allows me to add HTML, in the comment. The HTML even executes in the Shop's Admin Panel when viewing comments for a particular blog. 

PoC (see comment section for JS execution): https://derp-10.myshopify.com/blogs/news/43260355-first-post

Video: https://www.dropbox.com/s/7ie1tiex1eo4kk9/Comment%20XSS.mov?dl=0

Thanks,
Prakhar Prasad


## Attachments
No attachments
