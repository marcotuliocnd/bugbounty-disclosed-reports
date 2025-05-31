# Stored XSS on Share-popup of a directory's Gallery-view

## Report Details
- **Report ID**: 145355
- **URL**: https://hackerone.com/reports/145355
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-17T11:35:04.019Z
- **Disclosed**: 2016-07-19T12:51:26.649Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi,
Nice with the program launch! Congrats!

I noticed that there was a Share-icon when toggling to the Gallery-view of a directory under "Nextcloud Files":
{F99938}

If your directory has a malicious name such as a HTML-payload: `<img src=x onerror=alert(1)>`, this HTML will run when clicking on the Share-icon:
{F99937}

I see that you have a proper CSP in place, but remember that Internet Explorer is not there yet:
{F99939}

Also, since any user could create files, a user could potentially execute this for an admin (if that admin is not using a CSP-supported browser that is).

Let me know if you need more information.

Regards,
Frans

## Attachments
- Screen_Shot_2016-06-17_at_13.27.09.png
- Screen_Shot_2016-06-17_at_13.31.39.png
- Screen_Shot_2016-06-17_at_13.33.09.png
