# securitytemplate.site domain hijack

## Report Details
- **Report ID**: 538651
- **URL**: https://hackerone.com/reports/538651
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-15T13:53:15.126Z
- **Disclosed**: 2019-04-15T15:38:29.667Z

## Reporter
- **Username**: drstache
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
Hi,

# Security-template
I realized that your [security-template project](https://github.com/EdOverflow/security-template) domain name seems to have expired, http://securitytemplate.site doesn't serve your content.

# Penultimate
I also found that it's possible to takeover the PenultimateIO's Twitter account. It seems that you have deleted the account, but it is possible to recreate it, as you can see on the screenshot ([https://twitter.com/settings/account](https://twitter.com/settings/account)):

{F469141}
{F469142}

I didn't change my username, but knowing that Twitter indicates it as available, I consider it achievable.

There are several references to the penultimateIO Twitter account, on your Twitter and on the Penultimate Github. 

- https://twitter.com/EdOverflow/status/965559093476954112
- https://github.com/Penultimate/challenges/wiki
- https://github.com/Penultimate/challenges/blob/master/XSS/000000-xss.html
- https://github.com/Penultimate/challenges/blob/master/XSS/000001-xss.html

Your Twitter and the Penultimate's Github are out of scope, as well as social engineering, but due to the ease of implementation I prefer to report it.



Have a nice day,
Florian

## Impact

This can be used by an attacker to conduct social enginerring attacks.

## Attachments
- 1.PNG
- 2.PNG
