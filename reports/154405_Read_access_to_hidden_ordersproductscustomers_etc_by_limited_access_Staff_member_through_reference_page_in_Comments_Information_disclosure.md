# Read access to hidden orders,products,customers etc. by limited access Staff member through reference page in Comments (Information disclosure )

## Report Details
- **Report ID**: 154405
- **URL**: https://hackerone.com/reports/154405
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-27T17:41:29.157Z
- **Disclosed**: 2018-12-06T15:04:05.384Z

## Reporter
- **Username**: indoappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Team ,

Note : I have reported multiple issues related to information which were closed a N/A due to some information lack. But this issue will look similar by title but it's different then other issues. Before testing anything i have insured that all other permissions are limited for the account so by any way he should not be able to get these information. 
Description : Any staff member with limited access can view the details of it's limited area. 
Ex: If staff member have limited access to orders , He can still view orders. If he has limited access to customers , he can still view customers details like name, email etc. 
This can be possible by comment section in products ,orders etc. In comment section you will see the # sign by which you can refer any page. Now you won't have access to the pages where your access is limited. Suppose you have access to products but no access to orders. When you will see # sign you can only find pages of products but you won't find the order related pages.
Now while commenting you need to add the ID of that order and you will be able to see details of that order in the comment . 


Steps to reproduce : 
Let's say a staff member has limited access to products and orders but he has access to products.
*Access details : No access to order, order_creation, customers , reports ,discount etc. 

1. Now open any transfer from product menu and and you will see the comment section where you will see the # sign by which you can refer any page of orders,products,customers etc. 
2. When you will click on this # you will notice that it will only show the products related reference pages. But it won't show the orders and customers pages because of your access issue. It means you don't access to it and you can't refer these pages.
3. Now put any product page and add some comment to it and save it. Intercept this request and change the product ID to order ID and the order details will be posted.Instead of order ID if you put customer ID , you will get the customers name and it's email address. 

So this is how any user who has limited access to any feature can access it by this method. 

POC : 

suppose a staff member have limited access to orders , draft_order and customers then he should not be able to access these information. 

HTTP request  Modified : 

POST /admin/transfers/774529/timeline_comments HTTP/1.1
Host: vijaygangani1110store.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-CSRF-Token: RZIoZCcT7SGMNDwD6wl0gHzb1ACcOm1uSXy/NbItuXwQr/95Jzg+24HCWIM4Wzc0Z/F76VYd4iuPF1jj7X0zrQ==
X-Requested-With: XMLHttpRequest
Referer: https://vijaygangani1110store.myshopify.com/admin/transfers/774529
Content-Length: 187
Content-Type: multipart/form-data; boundary=---------------------------191772538514734
Cookie:[cookie_values]
Connection: keep-alive

-----------------------------191772538514734
Content-Disposition: form-data; name="timeline_comment[body]"

[#O3599995137|Order #1005]
-----------------------------191772538514734--


I changed product ID to order ID here. In the timeline_body you have to add order ID to get the order details. If you want to retrieve the customers details you need to add the customer ID in the following format  : [#C3502872769| anyword] 

Here you will be able to get the email address ,name and profile photo of the customer. 


Impact : 
If any shopify owner wants to hire a expert in such a way that he should not be accessing customer details, orders ,order_creation and related items then staff member should not access these things from any where. But by this way the staff member can get access to all these information. 

Let me know of you need any other help from my side to reproduce this issue. I can provide VIdeo POC if needed. 


Best Regards !
Vijay Kumar 


## Attachments
No attachments
