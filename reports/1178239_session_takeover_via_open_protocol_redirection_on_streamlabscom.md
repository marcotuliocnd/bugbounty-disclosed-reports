# session takeover via open protocol redirection on streamlabs.com

## Report Details
- **Report ID**: 1178239
- **URL**: https://hackerone.com/reports/1178239
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-28T10:17:48.540Z
- **Disclosed**: 2021-09-01T15:49:43.285Z

## Reporter
- **Username**: f_m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
## Summary:
Hi Logitech team, on streamlabs.com the endpoint: `streamlabs.com/global/identity?popup=1&r=protocol://merch.streamlabs.com` redirect any authenticated user to a arbitrary protocol, and it merge the redirect link with an access_token.

{F1281409}

this means that if a malicious app that handle the protocol is installed on the device the access token will be steal by this app and consequently a session takeover is possible on multiple streamlabs domain 

## Steps To Reproduce:


  1. once authenticated on streamlabs.com go to: streamlabs.com/global/identity?popup=1&r=test://merch.streamlabs.com and intercept the request in burp.
  2. grab the redirection link in the response(as a malicious app can do, especially on mobile systems), change the protocol to https and open it in a private browser window
  3. finally in the private browser window go to: https://merch.streamlabs.com/ or https://streamlabs.com/<your_store_name> or https://streamlabs.com/my-portal?origin=cs

in every case you will be logged in as the victim

{F1281408}

{F1281407}

##possible fix

implement a protocol check on the redirection in this endpoint

## Supporting Material/References:

i attached 3 images

## Impact

session takeover by  malicious apps(on mobile systems, it's more common)

## Attachments
- 2.png
- 1.png
- redir.png
