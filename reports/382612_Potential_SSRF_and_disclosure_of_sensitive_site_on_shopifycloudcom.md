# Potential SSRF and disclosure of sensitive site on *shopifycloud.com

## Report Details
- **Report ID**: 382612
- **URL**: https://hackerone.com/reports/382612
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-17T14:01:13.005Z
- **Disclosed**: 2018-07-19T20:47:58.912Z

## Reporter
- **Username**: rijalrojan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
*Note: I am reporting this after talking with @shopify-peteryaworski*

**Summary**
There is a staging/testing site for payment cancellations and refunds at shopifycloud.com. This site allows sending post request and fetching the response back to the user. This leads to SSRF because it allows fetching potential internal clients and servers. 

**Description**
https://offsite-gateway-sim.shopifycloud.com/notification allows sending test request to a user supplied `x_url_callback` url. In such request it is allowed to submit Google metadata IPs and get a response back. Thankfully it seems that after the last SSRF report on Shopify, you guys have completely stripped the server from having any access to Google Metadata because for `v1beta1` this server responds with `This metadata api is not allowed in the metadata proxy`. Additionally for the regular `v1` it returns 403 because the header is missing. The only potential exploit here is that if there is any internal site only Google IP is able to access then someone can call that site and see its details. 

**Reproduction**
1. Go to https://offsite-gateway-sim.shopifycloud.com/notification and put http://metadata/computeMetadata/v1beta1/ as a test request.

## Impact

SSRF. The repo for this is private so I am assuming this has to be private too?

## Attachments
No attachments
