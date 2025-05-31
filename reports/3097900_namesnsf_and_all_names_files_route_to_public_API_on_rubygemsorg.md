# `/names.nsf` and all `/names*` files route to public API on rubygems.org

## Report Details
- **Report ID**: 3097900
- **URL**: https://hackerone.com/reports/3097900
- **State**: Closed
- **Severity**: none
- **Submitted**: 2025-04-16T21:57:11.366Z
- **Disclosed**: 2025-05-03T16:00:09.728Z

## Reporter
- **Username**: jagat-singh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
During the security assessment of the application hosted at https://rubygems.org/names.nsf, it was discovered that a sensitive file "names.nsf", is publicly accessible without proper authentication and it is supposed to be protected by authentication mechanisms to ensure that unauthorized users do not gain access to sensitive data stored within it.

Steps to Reproduce:

1.  Open the following URL in a browser:
     https://rubygems.org/names.nsf
 
2.   No authentication or authorization is required to access the file. The file is directly accessible to anyone with the URL.
3.The content of the file contains confidential data look at Attachment file and screenshot.

Evidence:
Screenshot and file Attached with attachment

Mitigation/Remediation Steps:
1. Authentication & Authorization:
 Ensure that access to the .nsf file is properly authenticated. Only authorized users should be able to access this file.

2. Restrict Direct Access:
Configure the web server to prevent unauthorized access to sensitive files such as .nsf. Use proper access control lists (ACLs) or configurations like .htaccess (if using Apache) to block direct access.


Recommendation:
It is recommended to immediately implement proper access control on the .nsf file to restrict public access. The organization should also consider using encryption and strong authentication mechanisms to secure all sensitive files within the application

## Impact

1.  Data Breach: Unauthorized users can view sensitive information, including personal and business-related data.
  2.  Privacy Violation: Exposure of personal and confidential user data could violate privacy regulations (e.g., GDPR, HIPAA).
  3.  Potential for Exploitation: If the file contains sensitive business data, attackers may use this information for phishing, social engineering, or further exploitation.
  4.  Loss of Trust: This exposure could harm the reputation of the organization, especially if customers' private information is accessed or compromised.

## Attachments
- screenshot.png
- names.nsf.txt
