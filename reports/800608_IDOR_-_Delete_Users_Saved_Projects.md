# IDOR - Delete Users Saved Projects

## Report Details
- **Report ID**: 800608
- **URL**: https://hackerone.com/reports/800608
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-20T12:48:33.555Z
- **Disclosed**: 2022-03-18T19:00:20.869Z

## Reporter
- **Username**: ahmd_halabi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Target Url**
https://█████/██████████/█████████={Target_id}

**Summary:**
Hello, I found an IDOR bug in deleting users saved projects. Through changing the search id in the above url in a GET request, you can delete saved projects for any users.

## Step-by-step Reproduction Instructions

1. Navigate to your account -> Saved Searches.
2. Copy the url of the delete request `https://████/█████/████████={search_id}`
3. Replace your search id with the target victim search id and send the request. The target saved search will be deleted from the victim
To be more clear I uploaded this video, please watch it.
{}

## Suggested Mitigation/Remediation Actions
Check the user that is deleting the saved searches if he is legitimate and the real owner of that search or not.

## Impact

This would lead the attacker to delete all users saved searches through bruteforcing their ids. And since the id are incremented in an easy sequence, attacker can do this attack very fast.

## Attachments
No attachments
