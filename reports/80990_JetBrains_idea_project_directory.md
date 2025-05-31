# JetBrains .idea project directory

## Report Details
- **Report ID**: 80990
- **URL**: https://hackerone.com/reports/80990
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-08-06T22:14:23.320Z
- **Disclosed**: 2019-09-19T15:52:32.803Z

## Reporter
- **Username**: linkks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Vulnerability description
The .idea directory contains a set of configuration files (.xml) for your project. These configuration files contain information core to the project itself, such as names and locations of its component modules, compiler settings, etc. If you've defined a data source the file dataSources.ids contains information for connecting to the database and credentials. The workspace.xml file stores personal settings such as placement and positions of your windows, your VCS and History settings, and other data pertaining to the development environment. It also contains a list of changed files and other sensitive information. These files should not be present on a production system.
This vulnerability affects /. 
Discovered by: Scripting (JetBrains_Idea_Project_Directory.script). 
Attack details
workspace.xml project file found at : /.idea/workspace.xml
Pattern found: 
<project version="4">

Request
GET /.idea/workspace.xml HTTP/1.1
Cookie: Vanilla-tk=5bf318378b39b486
Host: forum-es.ubnt.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

Response
HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Type: application/xml
Date: Thu, 06 Aug 2015 15:24:12 GMT
ETag: "4c42-51bf15d10be80-gzip"
Last-Modified: Tue, 28 Jul 2015 15:45:46 GMT
Server: Apache/2.4.7 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 19522
Connection: keep-alive
Original-Content-Encoding: gzip

The impact of this vulnerability
These files may expose sensitive information that may help an malicious user to prepare more advanced attacks.

How to fix this vulnerability
Remove these files from production systems or restrict access to the .idea directory. To deny access to all the .idea folders you need to add the following lines in the appropriate context (either global config, or vhost/directory, or from .htaccess): 
<Directory ~ "\.idea">
Order allow,deny
Deny from all
</Directory>

http://www.ducea.com/2006/08/11/apache-tips-tricks-deny-access-to-some-folders/

## Attachments
No attachments
