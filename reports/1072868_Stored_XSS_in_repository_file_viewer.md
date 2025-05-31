# Stored XSS in repository file viewer

## Report Details
- **Report ID**: 1072868
- **URL**: https://hackerone.com/reports/1072868
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-06T16:53:51.657Z
- **Disclosed**: 2022-05-19T15:19:10.772Z

## Reporter
- **Username**: kannthu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
There exists XSS in swagger-ui version used in GitLab open API viewer. The XSS exists due to the old version of DOMpurify used in swagger-ui that allows an attacker can  **inject any HTML elements with any attributes** (except script tag) on the page. 

The XSS in POC requires 1 click anywhere on the page to execute, because of CSP that does not allow to execute events from HTML tags. (f.e. <img src=1 onerror=alert(1)). I will try to find CSP bypass that will allow me to execute the script with no user interaction.

My script uses the CSP bypass presented in https://gitlab.com/gitlab-org/gitlab/-/issues/213273
```
<a   
  data-remote="true"
  data-method="get"  
  data-type="script"
  href="/wbowling/wiki/raw/master/test.js" 
  class='atwho-view select2-drop-mask pika-select'>
</a>  
```

### Steps to reproduce

1. Go to https://gitlab.com/kannthu/asdasdas123/-/blob/master/openapi.yaml (tested on Chrome and Firefox)
2. Click anywhere on the page
3. You should see the alert box

There is another way of executing this XSS. **You can add "url=https://gitlab.com/kannthu/asdasdas123/-/raw/master/openapi.yaml" parameter to the URL of any open API file in any repository, and the XSS will still work**. 

1. Open https://gitlab.com/gitlab-org/build/omnibus-mirror/alertmanager/blob/master/api/v2/openapi.yaml?url=https://gitlab.com/kannthu/asdasdas123/-/raw/master/openapi.yaml
2. Click anywhere on the page
3. You should see the alert box

### Impact

The stored XSS is triggering for any user that opens the page and clicks anywhere on the page. The PoC can easily be extended to steal the user's CSRF token and to take over the victim's account.

### Examples

- https://gitlab.com/kannthu/asdasdas123/-/blob/master/openapi.yaml
- https://gitlab.com/gitlab-org/build/omnibus-mirror/alertmanager/blob/master/api/v2/openapi.yaml?url=https://gitlab.com/kannthu/asdasdas123/-/raw/master/openapi.yaml


### What is the current *bug* behavior?
Gitlab uses an old version of swagger-ui.

### What is the expected *correct* behavior?
Gitlab should use the newest version of swagger-ui.

### Relevant logs and/or screenshots
F1146909

### Output of checks
This bug happens on GitLab.com

#### Results of GitLab environment info
-

## Impact

The stored XSS is triggering for any user that opens the page and clicks anywhere on the page. An attacker can render anything on that page - malicious form to steal the user's login and password, or simply get the user's CSRF token and to take over the victim's account.

## Attachments
- Screenshot_2021-01-06_at_17.47.53.png
