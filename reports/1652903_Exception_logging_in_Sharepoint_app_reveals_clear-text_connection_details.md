# Exception logging in Sharepoint app reveals clear-text connection details

## Report Details
- **Report ID**: 1652903
- **URL**: https://hackerone.com/reports/1652903
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-28T14:40:07.876Z
- **Disclosed**: 2022-11-26T12:46:33.424Z

## Reporter
- **Username**: kichernde_erbse
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
On Exceptions thrown in the context of the SharePoint app, connection credentials may be written to the Nextcloud log in clear text.

## Steps To Reproduce:

Attempt to configure a sharepoint mount in an erroneous way.

## Supporting Material/References:

  * was files publically: https://github.com/nextcloud/sharepoint/issues/141

## Impact

When an attacker gets hold of the nextcloud log, they may gain knowledge of credentials to connect to a SharePoint service.

## Attachments
No attachments
