# Internal attachments can be exported via "Export as .zip" feature

## Report Details
- **Report ID**: 186230
- **URL**: https://hackerone.com/reports/186230
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-29T03:04:52.536Z
- **Disclosed**: 2016-11-30T09:18:19.878Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello HackerOne Team

This newly disclosed report: #182358 __Partial disclosure of report activity through new "Export as .zip" feature__ was not completely fix.

I have found that i can still view the attachment after it is being removed on the thread.

Best PoC is this #182358 since this is the newly fix and disclosed.

Steps to reproduce

  1. Go to https://hackerone.com/reports/182358
  2. Export the report as .zip
  3. Now extract the .zip file (`HackerOne_Report-security#182358.zip`)
  4. You will see that the image is still there, but base on the thread, you guys removed it on disclosed report.

I have attached the .zip file downloaded and save on my local and i can still view the removed image.

__Disclosed partially removed attachment:__ {F138022}

Regards
Japz


## Attachments
No attachments
