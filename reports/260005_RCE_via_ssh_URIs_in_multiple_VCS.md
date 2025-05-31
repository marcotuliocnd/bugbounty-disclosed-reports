# RCE via ssh:// URIs in multiple VCS 

## Report Details
- **Report ID**: 260005
- **URL**: https://hackerone.com/reports/260005
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-14T20:53:18.957Z
- **Disclosed**: 2017-09-21T16:21:35.503Z

## Reporter
- **Username**: joernchen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I'd like to submit an RCE issue within Git SVN and Mercurial, the CVEs are:

*  CVE-2017-9800 (Subversion)
* CVE-2017-1000116 (Mercurial (hg))
* CVE-2017-1000117 (Git)

Further Info can be found at:

http://blog.recurity-labs.com/2017-08-10/scm-vulns

And product specific:

* https://public-inbox.org/git/xmqqh8xf482j.fsf@gitster.mtv.corp.google.com/T/#u
* http://subversion.apache.org/security/CVE-2017-9800-advisory.txt
* https://about.gitlab.com/2017/08/10/gitlab-9-dot-4-dot-4-released/

I think these issues which all are based on the same flaw could be worth
an IBB Bounty. However I'd like to point out that we at Recurity Labs
would like the bounty being donated to a charity. The to be determined
charity will be something in the field of brain aneurysm, this is due to
the fact that Felix, the founder of Recurity Labs, currently is
recovering from a brain aneurysm.


So, just let us know what you think about this.

Cheers,

joern

P.S. I took the CVSS Score from the Subversion Advisory
the Redhat advisory states a score of 6.3 (CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L) I guess the truth is somewhere in between.

## Attachments
No attachments
