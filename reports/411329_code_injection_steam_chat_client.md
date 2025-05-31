# code injection, steam chat client

## Report Details
- **Report ID**: 411329
- **URL**: https://hackerone.com/reports/411329
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-19T03:54:17.233Z
- **Disclosed**: 2019-01-07T20:01:32.520Z

## Reporter
- **Username**: zemnmez
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
The steam chat client allows oEmbed, apparently based on a whitelist. One of the whitelisted oEmbedis codepen. When a codepen is created, it can be sent as a link to another steam user, and the code inside the codepen will execute within the privileged Steam Chat context.

You can send these codepen links to someone and they'll perform some action when you open them

https://codepen.io/zemnmez/pen/mGQvvq this one pops calc.exe
https://codepen.io/zemnmez/pen/eLLYLr  this opens a ton of windows
https://codepen.io/zemnmez/pen/pOQBYa this one opens team fortress 2

## Impact

While poking around inside this context I noticed a few things:
1. `steam://` links are executed in a privileged mode not normally accessible in the steamwebhelper. `steam://`uris are executed immediately, and in most contexts without confirmation.  This codepen, if sent to a user will immediately run Team Fortress 2 when clicked, if installed: https://codepen.io/zemnmez/pen/zJMeYe (you can use the same technique with `runsafe` to nuke a user's settings).

Since there is no confirmation here, I strongly believe with some extra research a game could be opened with command line parameters and no confirmation that results in remote code execution as in [this paper](http://revuln.com/files/ReVuln_Steam_Browser_Protocol_Insecurity.pdf). Anything that otherwise happens with no confirmation, such as play / pausing music and accepting guest passes is controllable by this method.

2. All custom-protocol urls are executed, including windows internal protocol urls. the `jarfile:[FILEPATH] [PARAMS]` form can be used to run any java program on their PC, same with wscript.exe and .js or .vbs files via the `JSEFile:` protocol. In windows, every file format has its own custom protocol which is used internally to execute files of that format.

2. A `SteamClient` API is exposed via the JS VM to the browsing context.  Ordinarily this API is very slim (perhaps for security purposes), but by using `open('chrome-devtools://devtools/bundled/inspector.html')` to open a url that doesn't open in the browser we can spawn a new window with fewer restrictions. From here we can read the user's cursor position, move the window around, make it bigger smaller, paste (though I couldn't get the API to work for this) and generally be a nuisance. I feel very sure there are APIs I can abuse here, but I've had a hard time finding them.

## Attachments
No attachments
