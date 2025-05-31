# SQL Injection through /include/findusers.php

## Report Details
- **Report ID**: 1081145
- **URL**: https://hackerone.com/reports/1081145
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-01-19T02:42:46.716Z
- **Disclosed**: 2022-10-06T18:51:25.975Z

## Reporter
- **Username**: egix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: impresscms

## Vulnerability Information
## Summary:
The vulnerability is located in the `/include/findusers.php` script:

```
281.			$total = $user_handler->getUserCountByGroupLink(@$_POST["groups"], $criteria);
282.	
283.			$validsort = array("uname", "email", "last_login", "user_regdate", "posts");
284.			$sort = (!in_array($_POST['user_sort'], $validsort)) ? "uname" : $_POST['user_sort'];
285.			$order = "ASC";
286.			if (isset($_POST['user_order']) && $_POST['user_order'] == "DESC") {
287.				$order = "DESC";
288.			}
289.	
290.			$criteria->setSort($sort);
291.			$criteria->setOrder($order);
292.			$criteria->setLimit($limit);
293.			$criteria->setStart($start);
294.			$foundusers = $user_handler->getUsersByGroupLink(@$_POST["groups"], $criteria, TRUE);
```

User input passed through the "groups" POST parameter is not properly sanitized before being passed to the `icms_member_Handler::getUserCountByGroupLink()` and `icms_member_Handler::getUsersByGroupLink()` methods at lines 281 and 294. These methods use the first argument to construct a SQL query without proper validation:

```
461.		public function getUsersByGroupLink($groups, $criteria = null, $asobject = false, $id_as_key = false) {
462.			$ret = array();
463.	
464.			$select = $asobject ? "u.*" : "u.uid";
465.			$sql[] = "	SELECT DISTINCT {$select} "
466.					. "	FROM " . icms::$xoopsDB->prefix("users") . " AS u"
467.					. " LEFT JOIN " . icms::$xoopsDB->prefix("groups_users_link") . " AS m ON m.uid = u.uid"
468.					. "	WHERE 1 = '1'";
469.			if (! empty($groups)) {
470.				$sql[] = "m.groupid IN (" . implode(", ", $groups) . ")";
471.			}
```

This can be exploited by remote attackers to e.g. read sensitive data from the "users" database table through boolean-based SQL Injection attacks.

## ImpressCMS branch :
The vulnerability has been tested and confirmed on ImpressCMS version 1.4.2 (the latest at the time of writing).

## Steps To Reproduce:
Use the attached Proof of Concept (PoC) script to reproduce this vulnerability. It's a PHP script supposed to be used from the command-line (CLI). You should see an output like the following:

```
$ php sqli.php http://localhost/impresscms/
[-] Retrieving security token...
[-] Starting SQL Injection attack...
[-] Admin's email: admin@test.com
```

The PoC leverages both this vulnerability and the one reported at #1081137 to achieve unauthenticated exploitation.

## Impact

This vulnerability might allow **unauthenticated attackers** to disclose any field of the "users" database table, including the users' email addresses and password hashes, potentially leading to full account takeovers.

**NOTE**: normally, successful exploitation of this vulnerability should require an admin user session. However, due to the vulnerability described in report #1081137, this could be exploited by unauthenticated attackers as well.

## Attachments
- sqli.php
