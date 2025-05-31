# Open redirect open.rocket.chat/file-upload/ID/filename.svg

## Report Details
- **Report ID**: 368927
- **URL**: https://hackerone.com/reports/368927
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-19T17:04:38.639Z
- **Disclosed**: 2019-10-31T15:20:30.348Z

## Reporter
- **Username**: w2w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** Open redirect through svg file upload

**Description:** When you upload a file to a chat, the link to it will look like https://open.rocket.chat/file-upload/ID/filename.svg, but the file will be on storage.googleapis.com.
We can embed js in our svg and when the victim goes to https://open.rocket.chat/file-upload/6ksXL2Mk4MonCcTpx/svgxss.svg, a redirect to the phishing site will occur, or any other js, for example, downloading the virus, will work.
I see you have forbidden downloading html, shtml and php file, I recommend you also prohibit svg, since it is also dangerous.

  1. Upload svg file in any chat (attached to the report)
  2. Go to open.rocket.chat/file-upload/ID/filename.svg.

**PoC:** https://open.rocket.chat/file-upload/6ksXL2Mk4MonCcTpx/svgxss.svg

## Impact

open redirect

## Attachments
- svgxss.svg
