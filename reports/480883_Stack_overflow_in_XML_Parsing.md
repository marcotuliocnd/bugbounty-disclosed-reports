# Stack overflow in XML Parsing

## Report Details
- **Report ID**: 480883
- **URL**: https://hackerone.com/reports/480883
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-16T11:03:23.213Z
- **Disclosed**: 2019-08-25T12:50:13.333Z

## Reporter
- **Username**: ammm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: notepad-plus-plus

## Vulnerability Information
**Summary:** 

A stack buffer overflow vulnerability has been detected in XML parsing functionality  on Notepad++.

That's due to the fact that _invisibleEditView.getText function doesn't check buffer boundaries.

**Description:** 
Vulnerability src file: notepad-plus-plus/PowerEditor/src/Notepad_plus.cpp
Vulnerability line: line 1008
Variable affected: char encodingStr[128];
Function that overflows buffer: _invisibleEditView.getText

## Steps To Reproduce:

  1. Create a .xml file with a correct XML format
  2. Introduce a big XML field that overflows "encodingStr" buffer.
  3. Open the file with Notepad++ and application should crash.

## Supporting Material/References:

  * BoF_example1.xml -> Exploit example

## Impact

An attacker could create a malicious .xml file that triggers a stack buffer overflow on victim machine.

You only need to open attached .xml file example with Notepad++ to reproduce the exploit.

## Attachments
- BoF_Example1.xml
