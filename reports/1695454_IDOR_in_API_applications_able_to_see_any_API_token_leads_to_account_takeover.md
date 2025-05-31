# IDOR in API applications (able to see any API token, leads to account takeover)

## Report Details
- **Report ID**: 1695454
- **URL**: https://hackerone.com/reports/1695454
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-09-08T16:11:11.001Z
- **Disclosed**: 2022-11-01T22:46:58.148Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi,

@ehtis, thank you for the test account. Here is a critical report. :)
On Pressable, we can create API applications at https://my.pressable.com/api/applications, and we can access many things using the API token via following the [API docs](https://my.pressable.com/documentation/api/v1)

I created an API application and tried to update it, I saw this request :

████████

As you can see there is an `application[id]` parameter that contains the application ID. I changed it to my second account's application ID and that API app moved to my account. So, there is an IDOR but it doesn't have a great impact because it just removes the API application from the victim's account.

So I tried to escalate its impact and I noticed if we remove all parameters except `application[id]` and `authenticity_token`, then send the request, the endpoint gives an error with `Name must be provided` and prints the given application ID's page. And, that page contains `Client ID` and `Client Secret`!

With this information, the attacker can make many actions on the victim's account. (https://my.pressable.com/documentation/api/v1)

## Steps To Reproduce:

  1. Go to https://my.pressable.com/api/applications and create an API app
  1. Click on the application and turn on your proxy program 
  1. Click `Update` and you will send a POST request to `/api/applications`
  1. In this request, change the `application%5Bid%5D` parameter's value to the target app ID, **then remove all parameters except `application%5Bid%5D` and `authenticity_token`**
  1. The page will give an error and you will see the victim app's page which contains `Client ID` and `Client Secret`
  1. Now, you can use these API credentials on the Pressable API.

Notes:
- API application IDs are sequential, so the attacker doesn't have to guess the IDs, s/he can access all applications
- The impact is critical because we can access many things via the API, that includes the "collaborator" endpoint https://my.pressable.com/documentation/api/v1#collaborator-bulk-create

## Impact

The attacker can access all API credentials using this vulnerability, and that leads to account takeover (via adding collaborator etc.)

Regards,
Bugra

## Attachments
No attachments
