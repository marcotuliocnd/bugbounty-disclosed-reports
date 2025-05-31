# Bypass for Domain-level redirects (Unvalidated Redirects and Forwar)

## Report Details
- **Report ID**: 1582160
- **URL**: https://hackerone.com/reports/1582160
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-26T13:04:21.160Z
- **Disclosed**: 2022-06-22T22:57:33.323Z

## Reporter
- **Username**: thypon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

{F1745460}

While testing for the ability to define custom redirects in Gitlab Pages,
I discovered I was able to define `Domain-level redirects` which are explicitly disabled in the documentation.
At a first glance, the validation step seems to disable any link not starting with `/`,
It has however to be noted that distinct domain redirects can be defined even with starting slash/backslash.
For example, all these three examples will redirect to another domain:

- `//anotherdomain.com/...`
- `/\anotherdomain.com/...`
- `\\anotherdomain.com\...`

All these previous domains are equivalent to writing `https?://anotherdomain.com/...`

An attacker may define vanity URLs hosted on GitLab targeting phishing websites.

### Steps to reproduce

In order to reproduce this vulnerability follow these steps:

1. Generate a new pages project (eg. anyone from https://gitlab.com/pages ).
      You can create a new project forking https://gitlab.com/pages/jekyll
2. Enable CI/CD pipeline
3. Enable pages support in Settings
4. Add a `_redirects` file and include that file in the output through the `_config.yml` include directive
5. Add a redirect such as `/jekyll-test/test3.html /\desktop.pompel.me\test2.html 301```
6. Wait for the CI to complete the deploy
7. Navigate to the defined redirect
8. Verify that the redirect is reaching an external website

### Impact

An attacker may define vanity URLs hosted on GitLab targeting phishing websites.

### Examples

https://gitlab.com/miwaxe/jekyll-test/-/blob/master/_redirects

```
/jekyll-test/antani1.html /projectname/antani2.html 302
/jekyll-test/test1.html \\projectname\@desktop.pompel.me/test2.html 302
/jekyll-test/test3.html /\desktop.pompel.me\test2.html 301
```

### What is the current *bug* behavior?

Check the attached demo video {F1745467}

### What is the expected *correct* behavior?

The redirects should not happen to external domains. 
This is pointed out in the documentation https://docs.gitlab.com/ee/user/project/pages/redirects.html and is explicitly forbidden.

### Relevant logs and/or screenshots

Check the attached screenshot {F1745460}

## Impact

An attacker may define vanity URLs hosted on GitLab targeting phishing websites.

## Attachments
- screenshot_2022-05-25_at_16.07.32.png
- CleanShot_2022-05-25_at_16.20.33.mp4
