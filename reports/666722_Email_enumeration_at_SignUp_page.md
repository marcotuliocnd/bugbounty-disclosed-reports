# Email enumeration at SignUp page

## Report Details
- **Report ID**: 666722
- **URL**: https://hackerone.com/reports/666722
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-03T10:13:32.763Z
- **Disclosed**: 2019-09-04T07:42:59.298Z

## Reporter
- **Username**: sheerwood
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
Hi.

There's bad security practise at https://trade.go.exchange/en/auth/sign-up against User enumeration.

#### Description:

At the signup page here https://trade.go.exchange/en/auth/sign-up , when you enter an existing user's mail , a msg box says "Email is invalid."

F546294

The problem is that any used email gets the same error message. while when you enter any other e-mail regardless whether it is fake or not & valid or no it get accepted. which means any Email (could be fake) is valid except registred emails in the database.
so an attacker can compare both responses (success & failure) and enumerate users' emails in large scale.

#### Mitigation:
A better security practise is by simply saying that you sent a link to the e-mail no matter if they have an account already or no. If they have already registred and another process is done, the Email message must say that "someone tried to signup with that Email adress, if that's you please log in."

## Impact

- Leaking users' emails. / Information Disclosure.

## Attachments
- exist.JPG
