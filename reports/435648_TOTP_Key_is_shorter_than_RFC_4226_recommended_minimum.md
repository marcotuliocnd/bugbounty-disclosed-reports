# TOTP Key is shorter than RFC 4226 recommended minimum

## Report Details
- **Report ID**: 435648
- **URL**: https://hackerone.com/reports/435648
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-11-07T13:52:49.220Z
- **Disclosed**: 2018-12-07T17:17:20.141Z

## Reporter
- **Username**: insufficiententropy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
mongoose

**Observed Behavior:**
When creating a TOTP secret a 16 character base32 encoded string is presented to the user.

**Expected Behavior:**
I would expect a 32 character base32 secret to be presented.
The RFC recommends 160 bits of entropy, which is 32 character x 5 bits per character in a base32 string.
RFC 4226 Section 4 Requirement 6 -  128 bit minimum, 160 recommended.

**Phabricator Version:**
phabricator

24a061f844958cc22d6f4874535b57574a6c13c3 (Fri, Nov 2)

arcanist

83661809e532c3fe444a8bf7c7d6936e6377691b (Fri, Oct 26)

phutil

cf96fd681e7d35ad21c7aaaa0bd1869124e377ef (Thu, Nov 1)

diff

3.6 at /usr/bin/diff

git

2.19.1 at /usr/bin/git

hg

Not Available

pygmentize

2.2.0 at /usr/local/bin/pygmentize

svn

Not Available

**Reproduction Steps:**
Request a second factor for a user authenticated  with username and password, count the characters presented. It should be 32 not 16.

Problematic code is 
src/applications/auth/factor/PhabricatorTOTPAuthFactor.php:   
 return strtoupper(Filesystem::readRandomCharacters(16));

readRandomCharacters from phutils returns a random string using base32 characters.

## Impact

I have rated this a no impact, however I am not a cryptographer, and it is a clear violation of a cryptographic minimum key length requirement in a published RFC. Quantum supremacy may also be relevant here.

## Attachments
No attachments
