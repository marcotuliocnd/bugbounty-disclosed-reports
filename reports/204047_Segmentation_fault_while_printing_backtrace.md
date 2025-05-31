# Segmentation fault while printing backtrace

## Report Details
- **Report ID**: 204047
- **URL**: https://hackerone.com/reports/204047
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-06T23:57:57.045Z
- **Disclosed**: 2017-03-14T21:11:22.179Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The code below crashes the sandbox/mruby as it tries to print the backtrace. Incidentally, it does not crash mirb.
```
def foo(n)
  return '\' 
  if n \n' ensure % 
  if:n != if n == -1110
  else foo(n-1).%  
  end
end %foo(0)
```

We are still examining the bug and hope to produce a detailed analysis and a fix this week.

Thank you,
Dinko Galetic
Denis Kasak


## Attachments
No attachments
