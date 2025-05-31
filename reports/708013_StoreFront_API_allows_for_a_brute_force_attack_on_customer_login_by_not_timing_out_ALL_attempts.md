# StoreFront API allows for a brute force attack on customer login by not timing out ALL attempts

## Report Details
- **Report ID**: 708013
- **URL**: https://hackerone.com/reports/708013
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-04T22:13:38.873Z
- **Disclosed**: 2019-10-07T20:12:54.095Z

## Reporter
- **Username**: clew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
It seems that the service used for login purposes could be brute forced. the system fails when the password is incorrect, after some unsuccessful attempts the following message is shown:

 
{"data":{"customerAccessTokenCreate":null},"errors":[{"message":"Login attempt limit exceeded. Please try again later.","locations":[{"line":1,"column":10}],"path":["customerAccessTokenCreate"]}]}

 
However, it still possible to continue brute forcing and if you try with the real password it will work again. So in our case, we have been able to perform brute force attack.  

We feel Shopify should enforce the "limit exceeded" error for BOTH valid and invalid passwords.

## Impact

If the brute force attack succeeds, the attacker will then gain access to that user's shopify account, including contact information and order history.

## Attachments
- shopify_brute_force.png
