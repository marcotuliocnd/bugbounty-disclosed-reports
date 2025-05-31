# S3 bucket data at http://rockset-support.s3-us-west-2.amazonaws.com/ reveals user addresses based on latitudes and longitudes.

## Report Details
- **Report ID**: 947725
- **URL**: https://hackerone.com/reports/947725
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-30T09:51:44.819Z
- **Disclosed**: 2020-08-05T14:38:57.976Z

## Reporter
- **Username**: boy_child_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockset

## Vulnerability Information
At the s3 bucket located at http://rockset-support.s3-us-west-2.amazonaws.com/, a file was found called ``data.json.15``that contains of interest latitudes and latitudes of user addresses.
{F930036}

**Steps to reproduce:**
1, Download the file in the bucket with the command:
```
aws s3 sync s3://rockset-support .
```
2. Open the file labelled ``data.json.15``.
3. For each line, there will be a set of latitudes and longitudes. Copy a single pair. 
{F930037}

4. Open Google Maps, enter the coordinates and click search.
{F930058}

## Impact

Specific user location information violates the privacy policy stated by Rockset for its users allowing both targeted phishing attacks and physical risk.

## Attachments
No attachments
