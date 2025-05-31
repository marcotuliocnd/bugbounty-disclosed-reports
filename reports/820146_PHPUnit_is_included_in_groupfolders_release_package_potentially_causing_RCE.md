# PHPUnit is included in groupfolders release package potentially causing RCE

## Report Details
- **Report ID**: 820146
- **URL**: https://hackerone.com/reports/820146
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-03-16T13:33:19.649Z
- **Disclosed**: 2020-06-25T14:17:32.830Z

## Reporter
- **Username**: ledfan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The groupfolders tarball contains the phpunit code in the vendor directory (https://github.com/nextcloud/groupfolders/releases/download/v6.0.2/groupfolders.tar.gz) .
As discussed on https://thephp.cc/news/2020/02/phpunit-a-security-risk this really is a potential security risk.
The phpunit code contains a file called `eval-stdin.php` which evaluates the contents of `php://stdin`.
Note that the same issue was discovered in PrestaShop which according to thephp.cc claims:

```
I was contacted by the vendor of PrestaShop, an Open Source E-Commerce software, on January 6, 2020. They informed me that eval-stdin.php can be exploited for remote code execution when PHPUnit is publicly available on the web server and FastCGI is used to integrate PHP with that web server.
```

I was not able to exploit this using different FastCGI configurations. However, again according to phpcc:

```
An HTTP post payload can only be accessed via the php://stdin stream if PHP is used by the web server via CGI or FastCGI. I was not sure if php://stdin really behaves like this, so I reached out to PHP core developers. Joe Watkins and Christoph M. Becker were able to confirm that php://stdin behaves like this and that its implementation is based on the specifications for CGI and FastCGI, which mandate access to the request payload via the standard input stream.
```

If the Nextcloud is configured so that the url still contains `index.php` I was able to access the `eval-stdin.php` file without authentication.
Note that the following apps also include the phpunit package:
 - https://apps.nextcloud.com/apps/carnet
 - https://apps.nextcloud.com/apps/discoursesso
 - https://apps.nextcloud.com/apps/extract

## Impact

According to the PHP core developers and PrestaShop the `eval-stdin.php` makes it possible to perform RCE.
My research shows that in at least certain circumstances (i.e., index.php is not rewritten) the `eval-stdin.php` file is accessible.

## Attachments
No attachments
