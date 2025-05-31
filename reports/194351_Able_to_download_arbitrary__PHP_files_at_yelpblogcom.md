# Able to download arbitrary  PHP files at yelpblog.com

## Report Details
- **Report ID**: 194351
- **URL**: https://hackerone.com/reports/194351
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-12-28T07:43:55.562Z
- **Disclosed**: 2017-02-06T06:24:03.366Z

## Reporter
- **Username**: ret2jazzy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
There is a misconfigured wordpress installation at yelpblog.com, through which i am able to download any php files in wp-includes folder.

For a PoC, you can open https://www.yelpblog.com/wp-includes/wp-db.php, and the wp-db.php will be download(along with all the data in it)

As we all know that these PHP files can sensative information of a website, and the wp-includes folder is the base of a WordPress installation, Being able to download php files is a clearly wrong behaviour of a wordpress installation.
The PHP files in wp-includes can have a lot of sensative information about the server, which may help a attacker in compromising the server. He can even do a source code analysis if he is able to download arbitrary 
PHP files.


## Attachments
- PHP.png
