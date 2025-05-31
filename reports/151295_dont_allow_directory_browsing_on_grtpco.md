# don't allow directory browsing on grtp.co

## Report Details
- **Report ID**: 151295
- **URL**: https://hackerone.com/reports/151295
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-07-14T10:05:08.067Z
- **Disclosed**: 2016-07-14T10:21:59.231Z

## Reporter
- **Username**: zuh4n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello guys,

**_Details:_**
The web server is configured to display the list of files contained in this directory. As a result of a misconfiguration - end user / attacker able to see content of the folders with systemically important files
According to yours **Scope** (any other software we publish) - I found that one of sites: **_grtp.co_** is vulnerable to Directory listening

**_Vulnerable place:_**
http://grtp.co/v1/
http://grtp.co/v2/

**_PoC:_**

{F104876}

**_Impact:_**
Exposing the contents of a directory can lead to an attacker gaining access to source code or providing useful information for the attacker to devise exploits, such as creation times of files or any information that may be encoded in file names. The directory listing may also compromise private or confidential data.

**_Remediation:_**
- Configure your web server to prevent directory listings for all paths beneath the web root;
- Place into each directory a default file (such as index.htm) that the web server will display instead of returning a directory listing.

Let me know if you have any question.

Thanks for your attention,
Stas

## Attachments
- grtp.jpg
