# Pull Any Automated Record Brief

## Report Details
- **Report ID**: 1541740
- **URL**: https://hackerone.com/reports/1541740
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-04-14T23:40:36.606Z
- **Disclosed**: 2024-10-25T15:23:37.560Z

## Reporter
- **Username**: badlifeguard
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:** With some simple URL manipulation, an authenticated user is able to request other soldiers ARB/ORBs. 

## References
I am able to pull my own "Current Automated Record Brief", "Selection Board Record Brief", and all validated ones, then manipulate numbers in the request URL, and then pull any other valid number to pull a soldier. URL ID: "SRBHeaderID=#######"

## Impact

After pulling an ARB/ORB, someone would have access to view their last 4 SSN, Date of Birth, Place of birth, Clearance information, Mailing Address, and DODID. With most recent breaches of SSNs, one attacker would have enough information to verify and impersonate another soldier for malicious purposes.

## System Host(s)
█████, ████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Authenticate to https://████/SelfService/home/selfservice

Then you can test by clicking on your own "My Record Brief".

Enter developer mode in your chosen browser. 
First choose your "View Current Automated Record Brief"
In developer mode watch for "Network request" (Where 000000 will be your ID for your non-board record:  Index?SRBHeaderID=000000&isBoard=false&OT=0

You can manipulate the SRBHeaderID from 000001 to at least 4500000.

Similar to the other buttons, lead to the same results SRBHeaderID, Board, and OT change values.
Current Automated Record Brief
https://█████/SelfService/esrbss/PDF/Index?SRBHeaderID=000000&isBoard=false&OT=0
Current Selection Board Record Brief
https://█████████/SelfService/esrbss/PDF/Index?SRBHeaderID=000000&isBoard=true&OT=0
Validated Automated Record Brief
https://███████/SelfService/esrbss/PDF/Index?SRBHeaderID=0000000&isBoard=false&OT=2
Certified Selection Board Record Brief
https://█████/SelfService/esrbss/PDF/Index?SRBHeaderID=0000000&isBoard=true&OT=5

## Suggested Mitigation/Remediation Actions
Lock permissions on access to Record Brief files produced, generate the PDF from the backend, randomize/tokenize the URL to give one time URLs.



## Attachments
No attachments
