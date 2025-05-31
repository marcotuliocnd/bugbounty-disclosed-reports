# Ruby 2.3.x and 2.2.x still bundle DoS vulnerable verision of libYAML

## Report Details
- **Report ID**: 235842
- **URL**: https://hackerone.com/reports/235842
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-02T14:29:02.111Z
- **Disclosed**: 2017-10-25T13:58:30.824Z

## Reporter
- **Username**: usa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
libYAML 0.1.6 (and 0.1.5) has a DoS vulnerablitity known as [CVE-2014-9130](http://www.cvedetails.com/cve/CVE-2014-9130/).
Now Ruby 2.4.x bundles fixed version 0.1.7, but 2.3.x and 2.2.x still bundle 0.1.6.

Note that I'm the maintainer of Ruby 2.3.x and 2.2.x.
Therefore, this report is a kind of remainder.

## Attachments
No attachments
