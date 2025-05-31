# Gitlab is vulnerable to impersonation attacks due to broken links

## Report Details
- **Report ID**: 265696
- **URL**: https://hackerone.com/reports/265696
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-03T23:00:49.687Z
- **Disclosed**: 2017-09-06T16:43:13.597Z

## Reporter
- **Username**: b3nac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Good afternoon team,

#Vulnerability

There's a lot of possible attacks that can be carried out with broken external links as noted in this github post by edoverflow. https://gist.github.com/EdOverflow/24e0bb929169eb948bb7f3d0a2d5528f.

In this particular example I'm impersonating Ricardo who redesigned gitlabhq back in 2011.

#POC

Go to https://about.gitlab.com/2011/11/22/whats-next/ and Ricardo is hyperlinked to his github account. Well somewhere between 2011 and 2017 he decided to delete his profile. 

Before - F218161

After - F218162

Ricardo is back with a malicious url that has been shortened using bit.ly. Shortening the link hides that it's malicious. 

In conclusion I have taken over an embedded link inside the Gitlab.com domain. Please let me know if you have any questions. I am happy to help and will continue to look for broken links!

## Attachments
- DeletedGithubPageGitLab.PNG
- After.PNG
