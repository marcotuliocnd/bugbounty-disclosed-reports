# H1514 Server Side Template Injection in Return Magic email templates?

## Report Details
- **Report ID**: 423541
- **URL**: https://hackerone.com/reports/423541
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-10-13T22:34:15.431Z
- **Disclosed**: 2019-04-04T17:35:23.641Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Summary:**
Possible template injection in return magic email templates.

**Description:** 
I've been playing with return magic workflow email templates and there seems to be some kinda of template injection but I am not sure if it's exploitable or even valid.
Here is why I think it could be vulnerable: 
I set the email template to the following and then test the template and then the results go to my gmail inbox.
`{{ this }} ` -> `[Object Object]` 
`{{ this.__proto__ }}` --> `[Object Object]`
`{{ this.__proto__.constructor.name }}` --> `Object`
I couldn't go further but it seems like the backend is NodeJs.

## Steps To Reproduce:

1. Install Return Magic app
2. Navigate to `https://<shop>.myshopify.com/admin/apps/returnmagic`
3. Open Settings tab from the top menu and then open **Emails** --> **Workflow** from the left menu
4. Click Edit for any email template then at the editor click the code icon and enter `{{this}}` 
5. Go back to **Workflow** page and click **Send me a test email** for the template you edited then enter your email and check your inbox.
6. You'll see `[Object Object]`

## Supporting Material/References:
{F360290}

{F360291}

## Impact

Could be a Server Side template injection that can be used to take over the server ¯\_(ツ)_/¯

## Attachments
- Screen_Shot_2018-10-14_at_12.31.43_AM.jpg
- Screen_Shot_2018-10-14_at_12.31.49_AM.jpg
