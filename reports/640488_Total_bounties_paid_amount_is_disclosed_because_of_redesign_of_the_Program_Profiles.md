# Total bounties paid amount is disclosed because of redesign of the Program Profiles

## Report Details
- **Report ID**: 640488
- **URL**: https://hackerone.com/reports/640488
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-11T14:55:51.754Z
- **Disclosed**: 2019-08-02T22:45:28.619Z

## Reporter
- **Username**: asad0x01_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Description: On July 2 Hackerone redesigned the [Program Profiles](https://twitter.com/jobertabma/status/11460679483536834570).After the new program page design, I noticed that it is disclosing total bounties paid amount. For some program total bounties paid amount was hidden (████). It used to show like <$4000 if the bounty was $3990.But after the redesign, it is disclosing total bounty paid amount.


Steps to reproduce:

Go to any program page which used to hide total bounty amount (████████)


Now you should be able to see total bounties paid amount.


Please note that even if those above changed are made intentionally, this would allow others to know exact bounty amount paid to someone. For example, ███ does not disclose bounty awarded to a particular researcher. Since their total bounty amount is public one can determine how much they rewarded a particular researcher by **New Total bounty paid Amount - Old Total Bounty Paid Amount**. I see that there is a similar [report] (https://hackerone.com/reports/148050)

## Impact

This could disclose total bounty paid amount and bounty amount paid to a particular researcher in spite of program settings.

## Attachments
No attachments
