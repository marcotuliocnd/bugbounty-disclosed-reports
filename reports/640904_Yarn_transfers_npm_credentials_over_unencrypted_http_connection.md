# Yarn transfers npm credentials over unencrypted http connection

## Report Details
- **Report ID**: 640904
- **URL**: https://hackerone.com/reports/640904
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-12T11:31:20.661Z
- **Disclosed**: 2019-08-14T11:27:55.400Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
# Module

**module name:** yarn
**version:** 1.16.0
**npm page:** `https://www.npmjs.com/package/yarn`

## Module Description

> Fast, reliable, and secure dependency management.

## Module Stats

> Replace stats below with numbers from npm’s module page:

166 703 downloads in the last day
849 928 downloads in the last week
3 772 290 downloads in the last month

# Vulnerability

## Vulnerability Description

For scoped packages that are listed as `resolved "http://registry.npmjs.org/@...` in yarn.lock, yarn trasfers npm credentials (i.e. `_authToken`) over unencrypted http connection. This allows any MitM (for example, a proxy or a VPN) to sniff out npm credentials, given that the developer in question performs `yarn install` on such a yarn.lock file.

A quick search shows that there is a number of `yarn.lock` files affected by this on GitHub, some examples:
 * https://github.com/EC-Nordbund/ec-verwaltungs-app/blob/ab961352d5dd53834a51793d6e2c4bc69a2b22d4/packages/api/yarn.lock#L36
 *  https://github.com/nujabes403/boilerplate2/blob/61613e526aec02c5dd4227457deb8676d66780d0/yarn.lock#L7

There seem to be __many of those__ on GitHub.

Looks like not only it was possible to craft a yarn.lock with a malicious intent, but also this seems to be a common pattern that yarn created itself at some point or under some circumstances and that gets persistent from older versions.

## Steps To Reproduce:

1. Perform an `npm login` or just write `//registry.npmjs.org/:_authToken=38bb8d1f-a39b-47d1-a78e-3bf0626ff77e` (which is the format npm uses) to ~/.npmrc. **Doing this from your own account would leak your npm credentials on next steps, so better just use a placeholder.**
2. Create an empty package with a single dependency on `"@babel/core": "^7.5.4"`
3. Perform `yarn install`
4. Replace all occurances of `https://registry.yarnpkg.com` with `http://registry.npmjs.org/` in the generated `yarn.lock`
    
    Alternatively to steps 2-4 -- just use an already existing yarn.lock with `resolved "http://registry.npmjs.org/@` in it (lots of those on GitHub), but be careful with that.
5. Clear yarn cache and node_modules: `rm -rf ~/.cache/yarn/ node_modules`. Let's assume you just downloaded an affected yarn.lock on your clean machine.
6. Start wireshark with `tcp dst port 80` filter.
7. Run `yarn install`

Observed result is attached on a screenshot.

## Supporting Material/References:

- `Linux yoga 5.1.5-arch1-2-ARCH #1 SMP PREEMPT Mon May 27 03:37:39 UTC 2019 x86_64 GNU/Linux`
- Node.js v12.6.0
- npm 6.10.1

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

Attacker (MitM) being able to:
* Impersonate the affected account
* Publish packages from the affected account that could also get used by the affected account/company in the future (for protected packages) and by anyone in the ecosystem (for public packages)
* Perform logout and break installs of protected packages

## Attachments
- Screenshot_20190712_142351.png
