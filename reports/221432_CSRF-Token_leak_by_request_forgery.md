# CSRF-Token leak by request forgery

## Report Details
- **Report ID**: 221432
- **URL**: https://hackerone.com/reports/221432
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-16T18:18:57.745Z
- **Disclosed**: 2017-10-09T12:14:52.030Z

## Reporter
- **Username**: naure
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi,

I found the following issue in my own Gitlab installation.
This is a request forgery that reveals the Rails `authenticity_token` remotely, which in turn allows mounting state-changing CSRF attacks.

# Vulnerability

The web app code relies on `location.pathname` in a number of places to create new relative URLs.

Here is one:
https://gitlab.com/gitlab-org/gitlab-ce/blob/f78ecda55d5431f9a74ab2892b516ecb45f24d80/app/assets/javascripts/environments/folder/environments_folder_view.js#L21

And below, it sends a request to such a URL:
https://gitlab.com/gitlab-org/gitlab-ce/blob/f78ecda55d5431f9a74ab2892b516ecb45f24d80/app/assets/javascripts/environments/folder/environments_folder_view.js#L86

Now, a forged link containing `//namespace/repo/` will make these URLs absolute because of the leading double slashes. I was able to create an `attack.com` namespace which translates to `https://attack.com/repo/`.
The app will then send a request including the anti-CSRF token to an attacker controlled domain. Which it definitely should not, ever (see point 2. below).

# Impact

A malicious web page and the coordinated server will be able to perform actions through the victim's browser in a second.

In addition, this opens up a new attack surface as the app will process untrusted replies as trusted content. There is high risk of injecting javascript somewhere, maybe here:
https://gitlab.com/gitlab-org/gitlab-ce/blob/f78ecda55d5431f9a74ab2892b516ecb45f24d80/app/assets/javascripts/environments/components/environment_terminal_button.js#L33

# Recommendations

Issues of this kind should be fixed globally, since the code is recent and developers are likely to introduce more `document.location` dependencies regularly.

1. Validate or normalize requested URLs against //, /../, and co. This can be done in Rails or in JS, or both.

2. Forbid cross-domain requests in all `Vue.http` and `$.ajax` helpers, like this one:
https://gitlab.com/gitlab-org/gitlab-ce/blob/f78ecda55d5431f9a74ab2892b516ecb45f24d80/app/assets/javascripts/vue_shared/vue_resource_interceptor.js#L21

Best regards,
Aurel

## Attachments
No attachments
