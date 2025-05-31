# End-to-end encrypted file-drops can be made inaccessible

## Report Details
- **Report ID**: 1914115
- **URL**: https://hackerone.com/reports/1914115
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-03-21T20:28:56.615Z
- **Disclosed**: 2023-06-22T06:13:57.173Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Assume a filedrop that is send to 2 people, USER and ATTACKER

1. user uploads their E2EE encrypted fileA into the filedrop
2. All goes well
3. Now ATTACKER comes along and wants mess up the upload from USER
4. They obtain the metadatafile
5. They modify the entry in the filedrop list that USER created
6. They upload their new metadatafile
7. Unlock it
8. FileA is now not able to be decoded at all anymore.

## Impact

The CIA model (Confidentiality, integrity and availability) is here very easy to break. An attacker can almost trivially in this case break the availability.
Note that due to the nature of providing the metadatafile an attacker can trivially know if there are other filedrop files.

To solve
1. Do not provide the metadata file to the user in file drop at all
2. Only send back the new entry (which they can create without the metadatafile)
3. Append the new entry in the backend code.

## Attachments
No attachments
