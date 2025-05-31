# Github base action takeover which is used in `github.com/Shopify/unity-buy-sdk`

## Report Details
- **Report ID**: 1439355
- **URL**: https://hackerone.com/reports/1439355
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-01-02T11:23:22.159Z
- **Disclosed**: 2022-07-12T04:17:50.003Z

## Reporter
- **Username**: codermak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Shopify have a github repository https://github.com/Shopify/unity-buy-sdk
In the repository there is a github action, which is used a base action from an external github repository.
That github account as not registered on github.com
So I was able to takeover the account and host PoC.

## Shops Used to Test:
NA

## Relevant Request IDs:
NA

## Steps To Reproduce:

  1. Go to https://github.com/Shopify/unity-buy-sdk/blob/master/.github/workflows/build.yml#L71
  2. You will see this github repository `MirrorNG/unity-runner` getting used as base action at line 71
  3. Try accessing the github repository https://github.com/MirrorNG/unity-runner you will be redirected to https://github.com/MirageNet/unity-runner
  4. This happens when github organization name or username is renamed, github redirects all the old urls to new github account
  5. But with this, the old github username becomes available for anyone to register and when someones registers it the redirection will stop and all links will open newly created repositories.
  6. Try accessing the github organization https://github.com/MirrorNG you will see takeover message

**Note:** I haven't taken over the repository, so as to avoid breaking the existing action as its getting used.

## Supporting Material:

- https://github.com/Shopify/unity-buy-sdk/blob/master/.github/workflows/build.yml#L71
- https://github.com/MirrorNG

{F1565368}

## Reference

https://hackerone.com/reports/1087489

## Impact

An attacker can takeover the github account and host malicious action on it, when any any pull request is sent on the repository, it will end up running the action and you can see below screenshot, unity credentials are getting passed to that action. Action will get access to shopify's credentials.

{F1565369}

Also, since github actions can create github tokens for use at run time using `${{ secrets.GITHUB_TOKEN }}` an attacker can get access to all the private repositories of the organization

## Attachments
- Screenshot_from_2022-01-02_16-40-54.png
- Screenshot_from_2022-01-02_16-46-48.png
