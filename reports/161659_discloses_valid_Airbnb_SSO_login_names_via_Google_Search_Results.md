# ████ discloses valid Airbnb SSO login names via Google Search Results

## Report Details
- **Report ID**: 161659
- **URL**: https://hackerone.com/reports/161659
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-20T18:00:42.886Z
- **Disclosed**: 2016-10-09T16:40:53.181Z

## Reporter
- **Username**: aesteral
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: airbnb

## Vulnerability Information
Hello,

There is an Information leakage type weakness present on ███████ which supposedly works as a Single Sign On (SSO) gateway for Airbnb's corporate services. The weakness is present due to lack of robots exclusions policy file (robots.txt) present on this domain which allows web crawlers such as Google add URLs within this domain into their search indexes.

While ██████ is situated behind the coprorate network boundary and is not accessible from the Internet URLs which would generally make it unindexable by Google or other search engines various Google-made products like Chrome browser or Google Toolbar report URLs users open to Google which then adds those into the index making them searchable.

██████████ employs the following URL structure: https://████/people/alice_brown where alice_brown is a valid login name in Airbnb SSO an usually a valid address in @airbnb.com domain. You can see a certain amount of such valid login names at the following Google SERP URL: https://www.google.com/#q=site:██████████&filter=0

This information should obviously be kept private since it gives a malicious party additional knowledge about Airbnb's SSO system, valid account names to test for weak passwords and information for social engineering attacks against Airbnb's empolyees.

It is advised to make these URLs not indexable by supplying Google with a restrictions policy (robots.txt) for this domain.

## Attachments
No attachments
