# Tracking of users on third-party websites using the Twitter cookie, due to a flaw in authenticating image requests

## Report Details
- **Report ID**: 329957
- **URL**: https://hackerone.com/reports/329957
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-26T11:18:08.158Z
- **Disclosed**: 2019-02-08T23:01:40.893Z

## Reporter
- **Username**: cris-staicu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 
As part of our ([SoftwareLab@TU Darmstadt](https://www.sola.tu-darmstadt.de/de/software-lab/)) latest research project, we discovered a privacy-related vulnerability in multiple high-profile websites, including Twitter. An attacker exploiting this vulnerability can identify a user of your website while the user visits an attacker-controlled website, using the cookie you set in his or her browser. We call this vulnerability LeakyImages and below we describe the threat model, the exploit vector and the actual steps that need to be followed on your website to setup a LeakyImage between the attacker and the victim.

**Description:** 
*Threat model*: The attacker knows the victim’s ID/username on your website and she aims at identifying the user when visiting one of the websites she controls, such as a blog or a news website. Another flavor of this goal: the attacker wants to identify a user out of a group of potential target users. Moreover, she would like to link together user accounts created by the victim on different vulnerable websites. For example she would like to know that the visitor of the website has the email address john.doe@gmail.com and the facebook account facebook.com/johndoe1973. 

*Exploit*: The main insight of our exploit is that the attacker can use your platform to share an image “http://yoursite.com/myCuteCatImage.png” with the victim, so that the image is only accessible by the attacker and the victim. It is important that there is a cookie-based access control mechanism that enforces this former constraint. Since images are exempted from the same origin policy, when the victim visits an attacker-controlled website, the attacker instructs the victim’s browser to request this image. By checking whether the image gets loaded, the attacker can precisely identify whether the victim is the current visitor. In a sense, the attacker is able to setup a tracking pixel using your website and the reachability of this pixel leaks the identity of the user.

## Steps To Reproduce:

  1. The attacker writes a private message to the victim which contains the image.
  2. Right click on the image + copy image address
  3. This URL is a cookie-based authenticated URL which only allow access to the image for the two participants in the conversation. For example the URL https://ton.twitter.com/1.1/ton/data/dm/971042231900622855/971042220110426113/dsxFPPP0.jpg:large can only be accessed by the users CrisStaicu and johndoevici1988.

## Impact: 
The attacker can include the LeakyImage in a page he controls. If the image is correctly loaded, the Twitter identity of the current visitor is leaked. 

## Closing Remarks:
We believe that the described attack is a serious threat to the privacy of your users. We are looking forward to hearing from you and we would like to share further details if needed to aid in fixing the reported problem. We plan to publish a description of the vulnerability at an academic security conference and notify you as part of a responsible disclosure process. We will be happy to coordinate any public release of this information with you, and in turn, would be happy to receive feedback on whether and when you plan to address the problem.

## Impact

An attacker exploiting this vulnerability can identify a user of your website while the user visits an attacker-controlled website, using the cookie you set in his or her browser.

## Attachments
No attachments
