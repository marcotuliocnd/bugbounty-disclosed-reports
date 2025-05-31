# No user confirmation when an auto-updated extension gets more permissions

## Report Details
- **Report ID**: 199243
- **URL**: https://hackerone.com/reports/199243
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-18T04:39:31.825Z
- **Disclosed**: 2017-01-20T09:12:43.854Z

## Reporter
- **Username**: i1iii11iiiii111iii1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

In Chrome, when extensions are auto-updated, if the permissions change, the extension is preventatively disabled and the user has to confirm they wish to re-enable it with the additional permissions. While it appears Brave has a functioning Extension auto-updater (e.g. for the PDF extension), a simulation of an update to that Extension suggests that Brave will silently auto-update (and leave enabled) Extensions which request additional permissions.

Agreeing to run a certain extension (which needs a certain set of permissions) is not the same thing as the user consenting for a future update where the permission set grows to include, say, https://*/* or something. Users are shown those permissions in about:extensions and disable extensions that include things that they don't consent to. Auto-update should not be a silent mechanism for third party providers of extensions to elevate their privileges without the user's knowledge.

I realize that, today, the only extension is the PDF viewer, but your recent blog post says you're working on supporting other third party extensions and DevRel says they will use the auto-updater, so this is a heads up that this becomes exploitable once you start supporting other extensions. If that means this doesn't qualify for HackerOne no worries, I am not interested in disclosure or money or whatever just wanted to pass along a friendly note. 

## Products affected: 

From about:brave:

Name	Version
Brave	0.12.15
Muon	1.4.31
libchromiumcontent	53.0.2785.143
V8	5.3.332.47
Node.js	6.5.0
Update Channel	dev
os.platform	win32
os.release	10.0.14393
os.arch	x64

## Steps To Reproduce:

Install brave. View about:extensions so that it will auto-open the next time you launch Brave.
Quit brave.
Navigate to C:\Users\you\AppData\Roaming\brave\Extensions\jdbefljfgobbmcidnmpjamcbhnbphjnb in Windows explorer.

Rename folder from 1.6.387 to 1.6.385
Open folder
Edit manifest.json to change version number declared in manifest to 1.6.385
Also remove "tabs" permission from manifest.

(I'm not super familiar with Brave so if there's some other registry of extensions I should have manipulated to better simulate this update scenario, please advise and accept my apologies if this scenario is somehow invalid.)

Launch Brave

Observed: Brave extension auto-updater kicks in. I briefly saw 1.6.385 in the window before it updated to 1.3.387.
Brave obtains 1.6.387 and it unpacks it in my extensions folder alongside 1.6.385. Permissions go back to having "tabs".

Note that I was only able to reproduce on the first try, second try I had problems. I think I am running into some frequency limit for auto-update checks, I ran through the steps a second time (deleted the 387 folder and bounced Brave again) but this time it didn't auto update so was stuck back at my 1.6.385 simulation.  To get it to reliably reproduce, I had to blow away my entire c:\Users\you\AppData\Roaming\brave folder, launch once to get clean appdata, then repeat the steps above. This try (third try) reproduced the problem, so be advised that reproducing this might be a little fiddly. Sorry. Someone familiar with the design of Brave can certainly comment on if this how this was designed to work though - I suspect this may be as-currently-designed behavior?

## Supporting Material/References:

Brave DevRel statement that third party extensions will be coming and updated using this auto-updater:
https://twitter.com/BraveSampson/status/821549058485604352

## Attachments
No attachments
