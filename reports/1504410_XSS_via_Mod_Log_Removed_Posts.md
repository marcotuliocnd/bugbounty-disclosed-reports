# XSS via Mod Log Removed Posts

## Report Details
- **Report ID**: 1504410
- **URL**: https://hackerone.com/reports/1504410
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-03-09T00:56:21.837Z
- **Disclosed**: 2022-03-10T23:18:17.088Z

## Reporter
- **Username**: ahacker1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
I have discovered an XSS vulnerability regarding the mod notes feature. Specifically, the XSS payload executes when the victim removes a post in a subreddit and opens up the mod notes of the attacker.

## Steps To Reproduce:

1. The attacker creates a new post with the title containing the XSS payload.
2. The victim (mods of the subreddit) then must remove your post.
3. The payload executes when a victim (subreddit mod) opens up your mod notes. Sometimes, the mod notes are displayed when the victim hovers on your profile (this is true when a recent mod action has been taken on the user). 

## Supporting Material/References:

█████
█████

## Impact

Impact Below:

## Attachments
No attachments
