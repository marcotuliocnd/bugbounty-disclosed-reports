# Found multiple SAP NetWeaver vulnerable services

## Report Details
- **Report ID**: 1103212
- **URL**: https://hackerone.com/reports/1103212
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-14T14:49:11.664Z
- **Disclosed**: 2021-02-16T13:06:43.438Z

## Reporter
- **Username**: ganofins
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
# Summary:
Hello Team,
I found two (**redapi.acronis.com** and **redapi2.acronis.com**) sap Netweaver vulnerable services. They do not perform an authentication check which allows an attacker without prior authentication to execute configuration tasks to perform critical actions against the SAP Java system, including the ability to create an administrative user, and therefore compromising Confidentiality, Integrity, and Availability of the system, leading to Missing Authentication Check.

# Steps To Reproduce:
  1. Run the script {F1195428}
  2. You will see random user created

# POC:
Just for the POC, I have created a random user with creds
sapRpoc9049:Secure!PwD6751 (at redapi.acronis.com)
{F1195413}

# References:
https://github.com/chipik/SAP_RECON
https://nvd.nist.gov/vuln/detail/CVE-2020-6286
https://nvd.nist.gov/vuln/detail/CVE-2020-6287
https://launchpad.support.sap.com/#/notes/2934135
https://launchpad.support.sap.com/#/notes/2939665

**Please lemme know if you need any additional information reagarding this**

## Impact

# Impact:
This version of SAP netweaver does not perform an authentication check which allows an attacker without prior authentication to execute configuration tasks to perform critical actions against the SAP Java system, including the ability to create an administrative user, and therefore compromising Confidentiality, Integrity, and Availability of the system, leading to Missing Authentication Check.

## Attachments
- acronis_sap1.png
- acronis_sap.py
