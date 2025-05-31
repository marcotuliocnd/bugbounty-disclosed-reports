# [Textile] XSS in project README files

## Report Details
- **Report ID**: 205498
- **URL**: https://hackerone.com/reports/205498
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-11T12:44:15.142Z
- **Disclosed**: 2017-02-15T05:29:05.061Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi,

Another parser bypass here – I discovered that Textile markup can be used to inject a stored JavaScript payload into a project `README.textile` file :)

## Steps to Reproduce

1. Create a new GitLab project
2. Initialise the project by creating a `README` file
3. Set the file title to `README.textile`
4. Paste the below Payload into the file
5. Commit the file to the project and click on the link

## Proof of Concept Payload

```
"Security test link":javascript:alert(document.domain)
```

Thanks!

## Attachments
No attachments
