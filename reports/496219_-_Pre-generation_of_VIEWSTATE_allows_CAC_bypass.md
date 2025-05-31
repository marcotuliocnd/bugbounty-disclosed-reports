# █████ - Pre-generation of VIEWSTATE allows CAC bypass

## Report Details
- **Report ID**: 496219
- **URL**: https://hackerone.com/reports/496219
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-02-14T18:30:55.941Z
- **Disclosed**: 2020-05-11T16:44:53.459Z

## Reporter
- **Username**: cablej_dds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

As of today, ███ is back online (https://███████).

█████████ allows users to check a box labeled `Require CAC for Pick-up`. This option requires users to present their CAC in order to download files. As explained by ███:

> Choosing this option, however, does add a significant degree of assurance that the recipient is in fact who they claim to be by verifying their identity via the CAC.

However, this security control can be bypassed, allowing downloading files without CAC authentication.

(Note that a CAC bypass was reported in #429000. Since then, ████████ has deployed a patch for that report, although a different bypass is possible.)

**Description:**

The `pickupfiles.aspx` page is where recipients of both non-CAC and CAC-enforced files visit to retrieve files. If the file is CAC enforced, the user is redirected to `CACPickup.aspx`. If not, the user must present their password in order to download the file.

For requests that are not CAC enforced, the server generates a MAC enabled `VIEWSTATE` parameter containing the package ID. This package ID in the viewstate is then checked against the package ID in the request to ensure that the user is downloading the correct file. As the viewstate is MAC enabled, it is not possible to modify the parameter without the server throwing an error.

The challenge lies in obtaining a valid viewstate for a CAC-enabled file. The server does not return a viewstate for CAC files, instead immediately redirecting to the CAC pickup page. However, this can be bypassed by pre-generating a viewstate for possible future request IDS (these are incremental). Then, when an attacker wishes to bypass CAC authentication, they can simply lookup the pre-generated viewstate and make a valid request to download the file.

## Impact

This allows bypass of CAC authentication for picking up files, a significant security control on ███████.

## Step-by-step Reproduction Instructions

1. Send a test file on https://█████████ to see the most recent package ID.
2. Using a tool such as Burp Intruder, enumerate package IDs in the request to https://████████/safe/pickupfiles.aspx?id=package_id, beginning at the most recent package ID. A large number of viewstates can be computed in advance. For testing, I computed a couple hundred.
3. As a normal user, send a file transfer to yourself, enforcing the CAC required option.
4. Visiting the `pickupfiles.aspx` link in the file transfer email, observe that CAC authentication is enforced.
5. Look up the package ID in your table of pre-generated requests. Make a request with the associated viewstate and validation parameter (e.g. in Burp Suite, right click -> show response in browser) and enter the sent password.
6. Observe that the validation of the viewstate parameter passes, and you may now download the file.

## Suggested Mitigation/Remediation Actions

Prevent users from downloading files from `pickupfiles.aspx` when the file is CAC-enabled.

## Impact

.

## Attachments
No attachments
