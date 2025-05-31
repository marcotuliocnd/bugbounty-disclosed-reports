# Subdomain takeover of d02-1-ag.productioncontroller.starbucks.com

## Report Details
- **Report ID**: 661751
- **URL**: https://hackerone.com/reports/661751
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-27T08:21:18.351Z
- **Disclosed**: 2019-08-15T19:05:01.553Z

## Reporter
- **Username**: mindtrick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:**
 I was able to claim the subdomain: d02-1-ag.productioncontroller.starbucks.com using Azure Cloud Service

**Platform(s) Affected:**
Subdomain
Azure Cloud Service

## Steps To Reproduce:
1. Using dig, I was able to determine that the subdomain 'd02-1-ag.productioncontroller.starbucks.com'   was vulnerable to takeover.  The record showed status: NXDOMAIN and was pointing to the CNAME: 3edbac0a-5c43-428a-b451-a5eb268f888b.cloudapp.net.
2. Using this information, I was able to create a new Azure Cloud Service with the name '3edbac0a-5c43-428a-b451-a5eb268f888b'.  This would resolve to the CNAME record mentioned above.
3. I then crafted a website and uploaded it to the cloud service using this as a guide: https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-how-to-create-deploy-portal.
4. I was then able to view the uploaded site at http://d02-1-ag.productioncontroller.starbucks.com

## Supporting Material/References:
POC:
http://d02-1-ag.productioncontroller.starbucks.com/poc-2sKR4C.html


## How can the system be exploited with this bug?
See impact below.

## How did you come across this bug ?
Using enumeration, I was able to discover this domain and determined it was vulnerable by the DNS record data mentioned in the steps above.

## Recommendations for fix
To mitigate this issue you can:
* Remove the DNS record from the DNS zone if it is no longer needed.
* Claim the domain name in a permanent DNS record so it cannot be used elsewhere.

## Impact

This is extremely vulnerable to attacks as a malicious user could create any web page with any content and host it on the starbucks.com domain.  This would allow them to post malicious content which would be mistaken for a valid site.  They could steal cookies, bypass domain security, steal sensitive user data, etc.  Here is a nice write-up of the vulnerabilities:  https://0xpatrik.com/subdomain-takeover/

As mentioned in the write-up above the

## Attachments
No attachments
