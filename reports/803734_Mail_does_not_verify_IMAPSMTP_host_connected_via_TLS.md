# Mail does not verify IMAP/SMTP host connected via TLS

## Report Details
- **Report ID**: 803734
- **URL**: https://hackerone.com/reports/803734
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-24T14:56:20.816Z
- **Disclosed**: 2020-06-03T08:13:31.148Z

## Reporter
- **Username**: christophwurst
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The Mail app should verify that the servers it connects to are listed in the certificate's CN. Otherwise the connection should be aborted.

Originally reported at https://github.com/nextcloud/mail/issues/308

## Impact

The app could be forced into connecting to an insecure server.

## Attachments
No attachments
