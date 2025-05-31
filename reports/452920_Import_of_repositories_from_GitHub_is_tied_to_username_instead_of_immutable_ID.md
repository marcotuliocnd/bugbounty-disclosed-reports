# Import of repositories from GitHub is tied to username instead of immutable ID

## Report Details
- **Report ID**: 452920
- **URL**: https://hackerone.com/reports/452920
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-30T00:23:31.857Z
- **Disclosed**: 2018-12-02T16:42:41.425Z

## Reporter
- **Username**: emitrani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
When a user verifies a Github account at `/edit/elsewhere` the final result is a Github username tied to a Liberapay account. The issue is Github usernames are mutable. 

Consider the scenario.

1. I create an account called ed-liberapay (something likely to be claimed in the future)
2. Verify that I own that Github account on liberapay.com/edit/elsewhere
3. I go to my Github and update my username (this doesn't change anything on liberapay.com and Github won't redirect old links to the account to the new location)
4. Eventually that account is claimed by Ed and he creates impressive repos.
5. I go and import the repos into my account and pretend to own it.

## Impact

This can enable impersonation. 

I suspect the issue is caused in this function:

https://github.com/liberapay/liberapay.com/blob/master/liberapay/elsewhere/_base.py#L266

I haven't set up my own instance to see if GitHub is indeed going through the username path but in practice I was able to set up 2 accounts as described. Change the name of the attacker to something else and then import a different account's repos as my own.

## Attachments
No attachments
