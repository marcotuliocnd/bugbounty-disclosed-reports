# Two vulnerabilities in the ssl module

## Report Details
- **Report ID**: 159696
- **URL**: https://hackerone.com/reports/159696
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-16T09:41:04.755Z
- **Disclosed**: 2019-11-12T09:01:44.536Z

## Reporter
- **Username**: tehybel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I found two vulnerabilities in python's ssl module. 

The first is a Py_XDECREF call on an object which isn't owned, leading to use-after-free and/or double free scenarios.
The second vulnerability is an uninitialized variable use. 
  
I described both issues in detail in a mail to the PSRT. The mail and fix for both issues is here:

https://bugs.python.org/issue27773

## Attachments
No attachments
