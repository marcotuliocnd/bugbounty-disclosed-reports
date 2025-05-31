# Open redirect in Serendipity (exit.php)

## Report Details
- **Report ID**: 373932
- **URL**: https://hackerone.com/reports/373932
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-29T14:17:49.624Z
- **Disclosed**: 2018-11-09T14:53:43.894Z

## Reporter
- **Username**: bb9866f3f743d6bf69b6836
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hannob

## Vulnerability Information
## Summary

Serendipity contains a script named `exit.php` that can be directly accessed. When crafting an hyperlink pointing to this page with the parameter `url` containing a base64-encoded  URL, it will redirect the user to this URL.

## Description

The file `exit.php` contains the following code:

```php
<?php
// [...]
if (isset($_GET['url_id']) && !empty($_GET['url_id']) && isset($_GET['entry_id']) && !empty($_GET['entry_id'])) {
// [...]
} elseif (isset($_GET['url']) && !empty($_GET['url'])) {
    // No entry-link ID was submitted. Possibly a spammer tried to mis-use the script to get into the top-list.
    $url = strip_tags(str_replace('&amp;', '&', base64_decode($_GET['url'])));
}

if (serendipity_isResponseClean($url)) {
    header('HTTP/1.0 301 Moved Permanently');
    header('Status: 301 Moved Permanently');
    header('Location: ' . $url);
}
```

The interesting part is the handling of `$_GET['url']`. The function `serendipity_isResponseClean()` tries to prevent response splitting issues but does not validate the hostname of the URL where the user is redirected to. 

## Steps To Reproduce

1. Access https://blog.fuzzing-project.org/exit.php?url=aHR0cHM6Ly9nb29nbGUuY29t with a browser;
1. Notice that the `Location` header of the response contains an arbitrary URL (here, https://google.com).

## Impact

An attacker can craft an hyperlink pointing to https://blog.fuzzing-project.org that, once accessed, will redirect the victim to an arbitrary URL.

## Attachments
No attachments
