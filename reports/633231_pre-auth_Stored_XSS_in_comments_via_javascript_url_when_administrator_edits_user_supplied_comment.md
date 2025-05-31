# pre-auth Stored XSS in comments via javascript: url when administrator edits user supplied comment

## Report Details
- **Report ID**: 633231
- **URL**: https://hackerone.com/reports/633231
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-01T15:53:12.245Z
- **Disclosed**: 2020-08-18T18:01:25.262Z

## Reporter
- **Username**: simonscannell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
When a comment is submitted, it is filtered via `wp_rel_nofollow_callback()`, which adds the `rel` attribute to `<a>` tags within the anchor:

```
function wp_rel_nofollow_callback( $matches ) {
	$text = $matches[1];
	$atts = shortcode_parse_atts( $matches[1] );
	$rel  = 'nofollow';

	if ( ! empty( $atts['href'] ) ) {
		if ( in_array( strtolower( wp_parse_url( $atts['href'], PHP_URL_SCHEME ) ), array( 'http', 'https' ), true ) ) {
			if ( strtolower( wp_parse_url( $atts['href'], PHP_URL_HOST ) ) === strtolower( wp_parse_url( home_url(), PHP_URL_HOST ) ) ) {
				return "<a $text>";
			}
		}
	}

	if ( ! empty( $atts['rel'] ) ) {
		$parts = array_map( 'trim', explode( ' ', $atts['rel'] ) );
		if ( false === array_search( 'nofollow', $parts ) ) {
			$parts[] = 'nofollow';
		}
		$rel = implode( ' ', $parts );
		unset( $atts['rel'] );

		$html = '';
		foreach ( $atts as $name => $value ) {
			$html .= "{$name}=\"" .  $value . '" ';
		}
		$text = trim( $html );
	}
	return "<a $text rel=\"" . esc_attr( $rel ) . '">';
}
```

if the `rel` attribute is already set, the `<a>` tag is built back together with the values returned by `shortcode_parse_atts()`.  This is problematic, since `shortcode_parse_atts()` calls `stripcslashes()` on the attribute values, which for example allows turning `\x3a` into `:`. 

Therefor the `esc_url()` function can be bypassed by:
1. using a URL such as `javascript\x3aalert(1);` 
2. getting an admin to edit and update the comment containing the XSS payload
3. done

I recommend moving away from `shortcode_parse_atts()` because of side effects like these. I also got close to a XSS without user interaction through the same mechanisms but it fails luckily.

### PoC:

1. As an unauthenticated user, create a comment with the following content:
```
Hi!
I really enjoy your work. We've also written a blog post about it here: http://dummysite.com/awesome-blogpost. Feel free to check it out!
<a href="javascript\x3aalert(1);">Visit my web page</a>
```

2. create a second comment with the content:
```
I just noticed a typo in the URL! Could you please change it from dummysite.com to dummysite2.com? Thank you so much
```
3. Log in as an admin, go to the comments section and edit the comment and click save
4. View the comment on the post, click the "Visit my web page" URL and see the alert() box popping up.

## Impact

Through the XSS, RCE can be gained. Obviously a lot of user interaction is required but yeah, it is a super easy to copy & paste payload that could be used against non technical users. The XSS could then also be triggered via clickjacking.

## Attachments
No attachments
