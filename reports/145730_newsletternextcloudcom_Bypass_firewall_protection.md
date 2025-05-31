# newsletter.nextcloud.com: Bypass firewall protection

## Report Details
- **Report ID**: 145730
- **URL**: https://hackerone.com/reports/145730
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-18T17:37:03.322Z
- **Disclosed**: 2016-07-18T22:01:23.434Z

## Reporter
- **Username**: bug_cat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Security team,

I would like to report a vulnerability bypass firewall.
when you are trying to navigate this  [link](https://newsletter.nextcloud.com/admin) it needs authentication
but it’s possible to access to admin panel when you add `index.php` after `/admin/`.
`https://newsletter.nextcloud.com/admin/index.php`

P.o.C : video in attachment.

## Attachments
- firewall.ogv
