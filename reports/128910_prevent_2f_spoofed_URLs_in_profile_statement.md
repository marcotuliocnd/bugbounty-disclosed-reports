# prevent %2f spoofed URLs in profile statement

## Report Details
- **Report ID**: 128910
- **URL**: https://hackerone.com/reports/128910
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-07T08:13:13.625Z
- **Disclosed**: 2017-08-21T13:30:11.505Z

## Reporter
- **Username**: 007divyachawla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
https://gratipay.com%2f@google.com on clicking on this url this link will take to the google.com or any other malicious url. On seeing it will look like the link will take to the gratipay but onclicking the url it will redirect to the malicious site.Attacker with the help social engg. techniques will able to redirect the user to any Ransomware site for they nefarious purpose

POC:- Click on the link it will redirect to google.com

Fix:- The hostname must end in %2f, which gets URL-decoded to /.
This ensures that the browser only sends the request to the intended host.

## Attachments
No attachments
