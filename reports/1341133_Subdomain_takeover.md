# Subdomain takeover [​████████]

## Report Details
- **Report ID**: 1341133
- **URL**: https://hackerone.com/reports/1341133
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-09-16T07:36:39.522Z
- **Disclosed**: 2021-10-13T22:17:30.087Z

## Reporter
- **Username**: fdeleite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
The subdomain `███████` was pointing to an Azure Cloud App domain (araz-sp.centralus.cloudapp.azure.com), but that endpoint was not registered.

## Impact

It's extremely vulnerable to attacks as a malicious user could create any web page with any content and host it on the vulnerable domain. This would allow them to post malicious content which would be mistaken for a valid site. 

They could perform several attacks like:
 - Cookie Stealing
 - Phishing campaigns. 
 - Bypass Content-Security Policies and CORS.

 
## Recommendations for fix

* Remove the affected DNS record if not used 
 

### Supporting Material/References:

 - https://0xpatrik.com/subdomain-takeover/
 - https://hackerone.com/reports/661751

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Just go to 

http://████████ 

You will see a blank page, but checking the source code you will see proof of the take over. 

```
<html>  
<!-- poc by deleite --> 
 </html>
```

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
