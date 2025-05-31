# Memory disclosure in mruby String#lines method

## Report Details
- **Report ID**: 181319
- **URL**: https://hackerone.com/reports/181319
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-10T13:17:47.675Z
- **Disclosed**: 2016-12-16T20:53:52.497Z

## Reporter
- **Username**: isra17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
This bug was found with `jmlb337`.

Hey again,
while reviewing mruby for vulnerabilities, I stumble onto a case that allow an attacker to leak heap content including pointer that can be used along another vulnerability to craft a complete exploit.

## Reproduction Step
1. Allocate a string with a few lines.
2. Call String#lines and free or reallocate the string.
3. Allocate a few objects.
4. The next lines will now contains the value of the newly allocated data, including pointer used by `mrb_value`s.

## PoC
```ruby
@a = []
$a = ("a"*0xf + "\n") * 1000
$a.lines do |l|
  $a.clear
  foo = "UUUUUUUU" * 1000
  @a << l
end
```
Look at `@a` to get the "UUUU..." `mrb_value` object and strings.

## Explaination
The bug is triggered due to the caching of `p` at [string.c:310](https://github.com/mruby/mruby/blob/872517dff372ee6fde92c71861abf6ab9fbab958/mrbgems/mruby-string-ext/src/string.c#L310): 
```c
  char *p = RSTRING_PTR(self), *t;
  char *e = p + RSTRING_LEN(self);
```

However, while iterating on each line, the function allow the caller to provide a block to be called for each line [string.c:324](https://github.com/mruby/mruby/blob/872517dff372ee6fde92c71861abf6ab9fbab958/mrbgems/mruby-string-ext/src/string.c#L324): 
```c
      mrb_yield_argv(mrb, blk, 1, &arg);
```
This block let the attacker to update the `self` string, in which case `p` will now be a dangling pointer pointing to free memory. Allocating new objects will end up in this free location and let the next iteration read this data before giving it back to the block.

## Exploitability

The vulnerability is exploitable as long as the attacker can run arbitrary ruby code in the mruby interpreter. It should cover mruby-engine case as used by Shopify.

## Impact

This vulnerability comes handy to locate object address in the heap, by allowing reliable, cheap and simple memory disclosure. We would use this bug to build a complete RCE along with another reported bug in the following 1 or 2 week  (Will add a comment with the other report ID). I spoke with François Chagnon and we preferred to report the bugs as soon as possible while working on provable RCE afterward so it can get patched earlier.

## Proposed Fix
See patch in attachment.

## Attachments
- 0001-Fix-use-after-free-access-in-String-lines.patch
