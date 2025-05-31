# Phishing by Navigating Browser Tabs

## Report Details
- **Report ID**: 361054
- **URL**: https://hackerone.com/reports/361054
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-02T10:32:42.556Z
- **Disclosed**: 2018-06-04T11:52:22.418Z

## Reporter
- **Username**: 4w3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hi team,

I was create a PR on github https://github.com/liberapay/liberapay.com/pull/1127

### Details

Opened windows through normal hrefs with target="_blank" can modify window.opener.location and replace the parent webpage with something else, even on a different origin.

While this doesn't allow script execution, it does allow phishing attacks that silently replace the parent tab.

Hope you will not close it as `N/A` Thinking about resolve.Approve the PR.

Thanks,
@4w3

## Impact

If the links lack of rel="noopener noreferrer" attribute, third party site can change the URL of source tab using window.opener.location.assign and trick the user as if he is still in a trusted page and lead him to enter his secret information or credentials to this malicious copy.

## Attachments
No attachments
