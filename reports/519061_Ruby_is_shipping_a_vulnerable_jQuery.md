# Ruby is shipping a vulnerable jQuery

## Report Details
- **Report ID**: 519061
- **URL**: https://hackerone.com/reports/519061
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-30T14:10:34.921Z
- **Disclosed**: 2019-10-03T11:12:26.933Z

## Reporter
- **Username**: chrisseaton
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
No this isn't a report about the website!

Ruby ships Darkfish as part of RDoc

https://github.com/ruby/ruby/tree/HEAD/lib/rdoc/generator/template/darkfish
https://github.com/ruby/rdoc/tree/master/lib/rdoc/generator/template/darkfish
https://github.com/ged/darkfish

Darkfish includes jQuery v1.6.4, which is vulnerable to multiple CVEs, for example

https://nvd.nist.gov/vuln/detail/CVE-2012-6708
https://nvd.nist.gov/vuln/detail/CVE-2015-9251

Now I'm not sure how applicable these CVEs are to the generated HTML, or how likely it is someone would use the jQuery from this file in the rest of their site accidentally by including generated HTML, but I do think it's a problem to be shipping a version of jQuery that is getting towards a decade old.

Maybe Darkfish should update? But who's going to do that work?

Maybe we shouldn't ship Darkfish if nobody can update it?

What do people think should be done? I ship my own implementation of Ruby and I'm not happy with shipping this old version so may have to remove Darkfish myself.

## Impact

Low. Possibly a risk that someone includes RDoc generated HTML on their site and accidentally uses this jQuery for the rest of their site and makes themselves vulnerable to the CVEs.

## Attachments
No attachments
