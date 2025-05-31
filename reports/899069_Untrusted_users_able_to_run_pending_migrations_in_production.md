# Untrusted users able to run pending migrations in production

## Report Details
- **Report ID**: 899069
- **URL**: https://hackerone.com/reports/899069
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-15T22:43:10.080Z
- **Disclosed**: 2020-07-24T20:07:32.367Z

## Reporter
- **Username**: tenderlove
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Untrusted users able to run pending migrations in production

There is a vulnerability in versions of Rails prior to 6.0.3.2 that allowed
an untrusted user to run any pending migrations on a Rails app running in
production.

This vulnerability has been assigned the CVE identifier CVE-2020-XXXX.

Versions Affected:  6.0.0 < rails < 6.0.3.2
Not affected:       Applications with `config.action_dispatch.show_exceptions = false` (this is not a default setting in production)
Fixed Versions:     rails >= 6.0.3.2


Releases
--------

The new release (6.0.3.2) is available in the regular locations.

Workarounds
-----------

Until such time as the patch can be applied, application developers should
disable the ActionDispatch middleware in their production environment via
a line such as this one in their config/environment/production.rb:

config.middleware.delete ActionDispatch::ActionableExceptions

Patches
-------

As mentioned, we are releasing the following patch for the 6.0 release
series:

* 0001-6.0.3.1-Only-allow-ActionableErrors-if-show_detailed_excepti.patch


Credits
-------

This issue was discovered independently by Rafael França and Benoit Côté-Jodoin. 
The patch above was provided by Rafael.

## Impact

Using this issue, an attacker would be able to execute any migrations that 
are pending for a Rails app running in production mode. It is important to
note that an attacker is limited to running migrations the application 
developer has already defined in their application and ones that have not
already ran.

## Attachments
- 0001-6.0.3.1-Only-allow-ActionableErrors-if-show_detailed_excepti.patch
