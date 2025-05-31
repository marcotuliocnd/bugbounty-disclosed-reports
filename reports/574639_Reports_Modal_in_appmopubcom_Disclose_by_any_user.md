# Reports Modal in app.mopub.com Disclose by any user

## Report Details
- **Report ID**: 574639
- **URL**: https://hackerone.com/reports/574639
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-08T23:55:05.009Z
- **Disclosed**: 2019-10-02T23:03:31.526Z

## Reporter
- **Username**: updatelap
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:**

I sent this report and closed it "Informative" and asked me to send a new report if more information was available for exploitation  #544278

**Description:**

Twitter allows "mopub" users to create reports, and each report gives a unique ID to reach it, The report information is displayed by sending a GET Request to the endpoint https://app.mopub.com/reports/custom/report_modal/█████/

After the test it was found that any user logged in to "mopub" can access any report only by changing the value of the ID, which leads to the disclosure of user information such as "Email owner report"


#Attack scenario

IF the account administrator added a user with "Member" in the account, and then removed "Member" later. If the Member saves these UUID, he can view the information at any time

##Steps To Reproduce:

1. [create account and login https://app.mopub.com]
2. [Go to the link https://app.mopub.com/reports/custom/]
3. [Create "New Network Report"]
4. [now your report get id such as ███████] 1.[just change report_modal ID https://app.mopub.com/reports/custom/report_modal/‘UUID/]

###this reason for the closure of the previous report

>If an attacker ever had the "Member" role on an account they could copy the network report without >this attack. In addition, we do not believe it is realistic for an attacker to brute-force a meaningful >portion of this space. If you can demonstrate the ability to guess identifiers belonging to other accounts >in a more-or-less "real time" manner (e.g. within one day) then please let us know by opening a new >report, and we will be happy to consider it at that time.


## New info 
Yes, as I said, the member can copy the report, but after the re-test in depth, I found something that was not mentioned in the report., These reports are updated by current members or managers if a member before leaving the account collects the unique identifiers for these reports will be able to see the new information added to the reports

eg (Add more emails to report or change the information you are in)

## Impact

disclosure of user information

## Attachments
No attachments
