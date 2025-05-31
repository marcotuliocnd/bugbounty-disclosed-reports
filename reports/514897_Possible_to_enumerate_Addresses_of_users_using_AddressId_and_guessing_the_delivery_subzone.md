# Possible to enumerate Addresses of users using AddressId and guessing the delivery_subzone

## Report Details
- **Report ID**: 514897
- **URL**: https://hackerone.com/reports/514897
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-25T14:13:38.202Z
- **Disclosed**: 2020-07-15T08:03:14.353Z

## Reporter
- **Username**: bigbug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Description**

The title may seem a bit confusing but I will try to make it as simple as possible. Let us dive into it.

When we login to zomato.com and click on `Order Food`, We are redirected to the endpoint like `/mumbai/order-food-online?delivery_subzone=10159` where `mumbai` is the city and `10159` is the `delivery_subzone`. 

The important thing here is that the page contains our full address we selected for purchase. 

{F451667}

As we can see, the page displays our **full address** we selected. In our case, I have selected an address with Tag `Other`. This could also be our `Home` address in case of genuine regular users. 

On digging deeper this value comes from the cookie `selectedAddressId`, which is set when a user selects a saved address. 

When a request is sent, the server looks for this value to display the address on the order page. 


But there is a catch to it. The server only returns the **Full Address** if it matches the correct **delivery_subzone**. 
If the value of selectedAddressId does not match the delivery_subzone in which the address id falls under, the server only returns the **geo-location** and not the full address. 

Let us see this in practice:

**Request**

```
:method: GET
:path: /mumbai/order-food-online?delivery_subzone=10159
:authority: www.zomato.com
:scheme: https
user-agent: Mozilla/5.0 (Windows NT 6.3; rv:46.0) Gecko/20100101 Firefox/46.0
accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
accept-language: en-US,en;q=0.5
accept-encoding: gzip, deflate, br
referer: https://www.zomato.com
cookie: selectedAddressId=████████
```

Now in above request We have requested the server to fetch the Full Address of `AddressId=██████`. (This is my genuine AddressId) with the subzone 10159 (genuine subzone).

This is how a normal request looks like. The response will contain by **Full Address** because my subzone value is right. 

Now this can be used to enumerate the addresses of users **provided you have the right subzone value**

###Why is this attack Practical and Impactful

1. This can fetch the full address of any AddressId provided you have the right delivery_subzone value.
2. If an attacker has the right subzone value he can get the full address associated with the AddressId. 
3. This attack also works in an **unauthenticated manner**. meaning the attacker needs to just set the target AddressId in the cookie field without authenticating, which makes tracing difficult. (cookie: selectedAddressId=████)
4. **Lastly and Most Important** - There is **no Rate limiting**

The combination of an unauthenticated attacker with no rate limiting makes this attack seamlessly practical. I have tried couple of random values myself and managed to verify and obtain the full address of the victim.

**Steps to reproduce**

Here for the sake of reproducability, you can use my genuine address Id - `███`. This has value `██████` (My genuine Address :) )

1. Login to zomato
2. Click on `Order Food`
3. Intercept the request and send to repeater (Burp Suite)
4. Now change `selectedAddressId` cookie to `cookie: selectedAddressId=████`
5. You will receive mu full address in the response.

You can also use my alternate test account AddressId `███` and the delivery_subzone `1050`
The expected value is `Other - A wing, imaginary road, Dahisar West`. 

###Exploit Raw Request

```
:method: GET
:path: /mumbai/order-food-online?delivery_subzone=10159
:authority: www.zomato.com
:scheme: https
user-agent: Mozilla/5.0 (Windows NT 6.3; rv:46.0) Gecko/20100101 Firefox/46.0
accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
accept-language: en-US,en;q=0.5
accept-encoding: gzip, deflate, br
referer: https://www.zomato.com
cookie: selectedAddressId=████████
```

###Exploit CURL request

`curl "https://www.zomato.com/mumbai/order-food-online?delivery_subzone=1050" -H "Host: www.zomato.com" -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; rv:46.0) Gecko/20100101 Firefox/46.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "Referer: https://www.zomato.com" -H "Cookie: selectedAddressId=██████;" -H "Connection: keep-alive"`

## Impact

1. Enumerate Addresses of users with help of address ID and `delivery_subzone`
2. No Rate limiting leads to BruteForce of delivery_subzone to retrieve addresses
3. Unauthenticated attacker can enumerate addresses without any limitation

## Attachments
No attachments
