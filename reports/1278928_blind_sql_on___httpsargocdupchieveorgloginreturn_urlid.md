# blind sql on  [ https://argocd.upchieve.org/login?return_url=id= ]

## Report Details
- **Report ID**: 1278928
- **URL**: https://hackerone.com/reports/1278928
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-07-27T11:04:53.324Z
- **Disclosed**: 2021-07-28T16:14:48.790Z

## Reporter
- **Username**: ben_lay
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:
[i have discoverd a blind sql on your site login page which i confirmed using two scenarios to confirm its existance.]


## Steps To Reproduce:
[add details for how we can reproduce the issue]


use the following payloads 
this one retured a 200 ok response confirming sql vulnerability existance
id=291751-sleep(5)&hash=f42ffae0449536cfd0419826f3adf136

this one was blocked confirming the first one is going through and can be weponised

70418291&comment_id=291751-benchmark(1000000000,1-1)&hash=f42ffae0449536cfd0419826f3adf136


example link on how to reproduce  [ https://argocd.upchieve.org/login?return_url=id=291751-sleep(5)&hash=f42ffae0449536cfd0419826f3adf136]


Why -sleep(5), -benchmark(1000000000,1-1) payloads were used? I suspected that comment_id was processed as integer and was unescaped in the query so int-sleep(t) is a valid construction whatever the full query is, which doesn't require various quote/parenthesis tests for the quick manual confirmation. I found it also useful when WAF/filters block the quotes.
The severity was set to High because I propose Critical only for content injections:)

## Supporting Material/References:

[ https://owasp.org/www-community/attacks/Blind_SQL_Injection ]
[https://gerbenjavado.com/manual-sql-injection-discovery-tips/]



## Recommendations for Fixing/Mitigation
[The only sure way to prevent SQL Injection attacks is input validation and parametrized queries including prepared statements. The application code should never use the input directly. The developer must sanitize all input, not only web form inputs such as login forms.]

## Impact

The impact SQL injection can have on a business is far-reaching. A successful attack may result in the unauthorized viewing of user lists, the deletion of entire tables and, in certain cases, the attacker gaining administrative rights to a database, all of which are highly detrimental to a business.

## Attachments
No attachments
