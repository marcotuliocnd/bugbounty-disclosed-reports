# API Webhooks Fire And Are Unlisted After Permissions Removed

## Report Details
- **Report ID**: 227230
- **URL**: https://hackerone.com/reports/227230
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-09T13:36:39.233Z
- **Disclosed**: 2017-06-27T19:45:37.376Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi All,
quick note, I debated reporting this given recent developments and conversations. However, it seemed odd to wait until June to discuss the potential here, especially after I mulled over the design decision for two weeks having tested this April 25. That said, if you agree with the vulnerability, let's forego the bounty.

##Description
In testing out the API web hooks, I noticed that the scoping permissions only allow API credentials to create web hooks for those actions which are enabled with at least read permissions. If you try to create a web hook for an action the API doesn't have, an error is returned. However, if you create a web hook and then remove the permission for that action, the web hook still fires when the event is invoked. For example:

1. Create an API token
2. Give it read access to orders
3. Create a web hook for order creations
4. Remove permission to read orders from the API
5. Create an order
6. Web hook fires

At this point, I recognize this may be an intentional design decision, that removing permissions did not immediately delete / revoke web hooks to avoid accidents where admins accidentally change permissions and unintentionally disable their existing web hooks. However, if that is in fact the case, I believe this is still an issue in that after removing the associated permission, if you make an API call to get all web hooks, web hooks without explicit permission are not returned. In other words, if you have created only 1 web hook and remove the permissions associated with it, calling for all web hooks returns an empty array.

I also waited approximately an hour after creating my web hook and removing read access to ensure there was no queued action to remove the web hook itself. I can confirm, it doesn't appear that there is.

##Vulnerability
I'm reporting this as a vulnerability for two reasons: 

- First, once a permission is removed from an API token, that API can no longer make any read related calls. But, if a web hook was created first, that web hook will still fire and send the information to the defined endpoint. Assuming this is intended behaviour leads to the second reason.

-  If a web hook exists and permissions are removed for the action it is performing, the web hook is no longer listed when making the API call to get all web hooks. Additionally, there is no UI page I could find to list API created web hooks (/admin/settings/notifications does not list API created web hooks). This means the only way an admin can confirm there are no back door web hooks (for lack of a better term) is to have an API token with read access to everything an periodically check which web hooks exist.

From a malicious stand point, I thought this would give an attacker a subtle back door into ex-filtrating data from a site on a go forward basis. However, they would first need to compromise a site.

##Steps to reproduce
1. Log into your account
2. Visit the private apps administration page ``/admin/apps/private/``
3. Create an app
4. Give it access to read orders
5. Via cURL, make the call to create a web hook (changing the URL to your own requestb.in URL)

~~~
#!/bin/bash

creds=`cat ../creds`

curl -X POST "$creds/admin/webhooks.json" \
  -H "Content-Type: application/json" \
  -d @- << EOD 
    {
      "webhook": {
        "topic": "orders\/create",
        "address": "http://requestb.in/17m30us1",
        "format": "json"
      }
    }
EOD

printf "\n"
~~~

6. Go back to your app administration page and remove access to read orders
7. Via cURL, make the call to get all web hooks, it should return []

~~~
#!/bin/bash

creds=`cat ../creds`

curl "$creds/admin/webhooks.json?since=1" \
  -H "Content-Type: application/json" \

printf "\n"
~~~

8. Visit your site orders page, ``/admin/orders`` and create an order
9. Visit your ``requestb.in`` page, refresh and confirm the web hook fired

Please let me know if you have any questions.
Pete

##P.S.
I'd love to know if you don't mind me asking - when I originally tested this April 25, I swore I could create web hooks for any action with or without permissions. However, when I finally decided this should be reported as a vulnerability and went to confirm that behaviour on April 28 I couldn't any more. Am I just losing my mind or was there a code change that actually addressed that behaviour between April 25 and 28?

## Attachments
No attachments
