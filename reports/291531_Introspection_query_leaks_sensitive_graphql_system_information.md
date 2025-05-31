# Introspection query leaks sensitive graphql system information.

## Report Details
- **Report ID**: 291531
- **URL**: https://hackerone.com/reports/291531
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-18T16:58:42.150Z
- **Disclosed**: 2017-11-22T06:29:35.128Z

## Reporter
- **Username**: zuriel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Interospection query leaks sensitive data.

**Introduction**
As we know graphql was initially developed and used by facebook as an **internal query language** and so the features of graphql mostly revolve around internal and development areas.
Graphql executes queries using a type system with the data defined. An important but often ignored feature of graphql is the ability to ask graphql schema about the supported queries with the help of **Interospection Sytem**

**Description (includes Impact and Steps to Reproduce)**
An interospection system can completely reveal the backend system defined by developers inluding arguments,fields,types,descriptions,deprecated status of types and so on. 
This could easily give out the complete map of backend system along with the schema and directives. 

In our case graphql is implemented as an [endpoint] (https://hackerone.com/graphql) to retrieve sensitive data like user information, payout preferences, program policies, team settings etc.
Revealing the schema of the entire backend will serve as an attack ground for attackers in order to craft graphql queries that can retrieve fields that are normally not meant to be accessed by users.
Moreover any changes made or to be brought about can be easily revealed through **description** fields of types.

The following graphql query is an **interospection query** that completely reveals the defined system with all required details ([Reference] (https://gist.github.com/craigbeck/b90915d49fda19d5b2b17ead14dcd6da)). 

`{"query": "query IntrospectionQuery {__schema {queryType { name },mutationType { name },subscriptionType { name },types {...FullType},directives {name,description,args {...InputValue},onOperation,onFragment,onField}}}\nfragment FullType on __Type {kind,name,description,fields(includeDeprecated: true) {name,description,args {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true) {name,description,isDeprecated,deprecationReason},possibleTypes {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type { ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType {kind,name,ofType {kind,name,ofType {kind,name}}}}"}`

Upon looking into the response (ie the graphql system map returned), following things were observed:

+ **Deprecated Nodes could still be queried at root level**

The interospection query response returned deprecated status of nodes like "Report","Team" as "true":

eg.
> "isDeprecated": true,
  "deprecationReason": "Query for a <Node Name> node at the root level is not recommended. Ref T12456" 

But it was seen that a graphql query could still be created with above nodes as root. 

eg. Query with Node **Team** at root level:

**Steps to Reproduce**

`{"query": "query {team(handle:\"security\"){id,_id,about,base_bounty,bug_count}}"}`

This returned valid data even if it was supposed to be deprecated:

> {
	"data": {
		"team": {
			"id": "Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=",
			"_id": "13",
			"about": "Vulnerability disclosure should be safe, transparent, and rewarding.",
			"base_bounty": 500,
			"bug_count": 236
		}
	}
}

This holds true for all nodes that shouldnt be allowed to query directly at root level: Report, Team, User.

**Impact**
Node queries not meant to be allowed at root level could still be executed and could potentially leak data not to be retrieved otherwise. 


+ **Additional Fields of Nodes can be disclosed**

The fields that are not retrieved normally could be retrieved due to knowledge of all fields on a type (or OBJECT). 

eg. the fields sla_missed_count sla_failed-count for a team:

**Steps to Reproduce** 
`{"query": "query {team(handle:\"security\"){sla_failed_count,sla_missed_count}}"}`

> {
	"data": {
		"team": {
			"sla_failed_count": 0,
			"sla_missed_count": 0
		}
	}
}

This was also possible due to "team" being allowed at root level.

**Impact**
Disclosure of additional fields on Nodes


+ **Description field leaks future implementations**

> "deprecationReason": "This is about to be replaced by .genius_execution" 
> "deprecationReason": "Deprecated in favor of .original_report" 

These were returned as deprecationReason fields for genius_execution_id and original_report_id respectively. 

**Impact**
May leak future implementations


**Possible fix**
As mentioned before, graphql was originally used as internal query language and so features like "Interospection System" was useful for development.
But When it is used as a method to query sensitive data, it becomes a threat. Interospection queries should be disabled.


Regards,
Zuriel

## Attachments
No attachments
