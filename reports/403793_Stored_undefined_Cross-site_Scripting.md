# Stored 'undefined' Cross-site Scripting

## Report Details
- **Report ID**: 403793
- **URL**: https://hackerone.com/reports/403793
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-01T10:14:55.867Z
- **Disclosed**: 2018-09-05T16:26:12.709Z

## Reporter
- **Username**: rootbakar___
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hello KhanAcademy Security Team,

I'm **rootbakar**, I found an XSS bug on 'BIO' in the profile, I used payload XSS **"/><svg/on<script>load=prompt(document.domain);>"/><svg/on<script>load= prompt (document.cookie);>** after I save it appears there is no trigger from the XSS, but when I try to change one of the values in the profile form and when I save it again an XSS trigger appears but with the words '**undefined**'. Every time I want to change both '**REAL NAME**' and '**LOCATION**' and when I press the save button again and after a few seconds an XSS trigger appears with the words '**undefined**'

**PoC**
This is Video Link
https://youtu.be/WGeaclSo_5A
(Not Public Video)

Best Regards,

**RootBakar**

## Impact

**Displayed 'undefined' XSS after user repeated click SAVE button**

## Attachments
- 2.png
- 1.png
- 3.png
