# Directory listening enabled in: 88.198.160.130

## Report Details
- **Report ID**: 156510
- **URL**: https://hackerone.com/reports/156510
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-04T14:18:19.756Z
- **Disclosed**: 2016-09-04T12:39:10.493Z

## Reporter
- **Username**: sandh0t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Summary:
=========
The Directory Listing option is still enabled in the web server **88.198.160.130** , which displays all the files and folders contained in the directories:
 **core** 
**apps**
**config**
**lib**
**settings**
**resources**

PoC:
====
Visit the following links:
```
http://88.198.160.130/core/
http://88.198.160.130/apps/
http://88.198.160.130/config/
http://88.198.160.130/lib/
http://88.198.160.130/settings/
http://88.198.160.130/resources/
```

## Attachments
- dir_list_1.PNG
- dir_list_3.PNG
- dir_list_2.PNG
- dir_list_4.PNG
