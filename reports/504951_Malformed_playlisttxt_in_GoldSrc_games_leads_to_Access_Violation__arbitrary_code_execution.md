# Malformed playlist.txt in GoldSrc games leads to Access Violation & arbitrary code execution

## Report Details
- **Report ID**: 504951
- **URL**: https://hackerone.com/reports/504951
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-04T22:02:57.059Z
- **Disclosed**: 2019-09-17T17:34:09.603Z

## Reporter
- **Username**: nyancat0131
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
A crafted `playlist.txt` can be used to exploit a stack overflow vulnerability in `GameUI.dll` that can lead to arbitrary code execution.

# Reproduction
Place attached `playlist.txt` in game directory (`valve`, `cstrike`, etc.). The game will crash when it tries to play `Splash` track.

# Exploitability
The file can be sent from server with `precache_generic` function (custom `mp.dll`, amxx plugins, etc.). I don't know ant way to force reload the playlist, so for the exploit to trigger, the client must be restarted. In my opinion, it's still dangerous. And this method won't work if the client already had `playlist.txt` in the game directory.

## Impact

The attacker can use this to do many things, from crashing the client to stealing important data.

## Attachments
- playlist.txt
- windbg_log.txt
- crash_hl.exe_20190305050103_1.dmp
