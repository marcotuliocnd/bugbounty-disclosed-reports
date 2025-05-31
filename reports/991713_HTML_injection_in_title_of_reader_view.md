# HTML injection in title of reader view

## Report Details
- **Report ID**: 991713
- **URL**: https://hackerone.com/reports/991713
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-25T23:46:39.185Z
- **Disclosed**: 2023-06-22T05:52:53.227Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Reader.html in Brave doesn't escape/trim HTML tags in %READER-TITLE%.
https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/Reader.html#L17
This allows any page to inject malicious HTML code in reader-mode page through `<title>{html code you want to inject}</title>`.

## Products affected: 

Brave iOS Version 1.20 (20.09.11.20), also current Nightly

## Steps To Reproduce:

* Open the following Google docs: https://docs.google.com/document/d/10kPw7PNOujlenF08i3jBgD4zqoG5148u8TRkoHj7io8/edit?usp=sharing
* Push reader-mode button shown in address bar.
* Malicious login form is rendered instead of the document
* Fill the form, then the user/password you filled are stolen to malicious website

## Supporting Material/References:

  * See attached movie file for the demonstration

## Impact

Malicious web contents can inject HTML code and manipulate readerized page (hosted in localhost:65XX).

Also, if injected HTML code contains a string `%READER-CONTENT%`, it is replaced to the original page contents.
https://github.com/brave/brave-ios/blob/87af4cbf0474bafd13673690aeee0c11059fbba2/Client/Frontend/Reader/ReaderModeUtils.swift#L29

So, attacker can steal user's sensitive information contained in the original HTML page through `<form><textarea>%READER-CONTENT%</textarea>`.
When you open the following Google search link in reader-mode, you can reproduce the above scenario as well.
https://www.google.com/search?q=%3Cform%3E%3Ctextarea%20name%3D%22dom%22%3E%25READER-CONTENT%25%3C%2Ftextarea%3E%3Cinput%20type%3D%22submit%22%3E%3C%2Fform%3E

## Attachments
- reader_injection.mov
