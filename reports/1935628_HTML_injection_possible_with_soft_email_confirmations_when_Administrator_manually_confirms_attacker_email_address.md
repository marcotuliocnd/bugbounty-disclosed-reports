# HTML injection possible with soft email confirmations when Administrator manually confirms attacker email address

## Report Details
- **Report ID**: 1935628
- **URL**: https://hackerone.com/reports/1935628
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-04-06T00:41:55.629Z
- **Disclosed**: 2024-10-08T13:58:39.034Z

## Reporter
- **Username**: cryptopone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Note: This report is similar to #1842867 but has the administrator manually confirming an unconfirmed email on the attacker's behalf, instead of impersonating the attacker's account.

Assuming a GitLab instance is configured to use soft email confirmation settings, an attacker can register an account and login, then change their email to include an HTML payload. If an administrator manually verifies the attacker's email address, the administrator might be subjected to executing *some* HTML code in the modal confirmation dialog. It appears tags such as `<form>` and `<script>` are filtered out before being displayed.

The `confirm_user_data` method in https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/helpers/users_helper.rb helps demonstrate the conditions required for this to work:

```ruby
  def confirm_user_data(user)
    message = if user.unconfirmed_email.present?
                _('This user has an unconfirmed email address (%{email}). You may force a confirmation.') % { email: user.unconfirmed_email }
              else
                _('This user has an unconfirmed email address. You may force a confirmation.')
              end

    modal_attributes = Gitlab::Json.dump({
      title: s_('AdminUsers|Confirm user %{username}?') % { username: sanitize_name(user.name) },
      messageHtml: message,
      actionPrimary: {
        text: s_('AdminUsers|Confirm user'),
        attributes: [{ variant: 'confirm', 'data-qa-selector': 'confirm_user_confirm_button' }]
      },
      actionSecondary: {
        text: _('Cancel'),
        attributes: [{ variant: 'default' }]
      }
    })

<rest of function trimmed>
```

We need to pass the `if user.unconfirmed_email.present?` check to have the email presented in the dialog. This only seems to occur if the attacker registers an account with soft email confirmations and then changes their e-mail afterward. If the instance has email confirmation changed to `Hard` after the attacker is setup, this exploit still triggers for this attacker but new registrations appear to follow the else condition (ie. the email is not displayed inside of the dialog).

### Steps to reproduce

#### Prerequisites (Administrator Account):
1. Go to the Admin general settings page (http://gitlab.example.com/admin/application_settings/general).
1. Expand sign-up restrictions and set "Email confirmation settings" to "Soft".
1. Save the changes.

#### Reproduction Steps (Attacker):
1. Register an account on the instance. (ex. Username: `AttackerSoftEmail`, Email: `attackersoftemail@example.com`)
1. Log into the account. You should now see a message at the top of the screen stating "Please check your email (attackersoftemail@example.com) to verify that you own this address and unlock the power of CI/CD. Didn't receive it? Resend it. Wrong email address? Update it."
1. Go to the user's profile (http://gitlab.example.com/-/profile).
1. Change the e-mail address by appending `<h2>testing<img/src=http://localhost:8000/test.png>` to the end of the address.
1. Save the changes.
1. (Optional) Start a python3 webserver to catch the image web request by running `python3 -m http.server` within an empty directory.

#### Reproduction Steps (Victim Administrator):
1. Log into GitLab as an Administrator/root.
1. Navigate to the Admin users panel and select the AttackerSoftEmail user (http://gitlab.example.com/admin/users/AttackerSoftEmail).
1. Note the email address for AttackerSoftEmail does not contain HTML.
1. Open the browser dev tools using `F12` and navigate to the Network tab.
1. Click the "Confirm user" button to to confirm the e-mail address.
1. Note the dialog text is modified due to the `<h2>` header and a broken image appears in the dialog.
1. Confirm using the network tab that the browser requested `http://localhost:8000/test.png` and returned a 404 if a python server was running. 

### Impact

Administrators on self-managed instances confirming the attacker's account/email will inadvertently run *some* HTML if the attacker has not validated their email and the instance is configured to use soft email confirmation during registration.

The Administrator is not made aware of the HTML payload contained in the attacker's email address when viewing the attacker's profile from the administrator user page.

My initial report uses the following reasoning for the CVSS score:

`AC:H`: An administrator manually confirming a users email address is not likely considered to be normal workflow. 
`PR:L`: Attacker requires an account but does not necessarily require special roles to perform this attack.
`UI:R`: Administrator needs to confirm the attacker's email address to trigger the payload.
`S:U`: Impact is localized to the exploitable component.
`C:L`: Attacker could leak the victim's IP address using `<img>` or try to convince get the admin to click a link.
`I:L`: Some information on the page can be altered.
`A:N`: No Availability impact.

### Examples

N/A

### What is the current *bug* behavior?

Attacker's HTML payload is rendered within context of the self-hosted GitLab instance.

### What is the expected *correct* behavior?

HTML code appended to the email address should not be rendered by the browser when an administrator clicks the `Confirm user` dialog.

### Relevant logs and/or screenshots

Attacker updates email address containing HTML payload.
{F2276105}

Administrator views the attacker's account in the admin user menu. Note the page does not display the HTML included in the attacker email.
{F2276106}

Administrator clicks `Confirm user` button and the HTML is rendered.
{F2276107}

Attacker controlled server obtains victim IP address.
{F2276108}

### Output of checks

#### Results of GitLab environment info

```
root@gitlab:/# gitlab-rake gitlab:env:info

System information
System:		
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	3.0.5p211
Gem Version:	3.2.33
Bundler Version:2.3.15
Rake Version:	13.0.6
Redis Version:	6.2.11
Sidekiq Version:6.5.7
Go Version:	unknown

GitLab information
Version:	15.10.2-ee
Revision:	a54d6973eae
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	13.8
URL:		http://gitlab.example.com
HTTP Clone URL:	http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	14.18.0
Repository storages:
- default: 	unix:/var/opt/gitlab/gitaly/gitaly.socket
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
root@gitlab:/#
```

## Impact

Administrators on self-managed instances confirming the attacker's account/email will inadvertently run *some* HTML if the attacker has not validated their email and the instance is configured to use soft email confirmation during registration.

The Administrator is not made aware of the HTML payload contained in the attacker's email address when viewing the attacker's profile from the administrator user page.

My initial report uses the following reasoning for the CVSS score:

`AC:H`: An administrator manually confirming a users email address is not likely considered to be normal workflow. 
`PR:L`: Attacker requires an account but does not necessarily require special roles to perform this attack.
`UI:R`: Administrator needs to confirm the attacker's email address to trigger the payload.
`S:U`: Impact is localized to the exploitable component.
`C:L`: Attacker could leak the victim's IP address using `<img>` or try to convince get the admin to click a link.
`I:L`: Some information on the page can be altered.
`A:N`: No Availability impact.

## Attachments
- AttackerWithHTMLTagsInEmail.png
- AdministratorViewingUserProfileWithoutSeeingEmailTags.png
- AdministratorConfirmingUserDialog.png
- AttackerControlledServerCapturesIP.png
