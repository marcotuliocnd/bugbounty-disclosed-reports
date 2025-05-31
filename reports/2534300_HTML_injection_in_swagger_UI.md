# HTML injection in swagger UI

## Report Details
- **Report ID**: 2534300
- **URL**: https://hackerone.com/reports/2534300
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-03T14:51:32.159Z
- **Disclosed**: 2024-08-27T08:52:45.073Z

## Reporter
- **Username**: ehaftab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ionity_gmbh

## Vulnerability Information
Hi team,
I hope you're doing well.
An HTML Injection vulnerability was discovered in the Swagger UI, which could potentially allow attackers to inject malicious HTML content. This vulnerability could be exploited to execute arbitrary scripts in the context of the user's browser, leading to cross-site scripting (XSS) attacks and other malicious activities.
* Swagger UI is a tool for visualizing and interacting with API documentation. During a security assessment, it was found that the Swagger UI is vulnerable to HTML Injection, which could lead to XSS attacks. This vulnerability exists because the application fails to properly sanitize user-supplied input before rendering it in the HTML context.
Steps to Reproduce:
1. Nevigate to the ``https://35.156.81.191/swagger?``
2. Add this payload ``config=https://gist.githubusercontent.com/zenelite123/af28f9b61759b800cb65f93ae7227fb5/raw/04003a9372ac6a5077ad76aa3d20f2e76635765b/test.json``
3. After putting payload you will see the fake log in page created successfully.

{F3324497}

## Impact

An attacker exploiting this vulnerability could perform the following actions:
* Execute arbitrary JavaScript code in the context of the user's browser.
* Steal sensitive information such as session tokens, cookies, and other data accessible through JavaScript.
* Perform actions on behalf of the user, such as API requests with the user's privileges.
* Redirect the user to a malicious website.

Please feel free to contact me if you need any further information or assistance in addressing this issue.
Kind regards
@ehaftab

## Attachments
- Screenshot_2024-06-03_201818.png
- Screenshot_2024-06-03_201714.png
