# Insecure randomness for default password in file sharing when password policy app is disabled

## Report Details
- **Report ID**: 1745702
- **URL**: https://hackerone.com/reports/1745702
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-10-21T11:35:30.862Z
- **Disclosed**: 2023-03-30T08:45:42.098Z

## Reporter
- **Username**: gorei
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Sharing links can be protected with a password. However, the function used for generating this password is using cryptographically insecure RNG.

`server-25.0.0\apps\files_sharing\src\utils\GeneratePassword.js` (lines 36-55):

```php
export default async function() {
	// password policy is enabled, let's request a pass
	if (config.passwordPolicy.api && config.passwordPolicy.api.generate) {
		try {
			const request = await axios.get(config.passwordPolicy.api.generate)
			if (request.data.ocs.data.password) {
				return request.data.ocs.data.password
			}
		} catch (error) {
			console.info('Error generating password from password_policy', error)
		}
	}

	// generate password of 10 length based on passwordSet
	return Array(10).fill(0)
		.reduce((prev, curr) => {
			prev += passwordSet.charAt(Math.floor(Math.random() * passwordSet.length))
			return prev
		}, '')
}
```

The first part of the function handles the password generation in a safe way when a password policy is present. However, there is another variant generating the password using `Math.random` function, which is not appropriate for use in a security-sensitive context.

Citation from [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random):
*"Note: Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead, and more precisely the window.crypto.getRandomValues() method."*

## Supporting Material/References:
  * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
 * https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues

## Impact

An attacker might be able to access the shared files even without knowledge of the password.

## Attachments
No attachments
