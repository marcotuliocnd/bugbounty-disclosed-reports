# Private partial disclosure of h1 infrastructure 

## Report Details
- **Report ID**: 283361
- **URL**: https://hackerone.com/reports/283361
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-10-26T22:17:15.436Z
- **Disclosed**: 2017-11-03T00:29:44.632Z

## Reporter
- **Username**: exadmin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Description**
I've found that following servers & services can be potentially interesting when attacking h1-infrastructure:
* Payments Admin ██████
* API Docs ██████████
* API █████████
* MailCatcher ██████████
* Story Book ███
* Karma ████████
* Core Test Server █████████
* Core Staging ████
* Core Production https://hackerone.com/
* Support Staging ███████
* Support Production █████████
* Payments Staging ███████
* Payments Production █████

At least ███ are enabled via Internet.
For example ████ is using Basic Authentication without any throtlling.
I've write JMeter script that performs bruteforcing by dictionary (nothing was found by 10K attempts but I've stopped bruteforcing as I do not understant possible impact on your staging service).

In my practice Staging servers often use forks of production data with some obfuscation of very sensitive data. But, any way real sensitive data can be still found in such instances and used against production.

**Steps to reproduce**
* login to the application and go to /bugs page
* find that███████.███████.js is downloaded by browser (perhaps for other user the hash-value can be different)
* look inside the *.js file - you will find uppermentioned links

**p.s.**
No such reports are registered currently in your Hacktivity thread.
brutforcing-jmeter script can be provided to you if necessary.

## Attachments
No attachments
