# [www.███] Reflected Cross-Site Scripting

## Report Details
- **Report ID**: 1184644
- **URL**: https://hackerone.com/reports/1184644
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-05T11:09:59.583Z
- **Disclosed**: 2021-06-30T20:42:52.577Z

## Reporter
- **Username**: celesian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Good morning, there's a reflected cross-site scripting vulnerability on https://www.██████████/█████
There was some difficult in making a payload for this vulnerability, mainly due to the WAF blocking some vectors; But exploitation is still possible.
Here's a proof of concept showing an alert popup.
https://www.████/███████?██████=-20a")});a=alert;a(1);//
## References

## Impact

A reflected cross-site scripting vulnerability can allow common client-side attacks.

## System Host(s)
www.██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Open the following URL: https://www.███/█████?█████=-20a")});a=alert;a(1);//
2. An alert box should pop-up, indicating the presence of the vulnerability.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
