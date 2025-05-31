# XMLRPC, Enabling XPSA and Bruteforce and DOS + A file disclosing installer-logs.

## Report Details
- **Report ID**: 865875
- **URL**: https://hackerone.com/reports/865875
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-04T17:15:07.880Z
- **Disclosed**: 2021-06-14T08:02:16.423Z

## Reporter
- **Username**: tandav
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
[XMLRPC+Installer_logs+Backup_Filename+Admin_username+disclosure]

## Steps To Reproduce:

  1. I was able to successfully exploit XMLRPC with the traditional method, the brute-force was done the username was there in the Installer Logs
  2. path to XMLRPC is http://13.92.255.102/xmlrpc.php + the username is in https://lonestarcell.com/installer-log.txt 
  3. Pingback ping can be used to dos the target server when mishandled
## Supporting Material/References:
I was able to reproduce this whole https://www.netsparker.com/blog/web-security/xml-rpc-protocol-ip-disclosure-attacks/

## Impact

1)Automated once from multiple hosts and be used to cause a mass DDOS attack on the victim.
2) This method is also used for brute force attacks to stealing the admin credentials and other important credentials
3) File disclosure is causing most harm as internal criticals are popping out

## Attachments
No attachments
