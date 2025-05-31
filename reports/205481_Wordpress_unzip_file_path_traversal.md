# Wordpress unzip_file path traversal

## Report Details
- **Report ID**: 205481
- **URL**: https://hackerone.com/reports/205481
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-11T12:11:51.002Z
- **Disclosed**: 2020-01-29T20:27:37.751Z

## Reporter
- **Username**: ajxchapman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
# Summary
The Wordpress unzip_file function (https://codex.wordpress.org/Function_Reference/unzip_file) is vulnerable to path traversal when extracting zip files. Extracting untrusted zip files using this function this could lead to code execution through placing arbitrary PHP files in the DocumentRoot of the webserver.

# Analysis
The unzip_file function takes a target directory, `$to`, as an argument into which the files in the zip should be extracted. If a maliciously crafted zip file is extracted with a filename starting with the parent directory specifier (`../`) the file will be extracted into the parent of the '$to' argument target directory. Filenames can be crafted in order to place files in any directory which the webserver has write permissions, for example a zip entry with a filename of `../../../../../../../../../../tmp/poc_file` would place the file contents in the '/tmp/poc_file' directory.

This vulnerability exists both when unzip_file uses PHP's built-in ZipArchive (/wp-admin/includes/file.php:`_unzip_file_ziparchive`) and the 3rd party PclZip (/wp-admin/includes/file.php:`_unzip_file_pclzip`) extraction methods. Neither of these functions check to confirm that the normalised output path is within the `$to` target directory.

An example zip, 'zip_poc.zip' is attached. If this is extracted with the unzip_file function, for example through the "Upload Plugin" admin function or the attached 'poc.php', a file called 'poc_output' will be extracted to the operating system '/tmp' directory. The 'poc.php' attachment shows how the unzip_file function may be used in a wordpress plugin. This Proof of Concept has been tested on Wordpress 4.7.2 running on Ubuntu 14.04 LTS.

It should be noted that the built-in PHP ZipArchive extractTo method is not vulnerable to this path traversal.

Cursory analysis of a number of popular Wordpress plugins suggests that gallery plugins, such as NextGen Gallery, which allow lower privilege non-admin users to upload zips to be extracted would be particularly susceptible to this issue.

# Suggested Remediation
The `_unzip_file_ziparchive` and `_unzip_file_pclzip` functions should normalise the output paths of zip file entries ensuring that after normalisation the paths reside within the `$to` argument target directory.

## Attachments
- zip_poc.zip
- poc.php
- Screen_Shot_2017-02-11_at_12.01.59.png
- Screen_Shot_2017-02-11_at_12.00.10.png
