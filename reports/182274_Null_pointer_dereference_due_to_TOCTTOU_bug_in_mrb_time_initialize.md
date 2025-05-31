# Null pointer dereference due to TOCTTOU bug in mrb_time_initialize

## Report Details
- **Report ID**: 182274
- **URL**: https://hackerone.com/reports/182274
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-15T13:01:54.580Z
- **Disclosed**: 2017-01-15T19:56:05.964Z

## Reporter
- **Username**: raydot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
mrb_time_initialize sets the data pointer to NULL before parsing function arguments. Parsing function arguments can call out to ruby code to call methods to do type coercion. If the type coercion method tries to access the time object it will dereference a NULL pointer.

The following snippet results in a native crash under mruby-engine:
```
$x = Time.new
class Tmp
    def to_i
        $x.mday
    end
end
$x.initialize Tmp.new
```

Attached is a patch to mruby to fix this issue.

## Attachments
- patch4.diff
