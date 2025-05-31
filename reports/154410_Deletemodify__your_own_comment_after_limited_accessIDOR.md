# Delete/modify  your own comment after limited access(IDOR)

## Report Details
- **Report ID**: 154410
- **URL**: https://hackerone.com/reports/154410
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-27T17:57:27.520Z
- **Disclosed**: 2016-08-09T00:26:34.692Z

## Reporter
- **Username**: indoappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Team,

Description : When user has access to some feature like orders , Transfer etc. where comment section is available. Suppose staff members comments in it . Now owner of the account limited access to orders , then he won't be able to access his comments and he won't be able to modify/delete  his comments. But this can be bypassed and he can still modify and delete his own comments. 
Comment ID can be used in any other feature's comment section to delete/modify comments. 

Suppose A staff member was given access to orders and products. Now he commented on the orders and after some days his access to orders was limited by owner. Now he should not be able to delete it's own comments but he can still delete these comments by delete request of  transfer comment section.

Steps to reproduce : 
1. Create a shop and add a staff member(Attacker) to it and provide him all the access.
2.Now from attackers account comment on any order.Let say comment ID is "12345"
3.Now from Owner account limit the access of orders so the staff member should not be able to access the comments.
4.Now go to attackers account and go to any transfer and comment on that transfer.(Staff member can go to the transfer because he has access to products.)
5.Now you will see the modify and delete options on the transfer comment.Delete or modify the comment and intercept the request.

HTTP request will look something like this : 

POST /admin/transfers/774529/timeline_comments/[Transfer_comment_ID]HTTP/1.1
Host: vijaygangani1110store.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html, application/xhtml+xml, application/xml
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-XHR-Referer: https://vijaygangani1110store.myshopify.com/admin/transfers/774529
X-CSRF-Token: DSyGAzUBvMcMmYFiUTMbgXMbWPIK97AYA8vNiQWh5GhYEVEeNSpvPQFv5eKCYVg1aDH3G8DQP13FoCpfWvFuuQ==
Referer: https://vijaygangani1110store.myshopify.com/admin/transfers/774529
Content-Length: 151
Cookie: [Cookie_values]
Connection: keep-alive

utf8=%E2%9C%93&_method=delete&authenticity_token=[ouath_token]

In the above request change the comment ID of transfer to order Comment ID and the comment will be deleted. The same can be applied to modification of the comment which should not happen .
This whole process work vice versa . Suppose i have limited access to transfer then i can delete the comment by orders and if i have limited access to orders then i can delete comment by transfer. 


Let me know if you need any Video POC regarding this to understand the issue more closely.

Best Regards !
Vijay Kumar  

## Attachments
No attachments
