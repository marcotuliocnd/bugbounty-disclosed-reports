# RCE as Admin defeats WordPress hardening and file permissions

## Report Details
- **Report ID**: 436928
- **URL**: https://hackerone.com/reports/436928
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-11-08T09:53:53.284Z
- **Disclosed**: 2020-06-09T09:09:01.539Z

## Reporter
- **Username**: simonscannell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
This vulnerability was found when I found myself in the following scenario:

My collegue set up WordPress on his local machine and challenged me to hack it. Before he gave me admin access he used the following hardeing mechanisms:

1. PHP Safe mode
2. The entire web directory was not writable
3. Disabled WordPress File edit
4. Disabled the ability to install plugins

The RCE demonsrated here allowed me to bypass all these restrictions and still execute arbitrary code on the machine. 

At fault is the wp_mkdir_p(); function.

## Overwriting directory permissions

wp_mkdir_p() is called by wp_upload_dir() when a user wants to upload a new media file. If the upload directory does not exist, WordPress will attempt to create it. WordPress determines what the upload directory is dynamically by calling get_option('upload_path'). 

```
function _wp_upload_dir( $time = null ) {
	$siteurl = get_option( 'siteurl' );
	$upload_path = trim( get_option( 'upload_path' ) );

	if ( empty( $upload_path ) || 'wp-content/uploads' == $upload_path ) {
		$dir = WP_CONTENT_DIR . '/uploads';
	} elseif ( 0 !== strpos( $upload_path, ABSPATH ) ) {
		// $dir is absolute, $upload_path is (maybe) relative to ABSPATH
		$dir = path_join( ABSPATH, $upload_path );
	} else {
		$dir = $upload_path;
```

Administrators can update that option to an arbitrary value in wp-admin/options.php

The value returned by _wp_upload_dir() is then passed to wp_mkdir_p();

```
function wp_mkdir_p( $target ) {
...

	if ( file_exists( $target ) )
		return @is_dir( $target );

	// We need to find the permissions of the parent folder that exists and inherit that.
	$target_parent = dirname( $target );
	while ( '.' != $target_parent && ! is_dir( $target_parent ) && dirname( $target_parent ) !== $target_parent ) {
		$target_parent = dirname( $target_parent );
	}

	// Get the permission bits.
	if ( $stat = @stat( $target_parent ) ) {
		$dir_perms = $stat['mode'] & 0007777;
	} else {
		$dir_perms = 0777;
	}

	if ( @mkdir( $target, $dir_perms, true ) ) {

		/*
		 * If a umask is set that modifies $dir_perms, we'll have to re-set
		 * the $dir_perms correctly with chmod()
		 */
		if ( $dir_perms != ( $dir_perms & ~umask() ) ) {
			$folder_parts = explode( '/', substr( $target, strlen( $target_parent ) + 1 ) );
			for ( $i = 1, $c = count( $folder_parts ); $i <= $c; $i++ ) {
				@chmod( $target_parent . '/' . implode( '/', array_slice( $folder_parts, 0, $i ) ), $dir_perms );
			}
		}

		return true;
	}

	return false;
}
```
In order to create the directory correctly, WordPress will first find out what the parent directory is by iterating over the path via dirname(). WordPress then copies the permissions of the parent directory so that the new upload directory will inherit those permissions.

if mkdir returns true, a check is made if our umask differs from the $dir_perms. If so, the $target path is exploded and  each part of it is chmod'd with the permissions of the $target_parent.

This function is vulnerable to a path traversal.


If an attacker sets 'upload_path' to

```
../../../../../../../var/tmp/content/../../../../../../home/simon/html/wordpress/../../../../../../var/tmp/content
```

the $target_parent will be 
```
../../../../../../../var/tmp/
```
which is writable, so the target permissions will be 777 (read, write, execute)

Since realpath() of the payload is /var/tmp/content and /var/tmp is writable, the call to mkdir() is successful. Then the call to umask() is made, which we can pass and then the $target path is exploded
and each part of it is appended to $target_parent (../../../../../../../var/tmp/) and then chmod with the permission bit of 777. 

This means at some point in the iteration the following call is made to chmod:

```
chmod('../../../../../../../var/tmp/content/../../../../../../home/simon/html/wordpress/', 0777);
```

This allowed me to set all directories writable again and bypass the first hardening mechanism.


## Uploading and executing a shell

In my other report, 'Remote Code Execution as Author' I have demonstrated how any file in the theme directory can be included and executed via the post meta value of _wp_page_template. Please read that report if the following is unclear.

By setting the upload_path to the theme directory and uploading a shell.txt with the content <?php phpinfo(); ?>

and then including it, I was able to execute arbitrary code.

## Impact

This is a universal code execution for administrators and dangers hardend WordPress installations and pretty much defeats https://codex.wordpress.org/Hardening_WordPress 

Depending on the plugins available of a target site, a simple reflected XSS can lead to RCE, even if all instructions for hardening are followed.

## Attachments
No attachments
