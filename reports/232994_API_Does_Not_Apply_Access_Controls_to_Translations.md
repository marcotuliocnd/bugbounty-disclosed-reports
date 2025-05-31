# API Does Not Apply Access Controls to Translations

## Report Details
- **Report ID**: 232994
- **URL**: https://hackerone.com/reports/232994
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-29T23:17:30.883Z
- **Disclosed**: 2017-06-02T11:23:24.335Z

## Reporter
- **Username**: 4cad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Summary
=======

The /api/ does not enforce access control on the translation files, allowing anyone to download full translation files. See the screenshot for an example project being viewed by an anonymous account that is configured to have no permissions.

Description
=======
On my local setup running Weblate 2.15-dev, I removed all permissions from the Guest group and restarted the server. When I tried to navigate to the test project through the UI the usual way at URL http://192.168.1.129:8000/projects/testproject/, I received an Access Denied message.

However I was able to find the project details through the API at http://192.168.1.129:8000/api/components/testproject/testcomponent/translations/ and even download the translations file by clicking on the "file_url" link, which in my case is "http://192.168.1.129:8000/api/translations/testproject/testcomponent/en_CA/file/".

Assessment
=======
I am marking this as Medium because from what I have seen the access controls are not that important to Weblate's mission and it does not seem designed to keep translations secret, although the existence of access controls through the web app suggests that this is something that people wanted enough to implement. If enforcing the read access controls is of any importance, then I would treat this with higher severity.

## Attachments
- Weblate_API_Access_Control.png
