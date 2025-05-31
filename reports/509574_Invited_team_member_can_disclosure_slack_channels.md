# Invited team member can disclosure slack channels

## Report Details
- **Report ID**: 509574
- **URL**: https://hackerone.com/reports/509574
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-14T07:38:46.001Z
- **Disclosed**: 2019-04-05T19:58:54.464Z

## Reporter
- **Username**: eremeev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello, this report is similar to #505493 (also still waiting for response), but accent is totally on another thing. I think it is important and should be fixed, and so i create new report.  

Invited team member without any permission can disclosure `private` channel names of slack integration.

If it is also by design, i very hope that it should be fixed.

For example, user1 and user2 can be in one slack team and one hackerone team, but user1 can't view names of some private slack channels in which he not invited. But he can disclosure it names by making graphql query to hackerone

**Description:**
Using graphql query

```
query{
  
  teams(where:{handle:{_eq:"hackeronetest_4hr1y"}}){
    edges{
      node{
        slack_pipelines{
          nodes{
            id
            descriptive_label
            team{
              handle
              slack_integration{
                channels{
                  name
                }
              }
            }
          }
        }
      }
    }
  }
}
```

invited team member(hackerone) without permission can access private slack channel names in which he not invited 

### Steps To Reproduce

1. as team admin create slack integration
1. create private channel
1. invite new team member to hackerone team, not required that user is invited to slack team
1.  remove any permissions for this user
1. login as invited user
1. send graphql query as described early: {F441244}

### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

what channels can see invited user:  {F441243}
what channels can see slack admin: {F441245}
what channels returns to invited user though graphql:  {F441251}

invited user **must not** view this channel name: `h1test`

### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?

no

## Impact

Disclosure private channels of slack integration

## Attachments
- Screenshot_2019-03-14_09-21-39.png
- Screenshot_2019-03-14_09-21-09.png
- Screenshot_2019-03-14_09-21-53.png
- Screenshot_2019-03-14_10-32-02.png
