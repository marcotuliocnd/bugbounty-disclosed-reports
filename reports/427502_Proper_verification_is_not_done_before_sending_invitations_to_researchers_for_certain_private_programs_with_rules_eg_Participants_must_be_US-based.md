# Proper verification is not done before sending invitations to researchers for certain private programs with rules e.g. "Participants must be US-based"

## Report Details
- **Report ID**: 427502
- **URL**: https://hackerone.com/reports/427502
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-23T20:27:34.452Z
- **Disclosed**: 2018-11-07T21:28:17.188Z

## Reporter
- **Username**: ateek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,

I would like to report something I just recently noticed upon receiving an automated invite from Hackerone for a private program. The program brief clearly states the following in program rules:

█████

This is where I believe the issue is. 

I live in ███ and according to the program rules I believe I should not be eligible to participate in this particular program since I am not based in the US however my observation is that currently there are no checks in place on Hackerone platform for this sort of validation and automated private invites are sent to random researchers who meet the criteria based on their reputation without validating if the researcher meets the "Locality and Jurisdiction" bar.

[+] Proof of concept:

Program that has the Locality/Jurisdiction rule in place:

█████████

Screenshot evidence of received email:

██████


Screenshot evidence that I was able to successfully accept the invite and now participating in the program successfully:

█████████


[+] Solution:

In this case, before sending an invitation to me, my profile should have been validated specially my location since this program has specific requirements regarding US based researchers only.

## Impact

Worst, This could cause "lawsuit" related issues/disputes between all parties and or any similar sort of a legal problem.

## Attachments
No attachments
