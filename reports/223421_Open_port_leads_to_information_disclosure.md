# Open port leads to information disclosure

## Report Details
- **Report ID**: 223421
- **URL**: https://hackerone.com/reports/223421
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T12:25:25.022Z
- **Disclosed**: 2018-09-10T09:40:40.291Z

## Reporter
- **Username**: str33
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Open port 10022 leads to disclosure of open-ssh version and current Debian version being used.

POC- 
1. I performed an nmap scan ( nmap -A -T4 -p- weblate.org)
2. I saw the port 10022 was open and I did a telnet connect to the port.
3. As soon as I did the telnet connect it returned me the openssh version and the debian version (check the .png file)
4.I wasn't able to run any sort of commands as whatever I typed returned a protocol mismatch error.


This doesn't necessarily mean a security issue as long as everything is being patched regularly. 


## Attachments
- Capture.PNG
