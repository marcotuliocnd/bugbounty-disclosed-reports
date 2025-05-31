# Disclosure of users' ip address whenever they view my fright offer on image preview (Without interaction)

## Report Details
- **Report ID**: 1782467
- **URL**: https://hackerone.com/reports/1782467
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-23T16:01:00.832Z
- **Disclosed**: 2024-02-19T08:42:48.747Z

## Reporter
- **Username**: bugsv2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
Hi kirill, wish you are fine today <3
I found a bug here leads to gimme the IP/User-Agent of the user without his interaction, Just by viewing my post in the interaction section.
I have changed my post image url. Let me show how ..

## Steps to reproduce:
1. Click on the 3 bars on top and click “Driver Mode”, Then click on the 3 bars again and go inside “Freight” section. Now you are inside the “Freight” as “Passenger”.
2. Now go to “Create Request” and fill all the informations, but let’s focus on the upload functionality here
    
    ██████
    
3. Now we see a request of ```/api/image/upload``` !! the function here is uploading the photos first, then use the link for the uploaded image as parameter in the final post request.
4. Now we gonna ( turn on interception ), and click “Order Freight”. the request of ```/api/order/create``` we gonna see the images' urls, edit them with burp collaborator or [webhook.site](http://webhook.site) 
    
    ███
    
    ██████
    
5. Now click “Order Freight”, Here we go!
6. Now we switch from the 3 bars on top to “Driver mode”, Then open the “Freight” section again!
7. Now we see our post there!
    
    ██████████
    
8. and everyone would see my post or get inside my post or submit an offer for me, the collaborator would get executed on the user. The link is gonna get opened in the background. So now i have his IP address !!
    
    ███████

## Impact

* Users’ IPs would get leaked.
* This can lean to suspicious activities.
* Attacker can detect users’ current location from IP, from sites like: [https://whatismyipaddress.com/ip-lookup](https://whatismyipaddress.com/ip-lookup)
* Attack can download files on the android device of the user. With submitting a link for 1 click download, It’s gonna get opened in the background from the user’s side and the file gonna get downloaded. So attacker can use malicious files later.
* Attack can make money from that by submitting earning urls to the users, He’s getting money from the users! this is threating InDriver reputation.
* Attacker can execute php codes from files on the user’s side.

## Attachments
No attachments
