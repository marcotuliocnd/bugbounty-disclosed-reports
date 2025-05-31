# Overwrite any file of the web server

## Report Details
- **Report ID**: 2733190
- **URL**: https://hackerone.com/reports/2733190
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-09-21T16:05:51.919Z
- **Disclosed**: 2024-11-05T05:11:59.942Z

## Reporter
- **Username**: goedix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mactaggart_scott

## Vulnerability Information
## Summary:
With this vulnerability an attacker can override all the files from the server due to a vulnerable module used to generate █████████s

## Steps To Reproduce:

  1. Go to ██████████ to check the actual payload (*Save ███████ to:*) to do it (███████goedix.php -> This will create a file in /██████_h1goedix.php but this can be edited to index.php and replacing any php file in the server or outside the web server) █████
  1. Go to ███████ to start the job that creates the ███ in the target filepath
  1. Go to https://██████████_h1goedix.php or the targeted file and check that it returns an empty page! ██████████

> As note, if you want to do any action in /█████████ you must modify with burp the request from `/█████████/index.php` to `/██████████`, otherwises it won't  work!

## Impact

An attacker can replace all the server files with empty pages! (I was finding to achieve RCE but I was not able to do it (I did tests injecting php code into the php files but it returns 500 internal server error)

## Attachments
No attachments
