# Passive mixed content issues on the site https://*.fanduel.com

## Report Details
- **Report ID**: 437800
- **URL**: https://hackerone.com/reports/437800
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-09T04:07:37.704Z
- **Disclosed**: 2018-12-21T13:03:17.552Z

## Reporter
- **Username**: mobius07
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fanduel

## Vulnerability Information
**Hello.**

**Summary:**

While browsing the sites https://www.fanduel.com and https://subscriptionapi.fanduel.com found a mixed content error on the site with HTTPS.
This error is located at https://www.fanduel.com/press and https://subscriptionapi.fanduel.com/press. Image are uploaded to the site via HTTP.
* Code: `<div class="post-image"><img src="http://medivetbiologics.com/wp-content/uploads/2015/04/Orlando-Sentinel-logo.png" alt=""></div>`

**Description:**

Passive mixed content is content sent over HTTP that is contained on the HTTPS page, but which can not change other parts of the page. For example, an attacker can replace a picture sent via HTTP with obscene content or a message to the user. The attacker can also view the activity of the user, observing which images are sent to the user. Knowing which pictures the user downloads, an attacker can figure out which pages the user is visiting.
Active mixed content has access to the entire DOM tree or part of it. This type can change the behavior of a page protected by HTTPS, and, theoretically, steal passwords from the user. Unlike passive content, the active is much more vulnerable.
In the case of active mixed content, the attacker can intercept the request by writing unwanted JavaScript code there, capable of stealing user personal data or installing dangerous software using vulnerabilities in plug-ins.
The risk associated with active content does not depend on the type of site and how valuable the user enters on it. The page can contain both publicly available information and data that is available only after authorization. Even if the page is public and does not contain any valuable data, with the help of active content, an attacker can redirect a user to other pages and steal cookies from there.

## Steps To Reproduce:

  1. Open any browser (Chrome, Opera etc).
  1. Follow this links https://www.fanduel.com/press and https://subscriptionapi.fanduel.com/press.
  1. View Developer Tools `Ctrl + Shift + I` (besides Internet Explorer - `F12`).
  1. Open the Console tab - there will be a warning that there are mixed content on the page.

## Supporting Material/References:

  * Screenshots - F372905, F372904, F372907, F372906.
  * https://resources.infosecinstitute.com/https-mixed-content-vulnerability/

Sincerely, Vyacheslav.

## Impact

If the HTTPS page includes content retrieved through regular, cleartext HTTP, then the connection is only partially encrypted. The unencrypted content is accessible to sniffers.

A man-in-the-middle attacker can intercept the request and also rewrite the response to include malicious or deceptive content. This content can be used to steal the user's credentials, acquire sensitive data about the user, or attempt to install malware on the user's system (by leveraging vulnerabilities in the browser or its plugins, for example), and therefore the connection is not safeguarded anymore.

## Attachments
- Mozilla_subscriptionapi.jpg
- Mozilla_www.jpg
- Chrome_subscriptionapi.jpg
- Chrome_www.jpg
