# A profile page of a user can be denied from loading by appending .html to the username

## Report Details
- **Report ID**: 475098
- **URL**: https://hackerone.com/reports/475098
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-05T17:12:03.115Z
- **Disclosed**: 2021-08-30T11:02:43.660Z

## Reporter
- **Username**: maruthi12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:** I was able to create a user with the username "dashboard.html". Once, the account is set up, when the user clicks on his profile, the actual dashboard will show up instead of his profile page. Same can be done for all the HTML pages in GitLab.



## Steps To Reproduce:


  1. Register a new user with "some_html_page_in_gitlab.html"
  1. After logging in. click on the profile tab, it will be redirected to the dashboard page.
  1. I even tried the username "profile.html", it is getting directed to the profile tab.

## Impact

The major impact here I can think of is that a user can hide his profile from the public just by having a clowny username.

## Attachments
No attachments
