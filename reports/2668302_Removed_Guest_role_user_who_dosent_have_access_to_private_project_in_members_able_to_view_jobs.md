# Removed Guest role user who dosent have access to private project in members able to view jobs 

## Report Details
- **Report ID**: 2668302
- **URL**: https://hackerone.com/reports/2668302
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-08-17T17:09:37.444Z
- **Disclosed**: 2024-09-18T16:31:39.047Z

## Reporter
- **Username**: tarun_sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
A removed guest role user, who no longer has access to private projects, is still able to view jobs associated with those projects. This issue indicates a potential security gap where access controls may not be effectively enforced after user removal.

Summary 
In the scenario where a user with a guest role is removed from a private project, their access should be completely revoked. However, in this case, despite the removal, the user can still view job details associated with the private project. This behavior suggests a flaw in the access control mechanism, allowing unauthorized visibility of sensitive project-related information.

Steps to reproduce 
1 Invite a guest role user to a private project through the owner account 
2 Through guest role user access the job as raw format 
>https://cdn.artifacts.gitlab-static.net/f3/93/id 


3 After Owner remove him from private project but still the link is accessible to him 
without having access to private project and that particular team 
That can disclose him some sensitive info such ( env , sensitive docker images , crtitical information to him ) 

Mitigations 
Ensure that the system correctly enforces access controls and revokes all permissions for removed users. This may involve auditing and enhancing the user role management and permission handling processes.

If you have any more more questions 
Comment on the report 

Regards 
@mrrobot

## Impact

As an attacker 
Removed users gaining access to job details can expose sensitive project data or operational information. This could lead to inadvertent or malicious leakage of internal processes and project specifics.

## Attachments
No attachments
