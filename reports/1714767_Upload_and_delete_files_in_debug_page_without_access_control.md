# Upload and delete files in debug page without access control.

## Report Details
- **Report ID**: 1714767
- **URL**: https://hackerone.com/reports/1714767
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-28T02:10:27.921Z
- **Disclosed**: 2023-02-24T18:40:53.460Z

## Reporter
- **Username**: 0r10nh4ck
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
I found a debug page with no access control that allows:
- Uploading files.
- Reading files if they are in JSON format.
- Delete files.

## Impact

- Insufficient access control.
- An attacker can delete files exposed by the application.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
## For upload file:
1. Use a browser to navigate to: https://█████/debug. 
2. Click on choose file button.
3. Set the file path in the location field
4. Click on the upload files button.
5.See the file uploaded on the list.

## For Read File
1. Select the file.
2. Click and Read File Content.
3. See the content file.

## For delete file:
1. Select the file.
2. Click on the Delete ENC Files button.

## Suggested Mitigation/Remediation Actions
- Implement access control on the page.



## Attachments
No attachments
