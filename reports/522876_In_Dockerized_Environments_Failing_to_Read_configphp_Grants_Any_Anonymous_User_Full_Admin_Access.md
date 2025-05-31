# In Dockerized Environments, Failing to Read config.php Grants Any Anonymous User Full Admin Access

## Report Details
- **Report ID**: 522876
- **URL**: https://hackerone.com/reports/522876
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-03T04:34:03.056Z
- **Disclosed**: 2019-07-27T10:42:10.149Z

## Reporter
- **Username**: theguynamedguy86
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Consider this deployment:
- Nextcloud is already installed in a Dockerized environment.
- There are two Nextcloud containers running in the environment.
- Both containers share the same MySQL database.
- Both containers share the same data (`/var/www/html/data`) and config (`/var/www/html/config`) via NFS-mounted or SMB-mounted Docker volumes.
- All of the values Nextcloud needs to complete first-run setup (database name and credentials, admin credentials, etc) are provided to both containers via environment variables (`NEXTCLOUD_ADMIN_USER`, `NEXTCLOUD_ADMIN_PASSWORD`, `MYSQL_HOST`, `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`).

Now, consider that one or both of the containers encounter an issue reading `/var/www/html/config/config.php`. This could be caused by an of the following:
- Transient failure connecting to the NFS/SMB server at the time either container is launching or restarting (especially in response to a failed Liveness check).
- Timeout or other transient failure in communication with the NFS/SMB server while the container is already running.
- One container attempting to read `config.php` while the other container is writing to the file, causing an incomplete read (possibly making the file look empty).

In this situation, Nextcloud will assume that it is NOT installed (since the config seems empty). As a result, Nextcloud will launch the installer the next time ANY user requests a page from _the container that temporarily cannot read the `config.php` file_.  This causes that instance of Nextcloud to overwrite the `config.php` with a new file that has the same database credentials as the old file (populating the credentials from the environment variables), but the new config flags Nextcloud as not yet being installed (i.e. `installed` is set to `FALSE`). Some time later, assuming that NFS/SMB services have been restored to normal (e.g. the transient issue has disappeared), ALL containers will now happily serve up the Nextcloud installer to ANY user because the container that failed to read the configuration file wrote a new one with a newer timestamp that indicates Nextcloud is not installed.

From here, ANY user who stumbles upon the installer page can provide ANY username and password and end up with a new admin account with full access to the existing Nextcloud installation.

Nextcloud should NOT allow the installer to be run if ANY database tables already exist in the target database. If this is not possible, Nextcloud should at least not allow the installer to be run if any `admin` users exist in the target database.

## Impact

An attacker interested in taking over an existing installation of Nextcloud could write a script to frequently monitor that installation until such a time as that installation suffers a temporary issue reading `config.php` and starts serving up the installer. At that point, the attacker can hop over to the installation, finish the setup process, and create a username and password of their choice to gain full admin access to the entire Nextcloud installation.

With admin access, the attacker can lock out all of the existing users of the system, change system settings, and download or erase all of the files on the Nextcloud installation.

## Attachments
No attachments
