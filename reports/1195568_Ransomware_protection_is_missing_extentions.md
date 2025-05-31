# Ransomware protection is missing extentions

## Report Details
- **Report ID**: 1195568
- **URL**: https://hackerone.com/reports/1195568
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-13T12:26:38.583Z
- **Disclosed**: 2021-06-16T08:42:24.626Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So again I'm not sure if this is in scope. However you do advertise this on your enterprise pages. So I assume so.

In any case. It seems your `ransomeware_protection` app is missing some common extentions.
See for example https://avepointcdn.azureedge.net/assets/webhelp/compliance_guardian_installation_and_administration/index.htm#!Documents/ransomwareencryptedfileextensionlist.htm

As one example the 'pec' extention is not on your list.

## Impact

It seems your ransomware list was last updated 6 months ago.
There have been several ransom wares since.

However since you claim things like 'Best Ransomware protection in the industry' I would expect a lot more regular updates etc.

Long story short. This might deep your users safe while in reality this app is not really maintained and outdated.

## Attachments
No attachments
