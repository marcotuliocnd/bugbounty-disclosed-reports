# Global default settings page is accessible to non-administrators

## Report Details
- **Report ID**: 1563139
- **URL**: https://hackerone.com/reports/1563139
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-05-09T00:25:46.319Z
- **Disclosed**: 2022-05-09T22:25:46.442Z

## Reporter
- **Username**: dyls
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
If you go to /settings/, it correctly redirects to /settings/user/username/ and does not give you the option to change global default settings. However if you go straight to /settings/builtin/global/, any user can edit the global default settings. According to https://secure.phabricator.com/D16048, it's supposed to be an administrator panel.

mongoose

## Impact

At worst, you can disrupt a Phabricator installation and change the accessibility theme, language, disable everyone's notifications. But there aren't any very sensitive settings that you can modify.

## Attachments
No attachments
