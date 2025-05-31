# Buffer overflow in yywarning_s

## Report Details
- **Report ID**: 535827
- **URL**: https://hackerone.com/reports/535827
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-04-11T14:44:25.684Z
- **Disclosed**: 2019-09-04T13:35:50.392Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
===
The following demonstrates a crash:

```
300000000000000000000000000000000000000000000000E0030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Debug info
==========
In the same vein as our last two reports, we've found more instances of problematic string concatenation. This crash happens due to a buffer overflow in `yywarning_s`. `strcat` is called without making sure `buf` is large enough. The patch below adds the check.

```diff
diff --git a/mrbgems/mruby-compiler/core/parse.y b/mrbgems/mruby-compiler/core/parse.y
index cb62ec3f..82df8c08 100644
--- a/mrbgems/mruby-compiler/core/parse.y
+++ b/mrbgems/mruby-compiler/core/parse.y
@@ -3759,10 +3759,15 @@ static void
 yywarning_s(parser_state *p, const char *msg, const char *s)
 {
   char buf[256];
-
-  strcpy(buf, msg);
-  strcat(buf, ": ");
-  strcat(buf, s);
+  const char delim[] = ": ";
+
+  if (strlen(msg) + strlen(s) + strlen(delim) + 1 > sizeof(buf)) {
+      strcpy(buf, msg);
+  } else {
+      strcpy(buf, msg);
+      strcat(buf, delim);
+      strcat(buf, s);
+  }
   yywarning(p, buf);
 }

```

Test platform
=============
* Arch Linux

mruby SHA: 9c252410cf6e43eb7e19683844c83581445fc089

Thank you,
Dinko Galetic
Denis Kasak

## Impact

DOS through crashing the mruby process and probable execution flow control through stack smashing.

## Attachments
- poc
- fix.diff
