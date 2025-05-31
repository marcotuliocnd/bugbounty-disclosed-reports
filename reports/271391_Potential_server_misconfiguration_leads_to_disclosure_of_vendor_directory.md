# Potential server misconfiguration leads to disclosure of vendor/ directory

## Report Details
- **Report ID**: 271391
- **URL**: https://hackerone.com/reports/271391
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-25T02:56:01.478Z
- **Disclosed**: 2017-10-23T05:47:08.128Z

## Reporter
- **Username**: h4ckninja
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hi,

Apologies for the weakness label, it was the closest I could find for what appears to be a server misconfiguration.

Typically, in MVC frameworks like Slim (which I see you are using here), Symfony, Laravel, etc., the front controller is the only thing exposed, leaving `vendor/`, `logs/`, and others outside of document root, inaccessible to web browsers.

However, it appears that here that's not the case, having `vendor/` accessible.

## PoC

`https://www.zomato.com/vendor/composer/installed.json`

`https://www.zomato.com/vendor/slim/slim/composer.json`

`https://www.zomato.com/vendor/bin/phpunit`

I can see that Slim is used, and various libraries are installed with `composer`.


## Why it's a concern

Recently, `phpunit` had an RCE vulnerability, that if exposed, would allow users to run arbitrary PHP code. PHPUnit is indeed installed: `https://www.zomato.com/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php`. However, it appears that you are fortunately running the patched version. Reference: `http://phpunit.vulnbusters.com/`.


## Additional notes

I did try other directories, like the `logs/` directory, but it doesn't seem to be exposed. Or at least the common `app.log` isn't available.

## Attachments
No attachments
