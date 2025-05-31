# Local File Disclosure on the ████████ (https://████/) leads to the source code disclosure & DB credentials leak

## Report Details
- **Report ID**: 685344
- **URL**: https://hackerone.com/reports/685344
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-31T01:46:36.296Z
- **Disclosed**: 2021-01-12T21:53:16.766Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
I discovered another LFD on the https://████/ (virtual host on the █████ IP)

##POC
https://█████/file.ashx?path=web.config
will download the website configuration file.
It exposes different DB credentials than in previous reports:
███

Similarly, attacker able to get content of any server-side file, such as source code of application:
https://███/file.ashx?path=index.aspx

## Impact

Source code & sensitive configuration data leakage. Attacker can use it to compromise the resource.

## Attachments
No attachments
