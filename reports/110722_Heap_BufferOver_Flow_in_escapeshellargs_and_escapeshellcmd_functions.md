# Heap BufferOver Flow in escapeshellargs and escapeshellcmd functions

## Report Details
- **Report ID**: 110722
- **URL**: https://hackerone.com/reports/110722
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-14T17:23:22.482Z
- **Disclosed**: 2019-11-12T09:38:12.891Z

## Reporter
- **Username**: libnex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
1) Bug report: https://bugs.php.net/bug.php?id=71270
2) Patch submitted and accepted: https://github.com/php/php-src/commit/2871c70efaaaa0f102557a17c727fd4d5204dd4b

---Description---


1)I found this vulnerability using a custom PHP engine fuzzer that I wrote. There exist a heap-based buffer over flow that allows one to write a user tainted data pass an allocated buffer. This vulnerability lies in the following functions:
	escapeshellarg 
	escapeshellcmd 

2) On a default php installation, the memory limit is set to 128MB and this vulnerability is not triggerable. My analysis shows that this is triggerable when memory limit is roughly > 1024mb. A quick search on github shows that it's not uncommon to see code like "ini_set('memory_limit', -1);"


3)I've created a POC that triggers the buffer over write with 0x414141414141.....

4) A string of 1024mb is created and passed into escapeshellarg. "l" contains the length of this string:

Breakpoint 2, php_escape_shell_arg (str=0x7fffad469028 'A' <repeats 200 times>...) at /home/elaw/php-7.0.0/ext/standard/exec.c:343
343             int x, y = 0, l = (int)strlen(str);

gdb-peda$ print l
$43 = 0x40000000            // 1024mb



5) This length "l" is then passed into zend_string_alloc as "4 * l + 2" which results in an integer overflow:

Temporary breakpoint 3, php_escape_shell_arg (str=0x7fffad000018 'A' <repeats 200 times>...) at /home/elaw/php-7.0.1/ext/standard/exec.c:348
348             cmd = zend_string_alloc(4 * l + 2, 0); /* worst case */


gdb-peda$ print 4* l + 2
$44 = 0x2 				   //Overflow


6) Stepping into zend_string_alloc to verify the integer overflow. Notice len=0x2:
zend_string_alloc (persistent=0x0, len=0x2) at /home/elaw/php-7.0.0/Zend/zend_string.h:121      
121             zend_string *ret = (zend_string *)pemalloc(ZEND_MM_ALIGNED_SIZE(_ZSTR_STRUCT_SIZE(len)), persistent);


7) Lets confirm the overflow again in the allocated (zend_string *) cmd. Notice cmd.len=0x2:
gdb-peda$ p *cmd
$52 = {
  gc = {
    refcount = 0x1,
    u = {
      v = {
        type = 0x6,
        flags = 0x0,
        gc_info = 0x0
      },
      type_info = 0x6
    }
  },
  h = 0x0,
  len = 0x2,
  val = "1"
}



8) The loops then writes pass the allocated buffer in

258		for (x = 0, y = 0; x < l; x++) {
....
321       ZSTR_VAL(cmd)[y++] = str[x];



9) Verifying the buffer overflow in 
gdb-peda$ p (zend_string *)cmd.len
$9 = (zend_string *) 0x2
gdb-peda$ x/100b (zend_string *)cmd.val
0x1625a58:      0x27    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625a60:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625a68:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625a70:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625a78:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625a80:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625a88:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625a90:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625a98:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625aa0:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625aa8:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625ab0:      0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0x1625ab8:      0x41    0x41    0x41    0x41


10) The vulnerability for php_escape_shell_cmd is identical.

## Attachments
No attachments
