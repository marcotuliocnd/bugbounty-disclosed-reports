# ████████ portal is open to enumeration once authenticated.  Session ID's appear static.  All PII available once a valid session ID is found.

## Report Details
- **Report ID**: 1150573
- **URL**: https://hackerone.com/reports/1150573
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-05T20:10:54.701Z
- **Disclosed**: 2021-04-20T19:33:36.076Z

## Reporter
- **Username**: gentlemenhacker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Once Authenticated to █████████ portal with valid credentials you can type in another members session id and you can see any service members data as if you were authenticated as them.

https://█████████

I did not see if there was a way to dump all session id's, but wouldn't be too surprised if it was vulnerable to this.

## References

Replacing that string above with valid session ID's let me see ██████ info

## Impact

All PII held in ██████████ portal exposed.  █████████.  
If website doesn't stop me, I could either dump the list of id's or utilize a tool to brute force a range.

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Step 1: Authenticate to █████████ portal with valid credentials. 
Step 2:  navigate straight to this page with a valid session id
https://████████
If you have a valid session id, you can see any service members data as if you were authenticated as them.

## Suggested Mitigation/Remediation Actions
random session ids.  better authorization to data.



## Attachments
No attachments
