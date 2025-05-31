# Possibility of Deface through translation tool - www.mozilla.com

## Report Details
- **Report ID**: 2053396
- **URL**: https://hackerone.com/reports/2053396
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-06T17:00:13.388Z
- **Disclosed**: 2023-10-27T08:48:29.732Z

## Reporter
- **Username**: astrounder
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
Hello team, how are you?

I hope you are well.

I am reporting the vulnerability as this is not a generic bug. And since the vulnerability has already been identified, I thought it important to let the Mozilla Team know.
As it says in the scope of the program, if a Mozilla site uses the third party application, the bug could be reported. So in this bug I preferred to report.

# Disclosure of Secrets for a Publicly Accessible Asset

## Overview of the Vulnerability

In the midst of a search, I found a credential of a third-party associated with Mozilla leaked on the internet. This credential gives access to [https://dashboard.smartling.com/](https://dashboard.smartling.com/).
Although the application is an external tool, this application is responsible for managing all translations of the Mozilla website and other *.Mozilla.com applications.
It manages jobs for translations, contains internal Mozilla documents, and has a tool to change any translation performed.
The account associated with this credential has access to some Mozilla projects.

```
API Tests
App Store Content
Blog Posts
Emails
Files
In-app messages (push notifications, etc.)
Mozilla.org Site
SL Test Project
SUMO Articles
Surveys
```

# PoC

* Jobs

{F2474698}

* Issues

███████

███████

█████

████

* Translating jobs

███████

* Editing

███████

* Files

██████████

█████

█████████

These leaks can be found on sites like [https://cyberintelligence.house](https://cyberintelligence.house), [https://dehashed.com/](https://dehashed.com/), and [https://intelx.io/](https://intelx.io/).
All the valid data I found are those inserted in the report.

**Steps to Reproduce:**
1. Use the following credentials to login to the application:

```
email: ████████
password: ████
```


**Note:**
I did not make any changes to the accessed application, and I did not copy any information. All accesses shown are for demonstrating proof of concept and impact only.

It is strongly advised that all the disclosed passwords be changed immediately, and an investigation be undertaken to determine how this leak occurred to prevent future occurrences.

If you need my IP, it is: ██████

Best regards,
Astrounder

## Impact

A malicious agent with access to this application can change translations of www.mozilla.com, create translation jobs, gain access to internal Mozilla documents, and other related access.

## Attachments
- image.png
