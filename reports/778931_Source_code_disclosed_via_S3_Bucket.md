# Source code disclosed via S3 Bucket

## Report Details
- **Report ID**: 778931
- **URL**: https://hackerone.com/reports/778931
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-21T09:45:54.403Z
- **Disclosed**: 2020-02-13T00:17:46.549Z

## Reporter
- **Username**: thevillagehack3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
### Summary
The Ruby having an Amazon S3 bucked named `http://rubyci.s3.amazonaws.com/` which lists some of their log files. Those logs having some informations to check the source code server side directories.

### Steps to Reproduce

1. direct to `http://rubyci.s3.amazonaws.com/`  which having **READ** Permission to all Objects hosted in that bucket
{F691099}
2. Can also able to access aws-cli through `aws s3 ls s3://rubyci`
3. direct to one of the object named ***last.txt***  as  ` http://rubyci.s3.amazonaws.com/aix71_ppc/ruby-2.1/last.txt `
{F691108}
4. scroll down and a line shown which directs to source code directory link `http://svn.ruby-lang.org/repos/ruby/branches/` that is a initial directory for all source codes
5. I can check and view each and every source codes of all ruby versions

### POC
## Video
{F691114}

## Impact

- The attacker can able to read any aws authorized object and use those informations to do potential attacks
- The source codes having some sensitive informations so the attacker can do impact to ruby codes that may cause major attack on users.

## Attachments
- 2.png
- 1.png
- Screenshot_from_2020-01-21_15-02-42.png
- video.webm
