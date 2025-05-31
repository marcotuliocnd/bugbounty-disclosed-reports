# The `stripe/veneur` GitHub repository links to a domain `veneur.org`, which is not under stripe's control

## Report Details
- **Report ID**: 2011298
- **URL**: https://hackerone.com/reports/2011298
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-06-02T17:08:21.859Z
- **Disclosed**: 2023-07-03T10:24:59.459Z

## Reporter
- **Username**: peterldowns
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripe

## Vulnerability Information
Initially reported at https://github.com/stripe/veneur/issues/1058. Since that report, the repository's sidebar has been updated to no longer link to the uncontrolled domain. Many of the 179 forks of this repository still contain the link to the uncontrolled domain.

## Summary:
- The github.com/stripe/veneur repository contains security-sensitive code which is designed to run within a company's private network, often as a sidecar on each of their application servers.
- The repository's README and documentation does not contain instructions for installing veneur. Instead, it linked to an external domain, `https://veneur.org`, which contained those instructions.
- The `https://veneur.org` domain appears to be no longer under Stripe's control.
- If the website is not under Stripe's control, it is an easily exploitable vector for a phishing or supply chain contamination attack. The targets of this attack would be user's of the open source release of veneur (not specifically Stripe), and Stripe customers.
- Example attack:
  - step one: control `https://veneur.org`, either because you are the current owner or you purchase the domain.
  - step two: recreate the old site, but edit the installation instructions to reference malicious source code or a docker image built with malicious code.
  - step three: a veneur user follows the instructions
  - outcome: attacker-controlled code/image running inside a privileged environment.
- Example attack two:
  - step one: control `https://veneur.org`, either because you are the current owner or you purchase the domain.
  - step two: replace the contents of the website with a fake Stripe login screen.
  - step three: a veneur user, who is likely to also be a Stripe user, enters their username and password into the fake login screen.
  - outcome: attacker gains access to privileged credentials. Because the `https://veneur.org` website is linked to by an official, Stripe-controlled repository, there is a much greater likelihood that the attack will succeedd than if it had to operate on a different domain.

## Steps To Reproduce:
1. Visit https://github.com/stripe/veneur
2. Click on the `https://veneur.org` link in the sidebar.

Since I initially reported this issue in the Github repository, at https://github.com/stripe/veneur/issues/1058 , the sidebar has been edited to no longer link to `https://veneur.org`. Many of the 179 forks of this repository still contain the link to the uncontrolled domain.

## Supporting Material/References:

Initial report with images:
- https://github.com/stripe/veneur/issues/1058

The link in the sidebar:
- https://user-images.githubusercontent.com/824173/242777008-1e2b02af-be8c-484c-b131-842d570bdb89.png

The contents of the website currently:
- https://user-images.githubusercontent.com/824173/242777079-12830e1c-7928-460c-81b0-26523062f510.png

## Impact

An attacker can easily impersonate Stripe, taking advantage of the fact that this website is linked to by an official Stripe-owned web page. They can use this as the beginning of a phishing or a supply-chain contamination attack targeting Stripe's customers.

## Attachments
No attachments
