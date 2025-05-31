# [RDoc] XSS in project README files

## Report Details
- **Report ID**: 200693
- **URL**: https://hackerone.com/reports/200693
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-24T07:48:07.729Z
- **Disclosed**: 2017-02-15T05:28:38.786Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi,

While experimenting with parser bypass techniques, I discovered that RDoc markup could be used to inject a stored JavaScript payload into a project `README.rdoc` file.

Please note that this issue is separate to my earlier report #200565 (XSS with AsciiDoc markup), marked as duplicate.

## Steps to Reproduce

1. Create a new GitLab project
2. Initialise the project by creating a `README` file
3. Set the file title to `README.rdoc`
4. Paste the below Payload into the file
5. Commit the file to the project and click on the "XSS" link

## Proof of Concept Payload
`XSS[JaVaScriPt:alert(1)] <-- click to test`

Thanks!

## Attachments
No attachments
