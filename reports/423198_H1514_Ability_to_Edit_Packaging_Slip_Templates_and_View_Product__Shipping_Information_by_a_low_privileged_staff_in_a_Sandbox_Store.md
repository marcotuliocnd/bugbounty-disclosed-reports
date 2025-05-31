# H1514 Ability to Edit Packaging Slip Templates and View Product & Shipping Information by a low privileged staff in a Sandbox Store

## Report Details
- **Report ID**: 423198
- **URL**: https://hackerone.com/reports/423198
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-13T02:48:24.830Z
- **Disclosed**: 2019-04-24T19:49:18.660Z

## Reporter
- **Username**: anshuman_bh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello, 

It was observed that it is possible to edit packaging slip templates and then view the product and shipping information in the packaging slip by a low privileged staff in a sandbox store by simply navigating to the URL `https://<store>.myshopify.com/admin/settings/packing_slip_template`. It appears that this endpoint does not have the proper authorization controls implemented as is the case throughout the rest of the application. 

In order to reproduce this, please follow the steps below:

* As a Storefront Admin, create a Sandbox Store and log in to it.

* Create a bunch of products and setup the shipping information at the endpoints `/admin/products` and `/admin/settings/shipping` respectively as shown below:

{F359765}

{F359766}

* Next, add a staff for this store and do not assign any permissions to that staff at the endpoint `/admin/settings/account` as shown below:

{F359767}

* Now, in a different browser, authenticate as the staff in this sandbox store and notice that you are not allowed to do anything as the Store admin because you don't have any permissions. 

{F359768}

* Now, as the staff, navigate to the endpoint `https://<store>.myshopify.com/admin/settings/packing_slip_template`. Notice that you can *edit* and save the packing slip template. And, then you can also preview the template as shown below:

{F359770}

{F359769}

* Notice that the PDF generated from the preview has the *product* information as well as the *shipping* information

## Impact

As a low privileged staff of a sandbox store (with no permissions), you are not supposed to edit or view any information of a store, if restricted by the store admin. A malicious low privileged staff can potentially leverage this vulnerability to edit packaging slip templates which can result in unauthorized information being sent to the customer. They can also view the product and shipping information of the store that they shouldn't have been able to otherwise.

## Attachments
- Screen_Shot_2018-10-12_at_7.37.14_PM.png
- Screen_Shot_2018-10-12_at_7.37.26_PM.png
- Screen_Shot_2018-10-12_at_7.39.44_PM.png
- Screen_Shot_2018-10-12_at_7.41.40_PM.png
- Screen_Shot_2018-10-12_at_7.44.01_PM.png
- Screen_Shot_2018-10-12_at_7.43.23_PM.png
