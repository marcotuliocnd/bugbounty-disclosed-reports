# DoS: type confusion in mrb_no_method_error

## Report Details
- **Report ID**: 181871
- **URL**: https://hackerone.com/reports/181871
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-11-13T03:58:33.109Z
- **Disclosed**: 2017-03-01T21:25:22.719Z

## Reporter
- **Username**: raydot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Overwriting the 'new' method of the NoMethodError singleton to not return an exception object leads to memory corruption and possibly arbitrary code execution.

Running the following code under the mruny-engine sandbox script results in a native crash:
    NoMethodError.define_singleton_method(:new) do "waat" end
    Object.q

Attached is a patch to mitigate the issue.


## Attachments
- patch1.diff
