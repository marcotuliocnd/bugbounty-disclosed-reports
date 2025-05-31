# New users can read all Nextcloud Deck data from previous user with same username

## Report Details
- **Report ID**: 882258
- **URL**: https://hackerone.com/reports/882258
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-25T13:56:48.398Z
- **Disclosed**: 2021-02-14T16:22:30.969Z

## Reporter
- **Username**: stefanniedermann
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
First of all: Sorry, i know there is no scope "Deck" but both Joas and Jus pointed me to hackerone to report this security issue.

1. As an administrator create Nextcloud account "test"
2. Log in as "test"
3. Go to Deck app and create some boards, stacks and cards with personal or confidential stuff.
4. As an administrator delete Nextcloud account "test"
5. As an administrator create new Nextcloud account "test" (password doesn't need to match)
6. Log in as "test" (This might be a completely other human than in step 2!)
7. Go to Deck app and see all the secret stuff from the previous user

## Impact

Attacker is able to see confidential or private data from previous users with the same user name.

Since the private data of the users is sacred, it is a no-go that the data isn't hard deleted form the database when the user account gets deleted, but it is even worse that another user with the same username can read all the stuff (without any effort to restore data).

## Attachments
No attachments
