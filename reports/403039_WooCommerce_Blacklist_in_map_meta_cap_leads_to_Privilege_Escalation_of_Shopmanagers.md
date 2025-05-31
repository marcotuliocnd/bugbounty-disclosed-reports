# WooCommerce Blacklist in 'map_meta_cap' leads to Privilege Escalation of Shopmanagers

## Report Details
- **Report ID**: 403039
- **URL**: https://hackerone.com/reports/403039
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-30T14:33:31.173Z
- **Disclosed**: 2019-12-19T14:25:01.563Z

## Reporter
- **Username**: simonscannell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
When the Shopmanager role is defined for the first time, it receives the following WordPress core privileges:

```
	// Shop manager role.
		add_role(
			'shop_manager',
			'Shop manager',
			array(
				'level_9'                => true,
				'level_8'                => true,
				'level_7'                => true,
				'level_6'                => true,
				'level_5'                => true,
				'level_4'                => true,
				'level_3'                => true,
				'level_2'                => true,
				'level_1'                => true,
				'level_0'                => true,
				'read'                   => true,
				'read_private_pages'     => true,
				'read_private_posts'     => true,
				'edit_users'             => true,
				'edit_posts'             => true,
				'edit_pages'             => true,
				'edit_published_posts'   => true,
				'edit_published_pages'   => true,
				'edit_private_pages'     => true,
				'edit_private_posts'     => true,
				'edit_others_posts'      => true,
				'edit_others_pages'      => true,
				'publish_posts'          => true,
				'publish_pages'          => true,
				'delete_posts'           => true,
				'delete_pages'           => true,
				'delete_private_pages'   => true,
				'delete_private_posts'   => true,
				'delete_published_pages' => true,
				'delete_published_posts' => true,
				'delete_others_posts'    => true,
				'delete_others_pages'    => true,
				'manage_categories'      => true,
				'manage_links'           => true,
				'moderate_comments'      => true,
				'upload_files'           => true,
				'export'                 => true,
				'import'                 => true,
				'list_users'             => true,
			)
		);
```

Most interestingly is the following privilege:

```
'edit_users'             => true,
```

With edit_users privileges, Shop managers can by default edit any user and set any user to any user role (including Admin). Since this is obviously not desirable, WordPress added meta capabilities. This allows to restrict Shop managers to not simply assign themselves Admin privileges.

WooCommerce implements these restrictions the following way:

```
/**
 * Modify capabilities to prevent non-admin users editing admin users.
 *
 * $args[0] will be the user being edited in this case.
 *
 * @param  array  $caps    Array of caps.
 * @param  string $cap     Name of the cap we are checking.
 * @param  int    $user_id ID of the user being checked against.
 * @param  array  $args    Arguments.
 * @return array
 */
function wc_modify_map_meta_cap( $caps, $cap, $user_id, $args ) {
	switch ( $cap ) {
		case 'edit_user':
		case 'remove_user':
		case 'promote_user':
		case 'delete_user':
			if ( ! isset( $args[0] ) || $args[0] === $user_id ) {
				break;
			} else {
				if ( user_can( $args[0], 'administrator' ) && ! current_user_can( 'administrator' ) ) {
					$caps[] = 'do_not_allow';
				}
			}
			break;
	}
	return $caps;
}
add_filter( 'map_meta_cap', 'wc_modify_map_meta_cap', 10, 4 );
```

Whenever any capability related to users is in question, WooCommerce disallows it if the target for the modification is an admin. 

However, this "blacklist" kind of approach is insufficient. The consequence is that a Shop manager can modify any user and can assign any user role that is not admin.

This means that if I were to hack a Shopmanager account, who does NOT posses the "unfiltered_html" capability, I can simply assign the user role editor, which does have the ability to post JavaScript code, to a random user or customer, change their password, log in and then get a Stored XSS working and hack the admin.

Also, if there are any other custom user roles registered on a Wordpress installation, I can also assign those to me.

For example, the Plugin https://de.wordpress.org/plugins/backwpup/ registers the user type BackWpUp Admin, a user who can create and download backups of the WordPress installation.


Proof of Concept:

Simply login as a Shop manager, set the user role of a random user (e.g. a customer) to editor, change their password and then log into WordPress as that user. Then create a Post with your JavaScript Payload.

## Impact

Since Stored XSS is a very reliable way to escalate your privileges to Admin and this is occurs in every WooCommerce installation, I marked this as a high impact.

## Attachments
No attachments
