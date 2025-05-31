# Registration bypass with leaked Invite Token

## Report Details
- **Report ID**: 1071102
- **URL**: https://hackerone.com/reports/1071102
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-04T13:48:48.160Z
- **Disclosed**: 2024-08-10T21:58:46.526Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:**

Regular expressions in the `validateInviteToken` route allows unauthenticated users to guess a valid invite token, that allows them to access a private channel or register accounts on a remote server with "Secret URL" registration method enabled.

**Description:**

The API route `validateInviteToken` passes an unauthenticated clients token bodyParam to the validateInviteToken method as found in [app/api/server/v1/invites.js#L45-L62](https://github.com/RocketChat/Rocket.Chat/blob/729e258326bcd1fd0685d6d4c4755e38c9f8831d/app/api/server/v1/invites.js#L45-L62)


```javascript
API.v1.addRoute('validateInviteToken', { authRequired: false }, {
	post() {
		const { token } = this.bodyParams;

		if (!token) {
			throw new Meteor.Error('error-invalid-token', 'The invite token is invalid.', { method: 'validateInviteToken', field: 'token' });
		}

		let valid = true;
		try {
			validateInviteToken(token);
		} catch (e) {
			valid = false;
		}

		return API.v1.success({ valid });
	},
});
```

The token is then passed to `Invites.findOneById(token)` without further checks of the input data, which allows to send an Object instead of a string. This object can be a `$regex` Mongo DB query, that reduces the number of queries required to leak a valid invite token.

Once found, an attacker can navigate to `/invite/:token` to then register a new account with access to the specific channel. After initial registration, the process can be repeated to join more rooms with non-expired invites.

```sh
curl 'https://open.rocket.chat/api/v1/validateInviteToken'
  -H "content-type: application/json"
  -d '{ "token": { "$regex": ".*" } }'
```

Expired invite token might mask other token because Mongo DB only returns one document (sorted by order of insertion). A valid strategy to leak a 6 character token (case-sensitive letters and numbers) is to prefix the regex (e.g. `^a.*`, `^b.*`, etc) and check the boolean result.

## Releases Affected:

  * 3.9.4

## Steps To Reproduce (from initial installation to vulnerability):

(Add details for how we can reproduce the issue)

  1.) Leak a valid token with consecutive `validateInviteToken` checks
  2.) Browse to `/invite/:leaked_token`
  3.) Register account

## Suggested mitigation

  * validate user input to be a String

## Impact

Unauthenticated attackers can leak invite links to register new accounts, although public registration is disabled. Authenticated users might gain unauthorized access to private chat rooms.

## Attachments
No attachments
