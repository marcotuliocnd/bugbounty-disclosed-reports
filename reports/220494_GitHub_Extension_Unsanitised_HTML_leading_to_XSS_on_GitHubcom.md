# [GitHub Extension] Unsanitised HTML leading to XSS on GitHub.com

## Report Details
- **Report ID**: 220494
- **URL**: https://hackerone.com/reports/220494
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-04-12T14:39:37.554Z
- **Disclosed**: 2017-04-24T08:41:06.487Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Hi,

I noticed that certain HTML is unsanitised by the Awesome Autocomplete for GitHub extension, leading to a case of XSS on the GitHub website.

Please note that I **do not have ownership nor affiliation** with the repository and user names in this report, nor the final JavaScript alert dialog. 

# Proof of Concept
I have tested the following Proof of Concept demonstrations with the following conditions:

### Extension
* Latest version of the Awesome Autocomplete extension

### Operating Systems
* macOS Sierra 10.12.4
* Windows 7 x64

### Browsers
* Google Chrome 57.0.2987.133 (latest)
* Safari 10.1 (latest)

## Unsanitised HTML
Please follow the below steps to demonstrate the presence of an unsanitised HTML issue.

1. Search for `'"><img src=x onerror=` on GitHub.com
2. Note the broken `<img>` element and requests to "x" on GitHub.com

The following images demonstrate that a broken `<img>` element was created in the context of GitHub.com by the Algolia extension:

{F175284}

{F175283}

## XSS on GitHub
Please follow the below steps to demonstrate the presence of a full XSS issue.

1. Search for `a'"><h1` on GitHub.com
2. Because of a specific repository name being loaded, a JavaScript alert dialog will appear:

{F175285}

As noted above, I am currently attempting to reproduce this vulnerability using my own repositories and JavaScript code (e.g. `document.domain` rather than "1337").

Please let me know if you require any additional information regarding these vulnerabilities.

Thanks!

## Attachments
- Unsanitised_2.png
- Unsanitised_1.png
- XSS_1.png
