# Information Exposure Through Directory Listing

## Report Details
- **Report ID**: 1316412
- **URL**: https://hackerone.com/reports/1316412
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-08-23T13:28:52.083Z
- **Disclosed**: 2021-08-27T11:15:01.488Z

## Reporter
- **Username**: sasikaran
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
##Vulnerability description
The web server is configured to display the list of files contained in this directory. This is not recommended because the directory may contain files that are not normally exposed through links on the web site.

##Link as POC:

https://www.torproject.org/static/
https://www.torproject.org/static/css/
https://www.torproject.org/static/findoc/
https://www.torproject.org/static/fonts/
https://www.torproject.org/static/js/
https://www.torproject.org/static/images/
https://www.torproject.org/static/keys/

For obvious reasons, I can not check whether this service is in scope, thats why i haven't searched for any critical informations and haven't check tokens and other stuff
Please let me know if you need some extra information.
Sorry for out of scope report, i thought it could be informative for you!
Thanks in advance!

## Impact

Exposing the contents of a directory can lead to an attacker gaining access to source code or providing useful information for the attacker to devise exploits, such as creation times of files or any information that may be encoded in file names. The directory listing may also compromise private or confidential data.

## Attachments
- Screenshot_from_2021-08-23_18-42-30.png
- Screenshot_from_2021-08-23_18-42-39.png
- Screenshot_from_2021-08-23_18-42-53.png
- Screenshot_from_2021-08-23_18-50-31.png
- Screenshot_from_2021-08-23_18-43-53.png
