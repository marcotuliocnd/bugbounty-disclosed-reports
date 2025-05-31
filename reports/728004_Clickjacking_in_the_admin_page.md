# Clickjacking in the admin page

## Report Details
- **Report ID**: 728004
- **URL**: https://hackerone.com/reports/728004
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-11-02T20:29:49.480Z
- **Disclosed**: 2020-01-02T16:18:51.083Z

## Reporter
- **Username**: ant_pyne
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** 

Hello Rocket.Chat,

There is a clickjacking vulnerability in a very critical page which is the admin info page. For my installation, the URL https://penetrationtester.rocket.chat/admin/users was used for creating the PoC.

**Description:** 

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.

The admin info page of all rocket.chat installations would be vulnerable.

## Steps To Reproduce (from initial installation to vulnerability):

1. Open the attached `Clickjacking.html` on a browser and if you are logged in from an admin account, you will see that the page is loaded.

Requirement for attack - Knowledge of the admin email and rocket.chat installation link.

**Reason for marking this as medium** - Even though Clickjacking is always considered a low hanging fruit, the impact this can have is humongous.

**Recommendation** - X-Frame options header.

## Impact

If the UI overlay can be performed correctly by the attacker, this can lead to account takeover, manipulation of admin account, making any user admin or deleting and/or adding any user.

## Attachments
- Clickjacking.html
- admin_clickjacking.png
