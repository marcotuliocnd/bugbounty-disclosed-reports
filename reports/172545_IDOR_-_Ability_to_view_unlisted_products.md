# IDOR - Ability to view unlisted products

## Report Details
- **Report ID**: 172545
- **URL**: https://hackerone.com/reports/172545
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-28T02:23:34.677Z
- **Disclosed**: 2018-04-27T01:28:34.602Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
Hi All,
I believe I've found a vulnerability on your sandbox site which allows attackers to view the details of listings that are unpublished.

##Description
While creating a product, I noticed there is a call to https://sandbox.reverb.com/api/listings/65905/product_bundle which returns json details about the product. I've included an example response below.

Given my product is unlisted, it is not included in my store. if I go to the listing directly as another user logged in, via the url https://sandbox.reverb.com/item/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src, I am redirected to /marketplace with a message that the listing isn't published and if I own it, I should log in.

However, if I use a proxy, create my own product and intercept the call to /api/listing/MYID/product_bundle and replace MYID with an unlisted product, I will receive the product details.

##Vulnerability
I'm reporting as listings which aren't published should not be accessible by non-owners, as the message indicates when you browse to the item direct via the listing url. This could result in unwanted behaviour for person listing the product.

##Steps to reproduce
1. Log in as User A
2. Create a listing
3. Using a proxy like burp, note the calls and look for /api/listing/YOURID/product_bundle
4. Repeat the call to your /api/listing/YOURID/product_bundle but change the id to 65905 - my unlisted product. You will receive the product details.

Please let me know if you have any questions.
Pete

##Example Response
HTTP/1.1 200 OK
Content-Type: application/hal+json
Content-Length: 5144
Connection: close
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Cache-Control: max-age=0, private, must-revalidate
Date: Wed, 28 Sep 2016 01:56:29 GMT
ETag: W/"5ff8ce43e23f8b60971b5c936f360764"
Server: nginx
Set-Cookie: _reverb_session=REDACTED
Strict-Transport-Security: max-age=31536000
Vary: Accept-Version
X-Request-Id: 652128de-43ce-4fe3-bdbf-7c5cbe773f04
X-Revision: e9f37a0b9054847f8d1124bda928320bd60e334a
X-Runtime: 0.126833
X-Cache: Miss from cloudfront
Via: 1.1 5f18659c165b505bcc54ed04c0bbd028.cloudfront.net (CloudFront)
X-Amz-Cf-Id: kC10ARARo89nYbkLCsh4aAgIWrFG3vOdW_zpreKA-CY6Bf7jq9ylKQ==

