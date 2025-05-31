# LDAP login possible even though account doesn't match user filter

## Report Details
- **Report ID**: 205908
- **URL**: https://hackerone.com/reports/205908
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-02-13T08:53:38.395Z
- **Disclosed**: 2019-07-27T08:57:51.612Z

## Reporter
- **Username**: gvde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
We have set up a ldap user filter to match only those users in our ldap directory which should get access to nextcloud. User count shows correct number of users as expected and the filter correctly shows only the users we want in an ldapsearch.

The ldap directory contains a lot of other accounts which don't match that filter and which should not get access to nextcloud. However, now we found out that it is possible for any valid user account in the ldap directory to log into nextcloud. The account is set up and login is successful even through the account does not match the filter.

The account won't be listed on the Users page of an nextcloud admin user, thus from that view the account doesn't exist.

I have just tested it with 11.0.1 (centos7, installed from rpms) and I was able to log in with a test account which does not match the user filter...


## Attachments
No attachments
