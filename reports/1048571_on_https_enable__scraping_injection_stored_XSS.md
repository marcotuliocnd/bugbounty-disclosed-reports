# ███ on https://████ enable ███ scraping, injection, stored XSS

## Report Details
- **Report ID**: 1048571
- **URL**: https://hackerone.com/reports/1048571
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-02T00:29:58.668Z
- **Disclosed**: 2021-05-11T20:25:05.873Z

## Reporter
- **Username**: skarsom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An open ████████ at the ████████ system enables quick and easy scraping of ███ without authentication nor authorization.

**Description:**
The █████ includes an open set of ██████endpoints at https://██████████. Any individual can execute requests on these endpoints without authorization nor authentication. These include the ability to view ████

Some of these endpoints are legitimately used in the ██████████ of the website, such as the one to ███████.

## Impact
An external, unauthorized, and unauthenticated attacker can scrape data of █████ by date on the ██████.

An external actor may also be able to perform injections against the database service through maliciously crafted attacks.

An external, unauthorized, and unauthenticated attacker can perform a stored XSS attack using on an ████████. 

## Step-by-step Reproduction Instructions

Data Extraction:
███████. Navigate to https://█████████.
████. Navigate to the "██████" ████ (https://████?████████████)
3. Enter the year ███████████████████████████████, the month █████████████, and the day █████████████, then press Invoke.
4. Success (█████████).
5. For further extraction, take one of the user IDs present in the JSON reply and paste it into the ███ ███████ (https://██████████?███████████).
6. For further extraction, take one of the profile IDs present in the JSON reply and paste it into the █████████ ██████ (also set "dbName" to "███") (https://█████████?███████). 

Stored XSS/Information Modification:
███. Navigate to the ███████ █████████ (https://█████████?███).
██████. Parameters: dbName = `██████████`, OUid = `█████████`, lngDesc = `████████`, modDesc = `███████`, wrkPLid = `███████`, clngPLid = `██████`, prfDate = `████████████/█████████/██████████████████████ ███████████████████:█████████████:███████████████████`, timeString = `Tue Dec ████████████ ██████████8:█████9:56 ███████████████████████████`, prfLink = `demofromskarsom`, CData = `<iframe onload="alert(██████)" style="display:none"></iframe>`, sessionID = `██████`
3. Click "Invoke".
4. Navigate to the following page, replacing `(GENSTRING)` with the integer that was returned from invoking the █████ request: `https://█████(GENSTRING)&B=███████&C=████████&D=demofromskarsom&view=true`
5. Success.

## Supporting Material
Navigate to████?A=███9█████98&B=██████&C=██████████&D=dodvdpdemo&view=true to see a stored XSS POC that I uploaded.
#███
#█████████
#████
#███████

## Suggested Mitigation/Remediation Actions
All endpoints unused by the frontend UI (based on a cursory search, this appears to be all but ███Plink) should be removed or guarded by authorization checks.

## Impact

Third-party actors can easily scrape language proficiency, testing, and student information through the ODA's debug UI and endpoints.

Third-party actors may also be able to perform injections against the database service through maliciously crafted strings within the INSERT and UPDATE ███s on the WS endpoints (did not attempt to prevent damage).

Third-party actors can further generate a page with a stored XSS attack within the "██████" of an inserted profile through█████.

## Attachments
No attachments
