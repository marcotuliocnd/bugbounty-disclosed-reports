# [BuddyPress 2.9.1] Open Redirect via "wp_http_referer" parameter on "bp-profile-edit" endpoint

## Report Details
- **Report ID**: 277502
- **URL**: https://hackerone.com/reports/277502
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-15T20:36:39.950Z
- **Disclosed**: 2017-11-02T16:56:46.533Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi,

In a similar manner to #228569, it is currently possible to execute authenticated open redirections via the `wp_http_referer` parameter used in the [BuddyPress](https://wordpress.org/plugins/buddypress/) extended user edit screen.

## Proof of concept

Upon accessing the below URL, please select the "Update Profile" button, then select the "**←Back to Users**" link. This will redirect a target to the attacker-specified address (in this case, "google.com").


```
http://instance/wp-admin/users.php?page=bp-profile-edit&wp_http_referer=https://google.com
```

### Supporting evidence

{F229538}

Thanks,

Yasin

## Attachments
- BuddyPress_Redirect.png
