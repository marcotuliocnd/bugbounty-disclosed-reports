# user_ldap app logs user passwords in the log file on level debug

## Report Details
- **Report ID**: 2101165
- **URL**: https://hackerone.com/reports/2101165
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-08T14:40:53.847Z
- **Disclosed**: 2023-11-21T11:39:25.405Z

## Reporter
- **Username**: alacn1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Nextcloud using ldap user authentication and loglevel debug write user passwords to log file.
Vulnerable versions: 26.0.4, 27.0.1.

## Steps To Reproduce:
  1. Use a nextcloud with ldap user authentication.
  2. Set nextcloud config loglevel to 0 (debug).
  3. Login to nextcloud using a ldap user.
  4. Search for lines with 'ldap_bind' in nextcloud log file.

## Supporting Material/References:
Sample log file:
```
{"reqId":"QRqbkhMpRAY1ugvQMrPk","level":0,"time":"2023-08-08T11:17:11-03:00","remoteAddr":"<IPADDRESS>","user":"--","app":"user_ldap","method":"POST","url":"/login","message":"Calling LDAP function ldap_bind with parameters [{},\"uid=<USERNAME>\",\"<PASSWORD>\"]","userAgent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36","version":"27.0.1.2","data":{"app":"user_ldap"}}
```

Affected file:
`apps/user_ldap/lib/LDAP.php`

Vulnerable code:
```
	private function preFunctionCall(string $functionName, array $args): void {
		$this->curArgs = $args;
		$this->logger->debug('Calling LDAP function {func} with parameters {args}', [
			'app' => 'user_ldap',
			'func' => $functionName,
			'args' => json_encode($args),
		]);
```

## Impact

Local administrator can retriave user passwords.

## Attachments
No attachments
