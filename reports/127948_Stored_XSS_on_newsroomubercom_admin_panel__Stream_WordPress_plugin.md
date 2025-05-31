# Stored XSS on newsroom.uber.com admin panel / Stream WordPress plugin

## Report Details
- **Report ID**: 127948
- **URL**: https://hackerone.com/reports/127948
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-03T09:22:57.277Z
- **Disclosed**: 2016-07-27T19:39:41.866Z

## Reporter
- **Username**: jouko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
*newsroom.uber.com* uses a WordPress plugin called Stream to log user activity. In some cases the logged events aren't sanitized properly and can contain HTML tags and JavaScript. An unauthenticated user can produce such a log message to inject JavaScript in the admin panel. When an administrator views the log, the script would be evaluated with administrator privilegs and can (under normal setup) be further used to inject attacker-supplied PHP code on the server.

#Reproducing#
The following command line can be used to inject JavaScript in the log with the *curl* tool:
~~~~
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e' --data 'post-password=foo' 'https://newsroom.uber.com/wp-login.php?action=postpass'
~~~~
Next, if an administrator clicks the Stream tab in the WordPress Dashboard, an alert box should pop up.

#Details#
The Stream plugin hooks many WordPress events to log user activity. In the file *connectors/installer.php* there is a *wp_redirect()* hook - the plugin checks every URL redirection to see if it involved the plugin editor. The code, compacted a bit:

~~~~php
        public static function callback_wp_redirect( $location ) {
                if ( ! preg_match( '#(plugin)-editor.php#', $location, $match ) ) {
                        return $location;
                }
                $type = $match[1];
                list( $url, $query ) = explode( '?', $location );
                $query = wp_parse_args( $query );
                $file  = $query['file'];
                if ( empty( $query['file'] ) ) {
                        return $location;
                }
                /* SNIP ... */ elseif ( 'plugin' === $type ) {
                        global $plugin, $plugins;
                        $plugin_base = current( explode( '/', $plugin ) );
                        foreach ( $plugins as $key => $plugin_data ) {
                                if ( $plugin_base === current( explode( '/', $key ) ) ) {
                                        $name = $plugin_data['Name'];
                                        break;
                                }
                        }
                }
                self::log(
                        _x(
                                'Edited %1$s: %2$s',
                                'Plugin/theme editing. 1: Type (plugin/theme), 2: Plugin/theme name',
                                'stream'
                        ),
                        compact( 'type', 'name', 'file' ),null, array( $type . 's' => 'edited' ));

~~~~
So if there is a redirect to a URL containing the string "plugin-editor.php" with a *file* query parameter, then the activity is logged. The *file* query parameter is included in the log entry.

The event is saved in Stream's database table and shown on the main tab of the plugin without sufficient HTML sanitizing.

There are many ways to generate an HTTP redirect in WordPress. The method used in the above example is requesting *wp-login.php* which, with appropriate arguments, redirects the browser back to the Referer: header's value.

#Impact#
The JavaScript stored by an unauthenticated attacker would get executed with administrator privileges, thus having full control over the site contents. Under a normal WordPress setup it could also modify existing PHP files via the plugin or theme editors, leading to server-side compromise.

I tested this on my local test system with the latest WordPress and Stream 1.4.9.

## Attachments
No attachments
