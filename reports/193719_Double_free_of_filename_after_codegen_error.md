# Double free of filename after codegen error

## Report Details
- **Report ID**: 193719
- **URL**: https://hackerone.com/reports/193719
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-23T23:54:50.274Z
- **Disclosed**: 2017-02-07T01:42:04.750Z

## Reporter
- **Username**: titanous
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following program causes a double free of `irep->filename` after a codgen error is triggered. I've poked at it a bit and it doesn't seem exploitable because the second free happens near the end of the program and there don't appear to be any overflows or useful heap control available. However, I'm not particularly skilled at this, so I may be wrong.

```ruby
def b
  def c
    a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a>>=a
  end
end
```

This is what it looks like when run by mruby-engine:

```text
bin/sandbox:20:in `sandbox_eval': user memory error (state: 0x00000101848010, chunk: 0x00000101875680)   (MRubyEngine::EngineInternalError)
0x00000101738e2d : (me_host_internal_error_new+0x189) [0x00000101738e2d]
0x00000101735722 : (mspace_free+0x1634) [0x00000101735722]
0x00000101739599 : (mruby_engine_allocf+0x57) [0x00000101739599]
0x0000010175c756 : (mrb_irep_free+0x342) [0x0000010175c756]
0x0000010175c726 : (mrb_irep_free+0x294) [0x0000010175c726]
0x00000101775901 : (mrb_generate_code+0x161) [0x00000101775901]
0x00000101739845 : (generate_code+0x245) [0x00000101739845]
0x0000010173972b : (me_mruby_engine_generate_code+0x75) [0x0000010173972b]
0x00000101737f32 : (ext_mruby_engine_eval+0x114) [0x00000101737f32]
0x000001010a55a4 : (vm_call_cfunc+0x1764) [0x000001010a55a4]
0x000001010a4692 : (vm_call_method+0x882) [0x000001010a4692]
0x00000101088820 : (vm_exec_core+0x13920) [0x00000101088820]
0x00000101098811 : (vm_exec+0x129) [0x00000101098811]
0x00000101099918 : (rb_iseq_eval_main+0x504) [0x00000101099918]
0x00000100f55434 : (ruby_exec_internal+0x148) [0x00000100f55434]
0x00000100f5535e : (ruby_run_node+0x78) [0x00000100f5535e]
0x00000100f0a06f : (main+0x79) [0x00000100f0a06f]
	from bin/sandbox:20:in `<main>'
bin/sandbox: unexpected return
```

Here's the ASAN report:

```text
codegen error:-:1: too complex expression
=================================================================
==22527==ERROR: AddressSanitizer: attempting double-free on 0x60200000db90 in thread T0:
    #0 0x4c4520 in free (/vagrant/bin/mruby+0x4c4520)
    #1 0x5bfc0b in mrb_default_allocf /vagrant/src/state.c:56:5
    #2 0x551427 in mrb_free /vagrant/src/gc.c:268:3
    #3 0x5c043f in mrb_irep_free /vagrant/src/state.c:162:3
    #4 0x5bfe8a in mrb_irep_decref /vagrant/src/state.c:133:5
    #5 0x5c0338 in mrb_irep_free /vagrant/src/state.c:158:5
    #6 0x5bfe8a in mrb_irep_decref /vagrant/src/state.c:133:5
    #7 0x6a732b in mrb_generate_code /vagrant/mrbgems/mruby-compiler/core/codegen.c:2960:5
    #8 0x673102 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5732:10
    #9 0x674815 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #10 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #11 0x7fc4a028cf44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #12 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x60200000db90 is located 0 bytes inside of 2-byte region [0x60200000db90,0x60200000db92)
freed by thread T0 here:
    #0 0x4c4520 in free (/vagrant/bin/mruby+0x4c4520)
    #1 0x5bfc0b in mrb_default_allocf /vagrant/src/state.c:56:5
    #2 0x551427 in mrb_free /vagrant/src/gc.c:268:3
    #3 0x5c043f in mrb_irep_free /vagrant/src/state.c:162:3
    #4 0x5bfe8a in mrb_irep_decref /vagrant/src/state.c:133:5
    #5 0x5c0338 in mrb_irep_free /vagrant/src/state.c:158:5
    #6 0x5bfe8a in mrb_irep_decref /vagrant/src/state.c:133:5
    #7 0x5c0338 in mrb_irep_free /vagrant/src/state.c:158:5
    #8 0x5bfe8a in mrb_irep_decref /vagrant/src/state.c:133:5
    #9 0x6a732b in mrb_generate_code /vagrant/mrbgems/mruby-compiler/core/codegen.c:2960:5
    #10 0x673102 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5732:10
    #11 0x674815 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #12 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #13 0x7fc4a028cf44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287

previously allocated by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5bfc25 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x550336 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x550984 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x5512c3 in mrb_malloc /vagrant/src/gc.c:236:10
    #5 0x5f963d in sym_intern /vagrant/src/symbol.c:81:17
    #6 0x5f8ea6 in mrb_intern /vagrant/src/symbol.c:95:10
    #7 0x5f97fb in mrb_intern_cstr /vagrant/src/symbol.c:107:10
    #8 0x5147fe in mrb_define_method /vagrant/src/class.c:402:32
    #9 0x5914c3 in mrb_init_numeric /vagrant/src/numeric.c:1281:3
    #10 0x6a23a4 in mrb_init_core /vagrant/src/init.c:46:3
    #11 0x5bfbc5 in mrb_open_core /vagrant/src/state.c:47:3
    #12 0x5bfd6c in mrb_open_allocf /vagrant/src/state.c:107:20
    #13 0x5bfd3a in mrb_open /vagrant/src/state.c:99:20
    #14 0x4f29d3 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:172:20
    #15 0x7fc4a028cf44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287

SUMMARY: AddressSanitizer: double-free (/vagrant/bin/mruby+0x4c4520) in free
==22527==ABORTING
```

