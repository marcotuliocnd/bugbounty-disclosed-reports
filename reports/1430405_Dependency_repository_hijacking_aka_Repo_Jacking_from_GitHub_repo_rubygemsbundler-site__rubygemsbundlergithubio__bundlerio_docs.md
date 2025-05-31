# Dependency repository hijacking aka Repo Jacking from GitHub repo rubygems/bundler-site & rubygems/bundler.github.io + bundler.io docs

## Report Details
- **Report ID**: 1430405
- **URL**: https://hackerone.com/reports/1430405
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-18T16:53:44.211Z
- **Disclosed**: 2021-12-19T11:12:13.915Z

## Reporter
- **Username**: akincibor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
Dependency repository hijacking (aka repo jacking) is an obscure supply chain vulnerability, conceptually similar to subdomain takeover. When the linked repository owner changes their username, it becomes immediately available to be re-registered by anyone. This means that any project that linked back to the original repository URL has now become vulnerable to remote code injection through dependency hijacking. A malicious attacker can register the old GitHub username, recreate the repository, and use it to serve malicious code to any project that depends on it.

# Step to produce PoC

1. Go to https://bundler.io/v2.2/guides/bundler_plugins.html
2. At the bottom, you will see: "Example Plugins"

{F1551051}

3. Click here [kddeisz/bundler-console](https://github.com/kddeisz/bundler-console), you will see the Takeover message.

{F1551052}

* Real repo address: https://github.com/kddnewton/bundler-console

# Remediation

I found a total of 12 places where this url is located and should be updated ASAP:

{F1551049}

* https://github.com/rubygems/bundler-site/blob/2ac68c38cf9b0ff620a24cc5defc28325b3908d5/data/known_plugins.yml at line 5
* https://github.com/rubygems/bundler-site/blob/2ac68c38cf9b0ff620a24cc5defc28325b3908d5/source/v1.16/guides/bundler_plugins.html.haml at line 222
* https://github.com/rubygems/bundler-site/blob/2ac68c38cf9b0ff620a24cc5defc28325b3908d5/source/v1.17/guides/bundler_plugins.html.haml at line 222
* https://github.com/rubygems/bundler-site/blob/2ac68c38cf9b0ff620a24cc5defc28325b3908d5/source/v2.0/guides/bundler_plugins.html.haml at line 222
* https://github.com/rubygems/bundler-site/blob/2ac68c38cf9b0ff620a24cc5defc28325b3908d5/source/v2.1/guides/bundler_plugins.html.haml at line 236
* https://github.com/rubygems/bundler-site/blob/2ac68c38cf9b0ff620a24cc5defc28325b3908d5/source/v2.2/guides/bundler_plugins.html.haml at line 236
* https://github.com/rubygems/bundler.github.io/blob/4dbdb8aa82bf034474d1c58a18563e31f541100d/guides/bundler_plugins.html at line 376
* https://github.com/rubygems/bundler.github.io/blob/4dbdb8aa82bf034474d1c58a18563e31f541100d/v1.6/guides/bundler_plugins.html at line 359
* https://github.com/rubygems/bundler.github.io/blob/4dbdb8aa82bf034474d1c58a18563e31f541100d/v1.7/guides/bundler_plugins.html at line 359
* https://github.com/rubygems/bundler.github.io/blob/4dbdb8aa82bf034474d1c58a18563e31f541100d/v2.0/guides/bundler_plugins.html at line 365
* https://github.com/rubygems/bundler.github.io/blob/4dbdb8aa82bf034474d1c58a18563e31f541100d/v2.1/guides/bundler_plugins.html at line 377
* https://github.com/rubygems/bundler.github.io/blob/4dbdb8aa82bf034474d1c58a18563e31f541100d/v2.2/guides/bundler_plugins.html at line 377

## Impact

As an attacker, I can host malicious content on the compromised Github repository. I can also host an SDK or malware, which the user will think is part of the plugins as it is referenced in your documentation, which can lead to an RCE for users referring to your documentation.

## Attachments
- Capture_d__cran_2021-12-18___15.41.51.png
- Capture_d__cran_2021-12-18___17.39.00.png
- Capture_d__cran_2021-12-18___17.44.55.png
- Capture_d__cran_2021-12-18___17.45.19.png
