# Campaign Account Balance and History Disclosed in API Response

## Report Details
- **Report ID**: 1587374
- **URL**: https://hackerone.com/reports/1587374
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-31T15:31:20.399Z
- **Disclosed**: 2022-11-30T19:31:34.579Z

## Reporter
- **Username**: sachin_kr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
During the security assessment of the application, it has been observed that server-side authorization checks are not implemented on the 'GET /campaign-manager-api/campaignManagerAccounts/:campaignId/accountCredits?q=account' HTTP request. As a result, an attacker can fetch the campaign wallet amount details like 'totalCreditAmount', and 'remaining credit amount' history of all the victim's account.

###Steps to reproduce:
1. Log in to LinkedIn.
2. Create an advertising account. 
███
3. After creating the account go to - the https://www.linkedin.com/campaignmanager/accounts/XXXXX/billing/transactions page.
4. Intercept the vulnerable requests and replay the request using the victim's campaign id. The response will disclose the campaign wallet details and history.
███████

###Vulnerable Request:
```
GET /campaign-manager-api/campaignManagerAccounts/█████████████/accountCredits?q=account HTTP/2
Host: www.linkedin.com
```

###IDs for testing:
███████████████████
████████████
█████████████████
█████████████████
The ids are in series so can be brute forced

## Impact

An attacker can access the complete wallet details like available amount and used amounts and the deposit history of victim's campaign account.

## Attachments
No attachments
