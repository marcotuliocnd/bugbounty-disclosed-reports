# Incorrect code generation when result of NODE_NEGATE is not used

## Report Details
- **Report ID**: 191689
- **URL**: https://hackerone.com/reports/191689
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-16T13:39:39.239Z
- **Disclosed**: 2017-01-12T00:37:02.807Z

## Reporter
- **Username**: dkasak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Introduction
============

Not using the result of `NODE_NEGATE` leads to incorrect code generation which could possibly result in arbitrary bytecode generation. Currently it is possible to produce a crash through a SIGABRT via an `assert` failure.

Proof of concept
================

assert_failure.rb
-------------

    -0E00;0

1. Run either:

    a. `mruby assert_failure.rb`
    b. `sandbox assert_failure.rb`

2. Both cause a crash via an `assert` failure.

Discussion
==========

The flaw was introduced in commit `d56a19cbf526190de036130fe3a5bf14a0705ee2`.

The problem is that `codegen` is called recursively on the argument of `NODE_NEGATE` without checking whether it is a valid node. This is problematic because `codegen` assumes that its `tree` argument is a valid node (i.e. that the node's type is stored under the `car` member, further nodes or data under the `cdr` member and that `filename_index` and `lineno` are set properly). This creates an opportunity for the attacker to control further code generation, though it might not be possible to place a valid node type in `car` with the current codebase. Nevertheless, `filename_index` *can* be controlled and this is what allows the POC to make the assertion on line 135 of `debug.c` fail:

    ruby: ext/mruby_engine/mruby/src/debug.c:135: mrb_debug_info_append_file: Assertion `irep->filename' failed.
    zsh: abort      mruby-engine/bin/sandbox assert_failure.rb

Running mruby with the following input in gdb:

    -0.5555555555555555555;0

And breaking on `parse.y:2885`, we can see that `filename_index` is set to 13621 (which is two '5' characters interpreted as an integer):

    (gdb) x/16hd yyvsp[0].nd->cdr
    0x79162c:       11824   13621   13621   13621   13621   13621   13621   13621
    0x79163c:       13621   13621   53      0       52      0       0       0
    (gdb) p yyvsp[0].nd->cdr->filename_index 
    $21 = 13621

Then, breaking `codegen.c:1230`, we see that `tree->filename_index` is indeed set to 13621:

    (gdb) p tree->filename_index
    $22 = 13621

This eventually leads to `assert` to fail.

Solution
========

To fix the problem, we should ensure `tree->car` is a valid node before calling `codegen` on `tree` in the case of `NODE_NEGATE`.

negate_node.patch
-----------------

    diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c
    index 90bafb3..9d47cca 100644
    --- a/mrbgems/mruby-compiler/core/codegen.c
    +++ b/mrbgems/mruby-compiler/core/codegen.c
    @@ -2232,7 +2232,9 @@ codegen(codegen_scope *s, node *tree, int val)
        nt = (intptr_t)tree->car;
        tree = tree->cdr;
        if (!val) {
    -        codegen(s, tree, NOVAL);
    +        if (tree && (intptr_t)tree->car < NODE_LAST) {
    +          codegen(s, tree, NOVAL);
    +        }
            break;
        }
        switch (nt) {

--
Denis Kasak


## Attachments
- assert_failure.rb
- 0001-Fix-code-generation-when-NODE_NEGATE-result-is-not-u.patch
