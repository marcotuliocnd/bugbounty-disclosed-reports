# Subdomain Takeover due to unclaimed domain pointing to Acquia Cloud

## Report Details
- **Report ID**: 874482
- **URL**: https://hackerone.com/reports/874482
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-14T21:39:08.263Z
- **Disclosed**: 2021-01-14T14:00:28.738Z

## Reporter
- **Username**: kumarp16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: insulet_corporation

## Vulnerability Information
ssue Details

The consultant identified that subdomain http:// or https://qa.myomnipod.com 

Web Site Not Found

Sorry, we could not find any content for this web address. Please check the URL.

If you are an Acquia Cloud customer and expect to see your site at this address, you'll need to add this domain name to your site via the Acquia Network management console.

Error Is displayed.

How did you come across this bug ?

Using enumeration, I was able to discover this domain and determined it

NOTE: The hostname was not claimed by me also because i need to pay certain amount to host a website.

## Impact

Sub-domain take over attacks can happen when a company creates a dns entry that points to a third party service, however forgets about the third party application leaving it vulnerable to be hijacked by another party. Hackers can claim subdomains with the help of external services. This attack is practically non-traceable.

## Attachments
- Screenshot_2020-05-15_Web_Site_Not_Found.png
