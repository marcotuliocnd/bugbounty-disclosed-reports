# Potential Authentication Bypass through "autologin" feature

## Report Details
- **Report ID**: 1081986
- **URL**: https://hackerone.com/reports/1081986
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-19T23:53:03.773Z
- **Disclosed**: 2022-03-22T22:56:24.152Z

## Reporter
- **Username**: egix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: impresscms

## Vulnerability Information
## Summary:
The vulnerability is located in the `/plugins/preloads/autologin.php` script:

```
45.			$uname = $myts->stripSlashesGPC($autologinName);
46.			$pass = $myts->stripSlashesGPC($autologinPass);
47.			if (empty($uname) || is_numeric($pass)) {
48.				$user = false ;
49.			} else {
50.				// V3
51.				$uname4sql = addslashes($uname);
52.				$criteria = new icms_db_criteria_Compo(new icms_db_criteria_Item('login_name', $uname4sql));
53.				$user_handler = icms::handler('icms_member_user');
54.				$users = $user_handler->getObjects($criteria, false);
55.				if (empty($users) || count($users) != 1) {
56.					$user = false ;
57.				} else {
58.					// V3.1 begin
59.					$user = $users[0] ;
60.					$old_limit = time() - (defined('ICMS_AUTOLOGIN_LIFETIME') ? ICMS_AUTOLOGIN_LIFETIME : 604800);
61.					list($old_Ynj, $old_encpass) = explode(':', $pass);
62.					if (strtotime($old_Ynj) < $old_limit || md5($user->getVar('pass') .
63.							ICMS_DB_PASS . ICMS_DB_PREFIX . $old_Ynj) != $old_encpass)
64.					{
65.						$user = false;
66.					}
```

User input passed through the "autologin_uname" and "autologin_pass" cookie values is being used at lines 51-54 to fetch an user object from the database, and then at lines 62-63 to check the correctness of the user's password. The vulnerability exists because of an unsafe way of comparing those parameters, due to comparison operator `!=` is being used instead of `!==` within the “if” statement at lines 62-63. The latter operator returns “true” only if the compared values are equal and the same type, while the first compare the values after “[type juggling](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Type%20Juggling)”. This might be exploited to bypass the authentication mechanism and login as any user without the knowledge of the relative password.

## ImpressCMS branch :
The vulnerability has been spotted on ImpressCMS version 1.4.2 (the latest at the time of writing).

## Steps To Reproduce:
Use the attached Proof of Concept (PoC) script to reproduce this vulnerability. It's a PHP script supposed to be used from the command-line (CLI). You should see an output like the following:
```
$ php auth-bypass.php http://localhost/impresscms/ admin
[-] Starting authentication bypass attack...
[-] 2021-01-20 022141
[-] You can autologin with the following cookies:
[-] Cookie: autologin_uname=admin; autologin_pass=2021-01-20 022141:0
```

**NOTE**: the script will try to send multiple requests with incremental dates within the `autologin_pass` cookie (that will be the value of the `$old_Ynj` variable), and this will generate a different MD5 hash for each request, until something like `0e174892301580325162390102935332` will be returned by the `md5()` function. For this reason, the exploitation likelihood is very low, and the script execution might take days, months, or a theoretically infinite time.

## Impact

This vulnerability could potentially be exploited to bypass the authentication mechanism and login without valid credentials.

## Attachments
- auth-bypass.php
