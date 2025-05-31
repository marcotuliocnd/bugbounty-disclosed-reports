# Email Confirmation Bypass in your-store.myshopify.com which leads to privilege escalation

## Report Details
- **Report ID**: 910300
- **URL**: https://hackerone.com/reports/910300
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-28T13:09:26.941Z
- **Disclosed**: 2020-09-15T06:47:43.076Z

## Reporter
- **Username**: say_ch33se
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify, I have found a bug by which I can verify any email on .myshopify.com, the bug is very strange but it works. Also I can take over the accounts but only the ones which do not have SSO.

To reproduce please follow the steps exactly as I written otherwise you will not be able to reproduce it.

Steps to reproduce: 

1. Go to your partners account and make a store
{F886149}

2. Go to your new store and don't verify email, then go to admin/settings/account/youraccountnumber
{F886151}

3. Change your email to victims email(in my case say_ch33se+111@wearehackerone.com)
{F886138}

4. Go to burps match and replace and replace your email with the email you want to takeover(in my case say_ch33se+111@wearehackerone.com)
{F886137}
{F886139}
{F886140}

5. Refresh the account page so its updated with victims email
{F886141}

6. Still on accounts page click on Upload photo and upload any photo and save
{F886142}

7. After that uncheck match and replace, refresh and on accounts page change email to your email which you own so you can get a confirmation email
{F886143}

8. In burp check match and replace again to replace your email with the email you want to takeover(same as above)
9. Go to your email which you own where is the confirmation link and click on it(in the browser where you are already logged in)
10. On that page where you verified email, upload another image
{F886144}

11. Now click on Review accounts
12. Enter stores password and you'll be greeted with Shopify ID
13. Click on Set up Shopify ID
{F886145}

14. And there you got it
{F886146}

15. Click continue and set up password
{F886147}
{F886148}

16. Now you can access vitims store and partner account without any problems

## Impact

Ability to confirm any email on your-store.myshopify.com and leverage SSO to take over accounts.

## Attachments
- burp1.png
- 3.png
- burp2.png
- burp3.png
- 4.png
- 5.png
- 6.png
- 7.png
- 8.png
- 9.png
- 10.png
- 11.png
- 1.png
- 2.png
