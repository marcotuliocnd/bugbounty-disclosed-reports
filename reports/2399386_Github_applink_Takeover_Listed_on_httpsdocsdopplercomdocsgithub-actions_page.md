# Github app(link) Takeover Listed on "https://docs.doppler.com/docs/github-actions" page

## Report Details
- **Report ID**: 2399386
- **URL**: https://hackerone.com/reports/2399386
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-03-02T17:17:29.890Z
- **Disclosed**: 2024-03-15T15:54:34.506Z

## Reporter
- **Username**: w3shi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: doppler

## Vulnerability Information
## Summary:
GitHub Apps are a type of integration that allows developers to extend the functionality of GitHub and automate workflows within the GitHub platform. 
developers can install the github app on need.

A Github app presented on `https://docs.doppler.com/docs/github-actions` was vulnerable to takeover. With this the attacker can achieve his needs and whoever goes to the link and install the app can be vulnerable.


## Steps To Reproduce:

  1. go to `https://docs.doppler.com/docs/github-actions`
  2. scroll unit you see this link:
  
{F3093438}
  
3.you could observe the following:
{F3093440}

# Mitigation:
Removing or replacing the github app link

## Impact

A GitHub app takeover can have significant repercussions, including unauthorized access to sensitive data, manipulation of code leading to vulnerabilities or disruptions in workflows, and a loss of trust in both the app developer and the GitHub platform. Additionally, there's a risk of data exfiltration, reputational damage, and potential legal consequences. Such incidents highlight the importance of robust security measures and proactive risk management to prevent unauthorized access and mitigate the impact of security breaches within the GitHub ecosystem.

## Attachments
- image.png
- image.png
