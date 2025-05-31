# H1514 [beerify.shopifycloud.com] GraphQL discloses internal beer consumption

## Report Details
- **Report ID**: 419883
- **URL**: https://hackerone.com/reports/419883
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-10-05T23:33:41.819Z
- **Disclosed**: 2019-05-08T19:15:14.581Z

## Reporter
- **Username**: emitrani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi security team,

**Summary:** With great pleasure we would like to report that we have discovered a GraqhQL endpoint that discloses internal beer consumption at your offices. 

**Description:** This endpoint is leaking internal app details about how much beer you have left on any given day.

## Steps To Reproduce:


  1) Do a blanket graphql introspection query on shopifycloud domains and download it.
{F356253}
  2) Send following query to find out what locations are configured with the app.

```
POST /graphql HTTP/1.1
Host: beerify.shopifycloud.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-type: application/json
Cookie: _y=36f02e8b-0639-47BB-8F16-B17F7ED46D62; _shopify_y=36f02e8b-0639-47BB-8F16-B17F7ED46D62; _shopify_fs=2018-10-02T22%3A40%3A00.828Z; master_device_id=fc39122b-3f8d-4407-a889-e8090ce47540; _s=3776a811-97F6-43EF-EDB5-757C5727133E; _shopify_s=3776a811-97F6-43EF-EDB5-757C5727133E; _shopify_sa_t=2018-10-03T01%3A12%3A12.231Z; _shopify_sa_p=
Connection: close
Upgrade-Insecure-Requests: 1
X-Forwarded-For: 127.0.0.1, 127.0.01, 127.0.0.1
X-HackerOne: Shopify
Content-Length: 69

{"query": "query allLocations{allLocations{address, code, contact}}"}
```
#### Response:
```
HTTP/1.1 200 OK
Server: nginx/1.15.4
Date: Fri, 05 Oct 2018 23:13:45 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
X-Cusco-Version: 0.4.10
ETag: W/"fb29943639fffbdc10edcc9fcc2645bc"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 77418b20cbbea262c662e9af85afdfa3
X-Runtime: 0.013611
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Dc: gke
X-Dc: gke
Content-Length: 152

{"data":{"allLocations":[{"address":"150 Elgin Street, Ottawa, ON, Canada, K2P1L4","code":"OTT150, 8th Floor","contact":"Alana Plomp (@alana.plomp)"}]}}
```

 Now with the response we learn the person working there as well as the code which is needed for the next step.
3) Use the code to pivot into critical information disclosure of beer consumption in the office
```
{"query": "query location{location(code:\"OTT150, 8th Floor\"){taps{edges{node{percentRemaining, beer{brewery, ibu, style, tastingNotes, beerLogo, abv}}}}}}"}
```
#### Response:

```
{"data":{"location":{"taps":{"edges":[{"node":{"percentRemaining":89,"beer":{"brewery":"Beau's Brewing Co","ibu":30,"style":"American-style Brown Ale","tastingNotes":"American Brown Ale pours dark brown with reddish highlights and a tan foam. The aroma features dark notes of cacao and molasses. The flavour is balanced between rich maltiness and hop bitterness. The finish offers clean dark malt with a touch of raisiny fruit.","beerLogo":"","abv":5.6}}},{"node":{"percentRemaining":2,"beer":{"brewery":"Beaus","ibu":20,"style":"Witbier","tastingNotes":"Match made is a slightly hazy Belgian-style witbier that features the pairing of tart, refreshing lime with the exotic spiciness of cumin. Thirst-quenching and food-friendly!","beerLogo":"","abv":5.6}}}]}}}}
```
4) Realize this location has a thirst for Witbier and plan your visit accordingly by bringing a 6 pack to the event
{F356254}

## Impact

This gives hackers who discover this endpoint an advantage as we know what kinds of beer Shopify employees enjoy and can use this to win them over during the event.

Cheers,
Eray & Rojan

## Attachments
- image_(3).png
- images.jpg
