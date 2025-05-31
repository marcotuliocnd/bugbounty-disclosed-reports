# Stored XSS in Post Preview as Contributor

## Report Details
- **Report ID**: 497724
- **URL**: https://hackerone.com/reports/497724
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-18T21:03:20.337Z
- **Disclosed**: 2020-08-18T18:02:04.483Z

## Reporter
- **Username**: simonscannell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Root cause

I noticed that the `get_the_content()` makes a preg_replace_callback after all other validation and sanitization has been performed.

```
function get_the_content( $more_link_text = null, $strip_teaser = false ) {
	global $page, $more, $preview, $pages, $multipage;

	$post = get_post();

	...
	if ( $preview ) // Preview fix for JavaScript bug with foreign languages.
		$output =	preg_replace_callback( '/\%u([0-9A-F]{4})/', '_convert_urlencoded_to_entities', $output );

	return $output;
}
```

Any JavaScript URL encoded characters will get replaced by the result of the `_convert_urlencoded_to_entities()` function.

```
function _convert_urlencoded_to_entities( $match ) {
	return '&#' . base_convert( $match[1], 16, 10 ) . ';';
}
```

This function replaces the URL encoded characters with a corresponding HTML entity.

This in fact leads to a bypass of `esc_url()`.

`esc_url()` usually prevents payloads such as `javascript:alert(1)` etc. It even understands `javascript&#3A;alert(1);`. However, the payload `<a href="javascript%u003Aalert(/XSS/)">text</a>` would not get sanitized by `esc_url()`. Due to the characters being converted back to HTML entities after the sanitization, the payload works again.

## Steps for replication

1. Create a new blog post
2. Paste the following HTML: `<a href="javascript%u003Aalert(/XSS/)">text</a>`
3. Preview the post and click the link

I have tested this with Firefox.

## Impact

If an attacker can trick an admin into previewing a post and get him to click the link, he can execute arbitrary JavaScript code in the context of the admin user. 

I have demonstrated in #428019 how using already existing CSS classes the link can be turned into an invisible overlay over the entire page, which makes exploitation way more likely.

## Attachments
No attachments
