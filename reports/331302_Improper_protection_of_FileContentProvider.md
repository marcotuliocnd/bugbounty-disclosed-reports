# Improper protection of FileContentProvider

## Report Details
- **Report ID**: 331302
- **URL**: https://hackerone.com/reports/331302
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-30T08:21:53.366Z
- **Disclosed**: 2020-03-01T14:05:16.781Z

## Reporter
- **Username**: mmmds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Some data in the FileContentProvider is protected against applications not related to NextCloud. The application checks if calling application package name contains "com.nextcloud.client" string. Every application with such substring in package name is allowed to fully access FileContentProvider.

com.owncloud.android.providers.FileContentProvider

``` java
    private boolean isCallerNotAllowed() {
        String callingPackage = this.mContext.getPackageManager().getNameForUid(Binder.getCallingUid());
        return callingPackage == null || !callingPackage.contains(this.mContext.getPackageName());
    }
```

## Impact

Malicious applications with "com.nextcloud.client" in their package names are able to access FileContentProvider without restrictions. For example they are able to read private keys to end-to-end encryption using URI: content://org.nextcloud/arbitrary_data

## Attachments
No attachments
