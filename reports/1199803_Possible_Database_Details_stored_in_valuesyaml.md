# Possible Database Details stored in values.yaml

## Report Details
- **Report ID**: 1199803
- **URL**: https://hackerone.com/reports/1199803
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-17T16:38:48.420Z
- **Disclosed**: 2021-12-09T17:47:01.628Z

## Reporter
- **Username**: sparta5537
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
The database details like username and database name are disclosed in the below mentioned file. Assuming a blank password since the password field was empty.

File Location : https://github.com/Sifchain/sifnode/blob/740331dad061ee0f5a3cf3798d429f294b70f0ae/deploy/helm/block-explorer/values.yaml 

I have attached screenshot in this report.

## Impact

An attacker can use this vulnerability to access the database once he is on the internal system.

## Attachments
- Database_details_-_Exposure.png
