# "Secure View" aka "Hide Download" can be bypassed easily

## Report Details
- **Report ID**: 788257
- **URL**: https://hackerone.com/reports/788257
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-03T13:18:19.732Z
- **Disclosed**: 2020-04-10T09:12:36.773Z

## Reporter
- **Username**: at5djl3pwjmunyutnoatp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The mid-2019 announced feature "Secure view" (https://nextcloud.com/blog/secure-view-prevent-your-shared-files-from-getting-downloaded/) allows for hiding the Download button on public shares.
Even though the announcement admits that there are always workarounds out there to get hands on the file anyway, the workaround for this one is way too simple: Just add **/download** to the URL (like you used to for every public share) and your browser starts downloading unhesitently.

For the sharee, the checkbox "Hide Download" is therefore very deceptive, since they very likely weigh themselves in false safety.

## Impact

Download a copy of a file or folder that's not supposed to be downloaded whatsoever

## Attachments
No attachments
