# Moving a report to a different program doesn't reassign the Custom Field Values

## Report Details
- **Report ID**: 511779
- **URL**: https://hackerone.com/reports/511779
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-18T18:18:07.087Z
- **Disclosed**: 2019-04-25T16:40:53.709Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
When a report is moved to a different program, all associated objects are either removed or copied to the new program. During an internal security review of the Custom Fields feature it was observed that this isn't the case for Custom Field Values. This means that even after a report has moved, the report is referencing an object that may not belong to a program the user controls.

# Proof of concept

* Submit a report to a program where you have the ability to move the report to another program
* Move the report to a program you also have access to
* Confirm through the Rails console that the report references values that belong to the program the report was submitted to

## Impact

The associated values and attributes may leak confidential information, either through the value itself or updating the attributes at a later point in time.

## Attachments
No attachments
