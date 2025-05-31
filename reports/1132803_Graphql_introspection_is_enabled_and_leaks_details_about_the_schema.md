# Graphql introspection is enabled and leaks details about the schema

## Report Details
- **Report ID**: 1132803
- **URL**: https://hackerone.com/reports/1132803
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-23T05:42:13.153Z
- **Disclosed**: 2021-05-09T13:26:34.043Z

## Reporter
- **Username**: sahil__soni
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: on

## Vulnerability Information
## Summary:
Hi team ! i've found a misconfiguration in your graphql Api on the endpoint https://www.on-running.com/en-in/graphql in which an attacker is able to run a graphql interospection query to fetch schemas , types , fields , available query operations  , after running interospection query on the graphql api endpoint  , an attacker is able to list all type of available api calls , so he'll be able to perform unauthorised api calls due to this misconfiguration.

###Interospection query : 

>{"query": "query IntrospectionQuery {__schema {queryType { name },mutationType { name },subscriptionType { name },types {...FullType},directives {name,description,args {...InputValue},onOperation,onFragment,onField}}}\nfragment FullType on __Type {kind,name,description,fields(includeDeprecated: true) {name,description,args {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true) {name,description,isDeprecated,deprecationReason},possibleTypes {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type { ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType {kind,name,ofType {kind,name,ofType {kind,name}}}}"}

## Steps To Reproduce:


  1. create an account on https://www.on-running.com

  2. navigate to the endpoint https://www.on-running.com/en-in/graphql
  
  3. visit to the endpoint and capture the request in burp proxy and send the request to repeater

  4. now put the interospection query into the request body and send the request

 5.after the in the response you'll get types of query operation's available , schemas so that by using these an attacker will be able to perform unauthorized call

{F1239441}



### as a proof  i'm performing a simple api call to check whether a user exist or not :

run the Query on the graphql api endpoint:


>query {
	userExists(email:"code")
} 

replace the code with an email address  , then if the user with the email exist then it returns true if not the false.

Similarly there are too many types of query operations available see in the below screenshot :

{F1239443}

Here in this scenerio the mutations is also available to modify a data on the graphql api  , see in the below screenshot that after running a interospection query it has revealed the mutations availabe so the attacker can craft a query to modify the data : 

{F1239459}


### here the issue is the  , due to the misconfiguration in graphql api  , it is allowing an arbitary user to run interospection query  , so here the after running interospection query it is revelaing the api calls available  which is a not a good security implimentation and you must have to forbid the user to run a interospection query otherwise an attacker will be able to perform unauthorised api calls .

## Impact

if attacker will get available query  operation types , fields  , mutations  so an attacker will be able to modify and list the data and will be able to perform unauthorised api calls

## Attachments
- interospection_query.png
- revealed_operations.png
- available_query_operations.png
- mutations_available.png
