# Ability to identify actual private from sandboxed programs using link hackerone.com/$handle/terms_acceptance_data.csv

## Report Details
- **Report ID**: 2381253
- **URL**: https://hackerone.com/reports/2381253
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-02-20T07:02:10.092Z
- **Disclosed**: 2024-06-20T21:21:49.426Z

## Reporter
- **Username**: ketr0it
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
I was looking through the settings of one of my sandboxed programs I use for testing and I noticed some weird behavior, when we go to any program's advanced vetting page hackerone.com/$handle/advanced_vetting, it loads up regardless of permission, granted no other confidential info is displayed since the GraphQL request appropriately restricts unauthorized users so this is what is shown:
{F3061767}
although this shouldn't happen, so far there wouldn't a significant risk from this behavior alone, but one thing I noticed from the Advanced vetting page (when it loads properly, of course) is that it has a link to download a .csv file:
{F3061769}
that leads to https://hackerone.com/$handle/terms_acceptance_data.csv
I decided to experiment with this link and sure enough, I found some risky behavior, when any HackerOne user goes to https://hackerone.com/$SANDBOXED_PROGRAM/terms_acceptance_data.csv the request goes through and we download the csv file, although it doesn't have any relevant information, just default text, take for example my own sandboxed program https://hackerone.com/test_pie77/terms_acceptance_data.csv if you or any user in Hackerone go to that link the request will go through and download the csv file, now let's take for example, ██████, they have a totally private program although you can access the embedded report submission form from their own security page, so if we go to █████ we can see that the request doesn't go through, confirming that the program is, in fact, private and we know that it is private and exists because when we try with a handle that doesn't exist it shows the Hackerone default 404 page like this:
{F3061796}
but when we go to ███ program:
█████████
it shows a different response
I tried this with other actual private programs and the behavior was the same, the request didn't go through, I tried with other sandboxed programs of mine using a second account and the behavior was the same, the request did go through, the only private program it did work was in HackerOne's own dummy invite-only program at https://hackerone.com/security-test-invite-only/terms_acceptance_data.csv this could be due to some misconfiguration on HackerOne's side as the request does goes through and we can see the csv file has been modified.
{F3061793}

### Steps To Reproduce

1. Use my sandboxed program as an example: https://hackerone.com/test_pie77/terms_acceptance_data.csv or replace my program's handle with a sandboxed program of yours and use a second account and go to that link
2. Check how you can download the Csv file confirming the program is sandboxed
3. Now replace the sandboxed program's handle with a private program's handle and see how it doesn't work, confirming the program is private

## Impact

Here we can clearly identify which programs are private, we can build a script or just try manually using company names that we might believe have a private program in Hackerone and check if they actually have one, leading to some loss of the confidentiality of all private programs in HackerOne. This is confirmed to be a valid vulnerability going by this text on HackerOne's policy page:
{F3061814}

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
