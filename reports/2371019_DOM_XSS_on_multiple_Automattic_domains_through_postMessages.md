# DOM XSS on multiple Automattic domains through postMessages

## Report Details
- **Report ID**: 2371019
- **URL**: https://hackerone.com/reports/2371019
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-02-12T11:08:21.025Z
- **Disclosed**: 2024-02-26T08:24:28.416Z

## Reporter
- **Username**: renniepak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi Automattic team,

I have found a 2 flaws that when combined lead to DOM XSS on every website that is using Jetpack with the [Likes](https://jetpack.com/support/likes/) feature enabled. 

The 2 flaws are respectively:

- A DOM XSS vulnerability on https://widgets.wp.com/sharing-buttons-preview/
- The Jetpack plugin creates a postMessage listener allowing messages from the "widgets.wp.com" origin, but will not validate nor encode the `avatar_url` parameter before applying it to the DOM causing XSS.

## Reproduction:

- Navigate to https://0-a.nl/jetpackxssclick.html?url=https://wordpress.com/blog/2024/01/31/http3/ and click the `PoC link`.

## Result

In the newly opened window a `alert(document.domain)` will pop on https://wordpress.com

{F3044196}

## Root causes

### XSS on widgets.wp.com

The DOM XSS here is caused by the following included script:

*https://widgets.wp.com/sharing-buttons-preview/js/preview.js*
```javascript
        if (_.isArray(r.custom)) {
            i = _.template(e("#tmpl-custom-button").html());
            s = _.map(r.custom, function(e) {
                var t = g.parseUrl(e.icon);
                return new d({
                    ID: e.name,
                    markup: i({
                        icon: o + "/" + t.host + t.pathname,
                        name: e.name
                    })
                })
            });
            n = n.concat(s)
        }
```
It's not that obvious because of the minified javascript but what happens is that 2 url parameters are parsed and used to add a UI element to the DOM:

?custom[0][icon]=iconurl&custom[0][name]=name

We can abuse the `name` parameter to create an XSS.

https://widgets.wp.com/sharing-buttons-preview/?custom[0][icon]=iconurl&custom[0][name]=%22%3E%3Cimg%20src%20onerror=alert()%3E

{F3044216}

### Insecure postMessage listener / codeblock

When we navigate to a website that has the Jetpack Likes feature enabled, a postMessage listener will be launched that will execute the `JetpackLikesMessageListener` function when a message arrives.

We can see it contains an origin check to only allow messages from widgets.wp.com. We can bypass this now since we have XSS on that domain:

```javascript
const allowedOrigin = 'https://widgets.wp.com';
	if ( allowedOrigin !== event.origin ) {
		return;
	}
```

When we follow the code to the `showOtherGravatars` case, you'll see it use a `liker.avatar_URL` parameter (that is received via a postMessage) directly with innerHTML. This will allow us to send a tampered postMessage causing the XSS to be triggered.

```javascript
element.innerHTML = `
				<a href="${ encodeURI( liker.profile_URL ) }" rel="nofollow" target="_parent" class="wpl-liker">
					<img src="${ liker.avatar_URL }"
						alt=""
						style="width: 28px; height: 28px;" />
					<span></span>
				</a>
				`;
```

## Mitigation

- Applying input validation and output encoding on the sharing-button page to mitigate the XSS https://widgets.wp.com/sharing-buttons-preview/
- Defence in depth: now any XSS on widgets.wp.com will lead to multiple XSSes all over the internet (anyone using the Jetpack Likes features). To mitigate this, I would also apply `encodeURI` to the avatar_url before using it in `innerHTML`. Upon further research it seemed older version of the plugin did exactly this, but in later versions this was removed.

## Impact

XSS on a number of Automattic domains:

https://0-a.nl/jetpackxssclick.html?url=https://wordpress.com/blog/2024/01/31/http3
https://0-a.nl/jetpackxssclick.html?url=https://jetpack.com/blog/wordpress-navigation-menu/

You probably have better insights in this (also I'd love to hear the actual number :) ) but searching publicwww.com revealed over 100k websites using this feature, meaning 100k domains vulnerable to this XSS.

This is also the reason I picked `High` for severity. If it was just wordpress.com I would probably have gone for `Medium` which is more typical for these kind of XSSes without providing more impact specific to the vulnerable domain. But in this case the vulnerability reaches far beyond the 1 domain.

In general, if an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user. Amongst other things, the attacker can:

* Perform any action within the application that the user can perform.
* View any information that the user is able to view.
* Modify any information that the user is able to modify.

## Attachments
- image.png
- Screenshot_2024-02-12_at_09.35.51.png
