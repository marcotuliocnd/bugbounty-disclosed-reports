# Open FTP on ███

## Report Details
- **Report ID**: 197976
- **URL**: https://hackerone.com/reports/197976
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-13T00:03:02.633Z
- **Disclosed**: 2019-12-02T18:33:41.729Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
FTP panel Allows anyone to connect to the FTP server,viewing and downloading any files hosted there. This isn't recommend especially if any sensitive information is stored

## Impact
High severity vulnerability allowing total information disclosure of internal directories, and being allowed internal access to the website.
## Step-by-step Reproduction Instructions

1. Connect to ████ or using an ftp program like Filezilla 
2. you'll see you have access below is a snippet 
```
220-You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. 
230 Login successful.
214-The following commands are recognized.
 ABOR ACCT ALLO APPE CDUP CWD  DELE EPRT EPSV FEAT HELP LIST MDTM MKD
 MODE NLST NOOP OPTS PASS PASV PORT PWD  QUIT REIN REST RETR RMD  RNFR
 RNTO SITE SIZE SMNT STAT STOR STOU STRU SYST TYPE USER XCUP XCWD XMKD
 XPWD XRMD
214 Help OK.
```

## Suggested Mitigation/Remediation Actions
Disable anonymous log in and create ftp accounts that follow security protocols 

## Attachments
No attachments
