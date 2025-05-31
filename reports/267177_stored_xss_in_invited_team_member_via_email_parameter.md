# stored xss in invited team member via email parameter

## Report Details
- **Report ID**: 267177
- **URL**: https://hackerone.com/reports/267177
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-09T12:05:19.202Z
- **Disclosed**: 2017-11-03T08:12:19.118Z

## Reporter
- **Username**: coldd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hey there, while testing your program I found a stored XSS vulnerability which can placed by owners or **other staff members who have ability to manage members** and it will triggered by visiting invited team member page (e.g. https://partners.shopify.com/642416/invitations/15406).

### Reproduction Steps

1. login to partners.shopify.com.
2. navigate to *Team* (e.g. https://partners.shopify.com/642416/memberships).
3. click on *Invite owner*.
4. use `<svg/onload=alert(document.cookie)>abcdef@test.com` as email address.
5. click on *Send invite*.
6. you'll see a warning: *There was a problem connecting to Shopify*.
7. navigate to *Team* section again (e.g. https://partners.shopify.com/642416/memberships).
8. open invited user page (e.g. https://partners.shopify.com/642416/invitations/15411).

note: it does not matter who send the invitation, attack can be triggered by other team members (including owners) by opening invitation page.

also attached two file to show you that this vulnerability can placed by both owners and staff members with *manage members* access.

## Attachments
- xxs_by_owner.mp4
- xss_by_team_memeber.mp4
- Screen_Shot_2017-09-09_at_4.25.58_PM.png
