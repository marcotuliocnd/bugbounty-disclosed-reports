# Potential code injection in fun delete_directory

## Report Details
- **Report ID**: 250587
- **URL**: https://hackerone.com/reports/250587
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-17T17:33:10.329Z
- **Disclosed**: 2017-09-07T14:56:56.831Z

## Reporter
- **Username**: freetom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: expressionengine

## Vulnerability Information
Under /system/ee/legacy/libraries/Functions.php, function delete_directory contains calls to `exec` 3 times using different, potentially "unsanitized" paramateres. As the PHP manual suggest, `escapeshellarg` should be used to sanitize individual arguments [1]. 

On an implementation in which the attacker controls the file name, arbitrary code execution is achieved. Better to fix it.

[1] http://php.net/manual/en/function.escapeshellarg.php

## Attachments
No attachments
