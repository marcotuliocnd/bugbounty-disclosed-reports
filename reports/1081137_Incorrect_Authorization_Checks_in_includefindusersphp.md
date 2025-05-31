# Incorrect Authorization Checks in /include/findusers.php

## Report Details
- **Report ID**: 1081137
- **URL**: https://hackerone.com/reports/1081137
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-19T01:59:23.180Z
- **Disclosed**: 2022-03-22T22:57:15.604Z

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
16.	include "../mainfile.php";
17.	xoops_header(false);
18.	
19.	$denied = true;
20.	if (!empty($_REQUEST['token'])) {
21.		if (icms::$security->validateToken($_REQUEST['token'], false)) {
22.			$denied = false;
23.		}
24.	} elseif (is_object(icms::$user) && icms::$user->isAdmin()) {
25.		$denied = false;
26.	}
27.	if ($denied) {
28.		icms_core_Message::error(_NOPERM);
29.		exit();
30.	}
```

As far as I can see, I believe this script should be accessible by admin users only (due to line 24). However, because of the if statements at lines 20-23, this script could be accessed by unauthenticated attackers if they will provide a valid security token. Such a token will be generated in several places within the application (just search for the string `icms::$security->getTokenHTML()`), and some of them do not require the user to be authenticated, like in `misc.php` at [line 181](https://github.com/ImpressCMS/impresscms/blob/48af29c6b8150fbf4220bb5cc4f3c57bcd818384/misc.php#L181).



## ImpressCMS branch :
The vulnerability has been tested and confirmed on ImpressCMS version 1.4.2 (the latest at the time of writing).

## Steps To Reproduce:
  1. Try to access the `/include/findusers.php` script without being logged into the application
  1. You will see an error message saying **"Sorry, you don't have permission to access this area."**
  1. Go to `/misc.php?action=showpopups&type=friend` and look at the HTML source code, search the string `XOOPS_TOKEN_REQUEST` and copy the value of the token
  1. Go to `/include/findusers.php?token=[TOKEN_VALUE]` and you will be able to access the script and e.g. search through the registered users

## Impact

This vulnerability might allow unauthenticated attackers to access an otherwise restricted functionality of the application, which in turn might allow an information disclosure about the CMS users (specifically, only the username and real name will be disclosed).

## Attachments
No attachments
