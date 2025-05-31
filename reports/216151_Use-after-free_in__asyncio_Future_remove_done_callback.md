# Use-after-free in _asyncio_Future_remove_done_callback

## Report Details
- **Report ID**: 216151
- **URL**: https://hackerone.com/reports/216151
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-26T04:18:18.622Z
- **Disclosed**: 2019-11-12T09:00:49.248Z

## Reporter
- **Username**: nedw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
http://bugs.python.org/issue28963

Callbacks could be removed from a list while it was iterated, leading to an out of bounds access. A fix for this bug is now in the CPython repository.

## Attachments
No attachments
