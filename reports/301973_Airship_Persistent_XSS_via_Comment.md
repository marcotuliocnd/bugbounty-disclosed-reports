# Airship: Persistent XSS via Comment

## Report Details
- **Report ID**: 301973
- **URL**: https://hackerone.com/reports/301973
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-03T13:49:01.314Z
- **Disclosed**: 2018-04-24T08:47:31.661Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Affected: Airship 2.0.0 (commit 15bdc0d)

CVSS
----

Medium 6.1 https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N

Description
-----------

The "name" field of a comment on a blog post is vulnerable to persistent XSS. 

When replying to a comment, the comment name is inserted into the DOM without encoding, leading to persistent XSS. 

By default, comments are open to anonymous users, although that can be disabled by an administrator.

Mitigating Factors
---------------------------

There are a couple of mitigating factors. 

Airship uses a CSP per default, which makes exploitation more difficult. The CSP can be disabled by an administrator though, and there may be attack possibilities even with the default CSP.

The attacked user has to actively click on "reply" for the payload to execute, meaning an attacker has to entice the user to do so.

Finally, the payload is shown in plaintext in the username field, which might make the attacked user suspicious. An attacker can try to hide it by using an overly long or complicated name. 

Details
-------

The vulnerability exists in file `/static/Hull/comments.js?`, specifically these lines where the author name is read out of the DOM and inserted into it again without proper encoding:

	window.replyTo = function(commentId, author) {
		$("#reply-to").html(
		    "<div class='blog-comment-label form-column'></div><div class='form-comment-field form-column'>" +
		    "<input type='hidden' name='reply_to' value='" + commentId + "' />" +
		        "Replying to " + author + " (Comment #" + commentId + ")" +
		    "</div>"
		);
	};

POC
---

0. Under bridge/admin/settings, check "allow unsafe inline" under javascript.
1. Leave a comment on a blog post. As name, use:
	'"><img src=no onerror=alert(1)>
2. Click on "Reply". The name will be read out via javascript and inserted into the DOM.

## Impact

With a successful exploitation, an attacker can among other perform arbitrary actions in the name of the attacked user, such as adding a new administrator, and thus gain full access to the application.

## Attachments
- persistent_xss.png
