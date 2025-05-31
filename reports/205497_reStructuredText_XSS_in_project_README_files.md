# [reStructuredText] XSS in project README files

## Report Details
- **Report ID**: 205497
- **URL**: https://hackerone.com/reports/205497
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-11T12:42:35.162Z
- **Disclosed**: 2017-02-15T05:29:36.447Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi,

While experimenting with parser bypass techniques, I discovered that reStructuredText markup can be used to inject a stored JavaScript payload into a project `README.rst` file.

## Steps to Reproduce

1. Create a new GitLab project
2. Initialise the project by creating a `README` file
3. Set the file title to `README.rst`
4. Paste the below Payload into the file
5. Commit the file to the project and click on the link

## Proof of Concept Payload

```
`Security test link`__.

__ javascript:alert(document.domain)
```

Thanks!

## Attachments
No attachments
