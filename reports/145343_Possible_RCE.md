# Possible RCE

## Report Details
- **Report ID**: 145343
- **URL**: https://hackerone.com/reports/145343
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-17T10:48:53.671Z
- **Disclosed**: 2018-03-08T13:26:03.865Z

## Reporter
- **Username**: paulos__
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello,

I just quickly took a glance, I am not entirely sure or didn't get a chance to test it but it seems there are some serious bugs.

In */apps/user_ldap/ajax/wizard.php*: 
```php
36: $action = (string)$_POST['action']; 
```
and it is called in multiple places. including line 83 & 99. one being `$action($loginName);` & since 
`$loginName` is defined as:

```php
$loginName = $_POST['ldap_test_loginname'];
```
would mean an RCE is achievable when $result is called
```php
$result = $wizard->$action($loginName);
``` 
 
This is because userinput is used as dynamic function name. ergo, arbitrary functions may be called.

All an attacker have to send is a POST request with action parameter containing a function name like action=eval&ldap_test_loginname=stufftoexecute

There is a very little chance the $wizard will stop this because arbritary wakeup & constract objects may be exploitable. like I said, I didn't get a chance to test this but seems fairly feasible. please think about it and let me know.

Thanks,
P


## Attachments
No attachments
