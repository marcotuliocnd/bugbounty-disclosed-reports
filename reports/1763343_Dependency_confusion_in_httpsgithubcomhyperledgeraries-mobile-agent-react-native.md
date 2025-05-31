# Dependency confusion in https://github.com/hyperledger/aries-mobile-agent-react-native 

## Report Details
- **Report ID**: 1763343
- **URL**: https://hackerone.com/reports/1763343
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-11-05T22:20:13.148Z
- **Disclosed**: 2023-02-07T16:07:24.440Z

## Reporter
- **Username**: r3drush
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
Hi,
I found dependency confusion vulnerability in your aries mobile agent. 

The agent is installed through npm which then download thepublic packages required by the application. Those dependencies are defined through the package.json file. I found that your agent depends on the package "aries-bifold" that is not currently present in the public repository; an attacker could upload its malicious package and then gain remote code execution on every target installing the agent.
I limited my research on finding the missing package without uploading the "malicious" package on npm because https://github.com/hyperledger/aries-mobile-agent-react-native is not in scope (but is not out-of-scope either), but the methods to exploit this vulnerability are well documented here:
1) https://dhiyaneshgeek.github.io/web/security/2021/09/04/dependency-confusion/

More about this vulnerability from the researcher who discovered it:
2) https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610

Cheers,
r3drush

## Impact

Remote code execution to clients installing the agent

## Attachments
No attachments
