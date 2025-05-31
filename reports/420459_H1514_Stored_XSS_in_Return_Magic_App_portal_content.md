# H1514 Stored XSS in Return Magic App portal content

## Report Details
- **Report ID**: 420459
- **URL**: https://hackerone.com/reports/420459
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-07T23:37:26.921Z
- **Disclosed**: 2019-11-08T11:03:14.937Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Summary:** 
Stored XSS vulnerability was found in return magic app portal content which executes in the application domain in `https://services.alveo.io/dashboard-shopify/settings/portal/content` 

**Description:** 
It's been found that Return Magic app allows users to add HTML content to their return portal without sanitizing the HTML which makes it possible to inject malicious tags that can be used to execute arbitrary JavaScript through other users' sessions.

## Steps To Reproduce:
1. Install Return Magic app
2. Navigate to `https://<shop>.myshopify.com/admin/apps/returnmagic`
3. Open **Settings** tab from the top menu and then open **Portal** --> **Content** from the left menu 
4. For the textarea where you enter your portal content, click the **Code** icon and enter `Test <img src=x onerror=alert(2)>` then click **Save** 
5. Now each time a user opens the portal settings page, `alert(2)` will be executed.
6. XSS also triggers in `https://services.alveo.io/portal/search?shop=<shop>.myshopify.com` 
{F356974}

## Impact

Through this vulnerability a malicious user will be able to execute JavaScript through other user's sessions' which allows him to do malicious actions such as stealing sensitive information, submitting requests that bypass csrf protection ..etc

## Attachments
- Screen_Shot_2018-10-08_at_1.36.21_AM.jpg
