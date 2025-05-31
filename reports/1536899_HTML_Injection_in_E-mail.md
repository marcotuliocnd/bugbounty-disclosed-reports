# HTML Injection in E-mail

## Report Details
- **Report ID**: 1536899
- **URL**: https://hackerone.com/reports/1536899
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-04-10T21:52:52.964Z
- **Disclosed**: 2022-06-14T10:21:46.411Z

## Reporter
- **Username**: mega7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello Gents,
+ While testing "account.acronis.com", I found that "first name" could be injected with HTML tags while sending an email invitation. But this attack requires user interaction to confirm the email first, then he/she will receive a welcome email "Welcome to your Acronis Cyber Protect trial!" Contains the injected payload!

### Steps to Reproduce:
1. Please register at https://www.acronis.com/en-us/products/cyber-protect/trial/#registration with the victim's email.
2. Inject "First Name" field with HTML tags, for example: `"/><img src="x"><a href="https://evil.com">login</a>`.
3. Check the email inbox, HTML tags will be executed. "Your Acronis Cyber Protect trial starts today!"

### Proof of Concept:
+ {F1687466}

## Impact

HTML Injection

## Attachments
- simplescreenrecorder-2022-04-10_23.48.42.mp4
