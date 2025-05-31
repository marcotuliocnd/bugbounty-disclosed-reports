# Unathorised access to admin endpoint on plus-website-staging5.shopifycloud.com

## Report Details
- **Report ID**: 1394982
- **URL**: https://hackerone.com/reports/1394982
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-09T00:38:01.921Z
- **Disclosed**: 2021-12-03T12:50:10.419Z

## Reporter
- **Username**: j0j0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
https://plus-website-staging5.shopifycloud.com/admin/ allows to access/modify and delete partners data.
While the environment seems to be staging, partner's/clients contact details look pretty real.

##Sorry:  
During the testing, I've created Test111 partner account, trying to escalate the issue, however can't find an option to delete it :| So far I  did receive some DNS interaction on my collaboration server, but I've decided to stop testing and ask first. Please let me know if I can play around and try escalating it to RCE or SQLi or something else (If it's matters to you)

## Shops Used to Test:
None

## Relevant Request IDs:
061890664b777d5f7e5cc84eefa5c8c5

## Steps To Reproduce:
Go to https://plus-website-staging5.shopifycloud.com/admin/ and check the administrative menu
█████████

Kind Regards,
j0j0

## Impact

Partners and customers data leakage, probably the issue can be escalated to something more impactful.

## Attachments
No attachments
