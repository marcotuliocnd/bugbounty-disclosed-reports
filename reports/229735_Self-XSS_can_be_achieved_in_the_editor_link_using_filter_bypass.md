# Self-XSS can be achieved in the editor link using filter bypass

## Report Details
- **Report ID**: 229735
- **URL**: https://hackerone.com/reports/229735
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-18T21:48:06.989Z
- **Disclosed**: 2017-06-02T10:04:08.827Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
##Description
I saw the fixed issue in the https://hackerone.com/reports/223692 and i think i found another filter bypass. I noticed that we actually can use special keywords like %(branch)s, %(file)s and %(line)s.
So XSS can be achieved in this way:
`%(branch)s:alert(1);//https://`
if the branch will be named `javascript`, the payload will be executed upon pressing the source code link of the file inside it.

##Steps to reproduce
1. Create some branch and name it javascript
2. Put some source files.
3. Click the link on source file. The `%(branch)s` will be replaced by branch name (`javascript`) and popup will be fired.

##Suggested fix
I recommend you to additionally sanitize string by disallowing special symbolst before first `:` occurence (if exist)

## Attachments
- zx.JPG
