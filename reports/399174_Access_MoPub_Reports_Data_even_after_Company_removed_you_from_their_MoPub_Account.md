# Access MoPub Reports Data even after Company removed you from their MoPub Account.

## Report Details
- **Report ID**: 399174
- **URL**: https://hackerone.com/reports/399174
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-24T23:21:37.544Z
- **Disclosed**: 2019-11-05T18:08:15.483Z

## Reporter
- **Username**: suyog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
##Description + Attacking approach

**API Workflow** :

- The MoPub Reporting API supports two separate CSV outputs where publishers can retrieve inventory or campaign performance data.

- Publishers can retrieve daily reports via making a GET request using the request parameters.

- This URL will return a 302 redirect response. The link to download the report will be returned in the response location header.

-----

**How you grab Report data even after company removed you**

- If Publisher/Company invite you for their MoPub Account with any permissions & Roles.
 ("administrators or Members" - it doesn't matter, which permission company gives you while invitation)

- After accept the invitation you have access to make all changes to the company account. 

-----

**Attacking approach start from here**

- In order to retrieve data, the API must first be enabled for company account.
- So, you can Enable data access through API (just click on checkbox in the Reports page of the MoPub UI.)
or it might be already enabled by publisher.
- Note down the "Reporting API access details". [i.e. API key, Inventory report ID, Campaign report ID]
- Also Note the Report ID of each MoPub Report present inside the Company Account.

**!!!**

- Now, the publisher/company doesn't want you with their MoPub account and they removed you from their Manage User settings.
- But they forgot to Reset API key.
- Now, you don't have any access of company account. 

> NOTE! **You have the "Reporting API access details (which you noted)".**

-----

**Access the Reporting API :**

- GET request using the request parameters.

[report_key=[individual_report_id ; inventory_report_id ; campaign_report_id]
api_key=[API_KEY]
date=Date of the report. Format YYYY-MM-DD]
https://app.mopub.com/reports/custom/api/download_report?report_key=[REP_KEY]&api_key=[API_KEY]&date=[YYYY-MM-DD]

- Sample Request:

██████████

-----

##Remediation :

1. API key must be auto-reset after the user removed from company.
2. **(for 2nd condition in impact)** Once the Data access is disabled, user should not be able to access reports data via API.


.


**Thank you : )**

## Impact

- Attacker(removed user) able to access Organization Current as well as in Future created MoPub reports in 2 conditions :

1. If API key is not reset and "data access through API" checkbox is enabled 
2. If API key is not reset and "data access through API" checkbox is disabled.

## Attachments
No attachments