The `MRB_CATCH` block in `mrb_generate_code` tries to avoid this by nulling the filename, but it doesn't take into account that ireps can be nested and so the filename in the nested irep gets freed even though it was not allocated for the irep.

Here is a patch that fixes the issue, and a patch that fixes a memory leak due to `s->iseq` not being cleaned up by the error handler:

```diff
From 44e50aa439acf092af28b3f5edd4ad3314c87106 Mon Sep 17 00:00:00 2001
From: Jonathan Rudenberg <jonathan@titanous.com>
Date: Fri, 23 Dec 2016 18:22:43 -0500
Subject: [PATCH 1/2] Fix double free of irep->filename after codegen error

---
 include/mruby/irep.h                  | 1 +
 mrbgems/mruby-compiler/core/codegen.c | 4 +---
 src/state.c                           | 5 ++++-
 3 files changed, 6 insertions(+), 4 deletions(-)

diff --git a/include/mruby/irep.h b/include/mruby/irep.h
index 8922f4b7..35ae2bba 100644
--- a/include/mruby/irep.h
+++ b/include/mruby/irep.h
@@ -39,6 +39,7 @@ typedef struct mrb_irep {
 
   struct mrb_locals *lv;
   /* debug info */
+  mrb_bool own_filename;
   const char *filename;
   uint16_t *lines;
   struct mrb_irep_debug_info* debug_info;
diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c
index fc54a064..3bae67c6 100644
--- a/mrbgems/mruby-compiler/core/codegen.c
+++ b/mrbgems/mruby-compiler/core/codegen.c
@@ -2847,6 +2847,7 @@ scope_finish(codegen_scope *s)
     memcpy(fname, s->filename, fname_len);
     fname[fname_len] = '\0';
     irep->filename = fname;
+    irep->own_filename = TRUE;
   }
 
   irep->nlocals = s->nlocals;
@@ -2954,9 +2955,6 @@ mrb_generate_code(mrb_state *mrb, parser_state *p)
     return proc;
   }
   MRB_CATCH(&scope->jmp) {
-    if (scope->filename == scope->irep->filename) {
-      scope->irep->filename = NULL;
-    }
     mrb_irep_decref(mrb, scope->irep);
     mrb_pool_close(scope->mpool);
     return NULL;
diff --git a/src/state.c b/src/state.c
index 1259ac3a..11b71dd6 100644
--- a/src/state.c
+++ b/src/state.c
@@ -159,7 +159,9 @@ mrb_irep_free(mrb_state *mrb, mrb_irep *irep)
   }
   mrb_free(mrb, irep->reps);
   mrb_free(mrb, irep->lv);
-  mrb_free(mrb, (void *)irep->filename);
+  if (irep->own_filename) {
+    mrb_free(mrb, (void *)irep->filename);
+  }
   mrb_free(mrb, irep->lines);
   mrb_debug_info_free(mrb, irep->debug_info);
   mrb_free(mrb, irep);
@@ -261,6 +263,7 @@ mrb_add_irep(mrb_state *mrb)
   irep = (mrb_irep *)mrb_malloc(mrb, sizeof(mrb_irep));
   *irep = mrb_irep_zero;
   irep->refcnt = 1;
+  irep->own_filename = FALSE;
 
   return irep;
 }
-- 
2.11.0
```

```diff
From ee8cfffe308f40aa31fb78a8b8f624b1439a7a7f Mon Sep 17 00:00:00 2001
From: Jonathan Rudenberg <jonathan@titanous.com>
Date: Fri, 23 Dec 2016 18:23:27 -0500
Subject: [PATCH 2/2] Fix leak of state->iseq during codegen error

---
 mrbgems/mruby-compiler/core/codegen.c | 1 +
 1 file changed, 1 insertion(+)

diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c
index 3bae67c6..b808cfb7 100644
--- a/mrbgems/mruby-compiler/core/codegen.c
+++ b/mrbgems/mruby-compiler/core/codegen.c
@@ -93,6 +93,7 @@ codegen_error(codegen_scope *s, const char *message)
   if (!s) return;
   while (s->prev) {
     codegen_scope *tmp = s->prev;
+    mrb_free(s->mrb, s->iseq);
     mrb_pool_close(s->mpool);
     s = tmp;
   }
-- 
2.11.0
```


## Attachments
No attachments
