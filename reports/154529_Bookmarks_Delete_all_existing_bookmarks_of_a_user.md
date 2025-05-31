# Bookmarks: Delete all existing bookmarks of a user

## Report Details
- **Report ID**: 154529
- **URL**: https://hackerone.com/reports/154529
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-28T07:48:03.410Z
- **Disclosed**: 2016-08-08T09:28:32.416Z

## Reporter
- **Username**: ctee
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
A logical bug in the bookmark app makes it possible to delete all the existing bookmarks of the user. 

Here are the steps to reproduce: 
- Create  couple of valid bookmarks
- Import a bookmark.html file that contains the line **<a href="">Bookmark</a>**. All the bookmarks of the user is replaced with blank url and Bookmark as description. 
- This is potentially a risk where a user could be sent malicious html file to delete the bookmarks or this could even happen unintentionally if the user uploads a html with blank urls. 

The logical flaw resides in the method **/apps/bookmarks/controller/lib/bookmarks.php** -> **addBookmark**  where SQL query will select all the bookmarks and update them. 



## Attachments
- screenshot1.png
- screenshot2.png
- urltest.html
