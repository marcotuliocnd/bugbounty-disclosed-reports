# Impersonation attack via Broken Link in Resellers Page

## Report Details
- **Report ID**: 266908
- **URL**: https://hackerone.com/reports/266908
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-08T05:45:55.821Z
- **Disclosed**: 2017-09-08T21:42:12.394Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
## Summary
A link on `https://about.gitlab.com/resellers/` was broken and could've allowed a user to impersonate a reseller and attack / scam your customers.

## Proof of Concept
1.) Visit https://about.gitlab.com/resellers/
2.) Hit `Ctrl+F` and find "intenso"
 {F219301}
3.) Now click the Facebook link and you'll see the Facebook page I've "hijacked"
(https://www.facebook.com/InTENSO.IT.Enterprise.Solutions)

This happened because this reseller either deleted their Facebook page or changed their username. Not much you could do about that, but I thought I'd report it because it could be used to attack / scam your customers.

## References
 This post by edoverflow => https://gist.github.com/EdOverflow/24e0bb929169eb948bb7f3d0a2d5528f


Sorry for the lower quality of this report, but decided to report it as it could actually be used to scam users.
Thanks,
Corben Douglas (@sxcurity)




## Attachments
- gitlab_hijack.png
