# Unpacker improperly validates symlinks, allowing gems writes to arbitrary locations

## Report Details
- **Report ID**: 270072
- **URL**: https://hackerone.com/reports/270072
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-21T02:34:09.396Z
- **Disclosed**: 2018-12-31T08:05:52.196Z

## Reporter
- **Username**: nmalkin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
# Unpacker improperly validates symlinks, allowing gems writes to arbitrary locations

The RubyGems installer attempts to prevent a gem from writing any files outside the install directory; however it is possible to bypass the check with a symbolic link in a crafted gem.

## Example structure of malicious gem
```
$ tar -xvf symlink.gem
metadata.gz
data.tar.gz
$ tar -tvf data.tar.gz
-rw-r--r-- 0/0              12 1969-12-31 16:00 README
lrw-r--r-- 0/0               0 1969-12-31 16:00 link -> /tmp
-rw-r--r-- 0/0               6 1969-12-31 16:00 link/HACKED
```


## Proof of concept
Using the attached `symlink.gem`:
```
gem install symlink.gem
# or
gem unpack symlink.gem
```
This will create a file /tmp/HACKED.

## Impact

The name and contents of the written file, as well as the file permissions, are arbitrary.
Using this technique, an attacker could easily get code execution, for example by overwriting a system binary or writing into a user's `.profile`.

Note that the exploit will even work with `gem unpack`, which is supposed to be safe of system-level side-effects.

For comparison, this exploit is more powerful than #243156 (and #270068) as the target directory doesn't need to contain a dash.

## Root cause

The code in [install_location](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/package.rb#L415) is supposed to check if the target filename is outside the destination directory. It does this by fully resolving (using `File.realpath`) the destination directory and then seeing if the target filename `.start_with?` that directory.

This test succeeds for a symlink that points outside the gem's install directory, because its "destination directory" is the directory where it's located (not where it points), which is local.

The test also succeeds for a file that uses the symlink to "escape" the local directory, because the symlink really is its prefix.

However, in combination, these files can allow for arbitrary writes, as shown.

The root cause vulnerability is the ability of symlinks to point outside the gem. This was actually forbidden in a [commit from 2015](https://github.com/rubygems/rubygems/commit/3a02b6379e62eb7a5eb359cc87473a65a355cfe6), but was made more permissive [in a later commit](https://github.com/rubygems/rubygems/commit/14b1eec7bd0f9fca5cedeae781fbef6f36dc466a), creating this vulnerability.


## Suggested remediation

The course of action we recommend is to (again) disallow symlinks that point outside the gem directory.



## Attached files

- `symlink.gem`, an example of a vulnerable gem. **Note**: extract this using `tar` instead of `gem` to avoid triggering the vulnerability (e.g., `tar -Oxf symlink.gem data.tar.gz | tar -tzvf -`)
- `make-symlink-gem.py`, sample code that generates the proof of concept (to run: `./make-symlink-gem.py > symlink.gem`)
- `0001-Add-a-test-test_extract_symlink_parent.patch`, test code that can be added to RubyGems to test for this vulnerability


## Attachments
- symlink.gem
- make-symlink-gem.py
- 0001-Add-a-test-test_extract_symlink_parent.patch
