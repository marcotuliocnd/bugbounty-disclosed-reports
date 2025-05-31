# RDoc::MethodAttr is vulnerable to Regular Expression Denial of Service (ReDoS)

## Report Details
- **Report ID**: 1378706
- **URL**: https://hackerone.com/reports/1378706
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-22T16:05:30.191Z
- **Disclosed**: 2023-07-18T09:19:26.247Z

## Reporter
- **Username**: sighook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
The method `block_params` in class `RDoc::MethodAttr` uses a regular expression that is vulnerable to Denial of Service due to catastrophic backtracking.

The regular expression is:
```
([A-Z:a-z0-9_]+)\.([a-z0-9_]+)(\s*\(\s*[a-z0-9_.,\s]*\s*\)\s*)?
```
Source: https://github.com/ruby/ruby/blob/master/lib/rdoc/method_attr.rb#L265

The ReDoS requence is: `(\s*\(\s*[a-z0-9_.,\s]*\s*\)\s*)`. It contains three overlapping repeating groups (repeated characters are 0x20, 0xa0, [09-0d]), so the worst-case complexity is cubic as there are 3 infinitely repeating groups. Cubic complexity here means that if the vulnerable part of the string is doubled in length, the execution time should be about 8 times longer (2^3).

# PoC

I have not found a way to exploit this vulnerability directly from the file documentation (by running rdoc), however directly it is very easy:

```ruby
use 'rdoc'
RDoc::MethodAttr.new(nil, nil).block_params = '0.0(' + ' '*3456 + '0'
```

The client's code that relies on `AnyMethod` is also vulnerable since it inherits `MethodAttr`:

```ruby
use 'rdoc'
RDoc::AnyMethod.new(nil, nil).block_params = '0.0(' + ' '*3456 + '0'
```

If an attacker  provides a malicious string to `AnyMethod|MethodAttr`'s `block_params` documentation parser, it will get stuck processing the input for an extremely long time, consuming 100% CPU.

## Impact

An attacker could cause an effective denial of service, by crafting an input which exploits catastrophic backtracking for the regular expression.

## Attachments
No attachments
