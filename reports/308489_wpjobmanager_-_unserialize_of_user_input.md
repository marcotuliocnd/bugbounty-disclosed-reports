# wpjobmanager - unserialize of user input

## Report Details
- **Report ID**: 308489
- **URL**: https://hackerone.com/reports/308489
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-23T23:55:00.084Z
- **Disclosed**: 2018-03-03T08:12:40.041Z

## Reporter
- **Username**: b258ea62bf297b02afa9854
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Vulnerability occurs in `get_job_listings` function to be more precise line 160 - 164 in `wp-job-manager-functions.php`.
```
$result = new WP_Query( $query_args );
$cached_query = false;
set_transient( $query_args_hash, $result, DAY_IN_SECONDS );
```
e.g. you perform `serialize` on object that have `esc_sql`-ed values and after that you insert it in the database.

Function `get_job_listings` is called on many places in the plugin where its input is filled in by not authorized users => pre auth unserialization of user supplied input like in `class-wp-job-manager-ajax.php` :
```
add_action( 'job_manager_ajax_get_listings', array( $this, 'get_listings' ) );
```

Same issue was reported and fixed here  https://woocommerce.wordpress.com/2017/11/16/woocommerce-3-2-4-security-fix-release-notes/
( there is H1 report for it ) and it is based on this research https://medium.com/websec/wordpress-4-8-3-wrecking-ball-b172e2511fad

## Impact

If found interesting POI gadget chain or underling PHP is vulnerable from latest `unserialize` issues could cause multiple vulnerabilities from XSS to RCE.

## Attachments
No attachments
