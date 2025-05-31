# Public google drive link Exposes Military Orders Containing PII (Name, SSN etc..) and Operational Details

## Report Details
- **Report ID**: 2926447
- **URL**: https://hackerone.com/reports/2926447
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-01-07T22:44:07.557Z
- **Disclosed**: 2025-01-24T14:50:26.425Z

## Reporter
- **Username**: entropydrifter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
I found google drive link `https://drive.google.com/drive/folders/█████████`  at `https://████████.aspx?Mode=ReadOnly&Id=90dd0d3b-0ed1-e76b-128f-11ebc799ba55` contains pdfs at '/████ Internal/Orders' that discloses the following PII:

Full Name: ███████
Social Security Number (SSN): ███████
Home Address: ████, ██████
Marital Status: Married, 3 dependents (M03 in January 2021 orders; S00 in earlier orders)
Security Clearance Level: ███

## How to reproduce 

1. Navigate to `https://██████.aspx?Mode=ReadOnly&Id=90dd0d3b-0ed1-e76b-128f-11ebc799ba55`.
2. Below the page you will find `https://drive.google.com/drive/folders/█████████`.
3. Go to `https://drive.google.com/drive/folders/███████`.
4. Open folder named `███████ Internal`.
5.Navigate to folder named `Orders`.
6. You will find the pdfs that discloses PII data as shown below in screen shots.

██████████

██████

## Impact

1. Privacy Violation: Exposes PII of personnel, violating privacy laws such as the U.S. Privacy Act of 1974.
2. Identity Theft and Fraud: Information like SSNs and home addresses can be used for malicious purposes.

## System Host(s)
www.yellowribbon.mil

## Affected Product(s) and Version(s)
https://█████████.aspx?Mode=ReadOnly&Id=90dd0d3b-0ed1-e76b-128f-11ebc799ba55

## CVE Numbers


## Steps to Reproduce
1. Navigate to `https://██████.aspx?Mode=ReadOnly&Id=90dd0d3b-0ed1-e76b-128f-11ebc799ba55`.
2. Below the page you will find `https://drive.google.com/drive/folders/█████`.
3. Go to `https://drive.google.com/drive/folders/███`.
4. Open folder named `███ Internal`.
5.Navigate to folder named `Orders`.
6. You will find the pdfs that discloses PII data as shown below in screen shots.

█████

██████

## Suggested Mitigation/Remediation Actions
Remove the folder or make it private at least



## Attachments
No attachments
