# Exposure of Private Personal Information to an Unauthorized Actor - PII  and soldier data (mos, schools, and speciality training)

## Report Details
- **Report ID**: 1556950
- **URL**: https://hackerone.com/reports/1556950
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-05-03T01:51:43.148Z
- **Disclosed**: 2025-01-24T14:49:36.727Z

## Reporter
- **Username**: hxhbrofessor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

Authenticated users on `https://█████████/SelfService/home/selfservice` can view other ████████'s data by following the page site for `My ███ Data` and start manipulating URL requests to view the following tabs: 
* Personnel
* Active Duty Tours
* ADOS
* Assignments
* ATRRS
* Data Discrepancies
* DJMS-RC Pay File Records
* DJMS-RC Pay Voucher
* Drill Attendance
* Education/Training
* Gains/Losses
* GI Bill Programs

Tester primarily focused on Personnel, ATRRS, and Education/Training tabs. 

## References

* CWE-359: Exposure of Private Personal Information to an Unauthorized Actor
* CWE-200 - Information Disclosure
* CWE-284 - Improper Access Control

## Contributers

- badlifeguard
- theonetruepengu

## Impact

The information displayed in Personnel, ATRRS, and Education/Training tabs shows a soldier's Last 4 of an SSN, Home of Record, MOS (Job title), and schools. Due to heightened tensions in today's GEO-Political climate, the availability of this information can be dangerous and potentially put a soldier's life at risk: scenario, insider threat working with an adversarial country to retrieve data.

## System Host(s)
████████, ██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* Authenticate to https://█████████/SelfService/home/selfservice with burpsuite
* Turn Intercept off
* Go to the bottome of the page and click on `My █████████ Data`
* On Burp, click proxy
** HTTP History
** Scroll to the last GET request with message 200
** URL should be `https://█████████/SelfService/Home/dynamicdata/section/██████████/██████████%20TPU/61/124948002`
** Right click over the message and send to `Intruder`
* Intruder Set up
** Clear all variables in Postions Tab
** in the get request highlight the `2` in `GET /SelfService/Home/dynamicdata/section/███████/████%20TPU/61/124948002` and on the right hand side of Intruder click `add variable`
** Payload Tab 
*** Payload Set > Payload Type > select numbers
*** Payload Options [Numbers] > From: 1 > To: 9 > Step: 1
** Options Tab
*** Grep Exact > add > refetch response > in the search box: search `Primary MOS` this will display a succesful record found.

Additional URLs  to manipulate utilizing the same steps above are:

```bash
Personnel
https://█████/SelfService/Home/dynamicdata/section/██████/███████%20TPU/61/124948002

ATTRS
https://██████████/SelfService/Home/dynamicdata/section/█████████/█████████%20TPU/444/124948002

Education/Training
https://████████/SelfService/Home/dynamicdata/section/█████/████%20TPU/2001/124948002

```

## Suggested Mitigation/Remediation Actions
Correct permissions on access to these URLs. Authenticated users should be checked against their own ID and data.



## Attachments
No attachments
