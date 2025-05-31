# Inline banner on Report page discloses whether organization runs a private program

## Report Details
- **Report ID**: 452973
- **URL**: https://hackerone.com/reports/452973
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-30T05:05:57.286Z
- **Disclosed**: 2018-12-11T17:54:36.757Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team , @jobert
**Description:**

Your engineers have created inscription - `You are participating in a private program for ████████. Please do not publicly discuss the program until the program goes public.`

When a hacker creates a report in an external program with a private page, we will see this inscription, which makes it clear that the program has a private part.

When a hacker creates a report in an external program that does not have a private page , we will not see this inscription.

It's more of a logical mistake. To fix this, I think you need to give the inscription in all reports for all programmes
### Steps To Reproduce

1. Create publish report for any programs

2. If we are created report for ████████ , ██████████ , ... We will see the inscription -
`You are participating in a private program for`***name_program***`. Please do not publicly discuss the program until the program goes public.` Because they have a private part

█████████

3. if we are creted report for ████, ... We won't see the inscription . Because they have not a private part

██████████

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

disclosure of external programs with private

## Attachments
No attachments
