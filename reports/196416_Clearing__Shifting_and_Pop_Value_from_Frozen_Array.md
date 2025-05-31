# Clearing , Shifting and Pop Value from Frozen Array  

## Report Details
- **Report ID**: 196416
- **URL**: https://hackerone.com/reports/196416
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-01-06T21:41:25.406Z
- **Disclosed**: 2017-08-30T13:20:50.498Z

## Reporter
- **Username**: an0n-j
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hey again!

Founded another missing best practice in mruby. That allow an attacker to Delete (pop) or clear the ___Frozen ARRAY___. This report is similar to [194866](https://hackerone.com/reports/194866)
POC
===
$a = [1,2,3,4,5].freeze

$a.pop         
>"#=> This will give 5 and ___$a___ will become [1,2,3,4]"

$a.shift       
> "#=> This will give 1 and ___$a___ will become [2,3,4,5]"

$a.clear        
> "#=> This will clear the whole FROZEN ARRAY."

Explanation
========
The issue is in __mrb_ary_pop__  ,  __mrb_ary_shift__  & in  __mrb_ary_clear__ methods of [Array.c](https://github.com/mruby/mruby/blob/master/src/array.c)  because there is no method calling to check the weather the Array is frozen or not.
I'm not too much familiar with ruby to determine its impact, may be it doesn't effect at all but it should be fix.

Fix
==
Apply __ary_modify__ method in all above mentioned methods.

## Attachments
No attachments
