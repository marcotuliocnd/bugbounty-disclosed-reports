# Privilege Escalation in Point Of Sale Application from POS Manage Staff Role to potentially Store Owner

## Report Details
- **Report ID**: 985150
- **URL**: https://hackerone.com/reports/985150
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-18T06:33:28.990Z
- **Disclosed**: 2020-11-19T16:23:26.769Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I was playing a bit with the Point Of Sale application and it came to my attention that it is possible to navigate from the Point Of Sale Application up to the Plan & Permission in the admin. I am not sure if this is  intentional, but since it leads to potentially take over a shop, I'm reporting it.

Within he Point Of Sale application, a staff with full admin permissions can open the Point Of Sale channel using the embedded **Magage POS roles** link. By doing so and by using some nested links, it is possible to navigate up to the Plan & Permissions admin view giving him access to some store owner permissions:
 1. Add staff account
 1. Manage staff account
 1. Update login service
 1. Transfer ownership (requires the shop owner password but could be used to bypass the 2FA protection)

Given that, a POS staff with only Manage Role could escalate his privileges up to Full Permissions and potentially even take over the shop if knows the admin password.

## Steps to reproduce
1. Create a Staff with Full Permissions
1. Create a POS user with only Manage Staff permissions
1. From the Point Of Sale Application, log-in with the admin user then enter the PIN of the POS User from Step 2
1. Go to **Staff**, select the staff with Full Permissions from Step 1 and change its PIN to 1234
1. Lock the application screen and log back in using the 1234 PIN, giving you Full Permissions access within the Application
1. Go to **Staff**, select any staff, edit its **POS APP ACCESS** and click on **Manage POS Roles**
1. From the Roles listing page, open the Full Permissions staff's role and scroll at the bottom down so you can see the **Assigned Staff** section and click on the Staff
1. Scroll at the bottom again and click on **Manage Shopify admin access**, this is opening up the staff page from **Plan and Permissions**.
1. At the top of the page, click on breadcrumb navigation **Plan and Permissions** link bringing you to the `https://shop.myshopify.com/admin/settings/account`

At this point, as the Point Of Sale application is using the physically authenticated user, you're given access to store owner features as mentioned earlier.

## Impact

A staff with **Manager Staff Role** within the Point Of Sale application can escalate his privilege to a Full Permission staff and could potentially transfer the shop ownership by using the **Transfer ownership** link within the **Plans & Permissions** page.

## Attachments
No attachments
