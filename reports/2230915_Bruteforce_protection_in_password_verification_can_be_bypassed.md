# Bruteforce protection in password verification can be bypassed

## Report Details
- **Report ID**: 2230915
- **URL**: https://hackerone.com/reports/2230915
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-29T07:37:23.669Z
- **Disclosed**: 2024-01-17T08:27:33.753Z

## Reporter
- **Username**: taise
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
nextcloud server have implemented IP address-based blocking as a measure to counter Bruteforce protection.
The source IP address is obtained through the getRemoteAddress() function. 

lib/public/IRequest.php
```php
	public function getRemoteAddress(): string {
		$remoteAddress = isset($this->server['REMOTE_ADDR']) ? $this->server['REMOTE_ADDR'] : '';
		$trustedProxies = $this->config->getSystemValue('trusted_proxies', []);

		if (\is_array($trustedProxies) && $this->isTrustedProxy($trustedProxies, $remoteAddress)) {
			$forwardedForHeaders = $this->config->getSystemValue('forwarded_for_headers', [
				'HTTP_X_FORWARDED_FOR'
				// only have one default, so we cannot ship an insecure product out of the box
			]);

			foreach ($forwardedForHeaders as $header) {
				if (isset($this->server[$header])) {
					foreach (explode(',', $this->server[$header]) as $IP) {
						$IP = trim($IP);

						// remove brackets from IPv6 addresses
						if (str_starts_with($IP, '[') && str_ends_with($IP, ']')) {
							$IP = substr($IP, 1, -1);
						}

						if (filter_var($IP, FILTER_VALIDATE_IP) !== false) {
							return $IP;
						}
					}
				}
			}
		}
```
It is determined that the IP address is retrieved based on the value of the X-Forwarded-For header when trusted_proxy is configured.

By adding the X-Forwarded-For header with valid ip format it is possible to bypass Bruteforce protection.

## Step to reproduce
1. Setting up a nextcloud server using trusted_proxy.
2. Attempts to log in multiple times with incorrect passwords.  Confirm that the `Throttler\sleepDelay` function causes a delay in response time.
3. Add  `X-Forwarded-For` header with valid ip format, the the delay is eliminated and Bruteforce protection is bypassed.

## Impact

an attacker can bypass bruteforce protection and bruteforce the login.

## Attachments
No attachments
