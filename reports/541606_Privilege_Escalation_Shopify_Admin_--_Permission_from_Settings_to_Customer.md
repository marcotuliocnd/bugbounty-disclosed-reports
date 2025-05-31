# [Privilege Escalation] Shopify Admin -- Permission from Settings to Customer

## Report Details
- **Report ID**: 541606
- **URL**: https://hackerone.com/reports/541606
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-17T22:43:29.590Z
- **Disclosed**: 2019-07-05T19:46:02.483Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

This is my first report to shopify, hope this report is not too bad considering the fact I can't verify this finding since I don't have shopify plus access.

##Summary 
This [page](https://help.shopify.com/en/api/reference/plus/multipass)  talks about the multipass, and quoting from the multipass page FAQ

###Security considerations
> If your secret ever leaks.... You should do this as quickly as possible since everybody who knows the secret can potentially access every customer account!

It means anyone with this secret can get access to every customer in this shopify instance.

And interestingly, the multipass secret is located in the Settings part of shopify, so it means if a shopify staff has no permission to view/edit customer's details but has the permission to view/edit the settings of the shopify account, then this secret would help him to gain access to customer's details for this shopify instance.

But this is all speculation since I don't  have a shopify plus account, so I can only assume this scenario was not considered while developing the Multipass feature. Hope I am correct, and if I am correct, then this would mean small privilege escalation from settings permission to customer permission for shopify staff.

## Steps to reproduce
1. As a shopify plus owner, visit `https://YOUR_SHOP.myshopify.com/admin/settings/account/new` to create a new account with only `Settings` permission {F471099}
2. As the newly added staff member, visit the confirmation email's link and create a password and login to your store's url, then visit `https://h1-shopfiy-ron.myshopify.com/admin/settings/checkout`
3. select Accounts are required or optional
4. Enable Multipass 
5. Now you are reading the secret of the multipass -- meaning you can read customer's details using that

Step 4 and 5 are not verified yet, if it works, it means this multipass feature helps a staff member to escalate access from `settings` to `customers`

## Impact

Step 4 and 5 are not verified yet, if it works, it means this multipass feature helps a staff member to escalate access from `settings` to `customers`

## Attachments
- ppppppoc.PNG
