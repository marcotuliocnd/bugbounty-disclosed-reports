# Private RSA key for Vagrant exposed in GitHub repository

## Report Details
- **Report ID**: 1183502
- **URL**: https://hackerone.com/reports/1183502
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-04T06:57:39.885Z
- **Disclosed**: 2021-05-07T18:10:47.103Z

## Reporter
- **Username**: sdushantha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
The private RSA key used for SSH on Vagrant is exposed in sifnode GitHub repository.

## Steps To Reproduce:
1. Visit [this link](https://github.com/Sifchain/sifnode/blob/4fb7523322f74e70600a10fff4dbdd42425c077f/ui/.vagrant/machines/default/virtualbox/private_key) which shows the `private_key` file used for your Vagrant virtual machine

## Suggested solution
Remove the private key from the repository. Even though you remove it, it will still be in the commit history. Therefore, refer to the article by GitHub on [removing sensitive data from a repository](https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository)

## Impact

By having the private SSH key published onto your GitHub repo, an attacker would be able to access your Vagrant virtual machine pretending to be you. The private key has the word "private"  for reason and therefore it shouldn't be accessible by unauthorized people.

## Attachments
No attachments
