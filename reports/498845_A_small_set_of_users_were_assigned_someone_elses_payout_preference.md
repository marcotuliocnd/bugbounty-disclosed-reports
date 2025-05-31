# A small set of users were assigned someone else's payout preference

## Report Details
- **Report ID**: 498845
- **URL**: https://hackerone.com/reports/498845
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-20T20:09:49.042Z
- **Disclosed**: 2019-02-20T21:38:34.418Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
On December 20th, 2016, HackerOne introduced a new payout preference that allowed employee bounties to be paid through payroll. At the time, a feature was added to our support backend that allowed the IT department to provision this special payout preference for HackerOne employees. To help the IT team, the Engineering team wrote a data migration to provision the payout preference for all current HackerOne employees. During this migration, an incorrect assumption was made that caused the payout preference to be provisioned for non-HackerOne employees.

HackerOne identified the discrepancy on February 19, 2019 and resolved it on February 20, 2019. No users were notified because none of them received any bounties and it only disclosed HackerOne employees' corporate email address. Twelve (12) users were affected.

# Root Cause
HackerOne's payments service is a separate system that takes care of receiving money from customers and sending it to people everywhere around the world. This service is separated from the core platform.

Both systems have a concept of a **User**. In the payments backend it identifies a natural person that holds information like a tax form, payout preferences, payouts, OFAC checks, etc. In the main platform it identifies any user that can sign into the platform. Both models are identified by an auto incrementing integer. These IDs were never intended to be identical, which is why the platform's **User** model contains a reference to the payments service **User** model.

Up until April 2016 these IDs were always identical. For every user that signed up for hackerone.com an API call would create a **User** object in the payments service. When the [HackerOne API](https://api.hackerone.com) publicly launched, **User** objects would be created in the core platform that would not have a corresponding **User** object in the payments backend because they are not able to receive bounties. This is when the primary keys of the tables started to diverge.

In December 2016, when the payroll feature was rolled out, a data migration was executed to create the new payout preferences in the payments backend. This payout preference was set as the default for these users and blocked the users from updating it. A list of users was queried from the core platform, which was needed because the core platform holds information about whether someone is an employee or not. This query generated a list of primary keys of users in the core platform. This list was then used to create the payout preferences.

However, because the first query used the core platform's user IDs instead of the payment service user IDs, the wrong primary keys were used to assign the payout preferences to the user. HackerOne employees that joined between April 2016 and December 2016 were incorrectly identified, resulting in non-HackerOne employees getting a HackerOne employee's payout preference. Twelve (12) users were affected.

All code changes go through mandatory code review at HackerOne. Because information from two separate systems had to be synchronized, a decision was made to manually run the data migration on a production console. This bypassed the mandatory code review. A code review from people more familiar with the integration might've caught the minor mistake in the data migration.

# Resolution and Recovery
The affected users were identified and a data migration was executed to reassign the original payout preference to the user. The payroll payout preference was removed from the users to avoid that they'd be able to access the corporate email address assigned to their account.

# Impact on Data
If the affected users would've received a bounty, it would've been send to a HackerOne employee instead of the user. These users would've also been able to see the HackerOne employee's corporate email address. Even though these payments are exported manually, we were not completely confident that we would've caught this in the export file. None of the users received a bounty and there is no evidence that the users accessed the HackerOne employees' corporate email address that was assigned to their account.

# Preventative Measures
A lot of improvements have been made since December 2016 that would've prevented the mistakes if it were to happen today. Some notable changes have been listed below.

* The payments backend API has been significantly improved, which removed the need to query information from two separate systems.
* Console access has been significantly limited and is currently being phased out completely.
* Alerting has been put in place for code executed on a production console.
* A user is notified when its default payout preference is updated, which would've caught this error sooner.

## Impact

See above post mortem.

## Attachments
No attachments
