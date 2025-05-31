# Private account causes displayed through API

## Report Details
- **Report ID**: 826005
- **URL**: https://hackerone.com/reports/826005
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-21T15:41:03.103Z
- **Disclosed**: 2020-04-21T19:02:59.588Z

## Reporter
- **Username**: ech0re
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stagingdoteverydotorg

## Vulnerability Information
## Summary:
Any authenticated user can see which causes a private account user is interested in, by sending a GET request to the API, even though this information is not displayed anywhere on the profile page.

In the profile settings, the following message is displayed for "Private Supporter" option :  
*People will be able to find and request to follow you, but only followers you accept will be able to see which organizations you support.*

Nothing is mentionned about the causes we're interested in, but as a private account, it would make sense to not disclose this information.

The fact that this information is not displayed on the web profile page makes me think that it is unintentional to send it as reponse to API requests from any user.

## Steps To Reproduce:
To reproduce this issue, I simply sent an API GET request to /api/users/<user_id_or_username>

  1. On https://www.every.org/settings/profile page, submit the form by clicking on "Update" button and get the send request with all csrf and cookie headers
  2. The first line will be **PATCH /api/me HTTP/1.1**, simply modify this to **GET /api/users/any_username** and re-send the request (you do not need to keep the body json data)
  3. Read the API Json response, especially the `"causes":[{"entityName":"Cause Follow","causeCategory":"SOME_CATEGORY"}]` part

## Example:

I have two accounts :
https://www.every.org/@bug.hunter (ech0bh+everyorg@wearehackerone.com) - "Attacker"
https://www.every.org/@bug.hunter3 (ech0bh+everyorg3@wearehackerone.com) - PRIVATE profile

This is **bug.hunter3** private profile, interested in "Education" cause :

{F755510}

This is an API GET request sent with **bug.hunter** account CSRF-Token (no cookie needed) :

```
GET /api/users/bug.hunter3 HTTP/1.1
Host: www.every.org
User-Agent: Mozilla/5.0 (---------------------------------) Gecko/20100101 Firefox/74.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://www.every.org/settings/profile
Content-Type: application/json
X-CSRF-Token: <csrf_token_here>
Origin: https://www.every.org
Content-Length: 0
Connection: close
Cookie: 
```

This is the reponse body :

```
{
  "message": "Found user",
  "data": {
    "user": {
      "entityName": "User",
      "id": "e03bb4c9-c904-46d5-92db-59b235743690",
      "firstName": "bug",
      "lastName": "hunter3",
      "profileImageUrl": "",
      "username": "bug.hunter3",
      "locationAddress": "",
      "isPrivate": true,
      "followedByCurrentUserStatus": "none",
      "followingCurrentUserStatus": "none",
      "causes": [
        {
          "entityName": "Cause Follow",
          "causeCategory": "EDUCATION"
        }
      ]
    },
    "followInfo": {
      "entityName": "Follow Info",
      "userId": "e03bb4c9-c904-46d5-92db-59b235743690",
      "followerCount": 0,
      "followingCount": 0
    }
  }
}
```

As we can see, I was able to know that bug.hunter3 is interested in "Education" cause, even though it is a private profile and I am not following it.

## Additional information:

Please note that bug.hunter2 (ech0bh+everyorg2@wearehackerone.com) is also my account which wasn't of any use here. I created it to test another vulnerability.

PS: The link reference in top of this submit page does not redirect to your security page. Indeed, there is a link to https://hackerone.com/every_org while your security page is https://hackerone.com/everydotorg.

Do not hesitate to ask any information you would need and I'll be happy to help.

## Impact

Following cause category information disclosure of any account (even private account that we do not follow).

## Attachments
- causes.png
