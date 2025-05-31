# HTML in Diffusion not escaped in certain circumstances

## Report Details
- **Report ID**: 148865
- **URL**: https://hackerone.com/reports/148865
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-02T14:39:29.049Z
- **Disclosed**: 2016-08-01T14:45:33.265Z

## Reporter
- **Username**: danny_b
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
HTML in Diffusion source code listing is not escaped

Steps to reproduce:
* have the syntax hilight turned on
* the file is bigger than 256kB, thus syntax hilight is claimed in header to be turned off automatically, however, plaintext file doesn't display like with regular (manual) syntax highlight off, but the content is being parsed

File should contain HTML constructions, but could be of any type (extension).
Having javascript constructions there with alert() within the HTML causes such dialogues to pop up on given page obviously.

## Attachments
No attachments
