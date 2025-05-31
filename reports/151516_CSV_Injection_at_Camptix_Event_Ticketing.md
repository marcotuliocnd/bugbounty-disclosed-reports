# CSV Injection at Camptix Event Ticketing

## Report Details
- **Report ID**: 151516
- **URL**: https://hackerone.com/reports/151516
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-15T14:13:39.389Z
- **Disclosed**: 2016-08-18T16:38:38.992Z

## Reporter
- **Username**: thezawad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hi,
As you mentioned the scope of vulnerability as
>Any plugin listed on my WordPress.org profile. 
I am reporting this issue.

I have seen from your [WordPress.org](https://profiles.wordpress.org/iandunn/#content-plugins) profile the second plugin listed is **Camptix Event Ticketing**
So I looked at the source code of the plugin (https://github.com/Automattic/camptix)
Although I don't have much knowledge about wordpress plugin development what I understood that you have good filtering for XSS (html tags) when submitting user data (in ticket form)
But no filtering to filter out CSV macros (starts with `=`)
So I installed it in my WP and checked out it with a very simple ticketing with only *Firstname* ,*Lastname* and *Email*

**Reproduction of Bug**
1. From any open to buy ticket sign up for one.
2. In the *First name , Last name* field type `=AND(2>1)` and `=7*7` respectively.
3. Save them.
4. Now from admin panel export the attendees information as CSV. Open the CSV with any application (eg. Excel) and you'll see the First name and Last name field executes the command.
This can be further used to perform command execution on Windows system (high risk)
[See this](http://www.contextis.com/resources/blog/comma-separated-vulnerabilities/)
Since the bug could be exploited by random user and the victim is admin, I think it should be patched.

The **Fix** could be simple. Just escape `=` and `-` `+` signs from user input. this will solve the issue I guess.

Hope you resolve and reward.

------------------------------
Zawad

## Attachments
No attachments
