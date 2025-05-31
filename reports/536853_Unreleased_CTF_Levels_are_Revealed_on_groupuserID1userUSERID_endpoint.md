# Unreleased CTF Levels are Revealed on /group/user/ID1?user=USERID endpoint

## Report Details
- **Report ID**: 536853
- **URL**: https://hackerone.com/reports/536853
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-12T17:21:55.416Z
- **Disclosed**: 2019-04-23T00:31:38.116Z

## Reporter
- **Username**: spaceraccoon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
At this moment, the two new upcoming CTF levels for https://ctf.hacker101.com/ctf have not been revealed. However, an IDOR at the https://ctf.hacker101.com/group/user/ID1?user=USERID endpoint reveals them (see attached screenshot)

**Description:**

### Steps To Reproduce

1. Create a group.
2. At the group index page (https://ctf.hacker101.com/group/groupIndex/GROUPID), click on the "details" button for yourself.
3. At the bottom, you should see the unreleased CTF levels.

### Optional: Supporting Material/References (Screenshots)

 * Attached screenshot with unreleased CTF at bottom

## Impact

Low level, but the user could get ahead of others by knowing upcoming levels, especially if there are prizes for being the first to complete them. Plus it reveals an interesting IDOR endpoint linked to the database.

## Attachments
No attachments
