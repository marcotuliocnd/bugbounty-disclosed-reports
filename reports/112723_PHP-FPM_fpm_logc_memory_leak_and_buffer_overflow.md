# PHP-FPM fpm_log.c memory leak and buffer overflow

## Report Details
- **Report ID**: 112723
- **URL**: https://hackerone.com/reports/112723
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-25T17:19:21.537Z
- **Disclosed**: 2019-11-12T09:38:12.882Z

## Reporter
- **Username**: imrerad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The FastCGI Process Manager (FPM) SAPI of PHP was vulnerable to memory leak and buffer overflow in the access logging feature.

PHP-FPM offers customization of the access log lines based on format string variables which can be specified with the access.format option of the FPM configuration file.
The log lines were compiled in php-fpm.c. The %{something}e fields were processed at line 237:

len2 = snprintf(b, FPM_LOG_BUFFER - len, "%s", env ? env : "-");

Then later in the code:
len += len2;
...
    if (!test && strlen(buffer) > 0) {
         buffer[len] = '\n';
        write(fpm_log_fd, buffer, len + 1);
    }

In case the string being appended to the access log line buffer was longer than the remaining space, the len variable became longer than the buffer (FPM_LOG_BUFFER) size, because snprintf returns the number of characters (excluding the terminating null byte) which would have been written to the final string if enough space had been available. Then the PHP engine performed an out-of-boundaries read and also wrote a \n character outside of the allocated memory.

The fix is available with the commit
http://git.php.net/?p=php-src.git;a=commit;h=2721a0148649e07ed74468f097a28899741eb58f
The fixed versions of PHP are: 5.5.31, 5.6.17 and 7.0.2.

More information (public security advisory):
http://www.search-lab.hu/about-us/news/111-some-unusual-vulnerabilities-in-the-php-engine

## Attachments
No attachments
