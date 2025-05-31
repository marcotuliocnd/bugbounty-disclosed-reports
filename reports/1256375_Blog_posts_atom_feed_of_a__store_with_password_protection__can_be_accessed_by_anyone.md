# Blog posts atom feed of a  store with password protection  can be accessed by anyone 

## Report Details
- **Report ID**: 1256375
- **URL**: https://hackerone.com/reports/1256375
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-09T20:33:17.577Z
- **Disclosed**: 2021-11-08T15:10:42.229Z

## Reporter
- **Username**: xenx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi shopify,
###DESCRIPTION
I found a issue with blog posts atom feed of a shopify store. So without password we can't access  the blog post atom feed at ```https://yourstore.myshopify.com/blogs/news.atom``` . But this can be bypass to access the atom feed of the blog posts.
For example try out this.  I have added two blog posts in my store which can't be access through https://testcheckagain.myshopify.com/blogs/news , it will just redirect you to password page or accessing atom feed give you ```401 error``` at https://testcheckagain.myshopify.com/blogs/news.atom. But it can be bypassed to check it at https://dummytext2showpoc-55204085816.shopifypreview.com/blogs/news.atom . So preview link can be exploited to get the atom feed of blog posts of password protected store. ```It can't be exploited for a partner development store```.

###STEPS
1.  Create a store at shopify.com
2. Add a blog post and make it visible.
3. If try to check the blog post atom feed in  a different machine you will be thrown ```401 error```.
4. To bypass this  try this link```https://dummytext2showpoc-store_id.shopifypreview.com/blogs/news.atom```.
5. You can the access atom feed

## Impact

Disclosing atom feed of blog posts of password protected store

## Attachments
No attachments
