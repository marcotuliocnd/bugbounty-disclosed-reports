# Undefined method_missing null pointer dereference

## Report Details
- **Report ID**: 181695
- **URL**: https://hackerone.com/reports/181695
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-12T03:27:22.300Z
- **Disclosed**: 2016-12-17T01:03:38.615Z

## Reporter
- **Username**: h72
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
It's possible to segfault mruby by undefining `BasicObject#method_missing` in certain cases.

There is a fallback method_missing C function (`mrb_method_missing`) which is called in _some_ cases when the VM fails to look up the `method_missing` method:

    > BasicObject.remove_method(:method_missing); 1.foo
    NoMethodError: undefined method 'foo' for 1

However the `mrb_method_missing` fallback is not consistently used.

`Kernel#__send__` calls into `mrb_funcall_with_block` in `vm.c`, which contains the following code at line 362 (as of commit 88604e39ac9c25ffdad2e3f03be26516fe866038):

        c = mrb_class(mrb, self);
        p = mrb_method_search_vm(mrb, &c, mid);
        if (!p) {
          undef = mid;
          mid = mrb_intern_lit(mrb, "method_missing");
          p = mrb_method_search_vm(mrb, &c, mid);
          n++; argc++;
        }

If the method search for `method_missing` fails, `p` will be a null pointer. Further down on line 380, `p` is tested with `MRB_PROC_CFUNC_P`, which deferences `p`.

This segfault can be reproduced with the following code:

    BasicObject.remove_method(:method_missing)
    1.__send__(:foo)

The method search logic in the `OP_SUPER` instruction is also buggy. The same bug can be triggered through `OP_SUPER` with the following code:

    BasicObject.remove_method(:method_missing)

    class A
      def foo
        super
      end
    end

    A.new.foo

I'm not familiar enough with the mruby VM internals to write a patch for this. It _should_ just be a matter of making sure `mrb_method_missing` is called if a `method_missing` method search fails (as the logic in `OP_SEND` instruction does).

## Attachments
No attachments
