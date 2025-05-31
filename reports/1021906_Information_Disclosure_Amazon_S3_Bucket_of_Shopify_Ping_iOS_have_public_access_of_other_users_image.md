# [Information Disclosure] Amazon S3 Bucket of Shopify Ping (iOS) have public access of other users image

## Report Details
- **Report ID**: 1021906
- **URL**: https://hackerone.com/reports/1021906
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-29T15:37:26.228Z
- **Disclosed**: 2020-11-21T14:17:04.854Z

## Reporter
- **Username**: justmek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify, when testing Shopify Ping share image function, I discovered an Amazon S3 bucket which has public access which allows an attacker to view all the image of other merchant & users.

## Steps To Reproduce:
1. Install Shopify Ping on your phone then enable Shopify Chat for your store.
2. Go to your Shopify Store and start chatting as a customer. ███
3. Log in to Staff account on Shopify Ping and click on send image ████████
4. Back to Shopify Store as Customer and inspect the website code, you will find the URL of image ██████████ https://ping-api-production.s3.us-west-2.amazonaws.com/oks██████
5. Now visit https://ping-api-production.s3.us-west-2.amazonaws.com, you can view all images of other stores. █████████

## Impact

Using this Bucket access, a hacker can steal all private images of other stores and the user who shared through Shopify Ping.

## Attachments
No attachments
