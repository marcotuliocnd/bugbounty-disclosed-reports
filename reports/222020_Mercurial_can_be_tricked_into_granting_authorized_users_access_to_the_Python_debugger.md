# Mercurial can be tricked into granting authorized users access to the Python debugger

## Report Details
- **Report ID**: 222020
- **URL**: https://hackerone.com/reports/222020
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-04-18T21:08:41.575Z
- **Disclosed**: 2017-07-12T14:35:50.100Z

## Reporter
- **Username**: claudijd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I reported this bug privately to Mercurial and they produced an out of band release to fix the bug here:

https://www.mercurial-scm.org/wiki/WhatsNew#Mercurial_4.1.3_.282017-4-18.29

I produced a very detailed proof of concept with a Metasploit exploit module, which can be seen publicly here:

https://github.com/rapid7/metasploit-framework/pull/8263

The TLDR is that many services which host Mercurial servers often write their own hg-ssh wrapper or heavily customize the hg-ssh wrapper.  If the customized wrapped does not explicitly validate user input to the repo attribute, an attacker can supply a string of "--debugger", which causes the internal hg binary to drop to a Pdb shell, which allows arbitrary Python code execution.

I'm submitting to this program because I believe source code management software like git and mercurial is considered critical infrastructure for the Internet.

## Attachments
No attachments
