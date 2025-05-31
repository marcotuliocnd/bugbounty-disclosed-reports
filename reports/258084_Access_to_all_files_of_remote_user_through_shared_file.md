# Access to all files of remote user through shared file

## Report Details
- **Report ID**: 258084
- **URL**: https://hackerone.com/reports/258084
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-08T20:58:53.598Z
- **Disclosed**: 2020-03-01T14:10:12.955Z

## Reporter
- **Username**: xuesheng
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
### Steps to reproduce
1. User A shares a file "movie.mp4" with user B.
2. User B uses webdav to access files (e.g. foldersync or nautilus)
3. share is shown as regular file (using webdav).
4. Copy the file and paste it to the same folder (still using webdav).
5. A new folder will appear with the name "(1)movie.mp4". This folder contains all data of user A (which is quite scary). Folder structure looks like: files, files_trashbin, cache, etc. (all user related files).
6. I was able to reproduce this with different combination of users and shared files.

### Expected behaviour
Only the shared file should be copied.

### Actual behaviour
All files of remote user are copied.

### Server configuration

**Operating system**: Ubuntu 16.04.3 LTS

**Web server:** apache2 (2.4.18-2ubuntu3)

**Database:** mariadb (10.0.24-7)

**PHP version:** php7 (7.0+35ubuntu6)

**Nextcloud version:** 12.0.1

**Updated from an older Nextcloud/ownCloud or fresh install:** originally owncloud, upgradepath according to the official documentation to nextcloud (owncloud 9 to nextcloud 9 or 10, can't remember).

**Where did you install Nextcloud from:** Nextcloud package was downloaded from official webpage (nextcloud.com)

**Signing status:**
<details>
<summary>Signing status</summary>

```
No errors have been found.
```
</details>

**List of activated apps:**
<details>
<summary>App list</summary>

```
Enabled:
  - activity: 2.5.2
  - admin_audit: 1.2.0
  - bookmarks: 0.10.1
  - bruteforcesettings: 1.0.2
  - calendar: 1.5.3
  - comments: 1.2.0
  - contacts: 1.5.3
  - dav: 1.3.0
  - federatedfilesharing: 1.2.0
  - federation: 1.2.0
  - files: 1.7.2
  - files_accesscontrol: 1.2.4
  - files_automatedtagging: 1.2.2
  - files_external: 1.3.0
  - files_pdfviewer: 1.1.1
  - files_retention: 1.1.2
  - files_sharing: 1.4.0
  - files_texteditor: 2.4.1
  - files_trashbin: 1.2.0
  - files_versions: 1.5.0
  - files_videoplayer: 1.1.0
  - firstrunwizard: 2.1
  - gallery: 17.0.0
  - logreader: 2.0.0
  - lookup_server_connector: 1.0.0
  - mail: 0.6.4
  - nextcloud_announcements: 1.1
  - notifications: 2.0.0
  - oauth2: 1.0.5
  - password_policy: 1.2.2
  - previewgenerator: 1.0.6
  - provisioning_api: 1.2.0
  - serverinfo: 1.2.0
  - sharebymail: 1.2.0
  - spreed: 2.0.1
  - survey_client: 1.0.0
  - systemtags: 1.2.0
  - theming: 1.3.0
  - twofactor_backupcodes: 1.1.1
  - updatenotification: 1.2.0
  - workflowengine: 1.2.0
Disabled:
  - encryption
  - user_external
  - user_ldap
```
</details>

**Nextcloud configuration:**
<details>
<summary>Config report</summary>

```
{
    "system": {
        "instanceid": "***REMOVED SENSITIVE VALUE***",
        "passwordsalt": "***REMOVED SENSITIVE VALUE***",
        "trusted_domains": [
            "***REMOVED SENSITIVE VALUE***",
            "***REMOVED SENSITIVE VALUE***",
            "***REMOVED SENSITIVE VALUE***"
        ],
        "datadirectory": "***REMOVED SENSITIVE VALUE***",
        "dbtype": "mysql",
        "version": "12.0.1.5",
        "dbname": "owncloud",
        "dbhost": "localhost",
        "dbtableprefix": "oc_",
        "dbuser": "***REMOVED SENSITIVE VALUE***",
        "dbpassword": "***REMOVED SENSITIVE VALUE***",
        "installed": true,
        "forcessl": true,
        "mail_smtpmode": "smtp",
        "mail_smtpsecure": "ssl",
        "mail_from_address": "***REMOVED SENSITIVE VALUE***",
        "mail_domain": "***REMOVED SENSITIVE VALUE***",
        "mail_smtpauthtype": "LOGIN",
        "mail_smtpauth": true,
        "mail_smtphost": "***REMOVED SENSITIVE VALUE***",
        "mail_smtpport": "465",
        "mail_smtpname": "***REMOVED SENSITIVE VALUE***",
        "mail_smtppassword": "***REMOVED SENSITIVE VALUE***",
        "theme": "",
        "maintenance": false,
        "logtimezone": "Europe\/Berlin",
        "loglevel": 0,
        "log_authfailip": true,
        "overwrite.cli.url": "\/owncloud",
        "secret": "***REMOVED SENSITIVE VALUE***",
        "forceSSLforSubdomains": true,
        "trashbin_retention_obligation": "30, 180",
        "memcache.local": "\\OC\\Memcache\\APCu",
        "memcache.locking": "\\OC\\Memcache\\Redis",
        "redis": {
            "host": "\/var\/run\/redis\/redis.sock",
            "port": 0,
            "dbindex": 0,
            "password": "***REMOVED SENSITIVE VALUE***",
            "timeout": 1.5
        },
        "htaccess.RewriteBase": "\/owncloud"
    }
}
```
</details>

**Are you using external storage, if yes which one:** not applicable

**Are you using encryption:** no

**Are you using an external user-backend, if yes which one:** no

### Client configuration
**Browser:** Firefox 54.0

**Operating system:** Ubuntu 16.04.3 LTS

### Logs
#### Web server error log
<details>
<summary>Web server error log</summary>

```
No errors related to issue.
```
</details>

#### Nextcloud log (data/nextcloud.log)
<details>
<summary>Nextcloud log</summary>

```
No errors related to issue.
```
</details>

#### Browser log
<details>
<summary>Browser log</summary>

```
Not applicable.
```
</details>


## Attachments
No attachments
