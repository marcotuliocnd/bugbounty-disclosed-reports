# Multiple server ssh usernames leaked in your github repository

## Report Details
- **Report ID**: 1265225
- **URL**: https://hackerone.com/reports/1265225
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-16T10:17:09.170Z
- **Disclosed**: 2021-07-19T19:37:30.463Z

## Reporter
- **Username**: praalsanthpro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
hi  security team,while searching on github,I have found multiple ssh usernames that belongs to your organization are exposed in the organization github repository

STEPS TO REPRODUCE:-
     1.Go to this repository. you will see the leaked multiple server ssh usernames.
          *https://github.com/iandunn/dotfiles/blob/31f4009ddfde9176ba5880687a5119f59183c267/.ssh/config


POC:-
    I have attached a screenshot.Have a look at this

## Impact

By knowing the valid usernames, an attacker can easily bruteforce the password and he can get access to your servers

## Attachments
- iandunn_ssh.PNG
