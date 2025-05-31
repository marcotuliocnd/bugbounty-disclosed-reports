# Code exec on Github runner via Pull request name

## Report Details
- **Report ID**: 2471956
- **URL**: https://hackerone.com/reports/2471956
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-04-19T16:38:36.797Z
- **Disclosed**: 2024-04-28T18:08:27.840Z

## Reporter
- **Username**: another_dude
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
Hi,
I have discovered command injection vulnerability in one of your Github repos.
Apologies for any inconvenience if this type of bug is not of interest to you. Allow me to explain the problem.
GitHub Actions, a powerful tool for automating workflows, can inadvertently introduce security vulnerabilities if not configured securely. Insecure GitHub Actions configuration can lead to various risks, including unauthorized access, data breaches, and code injection attacks.
Currently  https://github.com/hyperledger/cacti/tree/HEAD/.github/workflows/test_weaver-pre-release.yaml#L28 allows attacker to inject arbitrary command and run it on the Github runner. Note the usage of double quotes and untrusted `pull_request.name`.

## Steps to reproduce
- Create a new branch within your fork
- Create a pull request with the `U";cat $GITHUB_WORKSPACE/.git/config | xxd -p | base64; echo "D` title
- config file contains the access token in base64 form
- Wait until `check_release` workflow will be triggered
- Check job logs for encoded `$GITHUB_TOKEN` (by default Github will replace it with *** if you will try just echo it, that is why I used xxd + base64)
- I refrained from creating a PR on your repository to prevent the disclosure of sensitive information to the public and to avoid publicly exposing the vulnerability.
Example run could be found in my fork, attached as screenshot.

## Impact

Such scenario leaves possibility to access `$GITHUB_TOKEN` environment variable, potentially compromising the whole GitHub organization.
Good explanation of the problem could be found at github docs: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions

There are few limits to the attack:
- `$GITHUB_TOKEN` is a short lived token and for the real life attack, whole attack should be scripted until job is still running

## Attachments
- Screenshot_2024-04-19_at_18.27.28.png
