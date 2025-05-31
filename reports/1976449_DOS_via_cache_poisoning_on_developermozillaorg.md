# DOS via cache poisoning on [developer.mozilla.org]

## Report Details
- **Report ID**: 1976449
- **URL**: https://hackerone.com/reports/1976449
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-05-07T18:23:41.051Z
- **Disclosed**: 2023-06-05T16:10:09.062Z

## Reporter
- **Username**: zhero_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
Hello, after some research it appears that it is possible for an attacker to perform a DOS attack on the https://developer.mozilla.org page for an indefinite period.
This is possible by adding an ```X-Forwarded-Host``` header and a value causing an error on the back-end side (error 404), the bad configuration of the cache makes it possible to save the response there and to serve it to users visiting the page, making the page completely inaccessible for an indefinite period.
No information about the caching period is available in the response, but it is anyway possible to reinterpret the manipulation indefinitely.
For obvious reasons I performed my tests using a cache-buster - adding a URL parameter as we will see in the POC - so as not to affect the user experience.

## Steps To Reproduce:

  1. Pass your HTTP requests through your preferred proxy
  2. Go to : https://developer.mozilla.org then - in your proxy - send the request to your repeater
  3. Add the parameter of your choice to the URL, it will serve as a cache-buster and will not "poison" the site visited by users. In other words, the DOS will only be effective on the URL containing your parameter, you probably know this but let me clarify: this is very important in order not to damage the services.
  4. Add the following header :

```
X-Forwarded-Host: XXX
```
The request ready to send (```?my_cache_buster=test```) being my cache-buster :

{F2339007}

Once the request has been sent, the response will - as expected - contain a 404 error. Open another browser in incognito mode, and enter the full URL containing your cache-buster. You should get a 404 error. If this is still not the case, resend the request several times until the cache is poisoned :

{F2339009}

## Impact

An attacker can perform this attack (without a cache-buster this time) in order to make the service unavailable indefinitely. It is also possible in the case where the cache will be reset to make a small script to send requests every minute (for example) so that the cache is permanently poisoned making the site completely unavailable and causing financial damage to the company.

## Attachments
- image.png
- image.png
