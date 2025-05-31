# IDOR in locid parameter allowing to view others accounts Profile Locations 

## Report Details
- **Report ID**: 966949
- **URL**: https://hackerone.com/reports/966949
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-25T19:14:49.772Z
- **Disclosed**: 2020-09-02T19:26:35.197Z

## Reporter
- **Username**: cocoh__23
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
The application transmits in many occasions the **locid** parameter via URL, which means that this parameter may be being logged in plan text in the Apache server access.log, if not in others also. The fact that this happens, makes this parameter vulnerable not only to be read from this log file, but also be seen in the screen of any persons computer (Image. 1). 
I have identified that if any user gets or can reach the value of **locid** (for example via the scenarios above mentioned), he can use this value, to access others accounts profile locations. The fact why this happens is that there is not any server side control in place, which validates that the locations which is being requested from user A, is indeed from user B.  Here we see that if well the value of locid is a random hash, this security by obscurity does not provide any additional security, if the server is not controlling who access which information, and if the value of locid can be leaked via different vectors.

In order to validate the both things I mention here, the following steps are:

1- Login to https://www.yelp.com/
2- Go to https://www.yelp.com/profile_location
3- Click the Edit button and intercept the request that is made in Burp (you will see its a GET /profile_location/add_or_edit?nonce=<nonce>&locid=<locid>)
4- Replace the value of **locid** with any of these valid locids from my account (**wPhD_XkXv2z4Njqekn-sfg**,**yqLLfgos2xWB-Y9miJ8YcQ**,**pC5mbrTyFbCEaMHt4S4hqg**,**ZpA_GvjxD-06V_ElZfK7Uw**)
5- You will see my profile locations.

## Impact

This attack can be used to disclose personal information of Yelp users, attempting against the confidentiality of the application. If well this is low as it presents a pre-condicion which is not hard but also not easy, this should not be the only preventive measure, as this is considered security by obscurity, as you are trusting that because a hash is hard to crack, no one will be able to guess it, but as mentioned in the descripction, bruteforcing many times is the last resource as there are many other options. Furthermore, the fact that tue locid is being transfered in the URL, which means this value is possibly being logged, internal Yelp users could even take advantage of a vulnerability like this. I know it is not the case, but it does not provide confidence to the users. 
Moreover, the hash can be bruteforced as yelp does not have any preventive measures against it (Image2), which means that the pre-condition is even easier to achieve.

## Attachments
- Image_1.png
- Image_2.png
