# Installer can modify other gems if gem name is specially crafted

## Report Details
- **Report ID**: 270068
- **URL**: https://hackerone.com/reports/270068
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-21T02:26:57.258Z
- **Disclosed**: 2018-03-22T04:54:02.816Z

## Reporter
- **Username**: nmalkin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
# Installer can modify other gems if gem name is specially crafted

The `install_location` function allows writing to certain files outside the installation directory.

The `install_location` function in lib/rubygems/package.rb attempts to ensure that files are not installed outside `destination_dir`.  However the test it employs, a string comparison using `start_with?`, fails to prevent the case when `destination_dir` is a prefix of the path being written.

Example that should be prevented but is allowed:
```
install_location '../install-whatever-foobar/hello.txt', '/tmp/install'
# outputs '/tmp/install-whatever-foobar/hello.txt'
```

`gem install` always constructs `destination_dir` as `'#{name}-#{version}'`, so the vulnerability cannot overwrite arbitrary files.  However, a malicious gem with `name='rails'` and an empty version number (`version=''`), for example, could overwrite the files of any other gem whose name begins with `rails-`, like rails-i18n or rails-letsencrypt.

## Proof of concept

The attached ra.gem demonstrates the vulnerability. It assumes that some other gems have already been installed.

```bash
gem install --install-dir=/tmp/install rails-i18n rails-letsencrypt rails-html-sanitizer
gem install --install-dir=/tmp/install ra.gem
```

The malicious gem will do three things, each of which could potentially lead to code execution:

- delete an existing rails-letsencrypt-0.5.3 gem
- overwrite a code file in the rails-i18n-5.0.4 gem
- symlink rails-html-sanitizer-1.0.3 to a world-writable directory

The structure of the gem file reveals how the attack works:

```sh
$ tar -xvf ra.gem
metadata.gz
data.tar.gz
$ gzip -dc metadata.gz | head -n 4
--- !ruby/object:Gem::Specification
name: rails
version: !ruby/object:Gem::Version
  version: ''
$ tar -tvf data.tar.gz
-rw-r--r-- 0/0              12 1969-12-31 16:00 README
drwxr-xr-x 0/0               0 1969-12-31 16:00 ../rails-letsencrypt-0.5.3/
-rw-r--r-- 0/0              12 1969-12-31 16:00 ../rails-i18n-5.0.4/lib/rails_i18n.rb
lrw-r--r-- 0/0               0 1969-12-31 16:00 ../rails-html-sanitizer-1.0.3 -> /tmp/attacker-controlled
```

## Remediation

A sufficient fix is to append a directory separator to `destination_dir` before doing the `start_with?` check.

```
diff --git a/lib/rubygems/package.rb b/lib/rubygems/package.rb
index c36e71d8..f73f9d30 100644
--- a/lib/rubygems/package.rb
+++ b/lib/rubygems/package.rb
@@ -424,7 +424,7 @@ EOM
     destination = File.expand_path destination

     raise Gem::Package::PathError.new(destination, destination_dir) unless
-      destination.start_with? destination_dir
+      destination.start_with? destination_dir + '/'

     destination.untaint
     destination
```

## Attached files

- `ra.gem`, an example of a vulnerable gem
- `make-ra-gem.py`, sample code that generates the proof of concept (to run: `./make-ra-gem.py > ra.gem`)
- `0001-Add-test_install_location_suffix.patch`, test code that checks for this vulnerability. Run with `ruby -I"lib:test" test/rubygems/test_gem_package.rb`.


## Attachments
- ra.gem
- make-ra-gem.py
- 0001-Add-test_install_location_suffix.patch
