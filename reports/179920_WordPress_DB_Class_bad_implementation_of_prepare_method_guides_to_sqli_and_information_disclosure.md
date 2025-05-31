# WordPress DB Class, bad implementation of prepare method guides to sqli and information disclosure

## Report Details
- **Report ID**: 179920
- **URL**: https://hackerone.com/reports/179920
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-11-03T13:32:17.535Z
- **Disclosed**: 2017-11-13T14:56:48.898Z

## Reporter
- **Username**: b258ea62bf297b02afa9854
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Issue 1: Method checks if first argument is an array and if it is, it avoids the rest of the arguments and uses the first argument array values as input.

Issue 2: When input query has %s in it, then it quote and this guides to sql injection in case query that need to be prepared have quoted user controlled input in it.  

This leaves all wordpress plugins/ themes potentially vulnerable on this two types of attack. As PoC sqli in bbpress wp plugin and core wp function is shown.

PoC: 
1. There is SQLi in bbpress in case anonymous posting is allowed. ( check  bbpress-sqli.png)
2.  Demo for the Issue 1 and Issue 2 for the prepare method
3. Wordpress core function delete_metadata is vulnerable to sqli in case delete all e.g. last argument is true and meta value has value e.g. is user supplied / controlled.

## Attachments
- bbpress-sqli.png
- dh1.php
