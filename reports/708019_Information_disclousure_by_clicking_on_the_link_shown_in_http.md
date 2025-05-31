# Information disclousure by clicking on the link shown in http://████████/

## Report Details
- **Report ID**: 708019
- **URL**: https://hackerone.com/reports/708019
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-04T22:46:23.104Z
- **Disclosed**: 2019-12-02T20:02:16.883Z

## Reporter
- **Username**: pirateducky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

Looking at some subdomains using `aquatone` I noticed ` http://█████/` I clicked it and then started navigating the page, if I go to this link: `https://█████████/██████████wireframes/admin/round12/tsp_0-awarded.html` it is completely valid and shows some information that I'm unsure it should be online, it also shows me logged in as a user `Pat` and `Janelle`

## Impact

Information disclosure

## Step-by-step Reproduction Instructions

1. Navigate to ` http://████/`
2. Click `Main Index Page` 
3. Click ` Office & TSP` or use this link `https://███████/██████index-admin.html#` 

## Suggested Mitigation/Remediation Actions

If this is sensitive data - it should be restricted to only people who need to access it no the whole internet, there are certain action where it prompts for a password.

Thanks - 

If this is somehow *supposed* to be up I would like to self-close as to not affect my current profile

## Impact

Information disclosure, possibly a dev environment left open but unsure.

## Attachments
No attachments
