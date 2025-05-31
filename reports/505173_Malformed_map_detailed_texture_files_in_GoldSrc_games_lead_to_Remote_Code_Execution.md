# Malformed map detailed texture files in GoldSrc games lead to Remote Code Execution

## Report Details
- **Report ID**: 505173
- **URL**: https://hackerone.com/reports/505173
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-05T15:06:49.834Z
- **Disclosed**: 2019-09-17T17:34:12.214Z

## Reporter
- **Username**: nyancat0131
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
A crafted map detailed texture file (`maps/<map_name>_detail.txt`) can be used to exploit a stack overflow vulnerability in `hw.dll` that can lead to remote code execution.

# Reproduction
I used Counter-Strike for PoCs.

## Using a listen server
- Place attached `cs_assault_detail.txt` in `cstrike/maps` folder
- Start the game
- Open the console, type `r_detailtextures 1`
- Host a new game on `cs_assault`
- The game crashes when trying to load detailed textures

## Using a dedicated server
- Place attached `cs_assault_detail.txt` in `cstrike/maps` folder on the server
- Write an AMXX plugin that does the following:
 - Use `precache_generic` to precache `maps/cs_assault_detail.txt`
 - Use `client_cmd` to force clients to execute `r_detailtextures 1`
- Host a new server on `cs_assault`
- Open the client and connect to the server
- The client crashes when trying to load detailed textures
Note: `precache_generic` has some bug (https://github.com/ValveSoftware/halflife/issues/1551). The workaround is to setup `sv_downloadurl` for the server.

# Exploitability
Since the file can be sent from the server using `precache_generic`, and the server has the ability to slowhack clients, attackers can use this to trigger RCE on clients.

## Impact

Attackers can exploit this bug to execute arbitrary unauthorized codes on victim's computer.

## Attachments
- cs_assault_detail.txt
- windbg_log.txt
- crash_hl.exe_20190305214702_1.dmp
