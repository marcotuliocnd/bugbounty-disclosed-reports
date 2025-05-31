# Guest users can change the confidentiality attribute on those issues that have been assigned to them

## Report Details
- **Report ID**: 762271
- **URL**: https://hackerone.com/reports/762271
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-20T11:29:58.372Z
- **Disclosed**: 2020-11-09T09:44:50.775Z

## Reporter
- **Username**: 0xwintermute
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

A user with no association to a project nor group can use a mutation GraphQL query to change the confidentiality on those issues where they have been previously assigned. This functionality is restricted to those users which have been granted access to a project and hold at least the `Reporter` role, or those users that have created the issue.



### Steps to reproduce

A user creates an issue on a program and assigns by mistake the issue to our attacker account. The attacker will receive a notification, as he has been assigned to a new issue on a particular program.

The attacker could then craft a GraphQL mutation on the `issueSetConfidential` object and change the `confidentiality` attribute from `false` to `true`. This will have an immediate effect on the issue, hiding it from the rest of users holding the `Guest` role.

### Impact

As detailed above, an attacker with no role or permissions on a group that has created a project could hide issues from other users.



I'm completely aware of the likelihood of this scenario from happening, however I've not been able to exercise this functionality from the web interface nor the API. Hence why I believe this behavior is not intended and should not happen. Specially if the user performing this attack does not belong to the group that has created the project.



### Example

For this scenario lets gonna use two different accounts:

* `victim@gitlab.com`
* `attacker@gitlab.com`

As `victim@gitlab.com` lets create a new issue on a public project where we participate:

{F664563}

As the `attacker@gitlab.com`, if we attempt to access the issue, we will be presented with only the ability to write new comments:

{F664561}

If attacker attempts to perform the mutation GraphQL query mentioned above, the following response will be returned:

**GraphQL Query**

```
mutation {
  issueSetConfidential(input:{projectPath:"groupID/projectID", iid:"5", confidential:true}){
    errors
  }
}
```



**GraphQL Response**

```
{
  "data": {
    "issueSetConfidential": null
  },
  "errors": [
    {
      "message": "The resource that you are attempting to access does not exist or you don't have permission to perform this action",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "issueSetConfidential"
      ]
    }
  ]
}
```



We will get back later to this, for now lets focus again on our `victim@gitlab.com`. As we have decided to assign the recently created issue to a new user, which in this case will be our `attacker@gitlab.com` (Either by mistake or on purpose):

*Note* : In this case I'm going to use the quick action `/assign @username` as I cannot assign external users that do not belong to a project using the web interface (I'm not sure if this is kind of expected, but thought would be worth to be brought to your attention)



{F664559}



Right after doing this, the `attacker@gitlab.com` will receive a new notification on the UI, as shown below:

{F664560}

After visiting the new issue as the `attacker@gitlab.com` we can observe two things:

* There is no user assigned to the issue
* There is no option to change the `confidentiality` attribute through the web interface.

{F664561}

However, if we repeat the same GraphQL mutation query mentioned above, we will receive a different response this time:


**GraphQL Request**

```
mutation {
  issueSetConfidential(input:{projectPath:"groupID/projectID", iid:"5", confidential:true}){
    errors
  }
}
```

**GraphQL Response**

```
{
  "data": {
    "issueSetConfidential": {
      "errors": []
    }
  }
}
```

If we check the issue activity, we will observe the following message:

{F664562}

Our `attacker@gitlab.com` has been able to successfully change the `confidential` attribute for a finding, when this functionality was not being offered in first place through the web interface.

Additionally, if we open a new anonymous session and navigate to the issues page for this project, we will see that the issue is "gone".

{F664558}


### What's the current bug behaviour?

Changing `confidentiality` attributes on findings through a mutation GraphQL query should not be possible if such functionality is not offered neither through the web interface, nor the GitLab API.

This may allow an attacker without any special role nor privileges to arbitrarily change the confidentiality of those issues for which he/she has been assigned to. Revoking visibiility to uses with `Guest` or no role at all.



### What's the expected correct behaviour?

I would expect this action to not be possible from being executed as such functionality/behaviour is not present within the GitLab web interface nor GitLab API.

As a user with no privileges nor member of a group where the affected project belongs to, I would expect two things:

- Not being able to get any issues assigned as I'm not involve nor belongs to the project's group.
- Not being able to arbitrarily set the confidentiality attribute of an issue for which I've been assigned to, specially if I don't have enough permissions for such action.

## Impact

Please see the description provided above

## Attachments
- Issue_-_Anonymous_Window.png
- Issue_-_Attacker_Assigned.png
- Issue_-_Attacker_Notification.png
- Issue_-_Attacker_perspective.png
- Issue_-_Changed_by_attacker.png
- Issue_-_Created.png
