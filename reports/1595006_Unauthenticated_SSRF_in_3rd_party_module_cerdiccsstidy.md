# Unauthenticated SSRF in 3rd party module "cerdic/csstidy"

## Report Details
- **Report ID**: 1595006
- **URL**: https://hackerone.com/reports/1595006
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-08T14:50:19.532Z
- **Disclosed**: 2022-09-03T06:29:46.782Z

## Reporter
- **Username**: eg42
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
The mail extension in nextcloud includes a module called "cerdic/csstidy" which basically ships with a publicly accessible test/example interface to play with the CSS formatter and optimiser (/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php). This module allows contacting any remote server via http, which makes it vulnerable to SSRF. We've tried reaching out to the csstidy developers directly but couldn't reach them yet, so we're reaching out to you so they can fix this before csstidy pushes out a fix.

It's also possible to download remote data as a CSS file into a temporary directory in /apps/mail/vendor/cerdic/css-tidy/temp/. At the moment, this doesn't look to be exploitable on its own, and probably requires another vulnerability to exploit, e.g. a Local File Inclusion vulnerability could be turned into a Remote File Inclusion by first creating a CSS file containing PHP code (downloaded from a remote server via the csstidy vulnerability), and then including the local file via the LFI bug.

## Steps To Reproduce:

  1. Install the mail extension
  2. Visit: http://example.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php (no authentication is required)
  3. Either use the interface to set "CSS from URL" on the bottom or set the "url" parameter manually, for example: http://example.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://localhost/test
  4. To download remote data as CSS file, either use the interface or try this: http://example.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://localhost/apps/richdocuments/docs/custom.css&custom=1&template=4

## Supporting Material/References:

* Problematic line in csstidy: https://github.com/Cerdic/CSSTidy/blob/master/css_optimiser.php#L376

## Impact

Usually, SSRFs are not considered a high-impact vulnerability, and I would likely agree on most PHP projects, but (a) this vulnerability can be exploited by an unauthenticated attacker and (b) nextcloud is also designed to be used at a home network which opens the possibility of not only attacking other local services, but also the router of the home network. The ability to receive and write CSS files can also be used by the attacker to find out what other services are running on devices in the network or what kind of router is used etc., before running additional attacks.

## Attachments
No attachments
