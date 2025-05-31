# Unsafe handling of protocol handlers

## Report Details
- **Report ID**: 369185
- **URL**: https://hackerone.com/reports/369185
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-20T14:09:09.983Z
- **Disclosed**: 2018-09-24T23:36:53.728Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Brave browser (macOS) handles protocol handlers in unsafe way (and differently from other browsers).
Key differences between protocol handlers handling in Brave and other browsers:

### Open external app vs Open "Terminal" 

Brave only asks about opening external app. 
Other browsers (e.g. Chrome) asks about opening a specific app. 

Try to open a `ssh://` link in Chrome: browser opens a popup with a question similar to "Do you want to open "Terminal"?" 

Opening `ssh://` in Brave results in a popup with a content similar to : "Do you want to open external app for ssh://"

> Sorry, I didn't remember actual popups' content + I've got RU version

#### Impact

User doesn't know which app will be opened after allowing to open an external app.
That means it easier for attacker to trick user to open an external app in Brave compared to other browsers.

This applies to all protocol handlers in Brave browser, not only `ssh://` or `telnet://`.

### ssh:// and telnet:// without confirmation

In Chrome/Safari/FF, after opening Terminal using `ssh://` link, Terminal shows an alert with a text similar to "Do you want to initiate ssh session with **example.com*?".

Next things worth noting:
1. There is an additional confirmation dialog in Terminal while navigating to ssh:// through browser.
1. Default answer in the confirmation dialog is negative. ("Don't connect")
3. **example.com**: user sees exact host

Brave browser initiates `ssh://` and `telnet://` sessions automatically after opening the external app (Terminal) without confirmation messages.

If browser handles `ssh://` URLs  by default, any iframe with `src="ssh://example.com"` could automatically start ssh session without user's interaction.  Additionally, it's possible to silently initiate ssh connection, by running `alert()` on `window.onblur` event - Terminal isn't visible in this case.

Same applies to `telnet://` too.

## Version:
Brave	0.22.810
V8	6.7.288.43
rev	8f30eeb
Muon	7.0.6
OS Release	17.6.0
Update Channel	Release
OS Architecture	x64
OS Platform	macOS
Node.js	7.9.0
Brave Sync	v1.4.2
libchromiumcontent	67.0.3396.71

## Steps To Reproduce:

1. Open exploit.html
2. Click `ssh://google.com` link
3. Allow opening an external app
4. Terminal launched without additional alerts/warnings

1. Open `exploit.html`
2. Click `ssh://google.com` link
3. Remember `ssh://` (set as default handler)
4. Add iframe <-- Any iframe could automatically trigger ssh connection without confirmation

## Impact

1. No confirmation message for external apps. - definitely bad behavior. Brave handles all protocol handlers in this way, not only `ssh://` || `telnet://`

2. SSH connection without confirmation - ssh sessions leak important user info: IP, username, etc. Also, it opens a wider attack surface.

3. If `ssh://` is allowed to open by default (i.e. "remembered"): Any iframe could automatically trigger ssh session. It's possible to start ssh session without user's notice by calling `alert()` after navigation to `ssh://`

4. Terminal doesn't alert hostname in confirmation dialog (because of no confirmation dialog), so it's possible to spoof host to which user connects. 

Example/Attack scenario for #4:
1. link points to `ssh://abc.xyz` and the text of the link is "Connect to google.com". 
2. User clicks and initiates connection to abc.xyz. 
3. In most cases host will be visible in terminal tab's header. However, because ssh command isn't printed in terminal output while navigating through `ssh://` URLs, it's ease to not notice real host name and continue treat it as `google.com`.

## Attachments
- exploit.html
