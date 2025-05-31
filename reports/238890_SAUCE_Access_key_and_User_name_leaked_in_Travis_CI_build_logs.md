# SAUCE Access_key and User_name leaked in Travis CI build logs

## Report Details
- **Report ID**: 238890
- **URL**: https://hackerone.com/reports/238890
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-11T04:40:20.704Z
- **Disclosed**: 2017-07-12T15:47:02.929Z

## Reporter
- **Username**: an0n-j
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
hello algolia team,
I founded the SAUCE Access_Key and User_name was leaked in Travis CI build logs of instantsearch.js product [#Line-249-&-250](https://travis-ci.org/algolia/instantsearch.js/builds/225176027#L249).
This can be used to perform every API calls of sauce-lab.(e.g Creating a Sub account. I created a test account for testing. sorry for this ;) ).

You should revoke the access_key and secure the key in Travis Cl build logs.

## Attachments
No attachments
