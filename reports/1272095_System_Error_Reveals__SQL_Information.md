# System Error Reveals  SQL Information

## Report Details
- **Report ID**: 1272095
- **URL**: https://hackerone.com/reports/1272095
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-21T12:57:40.134Z
- **Disclosed**: 2021-09-09T19:59:23.377Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello,

While testing your program i came across an endpoint that is leaking sql errors and queries from on of your websites.

I use the following google dork to detect this:

site:████████ "sql error"

Endpoints leaking data:
https://www.██████/██████████
https://www.███████/███

Some of the errors found on https://www.███/█████:
SQLSTATE	  █████████
DATASOURCE	  ███
VENDORERRORCODE	  ███
SQL	   SELECT █████████, █████', '█████████, ██████, ████, ███████, ███████, ████████
(..)
██████████-████████: ██████" ████"
███
████
██████████
████
█████
(..)


Some of the errors found on https://www.███████/████:
SQLSTATE	  █████████
DATASOURCE	  █████
VENDORERRORCODE	  ███
SQL	   SELECT ██████████ ███████ ███████, ██████, ██████, █████, █████, ████████
(...)
█████████-███: ███████" █████"
██████
███████
████
█████
██████████
(...)

Best Regards
Miguel Santareno

## Impact

Attacker can use the error messages to gain further knowledge of the SQL system to launch future attacks.

## System Host(s)
www.███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Open the following endpoints https://www.██████████/█████ and https://www.█████████/███████ and you should be able to see the information above mentioned.

## Suggested Mitigation/Remediation Actions
Remove any mention of the SQL database calls in the stack trace error.



## Attachments
No attachments
