# Multiple File Manipulation bugs in WP Super Cache 

## Report Details
- **Report ID**: 240886
- **URL**: https://hackerone.com/reports/240886
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-17T01:02:06.362Z
- **Disclosed**: 2018-10-29T12:20:46.370Z

## Reporter
- **Username**: paulos__
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
### Summary

I got redirected to report the vulnerabilities here by Brandon Kraft (one of your developers), so I am reporting them here.

Basically, the issue is caused because of insufficient filtering (there is one but it can be bypassed)

For instance, in /wp-cache.php, you used:

`1575: $page = str_replace('..', '', preg_replace('/[ <>\'\"\r\n\t\(\)]/', '', $_POST['deletepage'])) . '/';`

to fight File inclusion attacks by filtering out .. so ../../../other/directories attacks won't happen. however there is a bypass for this, while pocking around, I noticed .%00.../.%00.../path works the same as ../../path because of the nullbyte in the middle. to test if your patch can stop this, lets try:
```php
$page = str_replace('..', '', preg_replace('/[ <>\'\"\r\n\t\(\)]/', '', $_GET['deletepage'])) . '/';
unlink($page);
```

By sending .%00.../.%00.../path.file -- an attacker can delete file in my example.

Now this vulnerability is all over the code and by looks of it, affects all kinds of versions including the latest one.

In `/wp-cache.php`:
```php
1575: $page = str_replace('..', '', preg_replace('/[ <>\'\"\r\n\t\(\)]/', '', $_POST['deletepage'])) . '/'; 
1576: $pagefile = realpath(ABSPATH . $page . 'index.html'); 
1584: unlink unlink($pagefile); 
```

or 
```php
1576: $pagefile = realpath(ABSPATH . $page . 'index.html'); 
1575: $page = str_replace('..', '', preg_replace('/[ <>\'\"\r\n\t\(\)]/', '', $_POST['deletepage'])) . '/';
1585: unlink unlink($pagefile . '.gz'); 
```

or in `/wp-cache-phase1.php`:

where `$requset_uri` is defined as:
```php
15: $request_uri = str_replace('..', '', preg_replace('/[ <>\'\"\r\n\t\(\)]/', '', $_SERVER['REQUEST_URI'])); 
```

and used multiple times all over the code. 

And in /advanced-cache.php to unlink file, to delete, read, rename, opendir and in multiple places all over the code base.

I believe instead of reporting each, reporting why the mitigation is bypassable is so much more easier.

### Recommended Fix:

To include nullbytes in the str_replace check.


Thanks,
Paulos

## Attachments
No attachments
