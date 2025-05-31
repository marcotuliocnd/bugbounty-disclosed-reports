# SSRF In plantuml (on plantuml.pre.gitlab.com)

## Report Details
- **Report ID**: 689245
- **URL**: https://hackerone.com/reports/689245
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-06T00:02:52.414Z
- **Disclosed**: 2020-08-17T13:55:48.552Z

## Reporter
- **Username**: plazmaz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the (parenthesized) sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

### Summary

The site https://plantuml.pre.gitlab.com is vulnerable to SSRF. While I haven't spun up an instance to test if gitlab's integration with plantuml is vulnerable to this, it seems feasible that it is, given a few facotrs:
#1 The SSRF is due to a feature in plantuml
#2 A PlantUML integration exists for gitlab community edition
#3 Due to conversation in gitlab (https://gitlab.com/gitlab-org/release/framework/issues/448, https://gitlab.com/gitlab-com/gl-infra/infrastructure/issues/2163/) I believe this is a staging server for plantuml

### Steps to reproduce

(Step-by-step guide to reproduce the issue, including:)
1. Visit the following link:
https://plantuml.pre.gitlab.com/uml/Aov9B2hXKW02AvTyXUByt5I5ufBIj3Hhi9XYPbvoJcbAga96IKc1bRw-eP6vdW4G6bfP65WOS1MNv1TO0m00
2. Note that the UML of the website is included

Note: It seems that while I was testing, access to instance metadata (169.254.169.254) was blocked (or limited), as the server now returns an error after timing out for the following uml, where previously it returned information:
```
@startuml
start
    :Do some stuff;
    !include http://169.254.169.254/
stop;
@enduml
```


### Impact
This allows attackers to access internal endpoints and data. Additionally, had the instance metadata not been restricted, accessing that information would be feasible. Additionally, this will likely allow for bypassing of the block of /proxy mentioned in this issue: https://gitlab.com/gitlab-org/release/framework/issues/457

### What is the current *bug* behavior?

The plantuml server returns data from internal addresses:
https://plantuml.pre.gitlab.com/png/Aov9B2hXKW02AvTyXUByt5I5ufBIj3Hhi9XYPbvoJcbAga96IKc1bRw-eP6vdW4G6bfP65WOw7CLb-GNM0C0

### What is the expected *correct* behavior?
The plantuml server does not allow link-local network includes via the `include` statement

## Impact

It's difficult to say, but given the default plantuml installation allows for this SSRF, it's likely multiple on-premises installations would open a risk for SSRF once plantuml is enabled. This site also allows for accessing other resources on its network in its current state

## Attachments
No attachments
