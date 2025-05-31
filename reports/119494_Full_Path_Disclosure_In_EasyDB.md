# Full Path Disclosure In EasyDB

## Report Details
- **Report ID**: 119494
- **URL**: https://hackerone.com/reports/119494
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-29T17:26:30.545Z
- **Disclosed**: 2017-10-16T05:53:39.984Z

## Reporter
- **Username**: supernatural
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Hi,

as reported in #115337
about a full path disclosure in EasyDB

you fixed some of them in last commits
but `single` function is vulnerable too and not fixed yet!

    if(count($params) != count($params,COUNT_RECURSIVE)){
                throw new \InvalidArgumentException("Invalid params");
    }
this will check $params to be 1d array,
add this code before line 366 in EasyDB.php


Regards

## Attachments
- easydb.png
