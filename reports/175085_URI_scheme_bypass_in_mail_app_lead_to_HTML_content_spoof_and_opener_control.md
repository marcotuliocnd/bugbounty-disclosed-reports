# URI scheme bypass in mail app lead to HTML content spoof and opener control

## Report Details
- **Report ID**: 175085
- **URL**: https://hackerone.com/reports/175085
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-11T07:59:08.673Z
- **Disclosed**: 2017-01-12T20:02:32.175Z

## Reporter
- **Username**: trichimtrich_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Bug
When we load a HTML mail from mailbox via api, etc
`http://nextcloud/index.php/apps/mail/accounts/<accountID>/folders/SU5CT1g=/messages/<mailID>/html`
Our content will be passed to HTML Purifier to strip malicious XSS patterns.
After that, an filter will apply to transform acceptable URI schemes `http, https, ftp, cid` to redirect/proxy service. 
There's a bug in here, only `http, https, cid` scheme are filtered.
So we can add `src` attribute or `href` from url with scheme `ftp` or `NULL` (like `'../../abc/xyz'`) . We can easily bypass image filter (also Content-Security-Policy)
Notice that there's a filter that append `target=_blank` to all `<a>` tag. This can lead to opener bug [https://mathiasbynens.github.io/rel-noopener/#hax] (https://mathiasbynens.github.io/rel-noopener/#hax) that I learned from [124620] (https://hackerone.com/reports/124620).
And finally it can leak accountID of user

## PoC
* Attacker create a shared link of a image

`http://192.168.200.117/nextcloud/index.php/s/HUw7Cwa40Phlt8v/download`
* Attacker start a ftp server and create a html page.

`ftp://chim:chim@localhost/test.html`
* Attacker send a HTML email

```
<h1>test schema</h1>
<p>
	<a href="http://file.trich.im">Link via redirect</a><br>
	<a href='ftp://chim:chim@localhost/hihi.html'>Bypass link</a>
</p>

<p>
	Filtered img<img src='http://192.168.200.117/nextcloud/index.php/s/HUw7Cwa40Phlt8v/download'><br>
	Bypass img <img src='/nextcloud/index.php/s/HUw7Cwa40Phlt8v/download'>
</p>
```

## Video Demo https://www.youtube.com/watch?v=BdOD49gokdI

## Attachments
- shareimg.png
- send.png
