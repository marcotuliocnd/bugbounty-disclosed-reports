# URL is vulnerable to clickjacking

## Report Details
- **Report ID**: 337219
- **URL**: https://hackerone.com/reports/337219
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-04-13T12:51:33.691Z
- **Disclosed**: 2018-04-14T12:52:07.378Z

## Reporter
- **Username**: hacker_one_one
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
##The browser has verified the identity:
Successfully implemented in IE browser

##Reproduce steps:
URLs do not have X-FRAME-OPTIONS set to DENY or SAMEORIGIN, and they are vulnerable to clickjacking.
Run under the browser's code and you will see that the listed links are vulnerable to clickjacking attacks
```
<html>
	<frameset cols="25%,25%,25%">
		<frame src="https://www.zomato.com/robots.txt" />
		<frame src="https://www.zomato.com/users/fan-feng-52680914" />
		<frame src="https://www.zomato.com/cairns-qld" />
	</frameset>
</html>
```
{F285366}

## Impact

Most of the zomato.com urls were tested and found that most basic urls support iframe display in IE.

E.g:
* https://www.zomato.com/users/fan-feng-52680914/edit
* https://www.zomato.com/invite
* https://www.zomato.com/cairns-qld
* https://www.zomato.com/cairns-qld/caffiend-cairns?zrp_bid=0&zrp_pid=14
* https://www.zomato.com/users/fan-feng-52680914/bookmarks
* https://www.zomato.com/users/fan-feng-52680914/managewallets

The hacker selected the **UI Redressing (Clickjacking)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
*.zomato.com

**Can a victim be tricked into unknowingly initiating a specific action?**
Yes

**What specific action can the user be tricked into?**
E.g: Hackers can lure users into the personal settings page, change data that is useful to hackers, delete accounts...

## Attachments
- zomatocom.png
