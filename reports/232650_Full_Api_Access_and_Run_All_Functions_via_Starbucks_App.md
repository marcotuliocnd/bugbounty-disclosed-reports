# Full Api Access and Run All Functions via Starbucks App

## Report Details
- **Report ID**: 232650
- **URL**: https://hackerone.com/reports/232650
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-28T15:10:12.674Z
- **Disclosed**: 2017-08-06T08:51:21.197Z

## Reporter
- **Username**: ynsy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
The tested application is Starbucks Turkey Android App. https://play.google.com/store/apps/details?id=com.starbucks.tr&hl=en 

All these things are made without any login. I did not login the app.
1. I tried to intercept traffic between starbucks app and server with burp suite. I could not be successful because of the ssl pinning. 
2. Before the unpinnig ssl, I look around the app's all screens.
3. When i look at the messages tab i saw a proccess on my burp history. 
4. Application sent a request to https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20 this url and it took a response.
5. I evaluated this request then i saw the Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz token.
6. I tried to reach this url via browser however, i couldnt because it wants to basic authentication and i tried the default password which comes to mind but i couldnt be successful. 
7. I remembered when there was a request on burp which has Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz token and i tried to add this token in my all request while trying to access via browser.
8. Bingoooo! It worked! I reach the https://crmproxy.protel.com.tr this api server and i looked around it then i found the api docs.
9. Finally, i tried to sent all request in api docs, i was successful in all of them. 

I added to all screenshots below. If there is any question, i may answer them.

Thank you,

Yunus Y.

## Attachments
- starbucks_basic_authentication_is_needed.png
- starbucks_burp_request.png
- starbucks_request_repeated_in_burp.png
- starbucks_api_docs_accessed.png
- starbucks_api_page_accessed.png
- starbucks_token_match_replace.png
- starbucks_api_clients_.png
- starbucks_customer_info.png
- starbucks_trsancation.png