{"main_listing":{"id":65905,"make":"\"><img onerror=alert(1) src=","model":"\"><img onerror=alert(1) src=","finish":"\"><Img Onerror=Alert(1) Src=","year":"","title":"\"><img onerror=alert(1) src= \"><img onerror=alert(1) src= \"><img onerror=alert(1) src=","created_at":"2016-09-22T12:46:10-04:00","shop_name":"\"><img onerror=alert(1) src='s Gear Depot","description":"\"&gt;&lt;img onerror=alert(1) src=","condition":"Mint","condition_uuid":"ac5b9c1e-dc78-466d-b0b3-7cf712967a48","condition_slug":"mint","price":{"amount":"5.00","amount_cents":500,"currency":"USD","symbol":"$","display":"$5"},"inventory":0,"has_inventory":false,"offers_enabled":true,"category_uuids":["62835d2e-ac92-41fc-9b8d-4aba8c1c25d5"],"listing_currency":"USD","sku":"\"><img onerror=alert(1) src=","state":{"slug":"draft","description":"Draft"},"wanted":false,"accepted_payment_methods":["paypal"],"location":{"country_code":"US","display_location":"United States"},"handmade":true,"draft":true,"live":false,"local_pickup_only":true,"cloudinary_photos":[{"id":140151,"public_id":"llyoz5rfodyrpz8cpcox","version":"1475027634","format":"jpg","resource_type":"image","path":"v1475027634/llyoz5rfodyrpz8cpcox.jpg","preview_url":"https://res.cloudinary.com/reverb-dev/image/upload/s--oTVOEOVd--/f_auto,fl_progressive/v1475027634/llyoz5rfodyrpz8cpcox.jpg"}],"shop":{"feedback_count":0,"preferred_seller":false,"rating_percentage":0.0},"stats":{"views":0,"watches":0},"offer_count":0,"shipping_policy":"I will ship with tracking to the listed regions. To negotiate shipping rates to other locations, please send me a message.","product_type":"accessories","sold_as_is":false,"return_policy":{"description":"This product can be returned within 7 days of receipt."},"is_my_listing":false,"photos":[{"_links":{"large_crop":{"href":"https://res.cloudinary.com/reverb-dev/image/upload/s--izU-PuyA--/a_exif,c_thumb,f_auto,fl_progressive,g_south,h_640,q_auto:eco,w_640/v1475027634/llyoz5rfodyrpz8cpcox.jpg"},"small_crop":{"href":"https://res.cloudinary.com/reverb-dev/image/upload/s--RYtQkDfv--/a_exif,c_thumb,f_auto,fl_progressive,g_south,h_296,q_auto:eco,w_296/v1475027634/llyoz5rfodyrpz8cpcox.jpg"},"full":{"href":"https://res.cloudinary.com/reverb-dev/image/upload/s--sD227f9W--/a_exif,c_limit,f_auto,fl_progressive,g_south,h_1136,q_auto:eco,w_640/v1475027634/llyoz5rfodyrpz8cpcox.jpg"},"thumbnail":{"href":"https://res.cloudinary.com/reverb-dev/image/upload/s--DhB5ugV9--/a_exif,c_thumb,f_auto,fl_progressive,g_south,h_192,q_auto:eco,w_192/v1475027634/llyoz5rfodyrpz8cpcox.jpg"}}}],"shipping":{"local":true,"us":false,"us_rate":null,"rates":[],"initial_offer_rate":{"region_code":null,"rate":{"original":{"amount":"0.00","amount_cents":0,"currency":"USD","symbol":"$","display":"FREE"},"display":{"amount":"0.00","amount_cents":0,"currency":"USD","symbol":"$","display":"FREE"}}}},"_links":{"photo":{"href":"https://res.cloudinary.com/reverb-dev/image/upload/s--izU-PuyA--/a_exif,c_thumb,f_auto,fl_progressive,g_south,h_640,q_auto:eco,w_640/v1475027634/llyoz5rfodyrpz8cpcox.jpg"},"self":{"href":"/api/listings/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src"},"update":{"method":"PUT","href":"/api/listings/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src"},"end":{"method":"PUT","href":"/api/my/listings/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src/state/end"},"want":{"method":"PUT","href":"/api/wants/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src"},"unwant":{"method":"DELETE","href":"/api/wants/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src"},"edit":{"href":"/api/listings/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src/edit"},"web":{"href":"https://sandbox.reverb.com/item/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src"},"make_offer":{"method":"POST","href":"/api/listings/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src/offer"},"add_to_wishlist":{"method":"POST","href":"/api/my/wishlist/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src"},"remove_from_wishlist":{"method":"DELETE","href":"/api/my/wishlist/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src"},"cart":{"href":"/api/cart/65905"},"buy":{"href":"https://sandbox.reverb.com/cart/add?cart_item%5Baction_source_attributes%5D%5Bdevice%5D=&cart_item%5Bproduct_id%5D=65905"},"flag":{"href":"/api/listings/65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src/flag"},"contact_seller":{"web":{"href":"https://sandbox.reverb.com/my/messages/new?item=65905-img-onerror-alert-1-src-img-onerror-alert-1-src-img-onerror-alert-1-src&to=6218-img-onerror-equals-alert-1-src-equals"}},"conversations":{"href":"/api/listings/65905/conversations"},"shop":{"href":"/api/shops/img-onerror-equals-alert-1-src-equals-s-gear-depot","web":{"href":"https://sandbox.reverb.com/shop/img-onerror-equals-alert-1-src-equals-s-gear-depot"}},"sales":{"href":"/api/listings/65905/sales"}}},"bundled_products":[]}

## Attachments
No attachments
