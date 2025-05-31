# User Information sent to client through websockets

## Report Details
- **Report ID**: 168223
- **URL**: https://hackerone.com/reports/168223
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-14T06:34:04.814Z
- **Disclosed**: 2016-12-07T19:33:01.275Z

## Reporter
- **Username**: archers123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
I noticed when monitoring the websocket requests that the account information of user, including user_id is sent to the client. 

__{"t":"d","d":{"r":8,"a":"p","b":{"p":"/carts/3671079_xjdJHqx88J435eDW5zxN/users/-KRbGN8R6uIjy6_OPx_j","d":{"id":25390626,"name":"Username}}}}__

## Attachments
No attachments
