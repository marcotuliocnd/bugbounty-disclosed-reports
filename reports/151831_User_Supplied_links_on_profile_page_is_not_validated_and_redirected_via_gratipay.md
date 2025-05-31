# User Supplied links on profile page is not validated and redirected via gratipay.

## Report Details
- **Report ID**: 151831
- **URL**: https://hackerone.com/reports/151831
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-07-16T22:35:05.883Z
- **Disclosed**: 2016-07-24T09:01:14.578Z

## Reporter
- **Username**: roshanpty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
User Supplied links on profile page is not validated and redirected via gratipay.
====================

Description
---------------------
The user profiles on gratipay has a profile statement section which is supported by markdown. An adversary can update the profile section with a hyper link URL to a malicious website. As gratipay doesn't redirect the request via a 302 redirect response if the adversary register a similar phishing website the user won't be aware that he/she is going out of the trusted site (gratipay)

Detailed Steps
---------------------
**Step 1:** Update the profile statement with a URL hyperlink.
**Step 2:** Click on the hyperlinked URL on the updated profile. It can be observed that the server issues no warning that the user is being redirected out of gratipay.

Solution
---------------------
* All user supplied URL's in the website must be redirected via the server only. 
* On implementing URL redirection, care should be taken that it is not vulnerable to Open Redirection [OWASP Open Redirection](https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet)
* A warning should be issued when a user is clicking on a website outside the host website. For example in the below line I am hyperlinking SecVibe website to the text of URL of hackerone.com. It can be observed that on clicking the same, hackerone verifies if the same is in fact a site outside hackerone and issues a warning.
[http://hackerone.com](https://secvibe.com)
{F105371}


## Attachments
- 2016-07-16_15_32_55-Leaving_HackerOne..._-_HackerOne.png
