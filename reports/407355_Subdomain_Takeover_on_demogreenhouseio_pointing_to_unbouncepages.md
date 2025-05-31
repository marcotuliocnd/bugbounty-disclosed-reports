# Subdomain Takeover on demo.greenhouse.io pointing to unbouncepages

## Report Details
- **Report ID**: 407355
- **URL**: https://hackerone.com/reports/407355
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-08T00:08:11.421Z
- **Disclosed**: 2020-03-05T11:26:29.424Z

## Reporter
- **Username**: ninadmathpati
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: greenhouse

## Vulnerability Information
Actuall this report is same as of this one:- https://hackerone.com/reports/38007  


Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.

Here there is a greenhouse domain  (demo.greenhouse.io) which is pointing towards unbounce pages so  this domain can be taken over can can be used to do any type of attacks mostly i can make a fake login page on your behalf and spoof your users, this is a critical vulnerability and needs to be fixed .

Vulnerable url : demo.greenhouse.io

PoC
Snapshot of the vulnerable page(actually for taking over from unbounce i need to take a paid subscription hich is of higher cost neraly 150-200$ i cannot afford that so as a poc i m showing you a vulnerable page hoping this should work )

cname: unbouncepages.com
Name: demo.greenhouse.io
Type: CNAME
Class: IN

## Impact

Impact
Risk
fake website
malicious code injection
users tricking
company impersonation
This issue can have really huge impact on the companies reputation someone could post malicious content on the compromised site and then your users will think it's official but it's not.

Remediation
Remove the cname entry or claim the subdomain demo.greenhouse.io on unbounce.com

See also
https://github.com/EdOverflow/can-i-take-over-xyz#unbounce
https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/
https://0xpatrik.com/subdomain-takeover/
https://medium.com/@ajdumanhug/subdomain-takeover-through-external-services-f0f7ee2b93bd
http://yassineaboukir.com/blog/neglected-dns-records-exploited-to-takeover-subdomains/



Best regards,
Hacker2202

## Attachments
- Screenshot_(476).png
