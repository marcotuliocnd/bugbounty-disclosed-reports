# Generated passwords are not fully validated by HIBPValidator

## Report Details
- **Report ID**: 1606961
- **URL**: https://hackerone.com/reports/1606961
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-20T09:28:43.850Z
- **Disclosed**: 2022-10-01T04:50:13.612Z

## Reporter
- **Username**: bjoernv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
If the Nextcloud server generates a secure random password (e.g. for sharing files), the validation is checked before the shuffle function str_shuffle() is called. In very rare cases it could happen, that a password is validated by HIBPValidator before str_shuffle(), but would not validate after shuffle.

## Steps To Reproduce:
Since the password generation is usung random chars, the source code must be manipulated to see the problem.

For instance take the password "Password123". Shuffle the Password to "o3rw1sasd2P". 

In Generator::generate()
- delete: $password .= $chars = $this->random->generate($length, $chars);
- insert: $password = "o3rw1sasd2P"

Let the validator check the password

- delete: $password = str_shuffle($password);
- insert: $password = "Password123";

See the insecure password "Password123" in UI.

## Supporting Material/References:
https://github.com/nextcloud/password_policy/blob/master/lib/Generator.php

## Impact

In very rare cases the password generator may generate weak passwords.

## Attachments
No attachments
