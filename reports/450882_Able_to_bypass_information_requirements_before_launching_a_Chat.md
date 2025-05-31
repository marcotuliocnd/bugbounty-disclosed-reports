# Able to bypass information requirements before launching a Chat.

## Report Details
- **Report ID**: 450882
- **URL**: https://hackerone.com/reports/450882
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-27T22:43:34.474Z
- **Disclosed**: 2018-12-20T19:48:19.241Z

## Reporter
- **Username**: notahackman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:**  Bypass of mandatory fields before a Chat session can begin.

**Description:**  URL allows for bypass straight into chat, and Chat personnel won't know my name, just that they are chatting with someone.

**Platform(s) Affected:** [website/mobile app - please include browsers and app versions used for repro.]
Chrome Web Browser

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Visit 
https://customerservice.starbucks.com/app/chat/chat_landing/euf/generated/optimized/1542660523/pages/chat/chat_landing.themes.starbucks.SITE.css
 2.  You have just bypassed the mandatory fields found on https://customerservice.starbucks.com/app/chat/chat_launch

3.  Voila you are effectively chatting with Starbucks employee without providing anything.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

Attached.

## How can the system be exploited with this bug?
  Bypass of required info that is mandatory.

## How did you come across this bug ?
Fiddling around.

## Recommendations for fix

 
* List any recommendations for bug fix

## Impact

Bypass and confuse agents, I can open an unlimited number of windows and start chatting with hundreds of agents if I want and affect your service if I was a malicious person.

## Attachments
No attachments
