# The possibility that unintended file operation may be performed because some methods of `Dir` do not check NULL characters.

## Report Details
- **Report ID**: 302338
- **URL**: https://hackerone.com/reports/302338
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-01-04T10:03:14.309Z
- **Disclosed**: 2018-04-01T09:11:40.963Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
It seems that `entries`,`new`, and `empty?` do not check NULL characters in methods of `Dir`.

```log
[vagrant@localhost ~]$ ls
test
[vagrant@localhost ~]$ irb
irb(main):001:0> Dir.open("/home/vagrant\0xxx") do |d|
irb(main):002:1* p d.read   # => "."
irb(main):003:1> p d.read   # => ".."
irb(main):004:1> p d.read
irb(main):005:1> p d.read
irb(main):006:1> end
"."
".."
".bash_logout"
".bash_profile"
=> ".bash_profile"

irb(main):007:0> d = Dir.new("/home/vagrant\0xxx")
=> #<Dir:/home/vagrantxxx>
irb(main):008:0> p d.read   # => "."
"."
=> "."
irb(main):009:0> p d.read   # => ".."
".."
=> ".."
irb(main):010:0> p d.read
".bash_logout"
=> ".bash_logout"
irb(main):011:0> p d.read
".bash_profile"
=> ".bash_profile"

irb(main):012:0> Dir.entries("/home/vagrant\0yyy")
=> [".", "..", ".bash_logout", ".bash_profile", ".bashrc", ".ssh", ".rbenv", ".pki", ".bash_history", "test"]

irb(main):013:0> Dir.empty?("/home/vagrant\0zzz")
=> false
```

## Impact

When using the corresponding method, unintended file operation may be performed.

## Attachments
No attachments
