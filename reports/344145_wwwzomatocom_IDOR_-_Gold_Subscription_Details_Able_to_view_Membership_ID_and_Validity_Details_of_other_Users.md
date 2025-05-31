# [www.zomato.com] IDOR - Gold Subscription Details, Able to view "Membership ID" and "Validity Details" of other Users

## Report Details
- **Report ID**: 344145
- **URL**: https://hackerone.com/reports/344145
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-04-28T06:02:35.953Z
- **Disclosed**: 2018-04-28T11:35:17.190Z

## Reporter
- **Username**: riya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hello Zomato,

The following URL : https://www.zomato.com/gold/payment-success?subscription_id=██████████&user_id=█████████ is vulnerable to IDOR in `subscription_id` field. Anyone can get Subscription Start & End Date and Plan Duration of a Membership ID just by changing the `subscription_id` parameter. 
{F291153}

MEMBERSHIP ID : ████
STARTED ON : 22 Dec 2017
VALID UP TO : 22 Jun 2018
Subscription Plan :  6 month plan

## Impact

Anyone can get Subscription Start & End Date and Plan Duration of a Membership ID.

___Cheers!
Riya___

## Attachments
No attachments
