# Mercurial git subrepo lead to arbritary command injection

## Report Details
- **Report ID**: 294147
- **URL**: https://hackerone.com/reports/294147
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-01T03:32:27.925Z
- **Disclosed**: 2019-09-26T20:15:09.181Z

## Reporter
- **Username**: pnig0s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hi IBB,

I'd like to submit a issue exist in Mercurial.
```
It is possible that a specially malformed repository can cause Git subrepositories to run arbitrary code in 
the form of a .git/hooks/post-update script checked in to the repository in Mercurial 4.4 and earlier. 
Typical use of Mercurial prevents construction of such repositories, but they can be created 
programmatically.
```
Further details of my original report can be found at:
https://bz.mercurial-scm.org/show_bug.cgi?id=5730

And the Mercurial security advisory
https://www.mercurial-scm.org/wiki/WhatsNew#Mercurial_4.4.1_.282017-11-07.29

Thanks,
Terry

## Impact

A crafted mercurial repo with an evil git subrepo can lead to execute arbritary command on user's OS. And other web applications or clients support mercurial repo management or invoke hg related command also have a risk affected by this vulnerability.

## Attachments
No attachments
