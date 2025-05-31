# The dashboard is exposed in https://███

## Report Details
- **Report ID**: 1566758
- **URL**: https://hackerone.com/reports/1566758
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-05-12T12:20:50.786Z
- **Disclosed**: 2022-09-06T18:53:22.564Z

## Reporter
- **Username**: alitoni224
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
At first, hello, after searching in sub-domains, the dashboard was accessed by Google Dorking Which is supposed to be protected
https://█████████l/arsys/forms/arpcp/ARPC%3AWeb%3AHier%3ADashboard/Default+Admin+View/?F536871388=1&mode=Submit&cacheid=c66791da

## References
https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure

## Impact

CWE-200
https://cwe.mitre.org/data/definitions/200.html

## System Host(s)
█████████l

## Affected Product(s) and Version(s)
website

## CVE Numbers
CVE-2020-7130

## Steps to Reproduce
After searching in Google dorking on a file extension or endpoint jspDashboard found in the URL
https://████████l/arsys/forms/arpcp/ARPC%3AWeb%3AHier%3ADashboard/Default+Admin+View/?F536871388=1&mode=Submit&cacheid=c66791da 
██████

==Note==
 that it is leaked, you can log out and bypass it by typing anything in the ```username``` box

## Suggested Mitigation/Remediation Actions
Collect sensitive information on a local server and protect endpoints


---------------------------------------
With best regards and love
Toni...



## Attachments
No attachments
