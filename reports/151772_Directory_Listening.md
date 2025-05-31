# Directory Listening

## Report Details
- **Report ID**: 151772
- **URL**: https://hackerone.com/reports/151772
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-16T15:51:31.651Z
- **Disclosed**: 2016-09-14T15:07:28.460Z

## Reporter
- **Username**: kiraak-boy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gocd

## Vulnerability Information
Hello Team,

Found Directory Listening :

http://IP:8153/go/NOTICE/

{F105317}


There is not usually any good reason to provide directory listings, and disabling them may place additional hurdles in the path of an attacker. This can normally be achieved in two ways:
Configure your web server to prevent directory listings for all paths beneath the web root;
Place into each directory a default file (such as index.htm) that the web server will display instead of returning a directory listing.

Thanks!

Best,
Arbaz

## Attachments
- dir.jpg
