# Is the Google Bucket Meant To Be Publicly Listable? https://cdn.shopify.com/shop-assets/

## Report Details
- **Report ID**: 1102546
- **URL**: https://hackerone.com/reports/1102546
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-02-13T05:14:37.685Z
- **Disclosed**: 2022-02-09T20:59:55.366Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I found that https://cdn.shopify.com/shop-assets/ is listing the all objects in https://storage.googleapis.com/arrive-assets-storage-production/

But when I directly visit https://storage.googleapis.com/arrive-assets-storage-production/, it says 

>Anonymous caller does not have storage.objects.list access to the Google Cloud Storage bucket.

So I wonder maybe it is unintentional that user can directly list all the objects in GCP using the link https://cdn.shopify.com/shop-assets/?

PoC

██████

## Impact

List objects in GCP that should be protected from anonymous users

## Attachments
No attachments
