# heap-buffer-overflow in gc_writebarrier_incremental

## Report Details
- **Report ID**: 1940002
- **URL**: https://hackerone.com/reports/1940002
- **State**: Closed
- **Severity**: none
- **Submitted**: 2023-04-09T13:21:30.598Z
- **Disclosed**: 2023-07-19T09:24:48.110Z

## Reporter
- **Username**: piao
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
how to reproduce:
build ruby-3.2.2 with asan
cat heap-buffer-overflow | ruby-3.2.2/miniruby -e 'Marshal.load(ARGF.read)'

## Impact

may over access memory

## Attachments
- heap_buffer_overflow
- heap_buffer_overflow.png
