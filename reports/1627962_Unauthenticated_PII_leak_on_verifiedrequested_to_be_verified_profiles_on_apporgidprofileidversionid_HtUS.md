# Unauthenticated PII leak on verified/requested to be verified profiles on ███████/app/org/{id}/profile/{id}/version/{id} [HtUS]

## Report Details
- **Report ID**: 1627962
- **URL**: https://hackerone.com/reports/1627962
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-06T14:00:59.734Z
- **Disclosed**: 2022-10-14T17:04:05.583Z

## Reporter
- **Username**: shreky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
On any published profile page,you can switch between their profile's versions(provided they have made at least 1 change after publication) ,which will make a GET request to **███/organization/{id}/profile{id}/version/{id}**.  
While proxying traffic through Burp Suite,another request is being sent to **████████*/app/org/*{id}/profile{id}/version/{id}** ,which exposes some information about the author such as **id,uuid and name**,BUT if  you switch to the version that is **verified/requested to be verified**,the same endpoint(but with different version id) will return the above info **+ their email**,which adds to the PII disclosure.  
Worst of all,this endpoint can be accessed even by unauthenticated users,and all steps above can be done unauthenticated aswell.  

## References
██████████

## Impact

Any **unauthenticated** person can obtain PII information from any **verified** profile or profiles that have **requested verification**.

## Attachments
No attachments
