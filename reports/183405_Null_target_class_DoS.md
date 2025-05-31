# Null target_class DoS

## Report Details
- **Report ID**: 183405
- **URL**: https://hackerone.com/reports/183405
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-19T02:41:38.411Z
- **Disclosed**: 2016-12-17T01:02:59.955Z

## Reporter
- **Username**: h72
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The `Object#instance_exec` method in `mrbgems/mruby-object-ext/src/object.c` executes a block in the context of an object. It sets the VM's `target_class` pointer to the singleton class of this object. `target_class` is used as the definition target for constants and methods.

If a singleton class cannot be created for an object, `target_class` is set to `NULL`. The `OP_CLASS` and `OP_MODULE` opcodes in the VM assume `target_class` is not null when defining new classes and modules.

This causes a null pointer dereference and segfaults the mruby VM.

Sample code:

```
1.instance_exec { class X; end }
```

## Attachments
No attachments
