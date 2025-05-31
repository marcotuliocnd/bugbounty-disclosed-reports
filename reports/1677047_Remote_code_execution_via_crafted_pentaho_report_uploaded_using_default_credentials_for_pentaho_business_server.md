# Remote code execution via crafted pentaho report uploaded using default credentials for pentaho business server

## Report Details
- **Report ID**: 1677047
- **URL**: https://hackerone.com/reports/1677047
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-08-22T18:07:27.373Z
- **Disclosed**: 2023-12-31T21:08:44.212Z

## Reporter
- **Username**: zer0code
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Good day,
                      While I do recon for mtn.ci domain I found  Pentaho business server at https://sm.mtn.ci:8888/pentaho with default credentials admin/password ,then I figured that I can upload  prpt reports to server which could use some beanshell,js and java to achieve RCE

## Steps To Reproduce:
1. Login to https://sm.mtn.ci:8888/pentaho admin/password  
{F1878259}
2. Use Pentaho report designer to create malicious report file  
{F1878260}
3. Upload and run the report   
{F1878261}  
{F1878262}

## Impact

The impact of an RCE vulnerability can range from malware execution to an attacker gaining full control over a compromised server.

## Attachments
- 02.png
- 01.png
- 03.png
- 04.png
