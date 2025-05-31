# SAML authentication bypass through unauthenticated `addSamlProvider` Meteor Call

## Report Details
- **Report ID**: 1049375
- **URL**: https://hackerone.com/reports/1049375
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-03T03:40:59.324Z
- **Disclosed**: 2021-01-08T15:43:08.658Z

## Reporter
- **Username**: fabianfreyer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** Rocket.Chat exposes an unauthenticated Meteor method `addSamlProvider`, which allows disabling SAML signature verification.

**Description:**

The `addSamlProvider` Meteor method sets a number of settings, among them a boolean flag that defaults to `false`:
```js
export const addSamlService = function(name: string): void {
	settings.add(`SAML_Custom_${ name }`, false, {
		type: 'boolean',
		group: 'SAML',
		i18nLabel: 'Accounts_OAuth_Custom_Enable',
	});
```

The provider `name` is entirely user-controlled in this case.

Secondly, if a SAML authentication provider does not have a certificate set, or the setting is falsy, no validation is performed:
```js
private verifySignatures(response: Element, assertionData: ISAMLAssertion, xml: string): void {
	if (!this.serviceProviderOptions.cert) {
		return;
	}
```

## Releases Affected:

  * all versions including `meteor-accounts-saml`, i.e. 0.8.0 and later.

## Steps To Reproduce (from initial installation to vulnerability):

On the login page of a Rocket.Chat instance supporting SAML authentication using a provider named `Default` (this is the default), run the following Meteor call:
```
Meteor.call("addSamlService", "Default_cert")
```

Then log in using an arbitrarily faked SAML response.

## Suggested mitigation

  * Remove the `addSamlProvider` Meteor method. All callers of the underlying function are server-side, therefore it needs not be exposed to the client.

## Impact

* An unauthenticated attacker can disable SAML certificate validation on an instance with SAML authentication enabled, and then log in as an arbitrary user with administrative privileges.

## Attachments
No attachments
