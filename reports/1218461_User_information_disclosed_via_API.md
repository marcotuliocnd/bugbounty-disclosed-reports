# User information disclosed via API

## Report Details
- **Report ID**: 1218461
- **URL**: https://hackerone.com/reports/1218461
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-06-06T08:07:33.006Z
- **Disclosed**: 2022-10-19T18:47:49.386Z

## Reporter
- **Username**: toormund
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
## Summary:

It appears that the requests for "system accounts" are fully available via an API endpoint that does not require authentication. 

The main issue is that among the information disclosed are user emails (many with gmail addresses) but the individual applications also include information that the user provides about their organization/integration such as IP addresses, physical locations and whether or not the system uses okta. 

## Steps To Reproduce:

Navigate to the following URL:  https://sam.gov/api/prod/iam/cws/v1/applications/

## Supporting Material/References:

Help desk article about what the [system accounts are](http://www.fsd.gov/gsafsd_sp?id=gsafsd_kb_articles&sys_id=c8d50f1d1b187c909ac5ddb6bc4bcbe2)

Here is an example object of what is returned from the endpoint:

```
{"uid":12345,"systemAccountName":"POC","interfacingSystemVersion":"beta.POCcom","systemDescriptionAndFunction":"example of data thgat is leaked","systemAdmins":"[]","systemManagers":"[{\"commonName\":\"James Bond\",\"uid\":\"fakepassword@gmail.com\",\"mail\":\"fake-fun@opayq.com\",\"name\":\"James Bond\",\"isGov\":false,\"id\":\"fake-fun@opayq.com\"}]","contractOpportunities":"","contractData":"","entityInformation":"","federalHierarchy":"","wageDeterminations":"","assistanceListings":"","referenceData":"","ipAddress":"","typeOfConnection":"","physicalLocation":"","securityOfficialName":"","securityOfficialEmail":"","uploadAto":"","authorizationConfirmation":false,"authorizingOfficialName":"","submittedDate":"2021-06-06T06:49:17.130+0000","submittedBy":"fake-fun@opayq.com","securityApprover":"","rejectedBy":"","rejectionReason":"","applicationStatus":"Draft","isGov":false,"migratedToOkta":false,"fips199Categorization":""}
```

## Impact

A threat actor could view personal information about users on the platform.

It is also theoretically possible that a threat actor could use information gathered from this endpoint to identify future targets and footholds.

## Attachments
No attachments
