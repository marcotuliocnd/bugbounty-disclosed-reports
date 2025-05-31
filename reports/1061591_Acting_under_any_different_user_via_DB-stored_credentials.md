# Acting under any different user via DB-stored credentials

## Report Details
- **Report ID**: 1061591
- **URL**: https://hackerone.com/reports/1061591
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-18T12:53:55.658Z
- **Disclosed**: 2021-03-01T11:02:24.045Z

## Reporter
- **Username**: alexanderhofstaetter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The issue is related to all Nextcloud versions. It is not patched yet. All versions (18-20) seems to be vulnerable. The issue came up in the following environment:

- nextcloud docker image (20.0.2 and 20.0.3)
- LDAP authentication
- external SMB shares via DB stored credentials

The problem came up after several users could not access their mounted SMB shares. When I checked, what was going on, it seems that DB credentials are getting stored from the session (table `oc_storages_credentials`) to the DB. The problem is, that there is no check if the current user in the session is the same as the user for whom the credentials get stored.

It seems that the credentials saved in the corresponding table (`oc_storages_credentials`) are wrong and therefore all SMB shares are showing errors.

When I initially add the external storage SMB mounts in the settings and then a user logs in the first time, the SMB shares work (with the correct login) which gets correctly saved in the DB.

Afterwards I can find one single entry on the `oc_storages_credentials`-table

However, when I (as an admin) navigate to: `https://cloud.example.org/settings/users` the table `oc_storages_credentials` gets (pre)populated with all the users (and some random credentials) - this also includes all users who weren´t logged-in yet. When the user logs in afterwards the credentials entry is already there and does not get updated.

### Steps to reproduce
1. Add external SMB mount with option "credentials saved in database"
2. Manually check the MYSQL table `oc_storages_credentials` - it should be empty
3. As an admin: navigate to (`/settings/users`) 
4. Recheck the MYSQL table `oc_storages_credentials` - there is an entry for every user now
5. The stored credentials in the DB are now the admin credentials
6. user can act as the admin user (their LDAP / AD password is stored in `oc_storages_credentials` for every user

### Expected behaviour
1. Do not populate the table `oc_storages_credentials` on "user list settings page"
2. If the current user credentials does not match the ones in the DB -> update it

### Actual behaviour
- `password::logincredentials/credentials` entries are getting deployed initially from the admin user ...

### Bugfix / Patch

There should be two files affected:
- `/apps/files_external/lib/Lib/Auth/Password/LoginCredentials.php`
- `/apps/files_external/lib/Listener/StorePasswordListener.php`


It looks like there is a form of wrong impersonation going on here. -> The git-Diff for a security conform bugfix is attached.

### Server configuration

I am using this docker image (no modifications): https://github.com/nextcloud/docker/tree/master/.examples/dockerfiles/full/fpm-alpine

**Operating system:** Docker on Ubuntu 20.04.1 LTS
**Web server:** nginx with php-fpm
**Database:** mariadb 10.5 as docker container
**PHP version:** 7php .4
**Nextcloud version:** 20.0.2
**Updated from an older Nextcloud/ownCloud or fresh install:** updated from nextcloud 18.0.11 -> 19.0 -> 20.0.3
**Where did you install Nextcloud from:**

## Impact

- Acting as a different user (as admin credentials are stored for every user in the DB)
- get a normal user account and accessing SMB shares on the network with higher privileges as himself
- getting access to internal ressources via external shared links

## Attachments
- external-storage-credentials.diff
- logs-and-debugging-info.txt
