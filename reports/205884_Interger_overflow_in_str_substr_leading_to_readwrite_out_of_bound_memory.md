# Interger overflow in str_substr leading to read/write out of bound memory

## Report Details
- **Report ID**: 205884
- **URL**: https://hackerone.com/reports/205884
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-13T05:26:12.272Z
- **Disclosed**: 2017-03-15T01:29:48.346Z

## Reporter
- **Username**: beyondchain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Failed check len & beg in str_substr when call mrb_str_aref_m by String. This can lead to read/write into invalid memory which may be memory corruption or  RCE.
this snippet causes a crash in mruby(i can't check mruby-engine by error undefined symbol >rb_utf8_str_new ):
```
$b="B"*2048
$expand=$b[0x40,0x7fffffff]
puts $expand.size()
puts $expand
```
And, here is error: beg=0x40, len=0x7fffffff, clen=0x800=> beg+len < clen(Integer Overflow)
```
static mrb_value
str_substr(mrb_state *mrb, mrb_value str, mrb_int beg, mrb_int len)
{
/**
*..some code here
**/
if (beg + len > clen) => Integer overflow here
    len = clen - beg;
  if (len <= 0) {
    len = 0;
  }
  return str_subseq(mrb, str, beg, len);
}
```

## Attachments
No attachments
