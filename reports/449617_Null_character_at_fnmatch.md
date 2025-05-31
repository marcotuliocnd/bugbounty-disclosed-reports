# Null character at fnmatch

## Report Details
- **Report ID**: 449617
- **URL**: https://hackerone.com/reports/449617
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-11-25T20:51:40.138Z
- **Disclosed**: 2019-10-16T23:20:23.268Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
I confirmed that it will behave unintentionally when null characters are entered in patterns with `fnmatch`,` fnmatch? `.

```log
$ ruby -v
ruby 2.5.3p105 (2018-10-18 revision 65156) [x86_64-darwin16]

$ irb
irb(main):001:0> require 'pathname'
=> true

# should not be true
irb(main):002:0> File.fnmatch("x\0yz", 'x')
=> true
irb(main):003:0> File.fnmatch?("abc\0", 'abc')
=> true
irb(main):004:0> Pathname('x').fnmatch("x\0yz")
=> true
irb(main):005:0> Pathname('abc').fnmatch?("abc\0")
=> true

# It does not work as a delimiter
irb(main):006:0> File.fnmatch("x\0yz", 'yz')
=> false
irb(main):007:0> Pathname('yz').fnmatch("x\0yz")
=> false

# error
irb(main):008:0> File.fnmatch('x', "x\0")
Traceback (most recent call last):
        3: from /usr/local/bin/irb:11:in `<main>'
        2: from (irb):8
        1: from (irb):8:in `fnmatch'
ArgumentError (path name contains null byte)
irb(main):009:0> Pathname("x\0").fnmatch('x')
Traceback (most recent call last):
        4: from /usr/local/bin/irb:11:in `<main>'
        3: from (irb):9
        2: from (irb):9:in `Pathname'
        1: from (irb):9:in `initialize'
ArgumentError (pathname contains null byte)
```

## Impact

When using these methods, unintended file operation may be performed.

## Attachments
No attachments
