# [acronis.secure.force.com] - Insecure Salesforce default/custom object permissions leads to information disclosure

## Report Details
- **Report ID**: 1023572
- **URL**: https://hackerone.com/reports/1023572
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-10-31T18:24:39.700Z
- **Disclosed**: 2021-08-17T10:45:49.695Z

## Reporter
- **Username**: amsda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi there,

I know that this domain https://acronis.secure.force.com is not listed in scope but I thought it would be a good idea to share this finding with you because this endpoint is leaking internal information/meetings.

**Target:** The Salesforce instance at https://acronis.secure.force.com.

**Description:** The web application at https://acronis.secure.force.com is built using Salesforce. Salesforce is a CRM for developing web applications providing a number of abstractions to simplify the development of data-driven applications. In particular, the Aura framework enables developers to build applications using reusable components exposing an API in order for the components to interact with the application.

During testing it was discovered that the Salesforce instance has loose permissions on the `Event` object for unauthenticated Guest users.

Therefore, a malicious attacker may be able to extract sensitive information belonging to other users of the application. To do this, an unauthenticated attacker may craft a HTTP request directly to the Aura API at https://acronis.secure.force.com/acc/aura, using built-in controller methods normally used by the Salesforce Lightning components.

**Steps to Reproduce:**
1) Ensure Burp Suite is sniffing all HTTP(S) requests in the background;
2) Navigate to https://aaroncostello-developer-edition.eu45.force.com, this is to retrieve a template aura request for use;
3) Find a POST request in Burp's Proxy history to the `/s/sfsites/aura` endpoint;
4) Send it to the repeater;
5) Modify both the Host header and Burp's target field to `acronis.secure.force.com`
6) Modify the POST request to `/acc/aura`
7) Change the message POST parameter to the payload below. **Please note that all other parameters should remain untouched**, and that in this example payload, a pageSize of 100 is used for speed however more records can be retrieved:

**Event**
```
{"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Event","layoutType":"FULL","pageSize":100,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}
```
8) Submit the request
9) The response contains sensitive information belonging to other users.

**Remediation:** Enforce [record level security (RLS)](https://help.salesforce.com/articleView?id=security_data_access.htm&type=5
) on the vulnerable object to ensure records are only able to be retrieved by the record owner, and privileged users of the application.

Thank you

## Impact

The Salesforce instance does not enforce sufficient authorization checks when specific objects are requested. As such, an unauthenticated attacker may be able to extract sensitive data from the records in these objects which contains information of other users. This includes internal information/meetings.

## Attachments
No attachments
