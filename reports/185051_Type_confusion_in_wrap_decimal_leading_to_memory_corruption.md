# Type confusion in wrap_decimal leading to memory corruption

## Report Details
- **Report ID**: 185051
- **URL**: https://hackerone.com/reports/185051
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-11-25T10:04:55.525Z
- **Disclosed**: 2017-01-15T20:03:46.620Z

## Reporter
- **Username**: raydot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Decimal can be redefined, causing the Decimal class lookup in wrap_decimal to be invalid. This can lead to memory corruption or arbitrary code execution.

The following snippet results in a native crash in mruby-engine
    olddecimal = Decimal.new(1)
    Decimal = Hash
    a = -olddecimal
    puts a

I suspect you caught this along with charliesome's similar bug for Struct. If not I'll follow up with a patch and an RCE exploit.

## Attachments
No attachments
