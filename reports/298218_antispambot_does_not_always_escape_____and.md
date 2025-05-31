# antispambot does not always escape <, >, &, " and '

## Report Details
- **Report ID**: 298218
- **URL**: https://hackerone.com/reports/298218
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-15T08:49:22.937Z
- **Disclosed**: 2019-09-16T17:45:51.322Z

## Reporter
- **Username**: flimm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
The `antispambot` function escapes some randomly selected characters from its first argument, for example:

```
<?php
echo antispambot( 'example@example.com' );
```

This would print out:

```
exa&#109;p&#108;&#101;&#64;&#101;xa&#109;pl&#101;&#46;&#99;o&#109;
```

Since this returns HTML, developers are not going to use `esc_html` with the return value of `antispambot`, since that would double-escape the result. Developers will assume that this function can be safely used with untrusted email addresses, which is a fair assumption. However, it turns out that `antispambot` cannot be trusted. Whether a character is escaped is randomly selected, even if the character is `<`, `>`, `&`, `"`, or `'`. These last five characters should always be escaped.

There is a chance that this will print out unescaped:

```
<?php
echo antispambot( '<script>console.log("hello");</script>');
```

Even though the chance of this happening is low, with enough repetitions this could happen eventually.

`antispambot` should always escape the five sensitive characters.

## Impact

If `antispambot` is being used by a plugin that passes to it untrusted input, an attacker could cause arbitrary client-side code to run. Since the probability of all of the characters remaining unescaped is low, only a small fraction of the attacks would succeed, and the attacker would need the ability to attack many times to see a few successes.

## Attachments
No attachments
