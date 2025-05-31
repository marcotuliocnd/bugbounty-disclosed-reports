# Gem signature forgery

## Report Details
- **Report ID**: 275269
- **URL**: https://hackerone.com/reports/275269
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-06T23:57:17.767Z
- **Disclosed**: 2018-08-03T20:23:47.955Z

## Reporter
- **Username**: plover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
# Summary

Inconsistencies in how `gem` processes gem files make it possible to reuse a signature from an existing signed gem and apply it to arbitrary contents. The forged gem will install even with `-P HighSecurity`.

The attached file multi_json-1.12.2.gem is a forged version of the genuine [multi_json-1.12.2.gem](https://rubygems.org/gems/multi_json/versions/1.12.2) gem with faked contents (just a single text file called HACKED). Here is how to check it. You must first trust the original developer's public key.
```
$ gem --version
2.5.2
$ wget https://raw.githubusercontent.com/intridea/multi_json/master/certs/rwz.pem
$ gem cert --add rwz.pem
Added '/CN=pavel/DC=pravosud/DC=com'
$ gem install --install-dir install -P HighSecurity multi_json-1.12.2.gem
Successfully installed multi_json-1.12.2
1 gem installed
$ ls install/gems/multi_json-1.12.2/
HACKED
```


# Details

The vulnerability stems from inconsistencies in how `gem` interprets the entries of the tar container. A tar file may contain multiple entries with the same name. When there are two data.tar.gz entries, for example, `gem` will honor the *second* one when verifying the signature, but the *first* one when installing files. The proof of concept gem uses this trick: it prepends an additional data.tar.gz entry to the genuine multi_json-1.12.2.gem. (The attached forge-gem.sh script was used to make it.)
```
$ tar tvf multi_json-1.12.2.gem
-r--r--r-- wheel/wheel     163 2017-10-05 16:05 data.tar.gz
-r--r--r-- wheel/wheel    1840 2017-09-04 21:51 metadata.gz
-r--r--r-- wheel/wheel     256 2017-09-04 21:51 metadata.gz.sig
-r--r--r-- wheel/wheel   16908 2017-09-04 21:51 data.tar.gz
-r--r--r-- wheel/wheel     256 2017-09-04 21:51 data.tar.gz.sig
-r--r--r-- wheel/wheel     270 2017-09-04 21:51 checksums.yaml.gz
-r--r--r-- wheel/wheel     256 2017-09-04 21:51 checksums.yaml.gz.sig
```

A similar bug affects checksums.yaml.gz: checksums are read from the first such entry, while the signature is verified on the last. This table summarizes the inconsistencies:

| file              | `extract_files` uses | `verify` uses |
|-------------------|----------------------|---------------|
| data.tar.gz       | first                | last          |
| checksums.yaml.gz | first                | last          |
| metadata.gz       | last                 | last          |


## Source code references

Here are the pieces of code that are responsible for the inconsistencies in processing.

[`extract_files`](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/package.rb#L334-L350) takes the *first* data.tar.gz entry:
```
  def extract_files destination_dir, pattern = "*"
    verify unless @spec

    FileUtils.mkdir_p destination_dir

    @gem.with_read_io do |io|
      reader = Gem::Package::TarReader.new io

      reader.each do |entry|
        next unless entry.full_name == 'data.tar.gz'

        extract_tar_gz entry, destination_dir, pattern

        return # ignore further entries
      end
    end
  end
```

[`read_checksums`](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/package.rb#L466-L474) [seeks](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/package/tar_reader.rb#L109-L119) to the *first* checksums.yaml.gz entry:
```
  def read_checksums gem
    Gem.load_yaml

    @checksums = gem.seek 'checksums.yaml.gz' do |entry|
      Zlib::GzipReader.wrap entry do |gz_io|
        YAML.load gz_io.read
      end
    end
  end
```

[`verify_files`](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/package.rb#L593-L606) and [`verify_entry`](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/package.rb#L566-L588) iterate over all entries in the tar file, filling in `@signatures` and `@digests`. In the case of entries with duplicate names, it overwrites previous values, meaning that the *last* result wins. `verify_entry` also handles metadata.gz, calling [`load_spec`](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/package.rb#L436-L450) afresh each time:
```
  def verify_entry entry
    file_name = entry.full_name
    @files << file_name

    case file_name
    when /\.sig$/ then
      @signatures[$`] = entry.read if @security_policy
      return
    else
      digest entry
    end

    case file_name
    when /^metadata(.gz)?$/ then
      load_spec entry
    when 'data.tar.gz' then
      verify_gz entry
    end
  rescue => e
    message = "package is corrupt, exception while verifying: " +
              "#{e.message} (#{e.class})"
    raise Gem::Package::FormatError.new message, @gem
  end
```
[`verify_checksums`](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/package.rb#L548-L561) and [`verify_signatures`](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/security/policy.rb#L283-L291) operate only on the precomputed `@checksums`, `@signatures`, and `@digests`.

Incidentally, [`get_metadata`](https://github.com/rubygems/rubygems/blob/v2.6.13/lib/rubygems/commands/unpack_command.rb#L161-L177), used by the `unpack` command, has its own extractor for metadata.gz, but it happens to grab the last entry, just like `verify_files`.


# Mitigation

The attached patch 0001-Add-tests-that-Gem-Package-verify-checks-duplicate-f.patch adds two new tests (both currently failing) that check signature verification when bogus files come before or after the genuine files.

The essential mitigation is to ensure that there is no ambiguity when processing a tar file that has multiple entries for the same file name. E.g., "data.tar.gz" must refer to one and only one entry in the tar file. One way to do it would be to set a policy in the code: e.g., last entry always wins (which would be consistent with the `tar` command). But that would be hard to enforce, especially in new code going forward. Another way would be not to permit duplicate entries; e.g., `verify_entry` could check whenever it is about to overwrite something in `@signatures`, `@digests`, or `@spec`, and return an error. This needs some care, as metadata and metadata.gz are both processed equivalently. It is possible, using symlinks, to create entries that effectively point to the same file, even though the paths differ; e.g.:
```
data.tar.gz
dir/ -> ..
dir/data.tar.gz
```
But this shouldn't be a problem for `gem`, as long as it continues to use strict string equality with unadorned paths like `"data.tar.gz"`.

Even when this bug is fixed, a weaker form of signature forgery is possible. There is nothing in a gem file that binds data.tar.gz and metadata.gz together: they are signed independently. It is possible to mix and match files from different signed gems. Suppose a signed gem example-1.0 has a security vulnerability, and the authors release a new signed update example-1.1. Someone (perhaps a malicious rubygems.org admin) could forge a gem containing data.tar.gz from example-1.0 and metadata.gz from example-1.1. Users would think they are running the updated code, but they are still running the old vulnerable code. Fixing this weaker form of forgery seems like it would require a redesign of the signature format. Ideally, the signature would be over the entire gem, and verified before any unpacking.

It seems that not many people are sign their gems or verify signatures. For most users the possibility of signature forgery doesn't put them at additional risk beyond the (already risky) status quo. The flaw affects only those users who use the `MediumSecurity` or `HighSecurity` profiles.


# Attachments

- **multi_json-1.12.2.gem** is a gem with a forged signature.
- **0001-Add-tests-that-Gem-Package-verify-checks-duplicate-f.patch** adds tests for specific instances of gem files that contain multiple entries with the same name.
- **forge-gem.sh** takes an existing signed gem and produces a forged gem containing an arbitrary data.tar.gz file.

How to run forge-gem.sh:
```
$ gem fetch multi_json
$ mkdir orig
$ mv multi_json-1.12.2.gem orig/
$ echo hacked > HACKED
$ tar czf data.tar.gz HACKED
$ ./forge-gem.sh orig/multi_json-1.12.2.gem data.tar.gz forged.gem
```
Be aware that if the original multi_json-1.12.2.gem and the new forged.gem are both in the same directory, then `gem install ./forged.gem` will—for some reason—install multi_json-1.12.2.gem instead. You have to hide the original file in another directory first.


## Attachments
- multi_json-1.12.2.gem
- 0001-Add-tests-that-Gem-Package-verify-checks-duplicate-f.patch
- forge-gem.sh
